# NO1、面向对接编程.一、类的创建与运用 二、类成员:类属性(类变量)和成员变量
# NO2、类的封装、继承和多态 一、封装  二、继承  三、多态

# NO1、面向对接编程


"""
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
"""

# 一、类的创建与运用

"""
◇ 类：用来描述具有相同属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例
◇ 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
◇ 方法：类中定义的函数。
◇ 实例化：创建一个类的实例，一个类的具体对象。
◇ 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外，通常不作为实例变量使用。
◇ 实例变量：定义在方法中的变量，只作用于当前实例的类。
◇ 数据成员：类变量或者实例变量，用于处理类及其实例对象的相关数据。
◇ 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个改写的过程叫做方法的覆盖，也称作方法的重写。
◇ 继承：指一个派生类继承基类的字段和方法。继承允许把一个派生类的对象作为一个基类对象对待
"""


# 1.第一个面向对象程序 需求：猫爱吃鱼，小猫要喝水
class Cat(object):
    def eat(self):
        print('%s爱吃鱼' % self.name)

    def drink(self):
        print('小猫要喝水')


tom = Cat()
# 变量是创建一个实例，<变量>=<类名>(),isinstance(tom,Cat)可测试某个对象是某个类的实例，是返回True,不是False
tom.name = 'Tom'
print(tom)
tom.eat()
tom.drink()

hello_kitty = Cat()
hello_kitty.name = 'hello_kitty'
hello_kitty.eat()
hello_kitty.drink()

# 2.__init__(self) 初始化的方法

"""
由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法
"""

print("__init__(self) 初始化的方法")

class Cat(object):
    def __init__(self, name):  # __init__初始化
        print('这是一个初始化方法')
        self.name = name

    def eat(self):
        print('%s爱吃鱼' % self.name)


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


# 练习1：栈的原理
class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        return True

    def pop(self):
        # 先判断栈是否为空
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

# 3、__ del __ 方法

"""
定义了 __ del __ 方法之后，当一个对象要从内存中销毁，销毁之前， __ del __ 方法会被自动调用。

如果想在对象被销毁前，再做一些事情，就可以使用 __ del __ 方法。
"""
print("__ del __ 方法")

class Cat(object):

    def __init__(self, name):
        self.name = name
        print('%s来了！' % self.name)

    def __del__(self):
        print('%s走了！' % self.name)  # 执行完变量的所有相关代码，然后才执行此句


tom = Cat('汤姆')
print(tom.name)

"""
·一个对象从类的实例化创建，生命周期开始
·一个对象的 __ del __ 方法一旦被调用，生命周期结束
·在对象的生命周期内，可以访问对象属性，或者让对象调用方法
"""

# 4、__str__方法

"""
使用print函数输出对象变量时，默认情况下，会输出这个变量引用的对象是由哪一个类创建的对象，以及这个变量在内存中的地址（用十六进制表示）。
如果在开发中，希望在使用print函数输出对象变量时，能够打印自定义的内容，那么就可以使用 __ str __ 这个内置方法。
@注意， __ str __ 方法必须返回一个字符串。
"""

print("__str__方法")

class Cat(object):

    def __init__(self, name):
        self.name = name
        print('%s来了！' % self.name)

    def __del__(self):
        print('%s走了！' % self.name)   # 执行完变量的所有相关代码，然后才执行此句

    def __str__(self):
        return '我是小猫：%s' % self.name  # 必须返回一个字符串


tom = Cat('汤姆')

print(tom)  # 因为定义了__str__方法，所以这里打印对象变量tom，只会输出方法里自定义的内容


# 5、私有属性

"""
实例可以轻松地获取和修改方法中定义的属性的值，但是有时候我们需要限制实例随意修改属性，这时候就要用到私有属性。
定义私有属性很简单，只要在定义属性名字的时候使用两条下划线作为开头，Python解释器就会认为这个属性是私有的，外部不能随便访问这个属性。
私有属性是只能在类内部被操作的属性，实例不能直接访问。也就是说，在对象的方法内部，是可以访问对象的私有属性的，但在外部不能。
在平时的实际项目中，我们可以使用这个特性保护一些不想让用户随意修改的属性
"""

print('私有属性')

class Dog:

    def __init__(self, name):
        self.__name = name  # 定义name私有属性
        self.__age = None  # 定义age私有属性
        print(self.__name, '取名成功')

    def set_age(self, age):
        if not isinstance(age, int):
            print('年龄必须是整型！')
            return False

        if age <= 0:
            print('年龄必须大于0！')
            return False

        self.__age = age

    def shout(self):
        print('汪汪汪！我今年%s岁' % self.__age)


dog = Dog('旺财')
dog.set_age('hello')
dog.set_age(-20)
dog.set_age(5)
dog.shout()

'''
print(dog.__name)
这是错误的语法，因为__name是私有属性，变量不能直接访问私有属性
在上面的例子中，__age是私有属性，实例化后只能通过set_age方法设置年龄，变量不能直接访问
'''

# 6、私有方法
"""
与私有属性一样，私有方法只能够在类内部被调用，实例不能够直接调用。
定义私有方法的方式跟定义私有属性一样，只要在定义方法名字的时候使用两条下划线作为开头即可。
调用私有方式的格式为“对象变量._类名__方法名（参数）”。这是因为Python解释器中，所有以双下划开发的方法都会被翻译成方法前面加上单下划线和类名形式
"""
print("私有方法")

class Dog(object):
    def __animal(self, name):
        print('我的名字叫：%s' % name)


dog = Dog()  # 创建对象变量
dog._Dog__animal("旺财")   # 调用私有方法


# 二、类成员:类属性(类变量)和成员变量

class TestClass(object):
    val1 = 100  # 类变量，可由类名调用TestClass.val1，也可以类对象调用inst.val1

    def __init__(self):
        self.val2 = 200     # 成员变量可由类的对象调用

    def fcn(self, val=400):
        val3 = 300      # val3不是成员变量，它只是函数fcn内部的局部变量
        self.val4 = val
        self.val5 = 500     # val4与val5都不是成员变量，虽然有self给出，但并没有在构造函数中初始化


if __name__ == '__main__':
    inst = TestClass()

    print(TestClass.val1)
    print(inst.val1)
    print(inst.val2)
    # print(inst.val3)  # 以下3个调用会报错
    # print(inst.val4)
    # print(inst.val5)

# 1.类属性（类变量）
print('类属性')

class Tool(object):
    # 要定义类属性，在类名下方使用赋值语句就可以
    count = 0  # 使用赋值语句，定义类属性，记录创建工具对象的总数

    def __init__(self, name):
        self.name = name

        Tool.count += 1  # 让类属性的值+1


# 创建工具对象
tool1 = Tool('斧头')
tool2 = Tool('锯子')
tool3 = Tool('铁锹')

print('一共创建了 %d 个工具对象！' % Tool.count)  # 输出工具对象总数

"""
因此，访问类属性有两种方式：①类名.类属性或②对象名.类属性（不推荐） 
注意，如果使用 “对象名.类属性 = 值” 赋值语句，只会给对象添加一个属性（即实例属性），而不会影响到类属性的值。
"""

# 2.类方法
"""
类方法就是针对类对象定义的方法。在类方法内部可以直接访问类属性或调用其它的类方法。
类方法需要用装饰器 “@classmethod” 来标识，告诉解释器这是一个类方法。
类方法的第一个参数不再是self，而是cls；这个参数和实例方法中的self参数类似；由哪一个类调用的方法，方法内的cls就是哪一个类的引用。
通过 “类名.” 调用类方法时，不需要传递cls参数。
在方法内部，可以通过 “cls.” 访问类的属性，也可以通过 “cls.” 调用其它的类方法。
定义类方法的语法格式如下：
@classmethod
def 类方法名(cls):
    代码块
"""
print('类方法')

class Tool(object):

    count = 0  # 使用赋值语句，定义类属性，记录创建工具对象的总数

    @classmethod  # 装饰器，标识类方法
    def show_tool_count(cls):  # 定义类方法
        print('工具对象的总数为：%d' % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1  # 让类属性的值+1


# 创建工具对象
tool1 = Tool('斧头')
tool2 = Tool('锯子')

Tool.show_tool_count()  # 调用类方法，cls参数不用传入实参

# 3.静态方法
"""
在开发时，如果需要在类中封装一个方法，这个方法既不需要访问实例属性或调用实例方法，也不需要访问类属性或调用类方法，这个时候，就可以把这个方法封装成一个静态方法。
静态方法需要用装饰器 “@staticmethod” 来标识，告诉解释器这是一个静态方法。
通过 “类名.” 调用静态方法。
静态方法不需要有类似self的参数。
定义静态方法的语法格式如下：
@staticmethod
def 静态方法名():
    代码块
"""

print('静态方法')

class Dog(object):

    @staticmethod  # 装饰器，标识静态方法
    def run():  # 定义静态方法
        print('小狗在跑...')


Dog.run()  # 调用静态方法，不需要创建对象，直接调用



# NO2、封装、继承和多态

"""面向对象编程具有三大特性——封装性、继承性和多态性，这些特性使程序设计具有良好的扩展性和健壮性。
封装：根据职责将属性和方法封装到一个抽象的类中
继承：实现代码的重用，相同的代码不需要重复的编写
多态：不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度
"""

# 一、数据封装
"""
#封装——小明爱跑步
#面向对象第一步 ： 将属性和方法封装到一个抽象的类中
#外界使用类创建对象，然后让对象调用方法
#对象方法的细节都封装在类的内部

需求：
1.小明体重75.0公斤
2.小明每次跑步会减肥0.5公斤
3.小明每次吃东西会增重1公斤
"""
class Person(object):
    def __init__(self, name, weight):
        # self.属性名 = 形参
        self.name = name    # 定义name属性
        self.weight = weight    # 定义weight属性

    def __str__(self):  # 用__str__方法存储自定义内容
        return '我的名字叫%s 体重是%.2f' % (self.name, self.weight)

    def run(self):
        print('%s爱跑步' % self.name)
        self.weight -= 0.5

    def eat(self):
        print('%s吃东西' % self.name)
        self.weight += 1


xiaoming = Person('小明', 76.0)   # 创建对象变量xiaoming
print(xiaoming)
xiaoming.run()   # 调用run（）方法
print(xiaoming)  # 打印自定义内容
xiaoming.eat()   # 调用eat（）方法
print(xiaoming)  # 打印自定义内容
"""在对象的方法内部，是可以直接访问对象属性的；同一个类创建的多个对象之间，属性互不干扰。"""


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


class HouseItem(object):    # 定义家具类
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '[%s]占地 %.2f' % (self.name, self.area)


# 1.创建家具
# bed = HouseItem('bed',4)
# print(bed)
# wardrobe = HouseItem('wardrobe',2)
# print(wardrobe)
# table = HouseItem('table',1.5)
# print(table)

class House(object):    # 定义房子类
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        self.item_list = []

    def __str__(self):
        # Python能够自动的将一对括号内的代码连接在一起
        return '户型:%s\n总面积:%.2f[剩余:%.2f]\n家具:%s' % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        # 1.判断家具的面积
        if item.area > self.free_area:
            print('%s的面积太大，无法添加' % item.name)

        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area


# 1.创建家具对象
bed = HouseItem('bed', 4)
# print(bed)
wardrobe = HouseItem('wardrobe', 2)
# print(yg)
table = HouseItem('table', 1.5)
# print(table)

# 2.创建房子对象
my_house = House('两室一厅', 100)
# 3.添加家具
my_house.add_item(bed)
my_house.add_item(wardrobe)
my_house.add_item(table)
print(my_house)

# 练习3
'''
1.士兵瑞恩有一把AK47
2.士兵可以开火(士兵开火扣动的是扳机)
3.枪 能够 发射子弹(把子弹发射出去)
4.枪 能够 装填子弹 --增加子弹的数量
Soldier                     Gun
-------------               -----------------
name                        model
gun                         bullet_count #子弹数量足够多才能完
成射击的动作
-------------               -----------------
__init__(self):                 __init__(self):
fire(self):                 add_bullet(self,count):#装填子弹的方法
                            shoot(self):
'''


class Gun(object):
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count = count  # 更换弹夹是直接去掉原有弹夹，换上满的弹夹，不是剩下的子弹数加上新的子弹数

    def shoot(self):
        if self.bullet_count <= 0:
            print('%s没有子弹了...' % self.model)
        else:
            self.bullet_count -= 1
            print('%s~~~~~%s' % (self.model, self.bullet_count))


class Soldier(object):
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:    # 在Python中，针对 “None” 比较时，建议使用 “is” 来判断
            print('%s还没有枪...' % self.name)
        else:
            # self.gun.add_bullet(10)
            self.gun.shoot()


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
ryan.gun.add_bullet(5)
ryan.fire()
ryan.fire()
ryan.gun.add_bullet(5)
ryan.fire()


# 二、继承
"""
继承的基本思想是，在一个类的基础上定义出另一个新的类，这个新的类不仅可以继承原来类的所有属性和方法，
还可以增加新的属性和方法；原来的类被称为父类，新的类被称为子类

父类的定义和一般类的定义一样，子类的定义格式如下:
# SubClass为子类的名字，BaseClass为父类的名字
class SubClass(BaseClass1, BaseClass2, ...
    代码块
"""

class Animal:  # 定义父类Animal

    def eat(self):
        print('能吃！')

    def drink(self):
        print('能喝！')

    def run(self):
        print('能跑！')

    def sleep(self):
        print('能睡！')


class Dog(Animal):  # 定义Animal的子类Dog

    def bark(self):  # 新增bark()方法
        print('能叫！')


class XiaoTianQuan(Dog):  # 定义Dog的子类XiaoTianQuan

    def fly(self):  # 新增fly()方法
        print('能飞！')


class Cat(Animal):  # 定义Animal的子类Cat

    def catch(self):  # 新增catch()方法
        print('能抓老鼠！')


print('Animal类的对象：')

animal = Animal()  # 创建animal对象

animal.eat()
animal.drink()
animal.run()
animal.sleep()

print('Dog类的对象：')

dog = Dog()  # 创建dog对象

dog.eat()
dog.drink()
dog.run()
dog.sleep()
dog.bark()

print('XiaoTianQuan类的对象：')

xiaotianquan = XiaoTianQuan()  # 创建xiaotianquan对象

xiaotianquan.eat()
xiaotianquan.drink()
xiaotianquan.run()
xiaotianquan.sleep()
xiaotianquan.bark()
xiaotianquan.fly()

print('Cat类的对象：')

cat = Cat()  # 创建cat对象

cat.eat()
cat.drink()
cat.run()
cat.sleep()
cat.catch()

"""
方法重写
当父类的方法不能满足子类的需求时，可以在子类中对父类的方法进行重写。方法重写有两种情况：
1.覆盖父类的方法。 如果在开发中，父类的方法实现和子类的方法实现完全不同，就可以使用覆盖的方式，在子类中重新编写父类的方法实现；具体的实现方式，
就是在子类中定义一个和父类中同名的方法，并且实现；重写之后，在运行时只会调用在子类中重写的方法，而不再会调用父类中名字相同的方法。
2.对父类方法进行扩展。 如果在开发中，子类的方法实现包含父类的方法实现，即父类原本封装的方法实现是子类方法的一部分，就可以使用扩展的方式；具体的实现方式，
是在子类中重写父类的方法，在需要的位置使用 “super().父类方法” 来调用父类的方法，在其它位置针对子类的需求编写子类特有的代码实现。

关于super:
在Python中是一个特殊的类
super()就是使用super类创建出来的对象
最常使用的场景就是在重写父类方法时，调用在父类中封装的方法实现
"""

class Animal:  # 定义父类Animal

    def eat(self):
        print('能吃！')

    def drink(self):
        print('能喝！')

    def run(self):
        print('能跑！')

    def sleep(self):
        print('能睡！')


class Dog(Animal):  # 定义Animal的子类Dog
    # 如果子类中，重写了父类的方法，在使用子类对象调用方法时，会调用子类中重写的方法
    def eat(self):
        print('小狗生病了，吃不下东西')

    def run(self):
        print('小狗腿折了，不能跑，只能走')


dog = Dog()  # 创建dog对象

dog.eat()  # 实现在子类中重写的方法
dog.drink()  # 实现从父类中继承的方法
dog.run()  # 实现在子类中重写的方法
dog.sleep()  # 实现从父类中继承的方法


""" 方法重写——扩展 """

class Animal:  # 定义父类Animal

    def eat(self):
        print('能吃！')

    def drink(self):
        print('能喝！')

    def run(self):
        print('能跑！')

    def sleep(self):
        print('能睡！')


class Dog(Animal):  # 定义Animal的子类Dog

    def eat(self):
        super().eat()  # 使用"super().父类方法"调用原本在父类中封装的eat()方法
        print('比隔壁邻居家的狗还能吃！！')

    def run(self):
        super().run()  # 使用"super().父类方法"调用原本在父类中封装的run()方法
        print('比隔壁邻居家的狗跑的还要快！！！')


dog = Dog()  # 创建dog对象

dog.eat()  # 实现在子类中重写的方法
dog.drink()  # 实现从父类中继承的方法
dog.run()  # 实现在子类中重写的方法
dog.sleep()  # 实现从父类中继承的方法

"""在Python中，子类可以拥有多个父类，并且具有所有父类的属性和方法。
class 子类名(父类名1, 父类名2, ...):
    代码块
"""

print('多继承')

class A:  # 定义父类A

    def test(self):
        print('我是C的父类：A')


class B:  # 定义父类B

    def demo(self):
        print('我是C的父类：B')


class C(A, B):  # 定义A、B的子类C

    pass  # 占位语句


c = C()  # 创建子类C的对象

c.test()  # 调用父类A的方法
c.demo()  # 调用父类B的方法


"""
MRO——方法搜索顺序
"""

print('MRO——方法搜索顺序')

class A:  # 定义父类A

    def test(self):
        print('A --- test方法')

    def demo(self):
        print('A --- demo方法')


class B:  # 定义父类B

    def test(self):
        print('B --- test方法')

    def demo(self):
        print('B --- demo方法')


class C(B, A):  # 定义A、B的子类C

    pass  # 占位语句


c = C()  # 创建子类C的对象

c.test()  # 调用父类A的方法
c.demo()  # 调用父类B的方法

print(C.__mro__)  # 使用内置属性__mro__查看子类对象调用方法的顺序

'''
先查看当前类，即C类，C类中没有要调用的方法，查看下一个类
因为在定义C类时，C的父类中，B类排在A类前面，所以先查看B类
B类中有要调用的方法，因此调用B类中的方法，调用完不再搜索
'''

# 三、多态
# 多态案例1
print('多态案例1')

class Human:  # 定义父类

    def work(self):
        print('人类要辛勤工作~')


class Programmer(Human):  # 定义human的子类

    def work(self):  # 重写父类的方法
        print('程序员要编写程序！！')


class Designer(Human):  # 定义human的子类

    def work(self):  # 重写父类的方法
        print('设计师要设计作品！！')


human = Human()
human.work()  # 调用父类的work()方法

programmer = Programmer()
programmer.work()  # 调用子类Programmer的work()方法

designer = Designer()
designer.work()  # 调用子类Designer的work()方法

# 多态案例2
"""
在Dog类中封装game()方法
普通狗只是简单的玩耍
定义XiaoTianDog类继承自Dog类，并且重写game()方法
哮天犬需要在天上玩耍
定义Person类，并且封装一个game_with_dog()方法
在方法内部，直接让狗对象调用game()方法
"""

print('多态案例2')

class Dog(object):  # 定义父类Dog

    def __init__(self, name):  # 定义初始化方法，并定义name参数
        self.name = name  # 定义name属性，并把参数赋值给它

    def game(self):  # 定义game()方法
        print('%s蹦蹦跳跳的去玩耍...' % self.name)


class XiaoTianDog(Dog):  # 定义Dog的子类XiaoTianDog

    def game(self):  # 重写父类的game()方法
        print('%s飞到天上去玩耍...' % self.name)


class Person(object):  # 定义Person类

    def __init__(self, name):  # 定义初始化方法，并定义name参数
        self.name = name  # 定义name属性，并把参数赋值给它

    def game_with_dog(self, dog):  # 定义game_with_dog()方法，并定义dog参数
        print('%s和%s快乐的玩耍...' % (self.name, dog.name))

        dog.game()  # 在方法内部调用game()方法


wangcai = Dog('旺财')  # 创建Dog类对象

fly_wangcai = XiaoTianDog('飞天旺财')  # 创建XiaoTianDog类对象

xiaoming = Person('小明')  # 创建Person类对象

xiaoming.game_with_dog(wangcai)  # 调用game_with_dog()方法，并传入实参wangcai

print('---------')

xiaoming.game_with_dog(fly_wangcai)  # 调用game_with_dog()方法，并传入实参fly_wangcai
