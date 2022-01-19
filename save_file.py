#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

import os
import cgi
import cgitb; cgitb.enable()

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径
    fn = os.path.basename(fileitem.filename)
    open('E:/' + fn, 'wb').write(fileitem.file.read())  # 'E:/' 这里写入的路径目录要对应到自己的服务器目录，不然写入会出错
    message = '文件 "'+fn+'" 上传成功'
else:
    message = "文件上传不成功"

print("Content-type:text/html", '<meta charset="utf-8"/>')
print()

print("""
<html>
<head>
<title>上传文件</title>
</head>
<body>
<p>%s<p>
</body>
</html>
""" % (message,))
