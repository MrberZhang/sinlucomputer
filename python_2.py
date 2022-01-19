# 实例1

# 1.1斐波那契数列的计算，F(0)=0,F(1)=1,···,F(n)=F(n-2)+F(n-1),n>=2

"""
a,b = 0,1
while a < 1000:
    print(a,end=",")
    a,b = b,a+b
"""

# 1.2根据圆的半径计算元的面积
'''
r = 25  # 半径
area = 3.1415*r*r
print(f"\n{area}")
print(f"{area:.2f}")    # 输出2位小数,f函数
print("{:.2f}".format(area))    # 输出2位小数format方法
'''

# 1.3绘制五角红星

'''
from turtle import *
color('red','red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()
'''

# 1.4程序运行计时
'''import time
limit = 10 * 1000 *1000
start = time.perf_counter()

while True:
    limit -= 1
    if limit <= 0:
        break
delta = time.perf_counter() - start
print("程序运行时间是：{}秒".format(delta))'''

# 1.5绘制七彩圆圈
'''import turtle

colors=['red','orange','yellow','green','blue','indigo','purple']

for i in range(7):
    c = colors[i]
    turtle.color(c,c)
    turtle.begin_fill()
    turtle.rt(360/7)
    turtle.circle(50)
    turtle.end_fill()   
turtle.done'''

# 习题1

# 1.根据输入的内容输出相应的结果
'''name = input("请输入对方的名字：")
s = input("请输入悄悄话内容：")
print(f"{name},听我说句悄悄话：{s*3}")'''

# 2.九九乘法表输出。
'''for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j,i,i*j),end=",")

    print('')'''

# 3.同切圆的绘制,绘制一组半径不同的同切圆
'''import turtle #进入绘制
turtle.pensize(3)

turtle.circle(20)
turtle.circle(40)
turtle.circle(60)
turtle.circle(80)'''

# 4.循环提示输入用户三个小爱好，并一起输出
'''hobbies = ""
for i in range(3):
    s = input("请输入你的小爱好（最多三个，按Q或者q结束）:")
    if s.upper() == 'Q':
        break
    hobbies += s + ""

print("你的小爱好是：",hobbies)'''

# 5.系统提示输入用户名字，并随机生成一个幸运数字，输出结果
'''import random
strl = input('请输入你的名字：')
print("Hello!{}".format(strl))
guard = ord(strl[0]) % 100
print("你的幸运数是",random.choice(range(guard)))'''

# 实例2

# 2.1 倒背如流，倒着输出录入的文本
'''s = input("请输入一段文本:")
i = len(s) - 1
while i >= 0:
    print(s[i],end="")
    i = i-1

#2.2 倒背如流，倒着输出录入的文本
s = input("\n请输入一段文本:")
i = -1
while i >= -1 *len(s):
    print(s[i],end="")
    i = i - 1

#2.2 倒背如流，倒着输出录入的文本,字符串高级切片
s = input("\n请输入一段文本:")
print(s[::-1])
'''

# 习题2

# 2.1输入一个整数N，并计算n的32次方
'''n = input("请输入一个整数：")
num = int(n) ** 32
print(num)'''

# 2.2 获得用户输入的一段文字，将这段文字进行垂直输出
'''text = input("请输入一段文字:")
for t in text:
    print(t)'''

# 2.3 获取用户输入的一个合法算式，列如1.2+3.4，输出运算结果
'''num=eval(input("请输入的一个合法算式，列如1.2+3.4："))
print(num)'''

# 2.4 获取用户输入的一个小数N，提取并输出整数部分
'''N = input("请输入一个小数:")
for i in N:
    if i != '.':
        print(i,end='')
    else:
        break'''

# 2.5 获取用户输入的整数N，并计算出1到N相加的和
'''N = int(input("请输入一个整数："))
sumb = 0
for i in range(N):
    sumb += i + 1 #同理 sum = sum+i+1

print("1到N求和结果：{}".format(sumb))'''

# 实例3

# 3.1 凯撒密码,每一个英文字母循环替换为字母表序列中该字符的后三个字符
'''ptxt = input("请输入一段文本：")
for p in ptxt:
    if "a" <= p <= "z":
        print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end="")
    elif "A" <= p <="Z":
        print(chr(ord("A")+(ord(p)-ord("A")+3)%26),end="")
    else:
        print(p,end="")

etxt = input("\n请输入加密后的文本：")
for p in etxt:
    if "a" <= p <= "z":
        print(chr(ord("a")+(ord(p)-ord("a")-3)%26),end="")
    elif "A" <= p <="Z":
        print(chr(ord("A")+(ord(p)-ord("A")-3)%26),end="")
    else:
        print(p,end="")'''

# 习题3

# 3.1.获得用户输入的一个整数，输出该整数百位级以上的数字。
'''num = input("请输入一个整数：")
if 0<= eval(num) <100:
    print("该整数没有百位级以上的数")
else:
    for n in num[:-2]:
        print(n,end="")'''

# 3.2.获得用户输入的一个字符串，将字符串按照空格分隔，然后逐行打出。
'''strs = input("请输入一个字符串：")
s = " ".join(strs)
print(s)
for i in s:
    if i != ' ':
        print(i)'''

# 3.3程序读入一个表示星期几数字（1-7），输出对应的星期字符串名称。例如3返回星期三
'''import random
num = random.randint(1,7)
if num == 1:
    print("星期一")
elif num == 2:
    print("星期二")
elif num == 3:
    print("星期三")
elif num == 4:
    print("星期四")
elif num == 5:
    print("星期五")
elif num == 6:
    print("星期六")
elif num == 7:
    print("星期天")'''

# 3.4.设n是一任意自然数，如果n的各位数字反向排列所得的自然数与n相等，则n被称为回文数。从键盘输入一个5位数字，请编写程序判断这个数字是不是回文数。
'''n = input("输入一个5位数字:")
m = n[::-1]

if int(m) == int(n):
    print("这是一个回文数")
else:
    print("这不是一个回文数")'''

# 3.5.输入一个十进制整数，分别输出二进制，八进制，十六进制字符串。

'''num = input('请输入一个整数：')

print(bin(eval(num)))  #二进制
print(oct(eval(num)))  #八进制
print(hex(eval(num)))  #十六进制
print(int(eval(num)))  #十进制'''

# 实例4

# 4.1 猜数字游戏

'''import random
target = random.randint(1,1000)
count = 0

while True:
    try:
        guess = eval(input("请输入一个猜测的整数（1至1000）："))
    except:
        print("输入有误，不计猜测次数！")
        continue

    count = count + 1

    if guess > target:
        print("猜大了")
    elif guess < target:
        print('猜小了')
    else:
        print('猜对了')
        break
print('此轮猜测的次数是：',count)'''

# 习题4

# 4.1 输入一个年份，输出是否为闰年。闰年条件：能被4整除但不能够被100整除，或者能够被400整除的年份都是闰年。
'''yearAge = input("请输入一个年份：")
if int(yearAge)%4 == 0 and int(yearAge)%100 != 0:
    print("你输入的年份是闰年")
elif int(yearAge)%400 == 0:
    print("你输入的年份是闰年")
else:
    print('你输入的年份不是闰年')'''

# 4.2 最大公约数计算。获得2个整数，求出这两个整数的最大公约数和最小公倍数。最大公约数的计算一般使用辗转相除法，最小公倍数则使用两个数的乘积除以最大公约数。
'''num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
f = num1*num2
if num1 / num2 > 1:   
    while True:
        s = num1 % num2
        if  s != 0:
            num1 = num2
            num2 = s

        else:
            print("最大公约数是：{}".format(num2))
            print("最大公倍数是：{}".format(f/num2))
            break
elif num2 / num1 > 1:
    while True:
        s = num2 % num1
        if  s != 0:
            num2 = num1
            num1 = s

        else:
            print("最大公约数是：{}".format(num1))
            print("最大公倍数是：{}".format(f/num1))
            break
else:
    print("最大公约数是：{}".format(num1))
    print("最大公倍数是：{}".format(f/num2))'''

# 4.3 统计不同字符个数。用户从键盘键入一行字符，编辑一个程序，统计并输出其中英文字符，数字、空格和其他字符个数。
'''s = input("输入一串字符：")
alpha,num,space,other = 0,0,0,0
for i in s:
    if i.isalpha():#英文字符
        alpha += 1
    elif i.isdigit():#数字
        num += 1
    elif i.isspace():#空格
        space += 1
    else:
        other += 1
print("英文字符数{},数字字符数{}，空格字符数{}，其他字符数{}".format(alpha,num,space,other))'''

# 4.4 猜数字游戏续。当用户输入的不是整数（如字母，浮点数等）时，程序会终止执行退出，改编题目1中的程序，当用户输入出错时，给出“输入内容必须是整数！”的提示，并让用户重新输入
'''import random
target = random.randint(1,1000)
count = 0

while True:
    try:
        guess = eval(input("请输入一个猜测的整数（1至1000）："))
    except:
        print("输入内容必须是整数！")
        continue

    count = count + 1

    if guess > target:
        print("猜大了")
    elif guess < target:
        print('猜小了')
    else:
        print('猜对了')
        break
print('此轮猜测的次数是：',count)'''

# 4.5 羊车门问题。有三扇关闭的门，一扇门后面停着汽车，其余门后是山羊，只有主持人知道每扇门后面是什么。
# 参赛者可以选择一扇门，在开启它之前，主持人会开启另外一扇门，漏出门后的山羊，然后允许参赛者更换自己的选择。请问参赛者更换选择后能否增加猜中汽车的机会？
# ——这是一个经典问题，请使用random库对这个随机时间进行预测，分别输出参赛者改变选择和坚持选择的概率。
'''import random
x = random.randint(5000,10000) #随机次数
change = 0 #改变
nochange = 0 #不改变
for i in range(1,x+1):
    a = random.randrange(1,4)
    b = random.randrange(1,4)
    if a == b:
        nochange += 1
    else:
        change += 1
print('不更改选择得到汽车的概率为：{}'.format(nochange/x))
print('更改选择得到汽车的概率为：{}'.format(change/x))'''

# 实例5 软文的诗词风
'''
txt = """
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。千金散尽还复来千金散尽还复来千金散尽还复来千金散尽还复来千金散尽还复来
"""
linewidth = 30   #预定输出宽度为30
def lineSplit(line):
    plist = [",","!","?",",","。","！","，","？"]
    for p in plist:
        line = line.replace(p,'\n')
    return line.split('\n')

def linePrint(line):
    global linewidth
##    while len(line) > linewidth:
##        print(line[0:linewidth])
##        line = line[linewidth:]    #这个循环是为了判断当句子超过限制时，分行居中显示
    print(line.center(linewidth,chr(12288)))

newlines = lineSplit(txt)
for newline in newlines:
    linePrint(newline)
'''

# 习题5

# 5.1 实现isNum()函数，参数一个字符串，如果字符串属于整数、浮点数或复数的表示，则返回True,否则返回False。
'''def isNum(num):
    try:
        num = eval(num)
        return True
    except:
        return False
print(isNum(input("输入一个参数:")))'''

# 5.2 实现isPrime()函数，参数为整数，要有异常处理，如果整数是质数，返回True 否则返回False。
'''from math import sqrt
def isPrime(s):
    if s == 1:
        return False
    for i in range(2,int(sqrt(s)+1)):  #判断是否是质数,在一般领域，2到根号n之间的数都无法被整除，则s是质数
        if s % i ==0:
            return False
    return True

try:     #异常处理，判断输入的是否整数
    s = int(input("请输入一个整数：")) 
    print(isPrime(s))
except:
    print("输入错误")'''

# 5.3 编写一个函数，计算传入字符串中数字、字母、空格已经其他字符的个数。
'''def function(strs):
    alpha,num,space,other = 0,0,0,0
    for i in strs:
        if i.isalpha():#英文字符
            alpha += 1
        elif i.isdigit():#数字
            num += 1
        elif i.isspace():#空格
            space += 1
        else:
            other += 1

    return print("英文字符数{},数字字符数{}，空格字符数{}，其他字符数{}".format(alpha,num,space,other))

function(input("输入一个字符串："))'''

# 5.4 编写一个函数，打印200以内的所有素数，以空格分割。
'''from math import sqrt
def number():
    for i in range(2,201):
        a = 1
        for j in range(2,int(sqrt(i)+1)):  #判断是否是质数,
            if i % j == 0:
                a=a*0
            else:
                a=a*1
        if a == 1:
            print(i,end=" ")            
number()'''

# 5.5 编辑一个函数，参数为一个整数n。用递归获取斐波那契数列中的第n个数并返回。
'''def fib(n):        
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n >= 3:
        return fib(n-1)+fib(n-2)
n = eval(input('请输入一个整数：'))
print(fib(n))'''

# 实例6

# 习题6

# 6.1 英文字符频率统计。编写一个程序，对给定字符串中出现的A~Z字母频率进行分析，忽略大小写，采用降序方式输出。
'''txt = input("输入一个字符串：")
txt = txt.lower()
t = {}
for i in txt:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        t[i] = t.get(i,0)+1   #计算字典键值的值
        ls = list(t.items())   #将字典转换为列表才可以进行排序
        ls.sort(key = lambda x:x[1],reverse = True)   #根据值进行降序排序，默认是升序
for i in range(len(t)):   #0到len(t), 循环遍历t的键值，分别将其复制给变量word count
    word,count = ls[i]
    print("{:<10}{:<5}".format(word,count))'''

# 6.2 中文字符频率统计。编写一个程序，对给定的字符串中出现的全部字符（含中文字符）频率进行分析，采用降序方式输出。
'''txt = input("输入一个字符串：")
t = {}
for i in txt:
    t[i] = t.get(i,0)+1 
    ls = list(t.items())
    ls.sort(key = lambda x:x[1],reverse = True)
for i in range(len(t)):
    word,count = ls[i]
    print("{:<10}{:<5}".format(word,count))'''

# 6.3 随机密码生成。编写程序在26个字母大小写和9个数字组成的列表中随机生成10个8位密码。
'''import random
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQSRTUVWXYZ123456789"
lists = list(s)
for i in range(10):
    password = ""
    for j in range(8):
        password += random.choice(lists)
    print(password)'''

# 6.4 重复元素判定。编写一个函数，接收列表作为参数，如果一个元素在列表中出现了不止一次，则返回TRUE，
# 但不要改变原来的列表的值，同时编写调用这个函数和输出测试结果的程序。
'''def fire(list1):  
    n = input("请输入一要判定的元素：")  #判断手动输入的元素
    list2 = list1.copy()
    if n in list1:
        list2.remove(n)
        if n in list2:
            print('True')
        else:
            print('False')
    else:
        print('False')

list1 = list(input("请输入元素以逗号（,）隔开：").split(","))
fire(list1)
print(list1)'''

'''def fire(lists):
    for n in lists:  #直接判定已有的列表元素
        num = lists.count(n)
        if num > 1:
            return True
        else:
            return False

list1 = list(input("请输入元素以逗号（,）隔开：").split(","))
print(fire(list1))
print(list1)'''

# 6.5 重复元素判定续。利用集合的无重复性，改编上一个程序，获得一个更快跟简洁的版本。
'''def is_repeat(lists):
    set1 = set(lists) 
    if len(set1) < len(lists):  #小于表示有重复，集合的无重复，自动去掉重复元素
        return True
    else:
        return False

list1 = input("请输入元素以逗号（,）隔开：")
list2 = list(list1.split(','))
is_repeat(list2)
print(list2)'''

# 实例7

# 实例7.1 国家财政数据趋势演算

# 代码中zip（x,y）函数用来获取2个组合数据类型x和y，并将他们的元素交织返回。
# 例如：x=[1,2,3],y=[4,5,6],zip(x,y)的返回值[(1,4),(2,5),(3,6)]
'''def parseCSV(filename):    
    dataNames,data = [],[]  #该函数解析CSV文件，从中取数据，并把数据表示为列表类型
    f = open(filename,'r',encoding='UTF-8')
    for line in f:
        splitedLine = line.strip('\n').split(',') #去掉换行符 以逗号分隔
        if '指标' in splitedLine[0]:
            years = [int(x[:-1]) for x in splitedLine[1:]]
        else:
            dataNames.append('{:10}'.format(splitedLine[0]))
            data.append([float(x) for x in splitedLine[1:]])
    f.close()
    return years,dataNames,data

def means(data):   #用来计算所有数的均值
    return sun(data) / len(data)

def linersRegression(xlist,ylist):   #用来根据xlist和ylist列表计算线性回归值
    xmeans,ymeans = means(xlist),means(ylist)
    bNumerator = -len(xlist) * xmeans * ymeans
    bDenominator = -len(xlist) * xmeans ** 2
    for x,y in zip(xlist,ylist):
        bNumerator += x * y
        bDenominator += x ** 2
    b = bNumerator / bDenominator
    a = ymeans - b * xmeans
    return a,b

def calNewData(newyears,a,b):   #用来计算新的数值
    return [(a + b * x) for x in newyears]

def showResults(years,dataName,newData):  #集中展示运行结果，重点在于格式化输出
    print('{:^60}'.format('国家财政收支线性估计'))
    header = '指标'
    for year in years:
        header += '{:10}'.format(year)
    print(header)
    for name,lineData in zip(dataNames,newDatas):
        line = name
        for data in lineData:
            line += '{:.10.1f}'.format(data)
        print(line)

def main():   #代表该程序的主逻辑部分，包括预分配列表变量，调佣各步骤或流程函数等
    newyears = [x+2010 for x in range(7)]
    newDatas = []
    years,dataNames,datas = parseCSV('finance.csv')
    for data in datas:
        a,b = linersRegression(years,dsata)
        newDatas.append(calNewData(newyears,a,b))
    showResults(newyears,dataNames,newData)

main()'''

# 习题7

# 7.1 输入一个文件和一个字符，统计该字符在文件中出现的次数。
'''def times(filename,char):
    count = 0
    f = open(filename,'r',encoding='utf-8')
    txt = f.read()
    txt = txt.lower()
    for i in txt:
        if char == i:
            count += 1
    f.close()
    return count

filename = input(请输入一个文件名：)
char = input(请输入一个字符：)

print(times(filename,char))'''

# 7.2 假设有一个英文文本文件，编写一个程序读取其内容并将里面的大写字母变成小写字母，小写字母变成大写字母。
'''f = open('english.txt','r',encoding='utf-8') #第一种方式
txt = f.read()
txt = txt.swapcase()
f = open('english2.txt','w',encoding='utf-8')
f.write(txt)
f.close()'''

'''def text(filename):
    f = open(filename,'r',encoding='utf-8')  #第二种方式
    txt = f.read()
    txt = txt.swapcase()
    f.close()
    return txt

def newtext(name,content):
    f = open(name,'w',encoding='utf-8')
    f.write(content)
    f.close()

newtext('english3.txt',text('english.txt'))'''

# 7.3 编写一个程序，生成一个10X10的随机矩阵并保存为文件（空格分隔行向量，换行分隔列向量），
# 再写程序将刚才保存的矩阵文件另存为csv格式，用户Excel或文本编辑器打开看看结果对不对
'''import random  
content = ''
for row in range(10):
    line = ''
    for line_row in range(10):
        line += "{} ".format(random.randint(1,9))
    content +="{}\n".format(line)

f = open('seven.txt','w',encoding='utf-8')
f.write(content)
f.close()

file = open('seven.csv','w',encoding='utf-8')
txt = content.replace(' ',',')#替换方法
file.write(txt)
file.close()'''

# 7.4 编写一个程序，读取一个Pyhon源代码文件，将文件中所有除保留字外的小写字母换成大写字母，
# 生成后的文件要能够被python解释器正确执行。

'''import keyword   #python关键字获取代码
keylist=keyword.kwlist
##print(keylist)
text_keyword = ['eval','input','format','print']  #源代码文件总的保留字

file = open('text7_4.py','r',encoding='utf-8')
text = file.read()
file.close()

new,temp = "",""
for i in text:
    if i.isalpha():   #如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False
        temp += i
##        print(temp)
    else:
        if (not keyword.iskeyword(temp)) and (temp not in text_keyword):
            temp = temp.upper()     #如果不是保留字和内置方法，变成大写形式        
        new += temp   #将temp添加进新字符串中
        new += i      #添加非字母i
        temp = ''     #清空临时字符串，用于下次继续使用
##print(new)

new_file = open('text7_4_2.py','w',encoding='utf-8')
new_file.write(new)
new_file.close()'''

# 7.5 编写一个程序，要求能够将元素为任意Python支持的类型（包括含有半角逗号的字符串）
# 的列表转储为csv，并能够重新正确解析为列表。
'''def savecsv(list_ele,filename):        #列表转存为csv文件
    f = open(filename,'w',encoding='utf-8')
    txt = ''
    for i in range(len(list_ele)):
        txt = txt + str(list_ele[i]) + '列表分隔处'
##    print(txt)
    x = txt.split('列表分隔处')
    del x[-1]  # 因为最后一个元素是''，所有需要删除掉
##    print(x)
    f.write(','.join(x))
    f.close()

def opencsv(filename):      #打开csv文件，解析内容否正确
    f = open(filename,'r',encoding='utf-8')
    text = f.read()
    text = text.replace(",",' ')   #将读取的csv文件内容去掉逗号
    print(text)
    f.close

def main():
    txt_ele = input("请输入列表元素,以空格分隔：")
    list_ele = txt_ele.replace(' ',',').split(',') #将输入元素转换为列表
##    print(list_ele)
    filename = input("请输入要保存的csv文件名：")
    savecsv(list_ele,filename)
    opencsv(filename)

main()'''

# 实例8

# 实例8.1 Web页面元素提取
'''
def getHTMLlines(inputfile):
    f = open(inputfile,'r',encoding='utf-8')    #获取HTML内容，并将结果转为一个分行的列表
    Is = f.readlines()
    f.close()
    print(Is)
    return Is

def extractImageUrls(htmlLines):    #程序核心，解析文件并提取图像的url
    urls = []
    for line in htmlLines:
        if 'img' in line:
            url = line.split('src=')[-1].split('"') #以src=为分割符保留最后一段，以"分隔
            print(url)
            if 'https' in url:
                urls.append(url)

    print(urls)
    return urls


def showResults(urls):
    count = 0
    for url in urls:
        print('第{:2}个URL：{}'.format(count.url))
        count += 1

def saveResults(filepath,urls):
    f = open(filepath,'w')
    for url in urls:
        f.write(url + "\n")

    f.close()


def main():
    inputfile = 'nation.html'
    outputfile = 'nation_urls.txt'
    htmlLines = getHTMLlines(inputfile)    #获取HTML内容，并将结果转为一个分行的列表
    imageUrls = extractImageUrls(htmlLines) #程序核心，解析文件并提取图像的url
    showResults(imageUrls)                 #将获取的链接输出到屏幕上面了
    saveResults(outputfile,imageUrls)      #保持结果到文件

main()
'''

# 习题8

# 8.1.用户输入一个年份，编写程序判断该年是否是闰年，如果年份能被400整除，则为闰年；如果年份能被４整除但不能被100整除也为闰年。

'''
years = eval(input("请输入一个年份："))
if years % 400 == 0:
    print("你输入的年份是闰年。")
elif years % 4 == 0:
    print("你输入的年份是闰年。")
else:
    print("你输入的年份不是闰年。")
'''

# 8.2.参考最后一个实例，尝试将不同标签中的内容分门别类地提取出来，再想想如何提取可以更为准确。(提示：可查阅HTML相关语法)

# 8.3.续上一题，找另外一个网站，尝试编程提取一些自己感兴趣的东西出来。(提示：可自行搜索用于HYM 解析的第三方库)

# 8.4.参考第6章最后一个例子，按照8.2节中的方法重新实现一个有较好的函数封装的《Hamlet》文本词频统计程序。

# 8.5.词云是设计和统计的结合，也是艺术与计算机科学的碰撞。worduloud是一款基于Python的词云第三方库，
# 支持对词语数量、背景蒙版、字体颜色等各种细节的设置，试结合上一题构建《》的词云效果。


# 实例9

# 实例9.1 程序计时  以1000万次循环为主体，模拟实际程序的核心模块，用time.sleep()来模拟实际程序的其他模块。

'''
import time
def coreLoop():
    limit = 10 ** 8
    while(limit > 0):
        limit -= 1

def otherLoop1():
    time.sleep(0.2)

def otherLoop2():
    time.sleep(0.4)

def main():
    startTime = time.localtime()
    print("程序开始时间：",time.strftime("%Y-%m-%d %H:%M:%S",startTime))
    startPerfCounter = time.perf_counter()
    otherLoop1()
    otherLoop1PerfCounter = time.perf_counter()
    otherLoop1Perf = otherLoop1PerfCounter - startPerfCounter
    coreLoop()
    coreLoopPerfCounter = time.perf_counter()
    coreLoopPerf = coreLoopPerfCounter - otherLoop1PerfCounter
    otherLoop2()
    otherLoop2PerfCounter = time.perf_counter()
    otherLoop2Perf = otherLoop2PerfCounter - coreLoopPerfCounter
    endPerfCounter = time.perf_counter()
    totalPerf = endPerfCounter - startPerfCounter
    endTime = time.localtime()
    print("模块1运行时间是：{}秒".format(otherLoop1Perf))
    print("核心模块运行时间是：{}秒".format(coreLoopPerf))
    print("模块2运行时间是：{}秒".format(otherLoop2Perf))
    print("程序运行中时间是：{}秒".format(totalPerf))
    print("程序结束时间：",time.strftime('%Y-%m-%d %H:%M:%S',endTime))

main()
'''

# 实例9.2 雪景艺术绘图 snowView.py
# 第一步构建图背景，第二部绘制雪花效果，第三步绘制雪地效果.

'''
from turtle import *
from random import *

def drawSnow():
    hideturtle()
    pensize(2)
    for i in range(100):
        r,g,b = random(),random(),random()
        pencolor(r,g,b)
        penup()
        setx(randint(-350,350))
        sety(randint(1,270))
        pendown()
        dens = randint(8,12)
        snowsize = randint(10,14)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)

def drawGround():
    hideturtle()
    for i in range(400):
        pensize(randint(5,10))
        x = randint(-400,350)
        y = randint(-280,-1)
        r,g,b = -y/280,-y/280,-y/280
        pencolor((r,g,b))
        penup()
        goto(x,y)
        pendown()
        forward(randint(40,100))

setup(800,600,200,200)
tracer(False)
bgcolor('black')
drawSnow()
drawGround()
done()
'''

# 习题9

# 9.1.使用turtle库绘制一个蜂窝状六边形。

'''
import turtle
import math

turtle.setup(600,500,None,None)
for y in range(2):
    pen_y = 190 - 45 * y
    pen_x = -300 - 7.5*math.sqrt(3)*pow(-1,y)+7.5*math.sqrt(3)
    turtle.penup()
    turtle.goto(pen_x,pen_y)
    turtle.down()
    for x in range(6):
        turtle.circle(30,steps=5)
        turtle.penup()
        turtle.forward(30*math.sqrt(3))
        turtle.pendown()
#turtle.done()   #完成绘图停留在界面，如果没有改方式会直接退出
'''
# 9.2.使用turtle库绘制一朵玫瑰花。
'''
import turtle
# 设置初始位置
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)

# 花蕊
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()

# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)

# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()

turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()

turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)
turtle.done()
'''

# 9.3.使用turtle库绘制一个颜色图谱。

'''
import turtle

turtle.setup(600,800,None,None)
turtle.pensize(10)
turtle.speed(10)
t = 0

#绘制颜色图谱
for r in range(0,256,80):
    for g in range(0,256,80):
        for b in range(0,256,80):
            turtle.pencolor(r/250,g/256,b/256)
            t += 10
            turtle.penup()
            turtle.goto(-250,350-t)
            turtle.pendown()
            turtle.forward(500)
'''

# 9.4.利用random库生成一个包含10个0~100之间随机整数的列表。

'''
import random

list1 = []
for i in range(10):
    t = random.randint(0,100)
    list1.append(t)

print(list1)
'''

# 9.5.利用time库将当前日期时间转化成类似“Sunday，8. January 2017 11:03PM"的格式。

'''
import time

t = time.localtime()
now = time.strftime("%A,%d.%m,%Y %I:%M%p",t  )
print(now)
'''

# 实例10

# 实例10.1 可视化词云

'''
import jieba
import wordcloud

txt = '程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织、计算机指令，使计算机能够自动进行各种运算处理'
words = jieba.lcut(txt)     #精确分词
newtxt = ' '.join(words)    #空格拼接
wordcloud = wordcloud.WordCloud(font_path='msyh.ttc').generate(newtxt)
wordcloud.to_file('词云中文例子图.png')    #保存图片
'''

# 实例10.2 Alice 梦游仙境

'''
import wordcloud
import imageio
##from scipy.misc import imread

mask = imageio.imread('AliceMask.png')
f = open('AliceInWonderland.txt','r',encoding='utf-8')
txt = f.read()
wordcloud = wordcloud.WordCloud(font_path='msyh.ttc',background_color="white",width=800,height=600,max_words=200,\
                      max_font_size=80,mask = mask).generate(txt)

wordcloud.to_file('AliceWonderland.png')
f.close()
'''

# 习题10

# 习题10.1. 使用jieba. lcut()对“Python是最有意思的编程语言”进行分词，输出结果，并将该选代器转换为列表类型。

'''
import jieba

txt = "Python是最有意思的编程语言"
words = jieba.lcut(txt)
print(words)
'''

# 10.2.使用jieba.lcut()对“今天晚上我吃了意大利面”进行分词，输出结果，并使“意大利面”作为一个词出现在结果中。
'''
import jieba

jieba.add_word("意大利面")
txt = "今天晚上我吃了意大利面"
newtxt = jieba.lcut(txt)
print(newtxt)
'''

# 10.3.自选一篇报告或者演讲稿，利用jeba分析出其词频排前5的关键词。

'''
import jieba

f = open("journalism.txt",'r',encoding='utf-8')
txt = f.read()
f.close()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) ==1:
        continue
    else:
        counts[word] = counts.get(word,0)+1

items = list(counts.items())  #将字典转为列表
items.sort(key=lambda x:x[1],reverse=True) #排序
for i in range(5):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
'''

# 10.4.参考本章最后的实例，选择你喜欢的小说，统计出场人物词频排名。

'''
import jieba

f = open("journalism.txt",'r',encoding='utf-8')
txt = f.read()
f.close()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) ==1:
        continue
    else:
        counts[word] = counts.get(word,0)+1

items = list(counts.items())  #将字典转为列表
items.sort(key=lambda x:x[1],reverse=True) #排序
for i in range(len(items)-1):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
'''

# 10.5.续上题，将上题结果以词云的方式展现，并尝试美化生成的词云图片。

'''
import jieba
import wordcloud

f = open("journalism.txt",'r',encoding='utf-8')
txt = f.read()
f.close()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) ==1:
        continue
    else:
        counts[word] = counts.get(word,0)+1

items = list(counts.items())  #将字典转为列表
items.sort(key=lambda x:x[1],reverse=True) #排序
word2=[]
for i in range(len(items)-1):
    word,count = items[i]
##    print("{0:<10}{1:>5}".format(word,count))
    word2.append(word)
newword = ' '.join(word2)    #空格拼接
wd = wordcloud.WordCloud(font_path='msyh.ttc').generate(newword)
wd.to_file('结果图片.png')
'''

# 练习题
# 1. 输入一个百分制成绩  要求输出成绩等级A、B、C、D、E，其中90~100分为A，80~89分为B，70~79分为C，60~69分为D，60分以下为E。
"""要求：
用if语句实现；
输入百分制成绩后要判断该成绩的合理性，对不合理的成绩应输出出错信息。 """

# try:
#     number = int(input("请输入一个整数0~100:"))
#     if 90 <= number <= 100:
#         print("你的成绩是A")
#     elif 80 <= number <= 89:
#         print("你的成绩是B")
#     elif 70 <= number <= 79:
#         print("你的成绩是C")
#     elif 60 <= number <= 69:
#         print("你的成绩是D")
#     elif number <= 60:
#         print("你的成绩是E")
#     elif number < 0 or number > 100:
#         print("你输入的数字不对")
# except:
#     print("你的输入有误")

# 2. 篮球比赛案例 篮球比赛是高分的比赛，领先优势可能很快被反超。作为观众，希望能在球赛即将结束时，就提早知道领先是否不可超越。体育作家Bill James发明了一种算法，用于判断领先是否“安全”。
"""算法描述：
获取领先的分数 ，减去3分；
如果目前是领先队控球，则加0.5；否则减0.5（数字小于0则变成0）；
计算平方后的结果；
如果得到的结果比当前比赛剩余时间的秒数大，则领先是“安全”的。
请编写程序实现上述算法的功能，并给出运行结果  """

# grade = eval(input("请输入领先的分数："))
# time = eval(input("请输入剩余时间:"))
# t = grade - 3
# w = input("目前是否为领先队控球（Y or N）：")
# if w == 'Y' or w == 'y':
#     t1 = t + 0.5
# else:
#     t1 = t - 0.5
# if t1 <= 0:
#     t1 = 0
# if t1 ** 2 >= time:
#     print("领先是安全的")
# else:
#     print("领先不安全的")


# 3.根据y=1+3-1+3-1+……+(2n-1)-1，
"""求：
y<3时的最大n值。 
与（1）的n值对应的y值。"""
# x, y = 1, 0
# while y < 3:
#     y = y + 1/(2*x-1)
#     x += 1
# print("y<3时的最大n值为:{}".format(x-1))
# print("与（1）的n值对应的y值:{}".format(y-1/(2*x-1))


# 4. 购物卡案例
"""小明单位发了100元的购物卡，小明到超市买三类洗化用品：洗发水（15元）、香皂（2元）、牙刷（5元）。要把100元正好花掉，可有哪些购买组合？"""
# money = 100
# n = money // 15
# for i in range(n, -1, -1):
#     m = (money - i * 15) // 5
#     for j in range(m, -1, -1):
#         k = (money - i*15 - j*5) // 2
#         if (money - i*15 - j*5) % 2 == 0:
#             print('可选择的购买组合:\t\t购买洗发水 {} 瓶，香皂 {} 块，牙刷 {}个。'.format(i, j, k))


# 5. 设计一个猜数游戏
"""首先由计算机产生一个[1,100]之间的随机整数，然后由用户猜测所产生的随机数。根据用户猜测的情况给出不同提示，
如猜测的数大于产生的数，则显示“High”，小于则显示“Low”，等于则显示“You won !”，游戏结束。用户最多可以猜7次，
如果7次均未猜中，则显示“You lost !”，并给出正确答案，游戏结束。游戏结束后，询问用户是否继续游戏，
选择“Y”则开始一轮新的猜数游戏；选择“N”则退出游戏。"""
# import random
# num = random.randint(0, 100)
#
#
# def game():
#     x = 1
#     while True:
#         if x <= 7:
#             s = int(input(f"输入你第{x}猜测的数字："))
#             if s > num:
#                 print("High")
#             elif s < num:
#                 print("Low")
#             elif s == num:
#                 print("You won")
#                 break
#
#         else:
#             print("You lost !")
#             break
#         x += 1
#
# game()
# g = input("输入“Y”则开始一轮新的猜数游戏；输入“N”则退出游戏:\n")
# if g == "Y" or g == "y":
#     game()

# 6.建立1个包含10个字符的字符串
"""建立1个包含10个字符的字符串，并根据键盘输入的数字n输出字符串中的第n个字符。当n值超过字符串的索引时，自动转为输出字符串中的最后1个字符。
要求：用try语句实现。  """
# n = int(input("请输入数字n："))
# a = "abcdefghij"
# try:
#     print(a[n-1])
# except:
#     print(a[9])


# 7. 编写函数  该函数可以输入任意多个数，函数返回输出所有输入参数的最大值、最小值和平均值。
# def num(s):
#     lis = list(s.split(","))
#     for i in range(len(lis)):
#         lis[i] = eval(lis[i])
#     print("输入所有参数的最大值是：{}".format(max(lis)))
#     print("输入所有参数的最小值是：{}".format(min(lis)))
#     print("输入所有参数的平均值是：{}".format(sum(lis)/(len(lis))))
#
#
# s = input("请输入任意整数个数以，隔开：")
# num(s)

# 8. 赶鸭子 一个人赶着鸭子去每个村庄卖，每经过一个村子卖去所赶鸭子的一半又一只。这样他经过了七个村子后还剩两只鸭子，问他出发时共赶多少只鸭子？
# y = 2
# x = 1
# while x <= 7:
#     y = (y+1) * 2
#     x += 1
# print(y)

# 9.将复数2.3x103-1.34x10-3j赋值给变量A，并分别提取A的实部和虚部。
# 10.计算下列表达式的值
# 11.建立一个包含10个字符的字符串A，然后对该字符串进行如下操作：
"""（1）计算输出字符串的长度；
（2）从第1个字符开始，每间隔2个字符取1个字符，组成子字符串B；
（3）将字符串A倒过来重新排列产生新的字符串C；
（4）将字符串A的前4个字符与字符串C的后5个字符进行组合，产生字符串D。"""
# a = "abcdefghij"
# print(len(a))
# b = a[::3]
# print(b)
# print(a[::-1])
# print(a[:4]+a[-5:])


# 12.分别格式化输出0.002178对应的科学表示法形式
"""分别格式化输出0.002178对应的科学表示法形式、具有4位小数精度的浮点数形式和百分数形式，并将输出宽度设定为10、居中对齐、星号*填充"""
# n = 0.002178
# print(f"科学表示法形式:{n:e}")
# print(f"具有4位小数精度的浮点数形式:{n:*^10.4f}")
# print(f"百分数形式:{n:*^10.4%}")

# 13.编写程序
"""从键盘输入一个1~7的数字，格式化输出对应数字的星期字符串名称。如：输入3，返回“您输入的是星期三”。"""

# 14.数字加密游戏
"""编程程序，从键盘任意输入1个4位数，将该数字中的每位数与7相乘，然后取乘积结果的个位数对该数字进行替换，最后得到1个新的4位数。"""
# s = input("请输入一个四位数：")
# new_s = ""
# for i in s:
#     t = (int(i) * 7) % 10
#     new_s += str(t)
# print(new_s)
