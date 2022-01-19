# Python MongoDB
"""MongoDB 是目前最流行的 NoSQL 数据库之一，使用的数据类型 BSON（类似 JSON）。"""
# PyMongo Python 要连接 MongoDB 需要 MongoDB 驱动，这里我们使用 PyMongo 驱动来连接。使用pip 安装pymongo。
# MongoDB需要先安装

# 创建数据库
"""创建数据库需要使用 MongoClient 对象，并且指定连接的 URL 地址和要创建的数据库名。"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydbtext"]  # 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。

# 判断前段注释的代码运行后，数据库时候已存在
dblist = myclient.list_database_names()
# dblist = myclient.database_names
# 注意：database_names 在最新版本的 Python 中已废弃，Python3.7+ 之后的版本改为了 list_database_names()。
if "mydbtext" in dblist:
    print("数据库已存在")


# 创建集合 MongoDB 使用数据库对象来创建集合，实例如下
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]

mycol = mydb["sites"]
"""注意: 在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。"""


# 判断集合是否已存在 我们可以读取 MongoDB 数据库中的所有集合，并判断指定的集合是否存在：
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydbtext']

collist = mydb.list_collection_names()
# collist = mydb.collection_names()
# collection_names 在最新版本的 Python 中已废弃，Python3.7+ 之后的版本改为了 list_collection_names()。
if "sites" in collist:  # 判断 sites 集合是否存在
    print("集合已存在！")
