# Python CGI编程

"""什么是CGI
CGI 目前由NCSA维护，NCSA定义CGI如下：
CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。  """

# 网页浏览
# import http.cookies
"""为了更好的了解CGI是如何工作的，我们可以从在网页上点击一个链接或URL的流程：
1、使用你的浏览器访问URL并连接到HTTP web 服务器。
2、Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容，否则返回错误信息。
3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息。
CGI程序可以是Python脚本，PERL脚本，SHELL脚本，C或者C++程序等。 """

# Web服务器支持及配置 需要先配置Apache
"""在你进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序。
Apache 支持CGI 配置： """


# 第一个CGI程序
"""我们使用Python创建第一个CGI程序，文件名为hello.py，文件位于/var/www/cgi-bin目录中，内容如下："""
#!C:/Users/zhangwei/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type:text/html", '<meta charset="utf-8"/>')
print()  # 空行，告诉服务器结束头部
print('<html>')
print('<head>')
# print('<meta charset="utf-8"/>')   # 注释掉这句，访问正常显示中文，添加上显示中文就是乱码
print('<title>Hello - 我的第一个 CGI 程序！</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! 我是来自菜鸟自学的第一CGI程序</h2>')
print('</body>')
print('</html>')

# GET和POST方法
# 浏览器客户端通过两种发放向服务器传递信息，这两种方法就是GET方法和POST方法。
# 使用GET方法传输数据
"""
GET方法发送编码后的用户信息到服务端，数据信息包含在请求页面的URL上，以"?"号分隔，
如下所示：http://www.test.com/cgi-bin/hello.py?key1=value1&key2=value2
有关GET请求的其他一些注释：
·GET请求可被缓存
·GET请求保留在浏览器历史记录中
·GET请求可被收藏为书签
·GET请求不应在处理敏感数据时使用
·GET请求有长度限制
·GET请求只应当用户取回数据
"""
# 简单的url实例：GET方法
# /cgi-bin/test.py?name=菜鸟教程&url=http://www.runoob.com

#!C:/Users/zhangwei/AppData/Local/Programs/Python/Python39/python.exe

# CGI处理模块
import cgi, cgitb

# 创建FieldStorage的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html", '<meta charset="utf-8"/>')
print()
print('<html>')
print('<head>')
print("<title>菜鸟教程 CGI 测试实例</title>")
print('<head>')
print("<body>")
print("<h2> %s <h2>" % (site_name, site_url))
print("</body>")
print('<html>')

# 简单的表单实例：GET方法
"""以下是一个通过HTML的表单使用GET方法向服务器发送两个数据，提交的服务器脚本同样是hello_get.py文件，hello_get.html 代码如下："""
#HTML代码
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/hello_get.py" method="get">
站点名称: <input type="text" name="name">  <br />

站点 URL: <input type="text" name="url" />
<input type="submit" value="提交" />
</form>
</body>
</html>
'''


# 使用POST方法传递数据 同样的hello_get.py源文件，处理POST方法传递过来的数据
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/hello_get.py" method="post">
站点名称: <input type="text" name="name">  <br />

站点 URL: <input type="text" name="url" />
<input type="submit" value="提交" />
</form>
</body>
</html>
</form>
'''


# 通过CGI程序传递checkbox数据(checkbox多选框)
# checkbox用于提交一个或者多个选项数据，HTML代码如下:
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/checkbox.py" method="POST" target="_blank">
<input type="checkbox" name="runoob" value="on" /> 菜鸟
<input type="checkbox" name="google" value="on" /> Google
<input type="submit" value="选择站点" />
</form>
</body>
</html>
'''
# 以下为 checkbox.py 文件的代码
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


# 通过CGI程序传递Radio数据（radio单选框）
# Radio 只向服务器传递一个数据，HTML代码如下：
"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/radiobutton.py" method="POST" target="_blank">
<input type="radio" name="site" value="runoob" /> 菜鸟教程
<input type="radio" name="site" value="google" /> Google
<input type="submit" value="提交" />
</form>
</body>
</html>
"""
# radiobutton.py 脚本代码如下：

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


# 通过CGI程序传递Textarea数据 (文本框)
# Textarea 向服务器传递多行数据，HTML 代码如下：
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/textarea.py" method="post" target="_blank">
<textarea name="textcontent" cols="40" rows="4">
在这里输入内容...
</textarea>
<input type="submit" value="提交" />
</form>
</body>
</html>
'''
# textarea.py 脚本代码如下：
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


# 通过CGI程序传递下拉数据。
# HTML下拉框代码如下，命名为dropdown.html：
"""
<!DOCTYPR html>
<html>
<head>
    <meta charset="utf-8">
    <title>菜鸟(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/dropdown.py" method="POST" target="_blank">
<select name="dropdown">
    <option value="" selected></option>>
    <option value="google" >Google</option>>
    <option value="runoob">菜鸟教程</option>
</select>>
<input type="submit" value="提交" />
</form>
</body>
</html>
"""
# dropdown 脚本如下：
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


# CGI中使用Cookie
'''
在 http 协议一个很大的缺点就是不对用户身份的进行判断，这样给编程人员带来很大的不便， 而 cookie 功能的出现弥补了这个不足。
cookie 就是在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据 ，当下次客户访问脚本时取回数据信息，
从而达到身份判别的功能，cookie 常用在身份校验中。
'''
# http cookie的发送是通过http头部来实现的，他早于文件的传递，头部set-cookie的语法如下：
'''
Set-cookie:name=name;expires=date;path=path;domain=domain;secure
name=name:需要设置cookie的值（name不能使用“；”和“，”），有多个name时用“;”分隔。例如：name1=name1;name2=name2;name3=name3
expires=date:cookie的有效期限，格式：expires="Wdy,DD-Mon-YYYY HH:MM:SS"
path=path:设置cookie支持的路径，如果path是一个路径，则cookie对这个目录下的所有文件及子目录有效，
例如：path="/cgi-bin/",如果path是一个文件，则cookie指对这个文件生效，例如：path="/cgi-bin/cookie.cgi"。
domain=domain:对cookie生效的域名，例如domain="www.runoob.com"
secure:如果给出此标志，表示cookie只能够通过SSL协议的https服务器来传递。
cookie的接收是通过设置环境变量HTTP_COOKIE来实现的，CGI程序可以通过检索该变量获取cookie信息
'''


# Cookie设置
'''Cookie的 设置非常简单，cookie 会在 http 头部单独发送。以下实例在 cookie 中设置了 name 和 expires：'''
#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

print('Set-Cookie: name="菜鸟教程";expires=Wed, 28 Aug 2016 18:30:00 GMT')
print('Content-Type: text/html', '<meta charset="utf-8">')

print()
print("""
<html>
  <head>
    <title>菜鸟教程(runoob.com)</title>
  </head>
    <body>
        <h1>Cookie set OK!</h1>
    </body>
</html>
""")

'''以上实例使用了 Set-Cookie 头信息来设置 Cookie 信息，可选项中设置了 Cookie 的其他属性，
如过期时间 Expires，域名 Domain，路径 Path。这些信息设置在 "Content-type:text/html" 之前。'''


# 检索Cookie信息
'''
Cookie信息检索页非常简单，Cookie信息存储在CGI的环境变量HTTP_COOKIE中，存储格式如下：
key1=value1;key2=value2;key3=value3....
'''

# 以下是一个简单的CGI检索cookie信息的程序：

#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

# 导入模块
import os
import http.cookies

print("Content-type: text/html", '<meta charset="utf-8">')
print()

print("""
<html>
<head>
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h1>读取cookie信息</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = http.cookies.SimpleCookie()
   # c=Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
        print("cookie data: "+data+"<br>")
    except KeyError:
        print("cookie 没有设置或者已过去<br>")
print("""
</body>
</html>
""")
# 将以上代码保存到 cookie_get.py

# 文件上传实例
# HTML设置上传文件的表单需要设置 enctype 属性为 multipart/form-data，代码如下所示：
"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
 <form enctype="multipart/form-data" 
                    action="/cgi-bin/save_file.py" method="post">
   <p>选中文件: <input type="file" name="filename" /></p>
   <p><input type="submit" value="上传" /></p>
   </form>
</body>
</html>
"""
# save_file.py 脚本文件代码如下：
# !/usr/bin/python3

import cgi, os
import cgitb;

cgitb.enable()

form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径
    fn = os.path.basename(fileitem.filename)
    open('/tmp/' + fn, 'wb').write(fileitem.file.read())  # '/tmp/' 为服务器目录要对应，不然会出错

    message = '文件 "' + fn + '" 上传成功'

else:
    message = '文件没有上传'

print("""\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,))

# 文件下载对话框
# 我们先在当前目录下创建 foo.txt 文件，用于程序的下载。
# 文件下载通过设置HTTP头信息来实现，功能代码如下：
#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

# HTTP 头部
print("Content-Disposition: attachment; filename=\"foo.txt\"")
print()
# 打开文件 path路径要一致
fo = open("foo.txt", "rb")

str1 = fo.read()
print(str1)

# 关闭文件
fo.close()
