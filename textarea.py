#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

# 引入 CGI 处理模块
import cgi, cgitb

# 创建 FieldStorage 的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "没有内容"

print("Content-type:text/html", '<meta charset="utf-8"/>')
print()
print("<html>")
print("<head>")
print("<title>菜鸟教程 CGI 实例</title>")
print("</head>")
print("<body>")
print("<h2>输入的内容是：%s</h2>" % text_content)
print("</body>")
print("</html>")