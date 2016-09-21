#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

mail_host = 'smtp.163.com'
mail_user = 'yxgtianya@163.com'
mail_pass = '#dzw**' 

sender = 'yxgtianya@163.com'
receivers = ['yuxuguang@weiche.cn']

message = MIMEMultipart()
#message = MIMEText('附件为测试报告', 'plain', 'utf-8')
h = Header('yxgtinaya@163.com', 'utf-8')
h.append('<yxgtianya@163.com>', 'ascii')
message["From"] = h
message['To'] =  'yuxuguang@weiche.cn'

subject = 'Test_report'
message['Subject'] = Header(subject, 'utf-8')

file_open = open('d:\\result.html')
try:
	all_the_html = file_open.read()
#	print all_the_html
finally:
	file_open.close()
	
message_html = all_the_html
message.attach(MIMEText(message_html, 'html', 'utf-8'))

att1 = MIMEText(open('d:\\result.html', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="result.html"'
message.attach(att1)

def send_report():
	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host)
		smtpObj.login(mail_user, mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print 'send mail sucessed'
	except smtplib.SMTPException:
		print 'send mail failed'
		
	