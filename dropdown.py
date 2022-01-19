#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

import cgi, cgitb

# 创建 FieldStorage 的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('dropdown'):
    dropdown_value = form.getvalue('dropdown')
else:
    dropdown_value = "没有内容"

print("Content-type:text/html", '<meta charset="utf-8"/>')
print()
print("<html>")
print("<head>")
print("<title>菜鸟教程 CGI 实例</title>")
print("</head>")
print("<body>")
print("<h2>选中的选项是：%s</h2>" % dropdown_value)
print("</body>")
print("</html>")
