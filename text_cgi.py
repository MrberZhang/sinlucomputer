#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

import os

print("Content-type:text/html", '<meta charset="utf-8"/>')
print()
print("<b>环境变量</b><br>")
print("<ul>")
for key in os.environ.keys():
    print("<li><span style='color=green'>%30s </span> : %s </li>" % (key, os.environ[key]))
print('</ul>')
