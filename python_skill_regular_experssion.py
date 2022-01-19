# python 正则表达式

"""
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。
"""

# re.match方法
"""
尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()返回None，
# 语法: re.match(pattern, string, flags=0)
# pattern-匹配的正则表达式
# string-要匹配的字符串
# flags-标志位，用于控制正则表达式的匹配方式。如：是否区分大小写，多行匹配等等。
匹配成功re.match()返回一个匹配对象，否则返回None。我们可以使用group(num)或groups()匹配对象函数来获取匹配表达式
"""
# group(num=0)-匹配的整个表达式的字符串，group()可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()-返回一个包含所有小组字符串的元组，从1到所含的小组号


import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配成功 span() 返回匹配成功的整个字符串索引
print(re.match('com', 'www.runoob.com'))       # 不在起始位置匹配成功


# 实例
import re

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符(\r,\n)之外的任何单个或多个字符
# （.*?） 表示"非贪婪"模式，只保存第一个匹配到的子串
matchobj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchobj:
    print("matchobj.group():", matchobj.group())
    print("matchobj.group(1):", matchobj.group(1))
    print("matchobj.group(2):", matchobj.group(2))
    print("matchobj.groups():", matchobj.groups())
else:
    print("No match!!")

# re.search 方法
"""
re.search 扫描整个字符串并返回第一个成功的匹配。
函数语法： re.search(pattern, string, flags=0)
参数：pattern 匹配正则表达式
string 要匹配的字符串
flags 标志位，用于控制正则表达式的匹配方式。如：是否区分大小写，多行匹配等等。
匹配成功re.search方法返回一个匹配的对象，否则返回None。
group(num=0)-匹配的整个表达式的字符串，group()可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()-返回一个包含所有小组字符串的元组，从1到所含的小组号
"""
import re
print(re.search('www', 'www.runoob.com').span())    # 在起始位置匹配成功 span()转换成元组输出
print(re.search('com', 'www.runoob.com').span())    # 不在起始位置匹配成功

# 实例
import re

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符(\r,\n)之外的任何单个或多个字符
# （.*?） 表示"非贪婪"模式，只保存第一个匹配到的子串
serachobj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchobj:
    print("serachobj.group():", serachobj.group())
    print("serachobj.group(1):", serachobj.group(1))
    print("serachobj.group(2):", serachobj.group(2))
    print("serachobj.groups():", serachobj.groups())
else:
    print("Nothing found!!")

# re.match与re.search的区别
"""
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，
而 re.search 匹配整个字符串，直到找到一个匹配。
"""
import re

line = "Cats are smarter than dogs"
matchobj = re.match(r"dogs", line, re.M | re.I)
if matchobj:
    print("match --> matchboj.group():", matchobj.group())
else:
    print("No match!!")

serachobj = re.search(r'dogs', line, re.M | re.I)
if serachobj:
    print("search --> serachobj.group():", serachobj.group(), "索引位置：", serachobj.span())
else:
    print("Nothing found!!")


# 检索和替换
# re.sub 方法
"""
Python 的re模块提供了re.sub用户替换字符串中的匹配项
语法： re.sub(pattern, repl, string, count=0,flags=0)
参数：pattern-正则中的模式字符串。
repl-替换的字符串，也可以是一个函数
string-要被查找替换的原始字符串
count-模式匹配后替换的最大次数，默认0表示替换所有的匹配
flags-编译时用的匹配模式，数字形式
前3个参数必选参数，后2个为可选参数
"""
import re
phone = "2004-959-559"  # 这是一个电话号码

num = re.sub(r'#.*$', "", phone)  # 删除注释
print("电话号码：", num)

num = re.sub(r'\D', "", phone)  # 移除非数字内容
print("电话号码：", num)


import re
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'

print(re.sub('(?P<value>\d+)', double, s))  # 当repl参数是一个函数时


# compile 方法
"""
compile函数用户编译正则表达式，生成一个正则表达式(pattern)对象，供match()和search()这两个函数使用
语法： re.compile(pattern[,flags])
参数：pattern-一个字符串的正则表达式
flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
  re.I 忽略大小写
  re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
  re.M 多行模式
  re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
  re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
  re.X 为了增加可读性，忽略空格和' # '后面的注释
"""

import re
pattern = re.compile(r'\d+')        # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')     # 查找头部，没有匹配
print(m)
# None
m = pattern.match('one12twothree34four', 2, 10)   # 从'e'的位置开始匹配，没有匹配
print(m)
# None
m = pattern.match('one12twothree34four', 3, 10)   # 从'1'的位置开始匹配，正好匹配
print(m)                                          # 返回一个 Match 对象
# <_sre.SRE_Match object at 0x10a42aac0>
print(m.group(0))   # 可省略0
# '12'
print(m.start(0))   # 可省略0 # start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# 3
print(m.end(0))     # 可省略0 # end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# 5
print(m.span(0))    # 可省略0 # span([group]) 方法返回 (start(group), end(group))。
# (3, 5)

# 在上面，当匹配成功时返回一个 Match 对象，其中：
# group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；

# 实例
import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I表示忽略大小写 () ()表示匹配只有2组
m = pattern.match('Hello World Wide Web')
print(m)            # 匹配成功，返回一个match对象
print(m.group())    # 返回匹配成功的整个子串
print(m.span())     # 返回匹配成功的整个字符串索引
print(m.group(1))   # 返回第一个匹配成功的字串
print(m.span(1))    # 返回第一个分组匹配成功的子串的索引
print(m.group(2))   # 返回第二个分组匹配成功的子串
print(m.span(2))    # 返回第二个分组匹配成功的子串索引
print(m.groups())   # 等价于 (m.group(1), m.group(2),...）
# print(m.group(3))   # 不存在第三个分组,会报错


# findall 方法
"""
在字符串中找到正则表达是所匹配的所有字串，并返回一个列表，如果有多个匹配的模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
注意：match 和 search 是匹配一次，findall匹配所有
语法： re.findall(pattern,string,flags=0) 或 pattern.findall(string[,pos[,endpos]])
参数：pattern-匹配模式
string-待匹配的字符串
pos-可选参数，指定字符串的起始位置，默认0
endpos-可选参数，指定字符串的结算位置，默认为字符串长度。
"""

# 查找字符串中的所有数字
import re
result1 = re.findall(r'\d+', 'runoob 123 google 456')
pattern = re.compile(r'\d+')    # 查找数字
result2 = pattern.findall("runoob 123 google 456")
result3 = pattern.findall('runoob 123 google 456', 0, 10)  # 匹配索引位置在0-10的字符

print(result1)
print(result2)
print(result3)

# 多个匹配模式，返回元组列表
import re
result = re.findall(r'(\w+)=(\d+)', "sett width=20 and height=10")
print(result)

# re.finditer 方法
"""
和findall类似，在字符串中找到正则表达式所匹配的所有字串，并把他们作为一个迭代器返回。
语法： re.finditer(pattern,string,flags)
pattern-匹配的正则表达式
string-要匹配的字符串。
flags-标志位，用于控制正则表达式的匹配方式.
"""
import re
it = re.finditer(r"\d+", "12a32bd43jf3")
print(it)
for match in it:
    print(match.group())

# re.split 方法
"""
split 方法按照能够匹配的子串将字符串分割后返回列表，
语法： re.split(pattern, string[, maxsplit=0, flags=0])
pattern-匹配的正则表达式
string-要匹配的字符串。
maxsplit-分割次数，maxsplit=1分割一次，默认为 0，不限制次数。
flags-标志位，用于控制正则表达式的匹配方式.
"""
import re
s1 = re.split("\W+", 'runoob, runoob, runoob.')
print(s1)
s2 = re.split("(\W+)", ' runoob, runoob, runoob.')
print(s2)
s3 = re.split("\W+", ' runoob, runoob, runoob.', 1)
print(s3)

s = re.split('a *', 'hello world')   # 对于一个找不到匹配的字符串而言，split不会对其作出分割
print(s)
