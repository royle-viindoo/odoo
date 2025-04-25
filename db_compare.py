import psycopg2

# Cấu hình kết nối đến 2 database
db1_config = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'v14_weldcom_data',
    'user': 'postgres',
    'password': '08020710'
}

db2_config = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'v17_weldcom',
    'user': 'postgres',
    'password': '08020710'
}

def get_table_counts(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = 'public'
    """)
    tables = cur.fetchall()
    table_counts = {}
    for (table,) in tables:
        try:
            cur.execute(f"SELECT COUNT(*) FROM public.{table}")
            count = cur.fetchone()[0]
            table_counts[table] = count
        except Exception as e:
            table_counts[table] = f'Error: {e}'
    return table_counts

def get_table(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = 'public'
          AND tablename NOT IN (
              SELECT table_name
              FROM information_schema.views
              WHERE table_schema = 'public'
          )
    """)
    return set([t[0] for t in cur.fetchall()])

def get_table_count(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = 'public'
          AND tablename NOT IN (
              SELECT table_name
              FROM information_schema.views
              WHERE table_schema = 'public'
          )
    """)

    counts = {}
    for (table, ) in cur.fetchall():
        cur.execute(f"SELECT COUNT(*) FROM public.{table}")
        counts[table] = cur.fetchone()[0]
    return counts

def _compare_table():
    with psycopg2.connect(**db1_config) as conn1, psycopg2.connect(**db2_config) as conn2:
        tables_db1 = get_table(conn1)
        tables_db2 = get_table(conn2)
        for t in (tables_db2 - tables_db1):
            print('%s,Bảng mới trên 17.0' % t)
        for t in (tables_db1 - tables_db2):
            print('%s,Bảng bị xóa trên 17.0' % t)

def _compare_table_count():
    with psycopg2.connect(**db1_config) as conn1, psycopg2.connect(**db2_config) as conn2:
        tables_db1 = get_table_count(conn1)
        tables_db2 = get_table_count(conn2)
        tables_db11 = get_table(conn1)
        tables_db22 = get_table(conn2)
        new_table = (tables_db22 - tables_db11)
        deleted_table = (tables_db11 - tables_db22)
        for t in tables_db2:
            diff = ''
            if t in new_table:
                diff = 'Bảng mới trên 17.0'
            elif t in deleted_table:
                diff = 'Bảng bị xóa trên 17.0'
            if t in tables_db1:
                print('%s,%s,%s,%s' % (t, tables_db2[t], tables_db1[t], diff))
            else:
                print('%s,%s,,%s' % (t, tables_db2[t], diff))
        for t in deleted_table:
            print('%s,,%s,%s' % (t, tables_db1[t], 'Bảng bị xóa trên 17.0'))

def _compare_table_id(table):
    with psycopg2.connect(**db1_config) as conn1, psycopg2.connect(**db2_config) as conn2:
        cur = conn1.cursor()
        cur.execute(f"SELECT id FROM public.{table} order by id")
        v14_ids = [c[0] for c in cur.fetchall()]

        cur = conn2.cursor()
        cur.execute(f"SELECT id FROM public.{table} order by id")
        v17_ids = [c[0] for c in cur.fetchall()]
        print(f'v17 new: {set(v17_ids) - set(v14_ids)}')
        print(f'v14 old: {set(v14_ids) - set(v17_ids)}')

#_compare_table()
_compare_table_id('product_product')
_compare_table_count()

