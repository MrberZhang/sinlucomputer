# 考勤系统
"""
1） 目前该系统已经实现了部分功能，你们只需要完成剩余功能即可，需要你们完成的功能会使用#todo的形式进行标注，
todo后面会列出这个地方的功能，形式如下：
if __name__ == "__main__":
    #todo 调佣加载学生信息函数

#如果登录成功，则添加考勤记录
success = login()
if success:
    #todo 完成考勤数据添加功能
    pass
2） 学生信息存储在stu_infos.csv文件中，第一行是列名行，后面每一行都是一个学生的信息，包含学号，姓名，密码.
no ,name,password
2019443089,韩磊，123456
2019443090，丁鑫，abcdef
3） 考勤记录最终会被保存到attendance.csv文件中，第一行是列名行，后面每一行代表一个学生的考勤信息，包含学号，姓名，时间，
考勤状态（只有出勤、迟到、请假、缺勤四种状态）。内容格式如下：
no ,name,time,state
2019443089,韩磊，2020-12-08 08:30:00,出勤
2019443089,韩磊，2020-12-08 08:30:00,迟到
2019443089,韩磊，2020-12-08 08:30:00,缺勤
2019443089,韩磊，2020-12-08 08:30:00,请假
4） 学生信息需要首先被加载到student_infos列表中，student_info中的每个元素都是一个字典，字典中的键都是各自列名，
而值则是每一行内容，按照示例数据构造出来的student_infos列表如下。
{
{'no':'2019443089','name':韩磊，'time':'2020-12-08 08:30:00','state':出勤}
{'no':'2019443089','name':韩磊，'time':'2020-12-08 08:30:00','state':迟到}
{'no':'2019443089','name':韩磊，'time':'2020-12-08 08:30:00','state':缺勤}
{'no':'2019443089','name':韩磊，'time':'2020-12-08 08:30:00','state':请假}
}
5） 考勤系统老师端总共有两个Python文件，一个main.py文件，该文件作为入口程序文件，实现主体框架，
主体流程就是：加载数据 登录 添加考勤数据；一个stu_attendance.py文件，定义了数据加载、登录等函数。

要求：
（1） 在stu_info.csv文件末尾添加一行自己的信息，密码随意写，名字和学号必须是自己。
（2） 查看两个Python文件中的todo注释，添加合适代码，最终提供添加的代码。
（3） 测试程序功能，提供程序运行截图。进行登录验证的时候使用自己的学号进行登录验证，并且需要测试如下2个分支：
3次都登录失败的情况、登录成功后成功添加考勤数据
"""
import csv
import time
student_infos = []


# 加载数据
def load_stu_info():
    """
    加载学生信息
    从stu_infos.csv文件中加载数据
    :return: 无
    """
    with open(r"stu_infos.csv", encoding='utf-8-sig') as file:
        f_csv = csv.reader(file)
        header = next(f_csv)
        for row in f_csv:
            student_info = {}
            for index in range(3):
                student_info[header[index]] = row[index]
            student_infos.append(student_info)


# 登录
def login():
    """
    用户使用学号和密码进行登录
    最多让用户登录三次，如果连续三次都登录失败（用户名或者密码错误），只要密码和用户都正确表示登录成功
    :return:登录成功返回True和学号，三次都登录失败返回False和None
    """
    retry_time = 0
    while retry_time < 3:
        user_no = input('请输入登录账号：')
        password = input('请输入密码：')
        for i in student_infos:
            if i['no'] == user_no and i['password']==password:
                return True,user_no
        print('用户名或者密码错误！！！请重新输入。')
        retry_time += 1
    else:
        return False, None


# 考勤记录写入
def add(user_no):
    for x in student_infos:
        if user_no == x['no']:
            name = x['name']
            break
    times=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    choices=['出勤', '迟到', '请假', '缺勤']
    a=int(input("\t该学生出勤情况：1-出勤\t2-迟到\t3-请假\t4-缺勤:"))
    if a==1:
        data=choices[0]
    elif a==2:
        data=choices[1]
    elif a==3:
        data=choices[2]
    else:
        data=choices[3]
    with open(r"attendance.csv", 'a+', newline='', encoding='utf-8') as f:
        wf = csv.writer(f)
        wf.writerow([user_no, name, times, data])  # 写入一行数据
        print("{}同学{}数据已经写入成功！操作时间是{}".format(name, data, times))


# 查询考勤记录
def select():
    student = []
    with open(r"attendance.csv", encoding='utf-8-sig') as file:
        f_csv = csv.reader(file)
        header = next(f_csv)
        for row in f_csv:
            students = {}
            for index in range(4):
                students[header[index]] = row[index]
            student.append(students)
        name=input("请输入你需要查找的姓名：")
        print("  学号\t\t姓名\t\t操作时间\t\t出勤状态")
        for a in student:
            if a['name']==name:
                print(a['no']+'\t'+a['name']+'\t'+a['time']+'\t\t'+a['state'])
            else:
                print("无此人！！！")
                break

# 主函数