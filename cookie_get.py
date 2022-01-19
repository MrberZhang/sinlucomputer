#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

# 导入模块
import os
import http.cookies

print("content-type:text/html", '<meat charset="utf-8" />')
print()

print("""
<html>
<head>
<title>读取写入的cookie信息</title>
</head>
<body>
<h1>读取cookie信息</h1>
""")

if "HTTP_COOKIE" in os.environ:
    cookie_string = os.environ.get("HTTP_COOKIE")
    c = http.cookies.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
        print("cookie data:" + data + "<br>")   # html中<br>换行的意思
    except:
    # except KeyError:
        print("cookie 没有设置或者已过期</br>")

print("</body>")
print("</html>")
