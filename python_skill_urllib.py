# Python urllib
"""Python urllib 库用户操作网页URL，并对网页的内容进行抓取处理。
本文主要介绍Python3的urllib。
urllib 包 包含以下几个模块：
· urllib.request - 打开和读取URL
· urllib.error - 包含urllib.request 抛出的异常
· urllib.parse - 解析URL
· urllib.robotparser - 解析robots.txt文件  """

# urllib.request
"""urllib.request 定义了一些打开URL的函数和类，包含授权验证、重定向、浏览器Cookies等。
urllib.request 可以模拟浏览器的一个请求发起过程。
我们可以使用urllib.request 的 urlopen 方法 来打开一个URL，语法格式如下：
url.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None) 
参数：
·url:   url 地址
·data： 发送到服务器的其他数据对象，默认为None 
·timeout： 设置访问超时时间
·cafile 和capath：cafile为CA证书，capath为CA证书路径，使用HTTPS需要用到
·cadefault: 已经被弃用
·context : ssl.SSLContext 类型，用来指定SSL设置 """

# 实例如下：
from urllib.request import urlopen
myURL = urlopen("https://www.runoob.com/")
print(myURL.read())  # 打开一个链接URL，使用read() 函数读取网页的HTML实体代码 read()读取整个网页内容，其参数可以指定长度

# # readline() - 读取文件的一行内容
from urllib.request import urlopen
myURL = urlopen("https://www.runoob.com/")
print(myURL.readline())

# readlines() - 读取文件的全部内容，它会把读取的内容赋值给一个列表变量。
from urllib.request import urlopen
myURL = urlopen("https://www.runoob.com/")
lines = myURL.readlines()
for line in lines:
    print(line)

# 我们对网页进行抓取时，经常需要判断网页时候可以正常访问，这里我们就可以使用getcode()函数获取网页状态码，返回200说明网页正常，返回404说明网页不存在
import urllib.request
myURL1 = urllib.request.urlopen("https://www.runoob.com/")
print(myURL1.getcode())

try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)

# 如果需要将抓取的网页保持到本地，可以使用File write()方法
# import urllib.request
# myURL3 = urllib.request.urlopen("https://www.runoob.com/")
# f = open("runoob.html", "wb")
# content = myURL3.read()
# f.write(content)
# f.close()
#
# # URL 的解码与编码可以使用urllib.request.quote() 与 urllib.request.unquote()方法：
# import urllib.request
# encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
# print(encode_url)
#
# unencode_url = urllib.request.unquote(encode_url)  # 解码
# print(unencode_url)

# 模拟头部信息
"""我们抓取页面一般需要对headers(网页头信息)进行模拟，这时候需要使用urllib.request.Request类：
class urllib.request.Request(url, data=None, headers = {}, origin_req_host=None, unverifiable=False,method=None)
参数：
· url ： url地址
· data ： 发送到服务器的其他数据对象，默认为None 
· headers ： HTTP请求的头部信息，子典格式 
· origin_req_host : 请求的主机地址，IP或域名
· unverifiable : 很少用整个参数，用户设置网页时候需要验证，默认是False
· method ： 请求方法，如GET、POST、DELETE、PUT 等 """
# 实例 py3_urllib_text.php 文件代码
import urllib.request
import urllib.parse

url = "https://www.runoob.com/?s="  # 菜鸟教程搜索页面
keyword = "Python 教程"
key_code = urllib.request.quote(keyword)  # 对请求进行编码
url_all = url+key_code
header = {
    'User-Agent': 'Mozilla/5.0 (x11;Fedora;Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}  # 头部信息
request = urllib.request.Request(url_all, headers=header)
reponse = urllib.request.urlopen(request).read()

fh = open("urllib_test_runoob_search.html", "wb")
fh.write(reponse)
fh.close()

# 表单使用POST 传递数据，我们先创建一个表单，代码如下，我这里使用PHP代码来获取表单的数据：
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8">
# <titile>菜鸟教程(runoob.com) urllib POST 测试 </titile>
# </head>
# <body>
# <from action="" method="post" name="myForm">
#     Name:<input type="text" name="name"><br>
#     Tag:<input type="text" name="tag"><br>
#     <input type="submit" value="提交">
# </form>
# <hr>
# <?PHP
# // 使用PHP来获取表单提交的数据，你可以换成其他的
# if(isset($_POST['name']) && $_POST['tag'] ){
# echo $_POST['name'] . '，' .$_POST['tag'];
# }
# ?>
# </body>
# </html>

# 实例
import urllib.request
import urllib.parse

url = "https://www.runoob.com/try/py3/py3_urllib_text.php"  # 提交到表单页面
data = {'name': "Runoob", "tag": "菜鸟教程"}  # 提交数据
header = {
    'User-Agent': 'Mozilla/5.0 (x11;Fedora;Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

data = urllib.parse.urlencode(data).encode("utf-8")  # 对参数进行编码，解码使用 urllib.parse.urldecode
request1 = urllib.request.Request(url, data, header)   # 请求处理
reponse1 = urllib.request.urlopen(request1).read()

fh = open("urllib_text_post_runoob.html", "wb")  # 将文件写入到当前目录中
fh.write(reponse1)
fh.close()


# urllib.error
"""urllib.error 模块为 urllib.request 所引发的异常定义了异常类，基础异常类是 URLError.
urllib.error 包含两个方法，URLError 和 HTTPError。
URLError 是OSError 的一个子类，用于处理程序在遇到问题时会引发此异常（或其派生的异常），包含的属性reason 为引发异常的原因，
HTTPError 是URLError 的一个子类，用户处理特殊HTTP错误例如作为认证请求的时候，包含属性code 的为HTTP 的状态码，reason为引发异常的原因，
headers 为导致HTTPError的特定HTTP 请求的 HTTP响应头  """
# 对不存在网页抓取并处理异常，实例：
import urllib.request
import urllib.error

myURL4 = urllib.request.urlopen("https://www.runoob.com/")
print(myURL4.getcode())

try:
    myURL5 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)

# urllib.parse
"""urllib,parse 用于解析URL，格式如下：
urllib.parse.urlparse(urlstring,scheme="",allow_fragments=True)
urlstring 为字符串的url 地址，scheme 为协议类型
allow_fragneebts 参数为false，这无法识别片段标识符。相反他们被解析为路径，为参数或查询组件的一部分，并 fragment 在返回值中设置为空字符串。  """
# 实例
from urllib.parse import urlparse

o = urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o)
"""从结果可以看出，内容是一个元组，包含 6 个字符串：协议，位置，路径，参数，查询，判断。
w我们可以直接读取协议内容："""
print(o.scheme, o.netloc)

# 完整内容如下：
"""
属性               索引          值           值（如果不存在）
scheme              0       URL协议           scheme参数
netloc              1       网络位置部分          空字符串
path                2       分层路径             空字符串
params              3       最后路径元素的参数     空字符串
query               4       查询组件             空字符串 
fragment            5       片段识别             空字符串
username                    用户名                None
password                    密码                  None
hostname                    主机名(小写)           None
prot                        端口号为整数（如果存在）  None  """

# urllib.robotparser
"""urllib.robotparser 用户解析robot.txt 文件。
robots.txt （统一小写） 是一种存放与网站跟目录下的robots 协议，它通常用户告诉搜索引擎对网站的抓取规则。
urllib.robotparser 提供了 RobotFileParser 类，语法如下："""
# class urllib.robotparser.RobotFileParser(url ="")
"""这个类提供了一些可以读取、解析robot.txt 文件的方法：
·set_url(url) - 设置robots.txt文件的URL。
·read() - 读取robots.txt URL 并将其输入解析器。 
·parse(lines) - 解析行参数。
·can_fetch(useragent,url) - 如果允许useragent按照被解析 robots.txt 文件中的规则来获取 url 则返回 True。
·mitime() - 返回最近一次获取robots.txt 文件的时间。这适用于需要定期检查 robots.txt 文件更新情况的长时间运行的网页爬虫。
·modified() - 将最近一次获取robots.txt文件的时间设置为当前时间。
·crawl_delay(useragent) - 以named tuple RequestRate(requests,seconds)的形式从robots.txt返回Request-rate 形参的内容。
如果此形参不存在或不适用于指定的useragent 或者此形参的robots.txt 条目存在语法错误，则返回None。
·site_maps() - 以list（）的形式从robots.txt返回Sitemap 形参的内容，如果此形参不存在，或者此形参的robots.txt条目存在语法错误，则返回None。 """
# 实例
import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")
rp.read()
rrate = rp.request_rate("*")
print(rrate.requests)  # 3
print(rrate.seconds)   # 20
# rp.crawl_delay("*")  # 6
# rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")  # False
# rp.can_fetch("*", "http://www.musi-cal.com/")  # True
