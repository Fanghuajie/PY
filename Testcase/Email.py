import logging
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage:

    def send_mail(self, file_path):
        # 定义SMTP服务器
        smtpserver = 'smtp.163.com'
        # 发送邮件的用户名和密码
        username = 'ezhoufhj@163.com'
        password = 'QGIWPHCMIZAHGMWG'  # 授权码
        # 接收邮件的邮箱
        receiver = '851868241@qq.com'
        # 创建邮件对象
        message = MIMEMultipart('related')
        subject = '自动测试化报告'
        # fujian = MIMEText(open(file_path1, 'rb').read(), 'html', 'utf-8')
        Text = MIMEText("Dear FHJ,\n 详细报告见附件")
        attment = MIMEApplication(open(file_path, 'rb').read())
        attment.add_header('Content-Disposition', 'attachment', filename='auto_report.html')
        # 把邮件信息封装到邮件对象中
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(Text)
        message.attach(attment)
        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        logging.info("邮件发送成功")
        smtp.quit()

