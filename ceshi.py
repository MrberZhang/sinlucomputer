"""from functools import reduce


def fun(x, y):
    if y < 10:
        return x * 10 + y
    else:
        return x * 100 + y


listA = [2, 4, 6, 8, 10, 12, 14]

print("输出结果为：", reduce(fun, listA))"""


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
