import base64
import odoorpc
import logging
import glob
import importlib
import ast
import subprocess
import psycopg2

from odoo.tools import pycompat

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

"""
import subprocess
import psycopg2

DB_NAME = "weldcomnew"
DB_USER = "postgres"
DB_PASSWORD = "5+tKatcZOv1RqZ7dIFAwrw=="
DB_HOST = "123.30.145.236"
DB_PORT = "4239"
LOCAL_FILE = f"./{DB_NAME}.sql"

DB_NAME = "weldcomnew"
DB_USER = "odoo"
DB_PASSWORD = "xxx"
DB_HOST = "172.17.0.2"
DB_PORT = "5432"
LOCAL_FILE = f"./{DB_NAME}.sql"
<connection object at 0x7fef081cd528; dsn: 'user=Odoo password=xxx dbname=weldcomnew host=172.17.0.2 port=5432 sslmode=prefer', closed: 0>
/var/lib/odoo/filestore/weldcomnew


try:
	conn = psycopg2.connect("user=Odoo password=xxx dbname=weldcomnew host=172.17.0.2 port=5432 sslmode=prefer")
	conn2 = psycopg2.connect("user=postgres password=5+tKatcZOv1RqZ7dIFAwrw== dbname=weldcom.vn host=123.30.145.236 port=4237 sslmode=prefer")
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("✅ Kết nối thành công!")
    
    # Tạo cursor để thao tác với DB
    cursor = conn.cursor()
    cursor.execute("SELECT version();")  # Kiểm tra phiên bản PostgreSQL
    print("Phiên bản PostgreSQL:", cursor.fetchone())

    # Đóng kết nối
    cursor.close()
    conn.close()
except Exception as e:
    print("❌ Lỗi kết nối:", e)

# Đặt mật khẩu vào biến môi trường (chỉ hiệu lực trong lệnh này)
backup_cmd = f'PGPASSWORD="{DB_PASSWORD}" pg_dump -U {DB_USER} -h {DB_HOST} -p {DB_PORT} -F c {DB_NAME} -f {LOCAL_FILE}'

# Chạy lệnh backup
subprocess.run(backup_cmd, shell=True, check=True)

print("Backup hoàn tất! File tại:", LOCAL_FILE)

# instance thật thì dùng thêm protocol='jsonrpc+ssl' port=443
odoo = rpc.ODOO('https://73658952-saas-18-1-all.runbot137.odoo.com', protocol='jsonrpc+ssl', port=443)

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
user_passwd = 'Longbien@2025#285A'


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

"""all_attachments_data = odoo.env["ir.attachment"].search_read([('store_fname', '!=', False)], ['store_fname'])
a = len(all_attachments_data)
i = 0
for att in all_attachments_data:
	if not os.path.exists(f'/home/royle/v14_weldcom_filestore/{att["store_fname"]}'):
		os.makedirs(f'/home/royle/v14_weldcom_filestore/{att["store_fname"].split("/")[0]}', exist_ok=True)
		att_data = odoo.execute('ir.attachment', 'read', [att['id']], ['datas'])
		with open(f'/home/royle/v14_weldcom_filestore/{att["store_fname"]}', 'wb') as f: 
			f.write(base64.b64decode(att_data[0]['datas']))
	i+=1
	print('%s / %s' % (i, a))
print(xxx)"""
menus = odoo.env["ir.ui.menu"]
modules = [
'abs_customer_validation',
'abs_dealer_management_system',
'abs_total_discount_so',
'account_accountant',
'account_analytic_parent',
'account_analytic_required',
'account_asset',
'account_auto_transfer',
'account_bank_statement_import',
'account_bank_statement_import_camt',
'account_bank_statement_import_csv',
'account_bank_statement_import_ofx',
'account_batch_payment',
'account_budget',
'account_budget_advance',
'account_financial_risk',
'account_followup',
'account_invoice_extract',
'account_invoice_extract_purchase',
'account_loan',
'account_lock_date_update',
'account_lock_to_date',
'account_menu',
'account_online_sync',
'account_online_synchronization',
'account_plaid',
'account_ponto',
'account_predictive_bills',
'account_reports',
'account_reports_tax',
'account_sepa_direct_debit',
'account_yodlee',
'advanced_web_domain_widget',
'analytic_enterprise',
'analytic_tag_dimension',
'analytic_tag_dimension_enhanced',
'approvals',
'approvals_purchase',
'approvals_purchase_stock',
'asterisk_calls',
'asterisk_calls_crm',
'asterisk_calls_custom',
'asterisk_common',
'attachments_center',
'attachments_manager',
'auditlog',
'auth_oauth_keycloak',
'barcodes_mobile',
'base_automation_hr_contract',
'bi_mail_cc_followers',
'bi_multiwarehouse_for_sales',
'bi_pos_combo',
'bi_sql_editor',
'bi_view_editor',
'bryntum_gantt_enterprise',
'ca_barcode_labels',
'contacts_enterprise',
'crm_enterprise',
'crm_facebook_leads',
'crm_opportunity_product',
'crm_team_parent',
'currency_rate_live',
'data_cleaning',
'data_merge',
'data_merge_crm',
'data_merge_utm',
'date_range',
'digest_enterprise',
'discount_account_invoice',
'discount_sale_order',
'documents',
'documents_fleet',
'documents_hr',
'documents_hr_contract',
'documents_hr_holidays',
'documents_hr_payroll',
'documents_hr_recruitment',
'documents_product',
'documents_project',
'documents_sign',
'documents_spreadsheet',
'documents_spreadsheet_account',
'documents_spreadsheet_crm',
'dusal_hierarchical_tree',
'event_enterprise',
'fleet_dashboard',
'formio',
'formio_crm',
'formio_customize',
'formio_data_api',
'formio_partner',
'formio_storage_filestore',
'hddt_connector',
'helpdesk',
'helpdesk_fsm',
'helpdesk_sale',
'helpdesk_timesheet',
'hr_appraisal',
'hr_attendance_mobile',
'hr_benefit',
'hr_contract_reports',
'hr_contract_sign',
'hr_contract_status',
'hr_contract_types',
'hr_contract_values',
'hr_disciplinary_tracking',
'hr_employee_seniority_months',
'hr_expense_extract',
'hr_expense_predict_product',
'hr_gantt',
'hr_holidays_gantt',
'hr_mobile',
'hr_payroll',
'hr_payroll_account',
'hr_payroll_edit_lines',
'hr_payroll_holidays',
'hr_recruitment_reports',
'hr_work_entry_contract',
'hr_work_entry_holidays',
'industry_fsm',
'industry_fsm_report',
'ks_dashboard_ninja',
'ks_dashboard_theme',
'ks_dn_advance',
'ks_dn_auto_mail',
'ks_dn_live_update',
'mail_attach_existing_attachment',
'mail_enterprise',
'mail_mobile',
'mail_tracking',
'mass_mailing_themes',
'mis_builder',
'mis_builder_budget',
'mis_builder_demo',
'mrp_account_enterprise',
'muk_website_grid',
'odoo_password_manager',
'oh_employee_creation_from_user',
'oi_login_as',
'oi_partner_employee',
'partner_duplicate_validation',
'partner_score',
'partner_sequence_automatic',
'payment_sepa_direct_debit',
'payment_vnpay',
'planning',
'pos_account_reports',
'pos_coupon',
'pos_enterprise',
'pos_hr_mobile',
'pos_user_restrict',
'product_brand',
'product_return_pos',
'project_category',
'project_enterprise',
'project_scrum',
'project_timesheet_synchro',
'prt_mail_messages',
'purchase_enterprise',
'purchase_request',
'purchase_request_department',
'purchase_stock_enterprise',
'queue_job',
'quick_order',
'report_xlsx',
'sale_account_accountant',
'sale_blanket_order',
'sale_commission',
'sale_commission_formula',
'sale_commission_product_criteria',
'sale_commission_product_criteria_discount',
'sale_commission_salesman',
'sale_coupon_domain_product_discount',
'sale_enterprise',
'sale_promotion_discount_in_field',
'sale_subscription',
'sale_subscription_dashboard',
'sale_subscription_sepa_direct_debit',
'setu_abc_analysis_reports',
'setu_rfm_analysis',
'sh_activities_management',
'sh_activity_base',
'sh_barcode_generator_simple',
'sh_emate',
'sh_product_qrcode_generator',
'sh_snippet_adv',
'sign',
'snailmail_account_followup',
'social',
'social_crm',
'social_facebook',
'social_linkedin',
'social_push_notifications',
'social_sale',
'social_twitter',
'sql_request_abstract',
'stock_account_enterprise',
'stock_accountant',
'stock_barcode',
'stock_barcode_mobile',
'stock_enterprise',
'stock_force_availability_app',
'swr_datepicker',
'theme_clean',
'theme_common',
'tictag_pos',
'tictag_theme',
'tictag_website',
'tictag_website_sale',
'timer',
'timesheet_grid',
'trevi_hr_job_categories',
'trevi_hr_usability',
'tt_bpm',
'tt_bpm_portal',
'tt_crm',
'tt_crm_extra',
'tt_custom_website',
'tt_customize',
'tt_data_cleaning',
'tt_data_merge_crm',
'tt_event_crm',
'tt_external',
'tt_helpdesk',
'tt_hr_enhanced',
'tt_hr_payroll_account',
'tt_hr_recruitment',
'tt_planning',
'tt_sign',
'tt_sign_recruitment',
'tt_signup_mobile',
'tt_sms',
'tt_subscription_assets',
'tt_survey',
'tt_timesheet',
'tt_website',
'tt_website_slides',
'web_action_conditionable',
'web_cohort',
'web_dashboard',
'web_domain_field',
'web_enterprise',
'web_gantt',
'web_grid',
'web_m2x_options',
'web_map',
'web_mobile',
'web_studio',
'website_animate',
'website_bootstrap_snippet',
'website_calendar',
'website_crm_score',
'website_editor_unsanitize_html_field',
'website_enterprise',
'website_event_social',
'website_event_track_gantt',
'website_event_track_social',
'website_formio',
'website_formio_dynamic',
'website_sale_dashboard',
'website_studio',
'weldcom',
'xf_pwa',

]
# lấy code bị sót
for x in [
'/web_enterprise/static/src/xml/base_mobile.xml',
'/web_enterprise/static/src/xml/base.xml',
'/web_enterprise/static/src/xml/control_panel.xml',
'/web_enterprise/static/src/xml/search_panel.xml',
'/web_enterprise/static/src/xml/web_calendar.xml',
]:
	content = menus.read_image(1, f'ks_dashboard_ninja,static/lib/css/Chart.css')
	f = open(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/ks_dashboard_ninja/static/lib/css/Chart.min.css', 'wb')
	f.write(base64.decodebytes(content.encode()))
	f.close()
for m in modules:
	content = menus.read_image(1, f'{m},__manifest__.py')
	if not content:
		print(m)
		continue
	with open(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/__manifest__.py', 'wb') as f: 
		f.write(base64.decodebytes(content.encode()))
# lấy manifest và __ini__.py
for m in modules:
	try:
		if not os.path.exists(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/__manifest__.py'):
			content = menus.read_image(1, f'{m},__manifest__.py')
			if content:
				os.makedirs(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}', exist_ok=True)
				with open(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/__manifest__.py', 'wb') as f: 
					f.write(base64.decodebytes(content.encode()))
		if not os.path.exists(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/__init__.py'):
			content = menus.read_image(1, f'{m},__init__.py')
			with open(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/__init__.py', 'wb') as f: 
				f.write(base64.decodebytes(content.encode()))
	except Exception as e:
		print(e)
	if not os.path.exists(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/__init__.py'):
		continue
	with open(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/__init__.py', 'r') as f: 
		for line in f:
			if line and 'from.' in line:
				line = line.replace('from.', 'from .') 
			if line.startswith("import ") or line.startswith("from "):
				parts = line.replace("import", "").replace("from", "").strip().split()
				module_name = parts[0].split('.')[0] or parts[1].split('.')[0]  # Chỉ lấy module chính
				os.makedirs(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/{module_name}', exist_ok=True)
				try:
					if not os.path.exists(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/{module_name}/__init__.py'):
						content = menus.read_image(1, f'{m},{module_name}/__init__.py')
						with open(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/{module_name}/__init__.py', 'wb') as fw: 
							fw.write(base64.decodebytes(content.encode()))
					with open(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/{module_name}/__init__.py', 'r') as f2: 
						for line2 in f2:
							if line2 and 'from.' in line2:
								line2 = line2.replace('from.', 'from .') 
							if line2.startswith("import ") or line2.startswith("from "):
								parts2 = line2.replace("import", "").replace("from", "").strip().split()
								module_name2 = parts2[0].split('.')[0] or parts2[1].split('.')[0]  # Chỉ lấy module chính
								file_path2 = module_name2.replace('.', os.sep) + ".py"
								if not os.path.exists(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/{module_name}/{file_path2}'):
									content = menus.read_image(1, f'{m},{module_name}/{file_path2}')
									if content:
										with open(f'/home/royle/Viindoo/source_code/customer-weldcom-14.0/{m}/{module_name}/{file_path2}', 'wb') as fw2: 
											fw2.write(base64.decodebytes(content.encode()))
									else:
										print('1')
				except Exception as e:
					print(e)
		print(m)

fnames = glob.glob('/home/royle/Viindoo/source_code/customer-weldcom-14.0/**/__manifest__.py')
for fname in fnames:
	
	manifest = {}
	with open(fname, 'r') as f2:
		manifest.update(ast.literal_eval(pycompat.to_text(f2.read())))
	for d in (manifest.get('data') or []) + (manifest.get('images') or []) + (manifest.get('qweb') or []) + (manifest.get('demo') or []):
		if '/*' in d:
			print(d)
			continue
		folder = d.split('/')[0]
		if '/' not in d:
			print('xx %s' %fname)
		if '/' in d and not os.path.exists(f'{fname[:-16]}/{folder}'):
			os.makedirs(f'{fname[:-16]}/{folder}', exist_ok=True)
		if len(d.split('/')) >=3:
			folder = d.split('/')[1]
			if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{folder}"):
				os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{folder}", exist_ok=True)
		if len(d.split('/')) >=4:
			folder = d.split('/')[2]
			if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{folder}"):
				os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{folder}", exist_ok=True)
		if len(d.split('/')) >=5:
			folder = d.split('/')[3]
			if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{folder}"):
				os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{folder}", exist_ok=True)
		file_path = f'{fname[:-16]}/{d}'
		if os.path.exists(file_path):
			continue
		content = menus.read_image(1, f"{fname.split('/')[-2]},{d}")
		if content:
			with open(f'{file_path}', 'wb') as fw2: 
				fw2.write(base64.decodebytes(content.encode()))

data = [
'/swr_datepicker/static/src/js/swr_datepicker.js',
'/sh_emate/static/src/js/s_product_editor.js',
'/advanced_web_domain_widget/static/src/js/widget/domain_selector_dialog.js',
'/advanced_web_domain_widget/static/src/js/widget/model_field_selector.js',
'/advanced_web_domain_widget/static/src/js/widget/model_record_selector.js',
'/advanced_web_domain_widget/static/src/js/widget/TerabitsDomainSelector.js',
'/advanced_web_domain_widget/static/src/js/fields/basic_fields.js',
'/advanced_web_domain_widget/static/src/js/fields/terabits_fields_registry.js',
'/asterisk_calls/static/src/js/channels.js',
'/asterisk_calls/static/src/js/systray.js',
'/asterisk_calls_crm/static/src/js/systray.js',
'/asterisk_calls_custom/static/src/models/activity/activity.js',
'/asterisk_calls_custom/static/src/components/activity/activity.js',
'/asterisk_calls_custom/static/src/components/activity_mark_done_popover/activity_mark_done_popover.js',
'/asterisk_common/static/src/js/support.js',
'/asterisk_common/static/src/js/originate.js',
'/asterisk_common/static/src/js/notification.js',
'/attachments_center/static/src/js/webKanbanRecord.js',
'/attachments_manager/static/src/libs/jQuery-contextMenu/jquery.contextMenu.js',
'/attachments_manager/static/src/libs/jQuery-contextMenu/jquery.ui.position.js',
'/attachments_manager/static/src/libs/docxtemplater/docxtemplater.js',
'/attachments_manager/static/src/libs/jszip/jszip.js',
'/attachments_manager/static/src/libs/mammoth/mammoth.browser.min.js',
'/attachments_manager/static/src/libs/sheetjs/xlsx.full.min.js',
'/attachments_manager/static/src/libs/canvas-datagrid/canvas-datagrid.js',
'/attachments_manager/static/src/libs/tui/fabric.min.js',
'/attachments_manager/static/src/libs/tui/tui-code-snippet.min.js',
'/attachments_manager/static/src/libs/tui/tui-color-picker.js',
'/attachments_manager/static/src/libs/tui/FileSaver.min.js',
'/attachments_manager/static/src/libs/tui/tui.image-editor-3.7.2/dist/tui-image-editor.js',
'/attachments_manager/static/src/libs/tui/tui.image-editor-3.7.2/examples/js/theme/white-theme.js',
'/attachments_manager/static/src/libs/tui/tui.image-editor-3.7.2/examples/js/theme/black-theme.js',
'/attachments_manager/static/src/libs/listjs1.5.0/listjs.js',
'/attachments_manager/static/src/libs/qrcode/qrcode.js',
'/attachments_manager/static/src/libs/webcam.js',
'/attachments_manager/static/src/libs/highlight/highlight.pack.js',
'/attachments_manager/static/src/libs/visualizer/visualizer.js',
'/attachments_manager/static/src/libs/uppy/uppy.min.js',
'/attachments_manager/static/src/libs/selection/selection.min.js',
'/attachments_manager/static/src/components/thread_custom/thread_custom.js',
'/attachments_manager/static/src/components/attachment_qrcode/attachment_qrcode.js',
'/attachments_manager/static/src/components/attachment_webcam/attachment_webcam.js',
'/attachments_manager/static/src/components/attachment_slider/attachment_slider.js',
'/attachments_manager/static/src/components/attachment_custom/attachment_custom.js',
'/attachments_manager/static/src/components/file_uploader_custom/file_uploader.js',
'/attachments_manager/static/src/components/attachment_box_custom/attachment_box_custom.js',
'/attachments_manager/static/src/components/attachment_box_custom/attachment_box_screen_record.js',
'/attachments_manager/static/src/components/attachment_box_favorites/attachment_box_favorites.js',
'/attachments_manager/static/src/components/attachment_list_custom/attachment_list_custom.js',
'/bi_pos_combo/static/src/js/bi_pos_combo.js',
'/bi_pos_combo/static/src/js/ProductCategoriesWidget.js',
'/bi_pos_combo/static/src/js/BiProductScreen.js',
'/bi_pos_combo/static/src/js/ClientScreenExtend.js',
'/bi_pos_combo/static/src/js/SelectComboProductPopupWidget.js',
'/bi_pos_combo/static/src/js/OrderWidgetExtended.js',
'/bi_pos_combo/static/src/js/ProductListWidget.js',
'/bi_pos_combo/static/src/js/Screens/ProductScreen/ControlButtons/SubmitOrderButton.js',
'/bryntum_gantt_enterprise/static/src/js/main.js',
'/bryntum_gantt_enterprise/static/gantt_src/js/app.js',
'/bryntum_gantt_enterprise/static/gantt_src/js/chunk-vendors.js',
'/dusal_hierarchical_tree/static/src/components/tree_item/TreeItem.js',
'/dusal_hierarchical_tree/static/src/hierarchical_tree_view/hierarchical_tree_view.js',
'/dusal_hierarchical_tree/static/src/hierarchical_tree_view/hierarchical_tree_model.js',
'/dusal_hierarchical_tree/static/src/hierarchical_tree_view/hierarchical_tree_controller.js',
'/dusal_hierarchical_tree/static/src/hierarchical_tree_view/hierarchical_tree_renderer.js',
'/formio_customize/static/src/js/form_builder_report_widget.js',
'/hddt_connector/static/src/js/pos.js',
'/ks_dashboard_ninja/static/src/js/ks_global_functions.js',
'/ks_dashboard_ninja/static/src/js/ks_dashboard_ninja.js',
'/ks_dashboard_ninja/static/src/js/ks_to_do_dashboard.js',
'/ks_dashboard_ninja/static/src/js/ks_filter_props.js',
'/ks_dashboard_ninja/static/src/js/ks_color_picker.js',
'/ks_dashboard_ninja/static/src/js/ks_dashboard_ninja_item_preview.js',
'/ks_dashboard_ninja/static/src/js/ks_image_basic_widget.js',
'/ks_dashboard_ninja/static/src/js/ks_dashboard_item_theme.js',
'/ks_dashboard_ninja/static/src/js/ks_widget_toggle.js',
'/ks_dashboard_ninja/static/src/js/ks_import_dashboard.js',
'/ks_dashboard_ninja/static/src/js/ks_domain_fix.js',
'/ks_dashboard_ninja/static/src/js/ks_quick_edit_view.js',
'/ks_dashboard_ninja/static/src/js/ks_dashboard_ninja_kpi_preview.js',
'/ks_dashboard_ninja/static/src/js/ks_date_picker.js',
'/ks_dashboard_ninja/static/lib/js/gridstack-h5.js',
'/ks_dashboard_ninja/static/src/js/ks_dashboard_ninja_graph_preview.js',
'/ks_dashboard_ninja/static/src/js/ks_dashboard_ninja_list_view_preview.js',
'/ks_dashboard_ninja/static/src/js/ks_to_do_preview.js',
'/ks_dashboard_ninja/static/src/js/ks_reload_menus_enterprise.js',
'/ks_dashboard_ninja/static/src/js/ks_list_renderer.js',
'/ks_dashboard_ninja/static/src/js/ks_form_renderer.js',
'/ks_dashboard_ninja/static/src/js/ks_create_dashboard_dialog_en.js',
'/ks_dashboard_ninja/static/src/js/ks_create_dashboard_dialog.js',
'/ks_dashboard_theme/static/src/js/ks_dashboard_item_gradient_theme.js',
'/ks_dashboard_ninja/static/lib/js/Chart.bundle.min.js',
'/ks_dashboard_theme/static/src/js/ks_dn_theme.js',
'/ks_dn_advance/static/src/js/ks_labels.js',
'/ks_dn_advance/static/src/js/ks_ylabels.js',
'/ks_dn_advance/static/src/js/ks_dashboard_ninja_tv_graph_preview.js',
'/ks_dn_advance/static/src/js/ks_dashboard_ninja_tv_list_preview.js',
'/ks_dn_advance/static/src/js/ks_dn_kpi_preview.js',
'/ks_dn_advance/static/src/js/ks_tv_dashboard.js',
'/ks_dn_advance/static/lib/js/owl.carousel.min.js',
'/ks_dn_advance/static/lib/js/print.min.js',
'/ks_dn_advance/static/lib/js/pdf.min.js',
'/ks_dn_advance/static/src/js/ks_website_dashboard.js',
'/ks_dn_live_update/static/src/js/ks_dn_live_update_notification.js',
'/odoo_password_manager/static/src/js/pw_password.js',
'/odoo_password_manager/static/src/js/abstract_controller.js',
'/odoo_password_manager/static/src/js/kanban_record.js',
'/odoo_password_manager/static/src/js/password_kanbancontroller.js',
'/odoo_password_manager/static/src/js/password_kanbanmodel.js',
'/odoo_password_manager/static/src/js/password_kanbanrecord.js',
'/odoo_password_manager/static/src/js/password_kanbanrenderer.js',
'/odoo_password_manager/static/src/js/password_kanbanview.js',
'/odoo_password_manager/static/src/js/bundle_password.js',
'/oi_login_as/static/src/js/login_as.js',
'/pos_coupon/static/src/js/coupon.js',
'/pos_coupon/static/src/js/Orderline.js',
'/pos_coupon/static/src/js/PaymentScreen.js',
'/pos_coupon/static/src/js/ProductScreen.js',
'/pos_coupon/static/src/js/ActivePrograms.js',
'/pos_coupon/static/src/js/ControlButtons/PromoCodeButton.js',
'/pos_coupon/static/src/js/ControlButtons/ResetProgramsButton.js',
'/quick_order/static/src/js/search_items.js',
'/sh_activities_management/static/src/js/activity_dashboard.js',
'/sh_activities_management/static/src/js/action_manager_act_window.js',
'/sh_activities_management/static/src/js/systray_activity_menu.js',
'/sh_emate/static/src/js/s_product_editor.js',
'/sh_snippet_adv/static/src/js/libs/owl/owl.carousel.js',
'/sh_snippet_adv/static/src/js/libs/aos/aos.js',
'/sh_snippet_adv/static/src/js/s_animation.js',
'/theme_clean/static/src/js/tour.js',
'/tictag_pos/static/src/js/pos.js',
'/tictag_theme/static/src/js/home_menu.js',
'/tictag_theme/static/src/js/expiration_panel.js',
'/tictag_theme/static/src/js/web_client.js',
'/web_enterprise/static/src/js/home_menu.js',
'/tictag_website/static/src/js/jquery.focuspoint.js',
'/tictag_website/static/src/js/script.js',
'/tictag_website/static/src/js/js_backend.js',
'/tictag_website_sale/static/src/js/script.js',
'/tictag_website_sale/static/src/js/payment_form.js',
'/tt_bpm/static/src/lib/bpmn-js/bpmn-modeler.development.js',
'/tt_bpm/static/src/js/BPMNComponent.js',
'/tt_bpm/static/src/js/BPMNWidget.js',
'/tt_bpm/static/src/lib/mxgraph/js/Init.js',
'/tt_bpm/static/src/lib/mxgraph/deflate/pako.min.js',
'/tt_bpm/static/src/lib/mxgraph/deflate/base64.js',
'/tt_bpm/static/src/lib/mxgraph/jscolor/jscolor.js',
'/tt_bpm/static/src/lib/mxgraph/sanitizer/sanitizer.min.js',
'/tt_bpm/static/src/lib/mxgraph/mxClient.js',
'/tt_bpm/static/src/lib/mxgraph/js/EditorUi.js',
'/tt_bpm/static/src/lib/mxgraph/js/Editor.js',
'/tt_bpm/static/src/lib/mxgraph/js/Sidebar.js',
'/tt_bpm/static/src/lib/mxgraph/js/Graph.js',
'/tt_bpm/static/src/lib/mxgraph/js/Format.js',
'/tt_bpm/static/src/lib/mxgraph/js/Shapes.js',
'/tt_bpm/static/src/lib/mxgraph/js/Actions.js',
'/tt_bpm/static/src/lib/mxgraph/js/Menus.js',
'/tt_bpm/static/src/lib/mxgraph/js/Toolbar.js',
'/tt_bpm/static/src/lib/mxgraph/js/Dialogs.js',
'/tt_bpm/static/src/js/BPMComponent.js',
'/tt_bpm/static/src/js/draw_web_client.js',
'/tt_bpm/static/src/lib/mxgraph/js/Init.js',
'/tt_bpm/static/src/lib/mxgraph/deflate/pako.min.js',
'/tt_bpm/static/src/lib/mxgraph/deflate/base64.js',
'/tt_bpm/static/src/lib/mxgraph/jscolor/jscolor.js',
'/tt_bpm/static/src/lib/mxgraph/sanitizer/sanitizer.min.js',
'/tt_bpm/static/src/lib/mxgraph/mxClient.js',
'/tt_bpm/static/src/lib/mxgraph/js/EditorUi.js',
'/tt_bpm/static/src/lib/mxgraph/js/Editor.js',
'/tt_bpm/static/src/lib/mxgraph/js/Sidebar.js',
'/tt_bpm/static/src/lib/mxgraph/js/Graph.js',
'/tt_bpm/static/src/lib/mxgraph/js/Format.js',
'/tt_bpm/static/src/lib/mxgraph/js/Shapes.js',
'/tt_bpm/static/src/lib/mxgraph/js/Actions.js',
'/tt_bpm/static/src/lib/mxgraph/js/Menus.js',
'/tt_bpm/static/src/lib/mxgraph/js/Toolbar.js',
'/tt_bpm/static/src/lib/mxgraph/js/Dialogs.js',
'/tt_bpm/static/src/lib/bpmn-js/bpmn-modeler.development.js',
'/tt_crm/static/src/js/systray_activity_menu.js',
'/tt_website/static/src/snippets/s_dynamic_snippet_partners/options.js',
'/tt_custom_website/static/src/js/script.js',
'/tt_customize/static/src/js/mail_activity.js',
'/tt_customize/static/src/models/activity/activity.js',
'/tt_customize/static/src/components/activity/activity.js',
'/tt_customize/static/src/models/user/user.js',
'/tt_customize/static/src/components/composer/composer.js',
'/tt_sign/static/src/js/sign.js',
'/tt_signup_mobile/static/src/js/website.js',
'/tt_customize/static/src/js/mail_activity.js',
'/tt_sms/static/src/models/activity/activity.js',
'/tt_sms/static/src/models/sms_template/sms_template.js',
'/tt_sms/static/src/components/activity/activity.js',
'/tt_sms/static/src/components/sms_template/sms_template.js',
'/tt_survey/static/src/js/survey.js',
'/tt_customize/static/src/js/mail_activity.js',
'/tt_timesheet/static/src/models/activity/activity.js',
'/tt_timesheet/static/src/components/activity_mark_done_popover/activity_mark_done_popover.js',
'/tt_customize/static/src/components/activity/activity.js',
'/tt_website_slides/static/src/js/libs/video-js.js',
'/tt_website_slides/static/src/js/libs/noprint.js',
'/tt_website_slides/static/src/js/slides_course_fullscreen_player.js',
'/website_bootstrap_snippet/static/src/js/code_embed_snippet.js',
'/website_formio_dynamic/static/src/js/website_formio_dynamic_editor.js',
'/website_formio_dynamic/static/snippets/000.js',
'/weldcom/static/src/js/pos.js',
'/weldcom/static/src/js/script.js',
'/xf_pwa/static/src/js/pwa/manager.js',
'/xf_pwa/static/src/js/module_version_info.js',
'/xf_pwa/static/src/js/pwa/register.js',
'/asterisk_calls/static/src/css/asterisk_calls.css',
'/asterisk_calls/static/src/css/systray.css',
'/attachments_manager/static/src/libs/tui/tui-color-picker.css',
'/attachments_manager/static/src/libs/tui/tui.image-editor-3.7.2/dist/tui-image-editor.css',
'/attachments_manager/static/src/libs/jQuery-contextMenu/jquery.contextMenu.min.css',
'/attachments_manager/static/src/css/listjs.css',
'/attachments_manager/static/src/libs/slidebar/slidebars.css',
'/attachments_manager/static/src/libs/uppy/uppy.min.css',
'/attachments_manager/static/src/css/attachment_dragdrop.css',
'/attachments_manager/static/src/libs/highlight/styles/default.css',
'/bi_pos_combo/static/src/css/custom.css',
'/bryntum_gantt_enterprise/static/src/css/main.css',
'/formio_customize/static/src/css/custom.css',
'/ks_dashboard_ninja/static/src/css/ks_dashboard_ninja_item.css',
'/ks_dashboard_ninja/static/src/css/ks_icon_container_modal.css',
'/ks_dashboard_ninja/static/src/css/ks_dashboard_item_theme.css',
'/ks_dashboard_ninja/static/src/css/ks_dn_filter.css',
'/ks_dashboard_ninja/static/src/css/ks_toggle_icon.css',
'/ks_dashboard_ninja/static/src/css/ks_dashboard_options.css',
'/ks_dashboard_ninja/static/lib/css/gridstack.min.css',
'/ks_dashboard_ninja/static/lib/css/gridstack-extra.css',
'/ks_dashboard_ninja/static/src/css/ks_dashboard_ninja_pro.css',
'/ks_dashboard_ninja/static/src/css/ks_dashboard_gridstack.css',
'/ks_dashboard_ninja/static/src/css/ks_to_do_item.css',
'/ks_dashboard_theme/static/src/css/ks_dn_theme.css',
'/ks_dashboard_ninja/static/src/css/ks_dashboard_ninja_pro.css',
'/ks_dn_advance/static/src/css/ks_tv_dashboard.css',
'/ks_dn_advance/static/lib/css/owl.carousel.min.css',
'/ks_dn_advance/static/src/css/ks_tv_dashboard.css',
'/odoo_password_manager/static/src/css/styles.css',
'/pos_coupon/static/src/css/coupon.css',
'/quick_order/static/src/css/style.css',
'/sh_activities_management/static/src/css/crm_dashboard.css',
'/sh_snippet_adv/static/src/css/libs/owl/owl.carousel.min.css',
'/sh_snippet_adv/static/src/css/libs/owl/owl.theme.default.min.css',
'/sh_snippet_adv/static/src/css/libs/aos/aos.css',
'/sh_snippet_adv/static/src/css/libs/aos/aos_extra.css',
'/sh_snippet_adv/static/src/css/libs/aos/layout.css',
'/tictag_pos/static/src/css/pos.css',
'/tt_bpm/static/src/lib/mxgraph/styles/grapheditor.css',
'/tt_bpm/static/src/lib/mxgraph/styles/grapheditor.css',
'/weldcom/static/src/css/pos.css',
'/advanced_web_domain_widget/static/src/scss/style.scss',
'/asterisk_calls_custom/static/src/scss/style.scss',
'/dusal_hierarchical_tree/static/src/components/tree_item/tree_item.scss',
'/dusal_hierarchical_tree/static/src/hierarchical_tree_view/hierarchical_tree_view.scss',
'/ks_dashboard_ninja/static/src/css/ks_dashboard_ninja.scss',
'/ks_dashboard_ninja/static/src/scss/ks_dn_gridstack.scss',
'/ks_dashboard_theme/static/src/scss/ks_dn_background.scss',
'/quick_order/static/src/scss/style.scss',
'/sh_emate/data/sh_emate_variables.scss',
'/sh_emate/static/src/scss/sh_emate_variables.scss',
'/sh_snippet_adv/static/src/scss/snippets_options.scss',
'/theme_clean/static/src/scss/primary_variables.scss',
'/theme_clean/static/src/scss/bootstrap_overridden.scss',
'/tictag_theme/static/src/scss/web_editor.scss',
'/tictag_theme/static/src/scss/fonts.scss',
'/tictag_theme/static/src/scss/primary_variables.scss',
'/tictag_website/static/src/scss/style.scss',
'/tictag_website/static/src/scss/style.scss',
'/tictag_website/static/src/scss/style_common.scss',
'/tictag_website_sale/static/src/scss/style.scss',
'/tt_bpm/static/src/scss/bpmn.scss',
'/tt_bpm/static/src/scss/primary_variables.scss',
'/tt_bpm/static/src/scss/style.scss',
'/tt_custom_website/static/src/scss/style.scss',
'/tt_custom_website/static/src/scss/webite_slides_style.scss',
'/tt_customize/static/src/scss/style.scss',
'/tt_customize/static/src/scss/style.scss',
'/tt_sms/static/src/components/sms_template/sms_template.scss',
'/tt_survey/static/src/scss/frontend.scss',
'/tt_survey/static/src/scss/report.scss',
'/tt_customize/static/src/scss/style.scss',
'/tt_website_slides/static/src/scss/videojs.scss',
'/xf_pwa/static/src/scss/module_version_info.scss',

]
import os

def delete_empty_folders(directory):
    for foldername, subfolders, filenames in os.walk(directory, topdown=False):
        for subfolder in subfolders:
            folder_path = os.path.join(foldername, subfolder)
            if not os.listdir(folder_path):  # Kiểm tra nếu thư mục rỗng
                os.rmdir(folder_path)
                print(f"Đã xóa thư mục rỗng: {folder_path}")

# Thay đổi đường dẫn thư mục cần quét
directory_path = "/home/royle/Viindoo/source_code/customer-weldcom-14.0"
#delete_empty_folders(directory_path)
for d in data:
	fname = f"/home/royle/Viindoo/source_code/customer-weldcom-14.0/{d.split('/')[1]}/__manifest__.py"
	if '/*' in d:
		print(d)
		continue
	d = '/'.join(d[1:].split('/')[1:])
	folder = d.split('/')[0]
	if not os.path.exists(f'{fname[:-16]}/{folder}'):
		os.makedirs(f'{fname[:-16]}/{folder}', exist_ok=True)
	if len(d.split('/')) >=3:
		folder = d.split('/')[1]
		if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{folder}"):
			os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{folder}", exist_ok=True)
	if len(d.split('/')) >=4:
		folder = d.split('/')[2]
		if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{folder}"):
			os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{folder}", exist_ok=True)
	if len(d.split('/')) >=5:
		folder = d.split('/')[3]
		if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{folder}"):
			os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{folder}", exist_ok=True)
	if len(d.split('/')) >=6:
		folder = d.split('/')[4]
		if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{d.split('/')[3]}/{folder}"):
			os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{d.split('/')[3]}/{folder}", exist_ok=True)
	if len(d.split('/')) >=7:
		folder = d.split('/')[5]
		if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{d.split('/')[3]}/{d.split('/')[4]}/{folder}"):
			os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{d.split('/')[3]}/{d.split('/')[4]}/{folder}", exist_ok=True)
	if len(d.split('/')) >=8:
		folder = d.split('/')[6]
		if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{d.split('/')[3]}/{d.split('/')[4]}/{d.split('/')[5]}/{folder}"):
			os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{d.split('/')[3]}/{d.split('/')[4]}/{d.split('/')[5]}/{folder}", exist_ok=True)
	if len(d.split('/')) >=9:
		folder = d.split('/')[7]
		if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{d.split('/')[3]}/{d.split('/')[4]}/{d.split('/')[5]}/{d.split('/')[6]}/{folder}"):
			os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{d.split('/')[3]}/{d.split('/')[4]}/{d.split('/')[5]}/{d.split('/')[6]}/{folder}", exist_ok=True)
	file_path = f'{fname[:-16]}/{d}'
	if os.path.exists(file_path):
		continue
	content = menus.read_image(1, f"{fname.split('/')[-2]},{d}")
	if content is not False:
		with open(f'{file_path}', 'wb') as fw2: 
			fw2.write(base64.decodebytes(content.encode()))
	else:
		print(file_path)

fnames = glob.glob('/home/royle/Viindoo/source_code/customer-weldcom-14.0/**/__manifest__.py')
for fname in fnames:
	manifest = {}
	with open(fname, 'r') as f2:
		manifest.update(ast.literal_eval(pycompat.to_text(f2.read())))
	for d in ['.pot', 'vi.po', 'vi_VN.po']:
		if '/*' in d:
			print(d)
			continue
		if d == '.pot':
			d = f"i18n/{fname.split('/')[-2]}.pot"
		else:
			d = f"i18n/{d}"
		folder = d.split('/')[0]
		if '/' not in d:
			print('xx %s' %fname)
		if '/' in d and not os.path.exists(f'{fname[:-16]}/{folder}'):
			os.makedirs(f'{fname[:-16]}/{folder}', exist_ok=True)
		if len(d.split('/')) >=3:
			folder = d.split('/')[1]
			if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{folder}"):
				os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{folder}", exist_ok=True)
		if len(d.split('/')) >=4:
			folder = d.split('/')[2]
			if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{folder}"):
				os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{folder}", exist_ok=True)
		if len(d.split('/')) >=5:
			folder = d.split('/')[3]
			if not os.path.exists(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{folder}"):
				os.makedirs(f"{fname[:-16]}/{d.split('/')[0]}/{d.split('/')[1]}/{d.split('/')[2]}/{folder}", exist_ok=True)
		file_path = f'{fname[:-16]}/{d}'
		if os.path.exists(file_path):
			continue
		content = menus.read_image(1, f"{fname.split('/')[-2]},{d}")
		if content:
			with open(f'{file_path}', 'wb') as fw2: 
				fw2.write(base64.decodebytes(content.encode()))

