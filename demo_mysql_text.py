import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",   # 数据库主机地址
    user="root",       # 数据库主机地址
    password="ABc,2zzwZerK",    # 数据库密码
    # database="mytext_db"   # 已创建的数据库可链接数据库
)

mycursor = mydb.cursor()



# 创建数据库
# mycursor.execute("CREATE DATABASE mytext_db") #已经创建库，不需要在运行，会报错
# mycursor.execute("SHOW DATABASES")  # 查询数据库是否存在
# for i in mycursor:
#     print(i)

# 创建数据表
# mycursor.execute("CREATE TABLE table_sites(name VARCHAR(255),url VARCHAR(255))") #已经创建表，不需要在运行，会报错


# 主键设置
"""创建表的时候我们一般都会设置一个主键（PRIMARY KEY），我们可以使用 "INT AUTO_INCREMENT PRIMARY KEY" 
语句来创建一个主键，主键起始值为 1，逐步递增。"""

# mycursor.execute("ALTER TABLE table_sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #已经创建，不需要在运行，会报错


# 插入数据
"""插入数据使用 "INSERT INTO" 语句"""

# sql = "INSERT INTO table_sites(name,url) VALUES (%s, %s)"
# val = ("baidu", "ww.baidu.com")
# mycursor.execute(sql, val)
#
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "记录插入成功") # mycursor.rowcount返回操作数据库的行数


# 批量插入数据
"""批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据："""
# sql = "INSERT INTO table_sites(name,url) VALUES (%s, %s)"
# val = [
#     ('Google', 'www.google.com'),
#     ('Taobao', 'www.taobao.com'),
#     ('Github', 'www.github.com'),
#     ('stackoverflow', 'www.stackoverflow.com')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()   # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "批量插入成功")  # mycursor.rowcount返回记录操作数据库的行数

"""如果我们想在数据记录插入后，获取该记录的 ID ，可以使用以下代码："""
# sql = "INSERT INTO table_sites(name,url) VALUES (%s, %s)"
# val = ('Taobao', 'www.taobao.com')
# mycursor.execute(sql, val)
# mydb.commit()
# print("1条记录已插入，ID为：", mycursor.lastrowid)  # mycursor.lastrowid获取该记录的 ID(重复运行会重复插入数据)

# 查询数据
"""查询数据使用 SELECT 语句："""
# mycursor.execute("SELECT * FROM table_sites")
# myresult = mycursor.fetchall()    # fetchall() 获取所有记录

# for x in myresult:
#     print(x)

"""也可以读取指定的字段数据"""
# mycursor.execute("select name,url from table_sites")
# myresult2 = mycursor.fetchall()

# for s in myresult2:
#     print(s)

"""如果我们只想读取一条数据，可以使用 fetchone() 方法"""
# mycursor.execute("select * from table_sites")
# myresult3 = mycursor.fetchone()
# print(myresult3)


# where 条件语句
"""如果我们要读取指定条件的数据，可以使用 where 语句："""
# sql = "select * from table_sites where name='baidu'"
# mycursor.execute(sql)
# myresult4 = mycursor.fetchall()
# for i in myresult4:
#     print(i)

"""也可以使用通配符 % """
# sql = "select * from table_sites where url like '%oo%'"
# mycursor.execute(sql)
# myresult5 = mycursor.fetchall()
# for x in myresult5:
#     print(x)

"""为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件："""
# sql = "select * from table_sites where name = %s"
# na = ("Taobao", )
# mycursor.execute(sql, na)
# myresult6 = mycursor.fetchall()
# for i in myresult6:
#     print(i)


# 排序
"""查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC"""
# sql = "select * from table_sites order by name"
# mycursor.execute(sql)
# myresult7 = mycursor.fetchall()
# for s in myresult7:
#     print(s)

"""降序排序实例"""
# sql = "select * from table_sites order by name desc"
# mycursor.execute(sql)
# myresult8 = mycursor.fetchall()
# for s in myresult8:
#     print(s)


# Limit
"""如果我们要设置查询的数据量，可以通过 "LIMIT" 语句来指定"""
# mycursor.execute("select * from table_sites limit 3")
# myresult9 = mycursor.fetchall()
# for s in myresult9:
#     print(s)

"""也可以指定起始位置，使用的关键字是OFFSET"""
# mycursor.execute("select * from table_sites limit 3 offset 2")  # 0为第一条，1位第二条，以此类推
# myresult10 = mycursor.fetchall()
# for s in myresult10:
#     print(s)


# 删除记录
"""删除记录使用DELETE FROM语句"""
# sql = "delete from table_sites where name = 'stackoverflow'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "条记录删除")  # 注意：要慎重使用删除语句，删除语句要确保指定了 WHERE 条件语句，否则会导致整表数据被删除。

"""为了防止数据库查询发生SQL注入攻击，我们可以使用 %s 占位符来转义删除语句的条件"""
# sql = "delete from table_sites where name = %s"
# na2 = ("Taobao", )
# mycursor.execute(sql, na)
# mydb.commit()
# print(mycursor.rowcount, "条记录删除")  # 已经删除0会显示0条被删除


# 更新表数据
"""数据表更新使用UPDATE语句"""
# sql = "UPDATE table_sites SET name ='ZH' where name ='zhihu'"   # 将name为zhihu的名称改为ZH
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "条记录被修改")  # update语句要确保指定了where条件语句，否则会导致整表数据被更新。

"""为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件："""
# sql = "update table_sites set name = %s where name = %s"
# vla = ("zhi", 'ZH')
# mycursor.execute(sql, vla)
# mydb.commit()
# print(mycursor.rowcount, '条记录被修改')

# 删除表
"""删除表使用DROP TABLE 语句，IF EXISTS 是关键字是用于判断表是否存在，只有存在的情况下才删除"""
# mycursor.execute("CREATE TABLE site2(id VARCHAR(255),name VARCHAR(255))")
sql = "drop table if exists site2"   # 删除已存在的数据表
# mycursor.execute(sql)
