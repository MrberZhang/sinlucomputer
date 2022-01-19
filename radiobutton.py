#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

# 引入CGI处理模块
import cgi, cgitb

# 创建FieldStorage()的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = "提交数据为空"

print("Content-type:text/html", '<meta charset="utf-8"/>')
print()
print("<html>")
print("<head>")
print("<title>菜鸟教程 CGI 实例</title>")
print("</head>")
print("<body>")
print("<h2>选中的网站是：%s</h2>" % site)
print("</body>")
print("</html>")

# 通过CGI程序传递Radio数据（radio单选框）radio 只向服务器传递一个数据
