#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

print('Set-Cookie: name="我是写入的数据信息";expires=Wed,28 Aug 2022 12:00:00 GMT')
print('Content-type: text/html', '<meta charset="utf-8"/>')

print()
print("""
<html>
  <head>
    <title>写入cookie信息</title>
  </head>
  <body>
    <h1>Cookie set OK！</h1>
  </body>
</html>
""")

# 以上实例使用了 Set-Cookie 头信息来设置 Cookie 信息，可选项中设置了 Cookie 的其他属性，
# 如过期时间 Expires，域名 Domain，路径 Path。这些信息设置在 "Content-type:text/html" 之前。
