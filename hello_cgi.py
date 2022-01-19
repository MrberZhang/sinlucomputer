#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

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
