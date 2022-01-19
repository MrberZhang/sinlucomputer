# Python3 MySQL 数据库连接 - PyMySQL 驱动
"""什么是 PyMySQL？
PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。
PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。
"""

# 数据库连接
"""
连接数据库前，请先确认以下事项：

您已经创建了数据库 TESTDB.
在TESTDB数据库中您已经创建了表 EMPLOYEE
EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
连接数据库TESTDB使用的用户名为 "testuser" ，密码为 "test123",
"""
# 实列
import pymysql

db = pymysql.connect(
    host="localhost",   # 数据库主机地址
    user="root",       # 数据库主机地址
    password="ABc,2zzwZerK",    # 数据库密码
    database="mysqltext_db",   # 已创建的数据库可链接数据库
)
cursor = db.cursor()  # 使用cursor()方法创建一个游标对象

"""数据表创建"""
# cursor.execute("DROP TABLE IF EXISTS sites")   # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("CREATE TABLE sites(id INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(25), lastName VARCHAR(25), age INT, sex CHAR(5), income FLOAT)")
# db.close()

"""使用预处理语句创建数据表"""
# cursor.execute("DROP TABLE IF EXISTS site2")
# sql = "CREATE TABLE site2(id INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(25), lastName VARCHAR(25), age INT, sex CHAR(5), income FLOAT)"
# cursor.execute(sql)
# db.close()

"""数据库插入操作1"""
# sql = "INSERT INTO sites(firstName, lastName,age,sex,income) Values('Mac','Mohan','55','M','2000')"
# try:
#     cursor.execute(sql)
#     db.commit()   # 提交到数据库执行
# except:
#     db.rollback()  # 如果发生错误数据回滚
#
# db.close()

"""数据库插入操作2"""
# sql = "INSERT INTO sites(firstName, lastName, age, sex, income) Values('%s','%s','%s','%s','%s')" % ('Mac', 'Mohan', '15', 'M', '2001')
# try:
#     cursor.execute(sql)
#     db.commit()   # 提交到数据库执行
# except:
#     db.rollback()  # 如果发生错误数据回滚
#
# db.close()

# 数据库查询操作
"""Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。"""
# sql = "select * from sites where income >= %s" % 1000
#
# try:
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for row in result:
#         rfname = row[1]
#         rlname = row[2]
#         rage = row[3]
#         rsex = row[4]
#         rincome = row[5]
#         print(rfname, rlname, rage, rsex, rincome)
# except:
#     print("Error: unable to fetch data")
#
# db.close()

# 数据库更新操作
"""更新操作用于更新数据表的数据，以下实例将 sites 表中 sex 为 'M' 的 age 字段递增 1："""
# sql = "UPDATE sites SET age = age+1 WHERE sex ='%c' " % 'M'
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#
# db.close()

# 删除操作
"""删除操作用于删除数据表中的数据，以下实例演示了删除数据表 sites 中 age 大于 20 的所有数据"""
# sql = "delete from sites where age > %s" % 20
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#
# db.close()

# 执行事务
"""
事务机制可以确保数据一致性。
事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
"""
sql = "DELETE FROM sites WHERE age > %s" % 10

try:
   cursor.execute(sql)  # 执行SQL语句
   db.commit()  # 向数据库提交
except:

   db.rollback()   # 发生错误时回滚

db.close()

# 错误处理
"""
Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
Error	警告以外所有其他错误类。必须是 StandardError 的子类。
InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。
"""