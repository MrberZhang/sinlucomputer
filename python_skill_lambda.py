# Python之lambda函数(匿名函数)

"""
lambda函数即为匿名函数，所谓匿名，意即不再使用 def 语句这种标准的形式定义一个函数；
匿名函数的使用是为了提高代码的性能，调用匿名函数时可绕过函数的栈分配；
匿名函数常用来表示函数内部仅包含 1 行表达式的函数。如果一个函数的函数体仅有 1 行表达式，则该函数就可以用 lambda 表达式来代替；

Python中使用lambda关键字创造匿名函数，其语法是：

    name = lambda [list] : expression表达式

解释：定义 lambda 表达式，必须使用 lambda 关键字；[list] 作为可选参数，等同于定义函数是指定的参数列表；
name 为该表达式的名称；expression 是一个参数表达式，表达式中出现的参数需要在[list]中有定义，
并且表达式只能是单行的，只能有一个表达式
"""

# 1.该语法格式等价于如下形式的普通函数形式:
'''
def name(list):
    return 表达式
name(list)
'''

def sum1(num1, num2):
    print(num1 + num2)


sum1(1, 2)

# 以上函数等价于如下lambda匿名函数
sum2 = lambda num1, num2: print(num1 + num2)
sum2(1, 2)

# 2.lambda特性
"""
lambda 函数是匿名的：
所谓匿名函数，通俗讲就是没有名字的函数。lambda函数没有函数名。

lambda 函数有输入和输出：
输入是传入到参数列表argument_list的值，输出是根据表达式expression计算得到的值。

lambda 函数拥有自己的命名空间：
lambda函数不能访问自己参数列表之外或全局命名空间里的参数，只能完成非常简单的功能。
"""
# 常见的lambda函数举例:
lambda x, y: x*y			# 函数输入是x和y，输出是它们的积x*y
lambda: None					# 函数没有输入参数，输出是None
lambda *args: sum(args)		# 输入是任意个数参数，输出是它们的和(隐性要求输入参数必须能进行算术运算)
lambda **kwargs: 1			# 输入是任意键值对参数，输出是1

# 3.lambda基础用法
"""将lambda函数赋值给一个变量，通过变量间接调用lambda函数"""
add1 = lambda x, y: x + y

"""#将lambda函数赋值给其他函数，将其他函数功能用该lambda函数替换 """

# 为了把标准库time中的sleep函数的功能屏蔽(Mock)，可以在程序初始化时调用：
import time

time.sleep = lambda x: None
# 这样，在后续代码中调用time库的sleep函数将不会执行原有的功能
# 例如：
time.sleep(3)   # 程序不会休眠 3 秒钟，而是因为lambda输出为None，所以这里结果是什么都不做


# A）、map()函数
"""
描述：map() 函数根据提供的函数对指定序列做映射；
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表；

语法：
map(function , sequence,...)

参数：
function - 函数
sequence - 一个或多个序列

返回值：
Python 2.x 版本返回列表
Python 3.x 版本返回迭代器
"""

# ===========一般写法：===========
# 1、计算平方数
# 定义一个函数，用于求平方
def square(x):
    return x ** 2


# 计算列表各个元素的平方
print("计算平方数一般写法:", map(square, [1, 2, 3, 4, 5]))

# 输出迭代器内容方法
listA = []
for i in map(square, [1, 2, 3, 4, 5]):
    listA.append(i)
print(listA)

# =========== 匿名函数写法：============
# 2、计算平方数，lambda函数写法
print("计算平方数，lambda函数写法:", list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

# 3、提供两个列表，将其相同索引位置的列表元素进行相加
print("将两个列表相同索引位置的列表元素进行相加:", list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))

# B）、reduce()函数
"""
描述：reduce() 函数会对参数序列中元素进行累积；
函数将一个数据集合（列表、元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，以此类推，最后得到一个结果；

语法：
reduce(function , sequence , init)

参数：
function - 函数，有两个参数
sequence - 可迭代对象(列表、元祖、集合等)
init - 可选参数，初始参数

返回值：
返回函数计算结果
"""

# 把序列 [a, b, c, d, e]变换成整数 abcde，reduce()实现：

from functools import reduce


def fun(x, y):
    if y < 10:
        return x * 10 + y
    else:
        return x * 100 + y


listA = [2, 4, 6, 8, 10, 12, 14]
print("输出结果为：", reduce(fun, listA))


# ===========一般写法：===========
from functools import reduce

# 1、两数相加
def add(x, y):
    return x + y


# 计算列表元素和：1+3+5+7+9
print("计算列表元素和:", reduce(add, [1, 3, 5, 7, 9]))

"""
===========执行步骤解析：===========
调用 reduce(add, [1, 3, 5, 7, 9])时，reduce函数将做如下计算：
1	先计算头两个元素：f(1, 3)，结果为4；
2	再把结果和第3个元素计算：f(4, 5)，结果为9；
3	再把结果和第4个元素计算：f(9, 7)，结果为16；
4	再把结果和第5个元素计算：f(16, 9)，结果为25；
5	由于没有更多的元素了，计算结束，返回结果25。
"""

# ===========匿名函数写法：===========
# 2、两数相加，lambda 写法
print("两数相加，lambda 写法:", reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


# C）、sorted()函数
"""
描述：sorted() 函数对所有可迭代的对象进行排序操作
语法：
sorted ( sequence , key , reverse )

参数：
sequence  -- 可迭代对象；
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序；
reverse -- 排序规则：reverse = True 降序 ， reverse = False 升序（默认）；

返回值：返回重新排序的列表

注意：sort 与 sorted 区别：
list.sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作；
list 的 sort 方法返回的是对已经存在的列表进行操作(不会新建新的list)，而内建函数 sorted 方法返回的是一个新的 list，
而不是在原来的基础上进行的操作(会新建新的list)
"""
# sorted() 函数对所有可迭代的对象进行排序操作

setA = {1, 3, 2, 4, 5, 7, 9}
# 默认升序排序
print("默认升序排序:" , sorted(setA))
# 利用key进行倒序排序
print("利用key进行倒序排序:", sorted(setA, key=lambda x: x * -1))
# 利用key进行升序排序
print("利用key进行升序排序:", sorted(setA, key=lambda x: x * 1))
# 利用参数 reverse排序： True 降序 ；False 升序（默认）
print("利用参数 reverse排序： True 降序", sorted(setA, reverse=True))
print("利用参数 reverse排序： False 升序（默认）", sorted(setA, reverse=False))

# ===========一般用法：===========
# 1、简单排序
a = [5, 7, 6, 3, 4, 1, 2]
# 使用sorted，保留原列表，不改变列表a的值
b = sorted(a)
print("原列表a为：", a)
print("排序后列表b为：", b)

# ===========匿名函数用法：===========
L = [('b', 2), ('a', 7), ('c', 11), ('d', 4), ('f', 9), ('e', 6)]
print("利用参数 key 排序，数字排序，默认升序：", sorted(L, key=lambda x: x[1]))
print("利用参数 key 排序，数字排序，降序：", sorted(L, key=lambda x: -x[1]))  # 当比较对象为数字时，-x表示降序，等同于reverse=True
print("利用参数 key 排序，字母排序，默认升序：", sorted(L, key=lambda x: x[0]))  # 当比较对象为字母时，x表示升序，等同于reverse=Flase
print("利用参数 key 排序，字母排序，降序：", sorted(L, key=lambda x: x[0], reverse=True))
# 4、按年龄升序，默认升序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print("按年龄升序，默认升序:", sorted(students, key=lambda s: s[2]))
# 5、按年龄升序
print("按年龄降序：", sorted(students, key=lambda s: s[2], reverse=True))

# 单列排序
# sorted()的应用，也可以通过 key 的值来进行数组/字典的排序
array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
print("age字段降序排列：", sorted(array, key=lambda x: x["age"], reverse=True))

# 多列排序
ListB = [{'name': 'alice', 'score': 38, "height": 170},
         {'name': 'bob', 'score': 18, "height": 175},
         {'name': 'darl', 'score': 28, "height": 160},
         {'name': 'christ', 'score': 28, "height": 185}]
# 先按照成绩降序排序，相同成绩的按照身高升序排序：
print("先按照成绩降序排序，相同成绩的按照身高升序排序：", sorted(ListB, key=lambda x: (-x['score'], x['height'])))


# D）、filter()函数
"""
描述：filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表(新建列表)
函数接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中

语法：
filter(function, iterable)

参数：
function -- 判断函数
iterable  -- 可迭代对象

返回值：
返回由符合条件元素组成的新列表
注意: Pyhton2.x 返回列表，Python3.x 返回迭代器对象
"""


# ===========一般用法：===========
# 1、过滤出列表中的所有奇数
def is_odd(n):
    return n % 2 == 1  # 奇数

# 结果降序排列
print("筛选出列表中所有奇数，结果降序排列：",
      sorted(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 20, 12, 15, 11, 14]), key=lambda x: -x))

# ===========匿名函数用法：===========
# 2、将列表[1, 2, 3]中能够被3整除的元素过滤出来
new_list = filter(lambda x: x % 3 == 0, [1, 2, 3, 6, 10, 15])
print(list(new_list))
