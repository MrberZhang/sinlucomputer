#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

# 引入CGI处理模块
import cgi, cgitb

# 创建Fieldstorage()的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('google'):
    google_flag = '是'
else:
    google_flag = '否'

if form.getvalue('runoob'):
    runoob_flag = '是'
else:
    runoob_flag = '否'

print("Content-type:text/html", '<meta charset="utf-8"/>')
print()
print("<html>")
print("<head>")
print("<title>菜鸟教程CGI实例</title>")
print("</head>")
print("<body>")
print("<h2>菜鸟是否选择了：%s</h2>" % runoob_flag)
print("<h2>google 是否选择了：%s</h2>" % google_flag)
print("</body>")
print("</html>")
