import base64
import odoorpc
import logging
import glob
import importlib
import ast
import subprocess
import psycopg2

import requests
from lxml import html, etree
import os

_logger = logging.getLogger(__name__)
datetime_format = "%Y-%m-%dT%H:%M:%S.%fZ"
user = "admin"
password = "admin"
http_method = "https"
odoo_host = "127.0.0.1"
odoo_db = "73658952-saas-18-1-all"

#odoo = rpc.ODOO(odoo_host, port=8014, version="14.0")"""
import urllib.request

# Nginx Basic Auth credentials
has_basic_auth = False
nginx_username = "wdi_demo"
nginx_password = "DemoWdiP@ss456!X"

# Odoo credentials
host = 'weldcomdemo.tictag.vn'  # or an FQDN (fullly qualified domain name), e.g. 'www.tvtmarine.com'
protocol = 'jsonrpc+ssl'  # or 'jsonrpc+ssl' for host with SSL
port = 443

#demo
db_name = 'weldcomnew'
user_name = 'tienhm@weldcom.vn'
user_passwd = 'tienHM@2024@@wdiDem0'

host = 'quantri.weldcom.vn'
db_name = 'weldcom.vn'
user_name = 'tienhm1@weldcom.com.vn'
user_passwd = 'Viindoo&Weldcom@2025#97BD'


opener = None
if has_basic_auth:
    # Create an HTTP opener with Basic Auth
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, f"https://{host}", nginx_username, nginx_password)
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)

# Prepare the connection to the server
odoo = odoorpc.ODOO(host=host, protocol=protocol, port=port, opener=opener)
version = odoo.version
odoo.login(db_name, user_name, user_passwd)

#d = [{'atype': 'text/javascript', 'url': '/web/static/src/scss/primary_variables.scss', 'filename': '/etc/odoo/odoo.conf', 'content': '', 'media': ''}]
#a = env['ir.qweb'].get_asset_bundle('web.assets_common', d)
#log(str(a.javascripts[0]._fetch_content()))
#ticTagJSC)(*1214@2020

# lấy filestore

all_attachments_data = odoo.env["ir.attachment"].search_read([('store_fname', '!=', False), ('id', '>=', 474400)], ['store_fname'])
a = len(all_attachments_data)
i = 0
ids = []
for att in all_attachments_data:
    if not os.path.isfile(f'/home/royle/v14_weldcom_filestore/{att["store_fname"]}'):
        os.makedirs(f'/home/royle/v14_weldcom_filestore/{att["store_fname"].split("/")[0]}', exist_ok=True)
        print('Downloading %s: %s' % (att['id'], att["store_fname"]))
        ids.append(att['id'])
    if len(ids) ==50:
        att_data = odoo.execute('ir.attachment', 'read', ids, ['datas', 'store_fname'])
        for x in att_data:
            f = open(f'/home/royle/v14_weldcom_filestore/{x["store_fname"]}', 'wb')
            f.write(base64.b64decode(x['datas']))
            f.close()
        ids = []
    i+=1
    print('%s/%s (%s%%)' % (i, a, 100*i/a))
if ids:
    att_data = odoo.execute('ir.attachment', 'read', ids, ['datas', 'store_fname'])
    for x in att_data:
        print('Downloading1 %s: %s' % (x['id'], x["store_fname"]))
        f = open(f'/home/royle/v14_weldcom_filestore/{x["store_fname"]}', 'wb')
        f.write(base64.b64decode(x['datas']))
        f.close()
    ids = []
print('done')

