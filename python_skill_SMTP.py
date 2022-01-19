# SMTP发送邮件

"""
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装.

Python创建 SMTP 对象语法如下：
import smtplib
smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
参数说明：
host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:runoob.com，这个是可选参数。
port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。

Python SMTP对象使用sendmail方法发送邮件，语法如下：
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
参数说明：
from_addr: 邮件发送者地址。
to_addrs: 字符串列表，邮件发送地址。
msg: 发送消息
这里要注意一下第三个参数，msg是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。
"""
# 实例
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "from@runoob,com"
receivers = ["465994350@qq.com"]  # 接收邮件，可设置为你的邮箱

# 三个参数:1为文本内容 2 plain为文本格式 3设置编码
message = MIMEText("python 邮件发送测试...", "plain", "utf-8")
message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
message['Subject'] = Header("测试", 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message, message.as_string())
    print("邮件发送成功")
except:
    print("error：无法发送邮件")