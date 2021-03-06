# Python JSON 数据解析
"""JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。
Python 中可以使用json 模块来对JSON 数据进行编码，它包含两个函数："""
# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。
"""在json 的编码过程中，Python的原始类型与json类型会相互转换，具体转换对照如下："""
# Python 编码为JSON类型转换对应表：
"""Python                                   JSON
dict                                        object
list,tuple                                  array
str                                         string
int,float,int-&float-derived Enums          number
True                                        true 
False                                       false
None                                        null
None                                        null  """
# JSON 解码为Python类型转换对应表
"""JSON                                     Python 
object                                      dict
array                                       list
string                                      str 
number(int)                                 int 
number(real)                                float
true                                        True 
false                                       False 
null                                        None  """

# json.dumps 与 json.loads 实例
# 演示Python 数据结构转为JSON：

import json

# python 字典类型转换为 JSON 对象
data = {
    "no": 1,
    "name": "runoob",
    "url": "www.runoob.com"
}

json_str = json.dumps(data)
print("python原始数据:", repr(data))
print("JSON 对象:", json_str)  # 输出的结果可以看出，简单类型通过编码后跟其原始的repr()输出结果非常相似

# 将JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']", data2['name'])
print("data2['url']", data2['url'])


"""如果你要处理的是文件而不是字符串，你可以使用json.dump() 和 json.load() 来编码和解码JSON数据"""

# 写入JSON 数据
with open("data.json", "w") as f:
    json.dump(data, f)

# 读取数据
with open("data.json", "r") as f:
    data3 = json.load(f)

print(data3)