# Pyhton 技能书

# 面向对接编程 

#一、面向对象

'''
1.概念:面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，
但各自的数据可能不同。

2.类和对象的关系
概括的说：类可以比作是某种类型集合的描述。
我们把一类相同的事物叫做类，其中用相同的属性（其实就是变量）描述，里面封装了相同的方法。
比如，汽车是一个类，它包括价格、品牌等属性。 对象就是从类中分离出来。

类是模板，对象是根据这个模板创建出来的
类只需要有一个，对象可以有多个（一张图纸可以造多个飞机）

3.类：属性（信息）和方法（你能完成的事）。
1）.类名：这类事物的名字，满足大驼峰命名法
2）.属性：这个类创建出的对象有什么特征
3）.方法：这个类创建出的对象有什么行为

创建类：class关键字来定义
在class关键字后，就要加上类名，类名 首字母一般要大写 且要符合 驼峰式命名法，
例如定义一个动物形状类：AnimalShape。在类名后面的括号，表示该类是从哪个类继承下来的，
没有合适的继承类，就使用object类，这是所有类最终都会继承的类，在这里先不讲解继承的概念。

<__main__.Cat object at 0x0000020FD6938F40> 变量tom是指向Cat的实例,at后面的值就是实例化对象的地址。
'''

#小猫爱吃鱼，小猫要喝水
class Cat():
    def eat(self):
        print('%s爱吃鱼' % self.name)
    def drink(self):
        print('小猫要喝水')

tom = Cat()
#变量是创建一个实例，<变量>=<类名>(),isinstance(tom,Cat)测试某个对象是某个类的实例，是返回True,不是False
tom.name = 'Tom'
print(tom)
tom.eat()
tom.drink()

hello_kitty = Cat()
hello_kitty.name = 'hello_kitty'
hello_kitty.eat()
hello_kitty.drink()


# 二.初始化的方法

'''
由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法
'''

class Cat():
    def __init__(self,name):    #__init__初始化
        print('这是一个初始化方法')
        self.name = name

    def eat(self):
        print('%s爱吃鱼' %self.name)
        
cat = Cat('tom')
print(cat.name)

hello_kitty = Cat('HK')
print(hello_kitty.name)
hello_kitty.eat()

'''
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
就可以把各种属性绑定到self，因为self就指向创建的实例本身。
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
但self不需要传，Python解释器自己会把实例变量传进去。
'''

#练习1：栈的原理

class Stack():
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)
        return True

    def pop(self):
        #先判断栈是否为空
        if self.stack:
            item = self.stack.pop()
            return item
        else:
            return False

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return False

    def length(self):
        return len(self.stack)

    def view(self):
        return ','.join(self.stack)


s = Stack()
s.push('1')
s.push('2')
item = s.pop()
print(item)

# 三、__str__方法

"""
如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：
不使用 __str__  ，print打印出来是个对象的地址；使用了就把对象变成字符串
"""

class Cat():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return '我是%s' %self.name


tom = Cat('牛奶')
print(tom)


# 四、数据封装

"""
#封装
#面向对象第一步 ： 将属性和方法封装到一个抽象的类中
#外界使用类创建对象，然后让对象调用方法
#对象方法的细节都封装在类的内部

需求
1.小明体重75.0公斤
2.小明每次跑步会减肥0.5公斤
3.小明每次吃东西会增重1公斤
"""

class Person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return '我的名字叫%s 体重是%.2f' %(self.name,self.weight)

    def run(self):
        print('%s爱跑步' %self.name)
        self.weight -= 0.5

    def eat(self):
        print('%s吃东西' %self.name)
        self.weight += 1

xiaoming = Person('小明',76.0)
print(xiaoming)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)

# 练习2
"""
需求：
1.房子有户型，总面积和家具名称列表
        新房子没有任何的家具

2.家具有名字和占地面积，其中
        床：占4平米
        衣柜：占2平米
        餐桌：占1.5平米
3.将以上三件家具添加到房子中
4.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""
class HouseItem():
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return '[%s]占地 %.2f' %(self.name,self.area)

#1.创建家具
# bed = HouseItem('bed',4)
# print(bed)
# wardrobe = HouseItem('wardrobe',2)
# print(wardrobe)
# table = HouseItem('table',1.5)
# print(table)

class House():
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        #剩余面积
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ('户型:%s\n总面积:%.2f[剩余:%.2f]\n家具:%s'%(self.house_type,self.area,self.free_area,self.item_list))

    def add_item(self,item):
        #1.判断家具的面积
        if item.area > self.free_area:
            print('%s的面积太大，无法添加' %item.name)

        #2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        #3.计算剩余面积
        self.free_area -= item.area

#1.创建家具对象
bed = HouseItem('bed',4)
# print(bed)
wardrobe = HouseItem('wardrobe',2)
# print(yg)
table = HouseItem('table',1.5)
# print(table)

#2.创建房子对象
my_house = House('两室一厅',100)
#3.添加家具
my_house.add_item(bed)
my_house.add_item(wardrobe)
my_house.add_item(table)
print(my_house)


# 练习3

"""
1.士兵瑞恩有一把AK47
2.士兵可以开火(士兵开火扣动的是扳机)
3.枪 能够 发射子弹(把子弹发射出去)
4.枪 能够 装填子弹 --增加子弹的数量
Soldier                     Gun
-------------               -----------------
name                        model
gun                         bullet_count #子弹数量足够多才能完成射击的动作
-------------               -----------------
__init__(self):                 __init__(self):
fire(self):                 add_bullet(self,count):#装填子弹的方法
                            shoot(self):
"""

class Gun():
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <=0:
            print('%s没有子弹了...' %self.model)
        else:
            self.bullet_count -= 1
            print('%s子弹剩下%s' %(self.model,self.bullet_count))

class Soldier():
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun == None:
            print('%s还没有枪...' %self.name)
        else:
            self.gun.shoot()
##            self.gun.add_bullet(5)

ak47 = Gun('ak47')
ak47.add_bullet(5)
ak47.shoot()

ryan = Soldier('瑞恩')
ryan.gun = ak47
ryan.fire()
ryan.fire()
ryan.fire()
ryan.fire()
ryan.fire()
ak47.add_bullet(5)
ryan.fire()
ryan.fire()
ryan.fire()

