# Python中的三元表达式
# result = 为真时的结果 if 判断条件 else 为假时的结果

# 示例:
x = 1
y = 2
result = x if x > y else y  # 如果条件成立，将x的值赋给result
print(result)

# 上面的三元表达式等价于

x = 1
y = 2
if x > y:
    result = x
else:
    result = y

print(result)

"""1. 结合函数结合使用"""


# 示例一: 求两个参数的最大值

def max2(x, y):
    return x if x > y else y  # 取两个值的比较大的


max2(1, 3)


# 示例二: 斐波那契数列

def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(10)])

"""2. 结合匿名函数使用"""
s = map(lambda x, y: x - y if x > y else y - x, [2, 1, 3], [4, 3, 1])  # 两个列表相减并保证不为负
print(list(s))

"""3. 结合列表推导使用"""
# 示例一: 将0-9的10个数，奇数用0表示，偶数用1表示
s2 = [0 if i % 2 == 0 else 1 for i in range(10)]
print(s2)

# 示例二: 常规写法
x = 100
L = []
L.append(1 if x > 0 else 0)
print(L)

"""4. 在处理Json格式中的一个典型应用"""
# 使用三元表达式的写法,一般的写法，可以看见，使用三元表达式的写法要简洁的多!

"""5. 三元表达式的一个变种"""
cond = True
name = ["Cat", "Tom"][bool(cond)]
print(name)
cond = ""
name = ["Cat", "Tom"][bool(cond)]
print(name)
