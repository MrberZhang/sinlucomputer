# Python 命令行参数(Arguments)

"""Python 提供了 getopt 模块来获取命令行参数。
Python 中也可以使用 sys 的 sys.argv 来获取命令行参数：
sys.argv 是命令行参数列表。
len(sys.argv) 是命令行参数个数。
注：sys.argv[0] 表示脚本名。 """

# 实例
# import sys
# print(f"参数个数为：{len(sys.argv)}个参数")
# print(f"参数列表：{str(sys.argv)}")


# getopt 模块
from random import choices

"""getopt模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是sys.argv。命令行选项使得程序的参数更加灵活。支持短选项模式- 和长选项模式-- 
该模块提供了两个方法及一个异常处理来解析命令行参数 """
# getopt.getopt 方法
"""getopt.getopt 方法用户解析命令行参数列表，语法格式如下：
getopt.getopt(args,options[, long_options])
方法参数说明：
·args：要解析的命令行参数列表
·options：以字符串的格式定义，options 后的冒号：表示如果设置该选项，必须有附加的参数，否则就不附加参数。
·long_options：以列表的格式定义，long_options 后的等号 = 表示该选项必须有附加参数，不带等号表示该选项不附加参数。
·该方法返回值由2个元素组成：第一个是（option,valus）元祖的列表，第二个是参数列表，包含那些没有 - 或 -- 的参数 
另外一个方法是 getopt.gnu_getopt，这里不多做介绍。 """
# Exception getopt.GetoptError
"""在没有找到参数列表，或选项的需要的参数为空时会触发该异常。
异常的参数是一个字符串，表示错误的原因，属性msg 和 opt 为相关选项的错误信息。 """
# 假定我们创建这样一个脚本，可以通过命令行向脚本文件传递两个文件名，同时我们通过另外一个选项查看脚本的使用。脚本使用方法如下：
# usage: test.py -i <inputfile> -o <outputfile>
# text文件代码如下所示：
# import sys, getopt
#
# def main(argv):
#     inputfile = ''
#     outputfile = ''
#     try:
#         opts, args = getopt.getopt(argv, "ji:o:", ["ifile=", "ofile="])
#     except getopt.GetoptError:
#         print('test.py -i <inputfile> -o <outputfile> ')
#         sys.exit()
#     for opt, arg in opts:
#         if 'opt' == "-h":
#             print('test.py -i <inputfile> -o <outputfile>')
#         elif opt in ("-i", "--ifile"):
#             inputfile = arg
#         elif opt in ("-o", "--ofile"):
#             outputfile = arg
#     print(f"输入的文件为：{inputfile}")
#     print(f"输出的文件为：{outputfile}")
#
#
# if __name__ == "__main__":
#     main(sys.argv[1:])


# argparse 模块 它可以满足我对命令解析器的几乎所有要求。它支持解析一个参数的多个值，自动生成帮助命令和帮助文档，支持子解析器，限制参数值的范围等等。
"""1. 命令行参数分为位置参数和选项参数：
位置参数就是程序根据该参数出现的位置来确定的
如：[root@openstack_1 /]# ls root/ #其中root/是位置参数
选项参数是应用程序已经提前定义好的参数，不是随意指定的
如：[root@openstack_1 /]# ls -l # -l 就是ls命令里的一个选项参数  """
# 2 使用步骤
"""（1）import argparse 首先导入模块
（2）parser = argparse.ArgumentParser（） 创建一个解析对象
（3）parser.add_argument() 向该对象中添加你要关注的命令行参数和选项
（4）parser.parse_args() 进行解析 """
# 3 argparse.ArgumentParser（）方法参数须知：一般我们只选择用description
"""
1 description - 命令行帮助的开始文字，大部分情况下，我们只会用到这个参数
2 epilog - 命令行帮助的结尾文字
3 prog - (default: sys.argv[0])程序的名字，一般不需要修改，另外，如果你需要在help中使用到程序的名字，可以使用%(prog)s
4 prefix_chars - 命令的前缀，默认是-，例如-f/–file。有些程序可能希望支持/f这样的选项，可以使用prefix_chars=”/”
5 fromfile_prefix_chars - (default: None)如果你希望命令行参数可以从文件中读取，就可能用到。例如，如果fromfile_prefix_chars=’@’,
命令行参数中有一个为”@args.txt”，args.txt的内容会作为命令行参数
6 add_help - 是否增加-h/-help选项 (default: True)，一般help信息都是必须的，所以不用设置啦。
7 parents - 类型是list，如果这个parser的一些选项跟其他某些parser的选项一样，可以用parents来实现继承，例如parents=[parent_parser]
8 三个允许的值： 
  # class argparse.RawDescriptionHelpFormatter 直接输出description和epilog的原始形式（不进行自动换行和消除空白的操作）
  # class argparse.RawTextHelpFormatter 直接输出description和epilog以及add_argument中的help字符串的原始形式（不进行自动换行和消除空白的操作） 
  # class argparse.ArgumentDefaultsHelpFormatter 在每个选项的帮助信息后面输出他们对应的缺省值，如果有设置的话。这个最常用吧！
9 argument_default - (default: None)设置一个全局的选项的缺省值，一般每个选项单独设置，所以这个参数用得少，不细说
10 usage - (default: generated)如果你需要修改usage的信息（usage: PROG [-h] [–foo [FOO]] bar [bar …]），那么可以修改这个，一般不要修改。
11 conflict_handler - 不建议使用。这个在极端情况下才会用到，主要是定义两个add_argument中添加的选项的名字发生冲突时怎么处理，默认处理是抛出异常。  """
# 4 add_argument()方法参数须知：
"""1 name or flags - 指定参数的形式，想写几个写几个，不过我们一般就写两个，一个短参数，一个长参数，看下面的例子”-f”, “–file”
2 可选的选项，位置不固定，想怎么写就怎么写，默认是可选的 # parser.add_argument(“-f”, “–file”, help=”test test test”)
3 位置固定的选项，例如”prog i_am_bar”，这样子的话，i_am_bar就是bar选项的值啦，默认是必须有的 # parser.add_argument(“bar”, help=”test test test”)
4 nargs - 指定这个参数后面的value有多少个，例如，我们希望使用-n 1 2 3 4，来设置n的值为[1, 2, 3, 4] #parser.add_argument(“-n”, “–num”, nargs=”+”, type=int) # 这里nargs=”+”表示，如果你指定了-n选项，那么-n后面至少要跟一个参数，+表示至少一个,?表示一个或0个,0个或多个 。
5 default - 如果命令行没有出现这个选项，那么使用default指定的默认值 #parser.add_argument(“+g”, “++gold”, help=”test test test”,default=”test_gold”) # 需要prefix_chars包含”+” 。
6 type - 如果希望传进来的参数是指定的类型（例如 float, int or file等可以从字符串转化过来的类型），可以使用 #parser.add_argument(“-x”, type=int) 。
7 choices - 设置参数值的范围，如果choices中的类型不是字符串，记得指定type哦 #parser.add_argument(“-y”, choices=[‘a’, ‘b’, ‘d’])
8 required - 通常-f这样的选项是可选的，但是如果required=True那么就是必须的了 #parser.add_argument(“-z”, choices=[‘a’, ‘b’, ‘d’], required=True)
9 metavar - 参数的名字，在显示 帮助信息时才用到. # parser.add_argument(“-o”, metavar=”OOOOOO”)
10 help - 设置这个选项的帮助信息
11 dest - 设置这个选项的值就是解析出来后放到哪个属性中 #parser.add_argument(“-q”, dest=”world”)
12 args = parser.parse_args(args) # 如果你没有args参数，那么就使用sys.argv，也就是命令行参数啦。有这个参数，就方便我们调试啊 。# args.world就是-q的值啦
13 action - The basic type of action to be taken when this argument is encountered at the command line.
14 const - A constant value required by some action and nargs selections. """
# # 例子1
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('echo')  # add_argument()指定程序可以接受的命令行选项
# args = parser.parse_args()   # parse_args()从指定的选项中返回一些数据
# print(args)
# print(args.echo)

# 例子2
# import argparse
# parser1 = argparse.ArgumentParser(description='this is a description')
# parser1.add_argument('--ver', '-v', action='store_true', help='hahahaha')
# # 将变量以标签-值的字典形式存入args字典
# args = parser1.parse_args()
# if args.ver:
#     print("True")
# else:
#     print("False")

# 例子 这个例子非常简单：在命令行中输入3个整型数，然后对它们进行求和操作
# import argparse
#
# def arg():
#     # 创建ArgmentParser()对象
#     parser2 = argparse.ArgumentParser(description='add')
#     # 添加参数
#     parser2.add_argument('--first', type=int, default='1', help='first num')
#     parser2.add_argument('--second', type=int, default='2', help='second num')
#     parser2.add_argument('--third', type=int, default='3', help='third num')
#     # 解析参数
#     args = parser2.parse_args()
#     args_vars = vars(args)
#     first = args_vars.get('first')
#     second = args_vars.get('second')
#     third = args_vars.get('third')
#     print(int(first) + int(second) + int(third))
#
#
# if __name__ == '__main__':
#     arg()


# add_argument() 方法详解
# add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
"""参数：
- name or flags ：一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
- action ：当参数在命令行中出现时，使用的动作基本类型
        -store_const :当从命令出现这个参数，则保存const中常量
        -store_true,store_false ：与上面store_const类似，只是保存的是真假值
- nargs ：命令行参数应当消耗的数目
- const ：被一些action 和nargs 选择所需求的常数
- default ：当参数未在命令行出现并且也不存在与命名空间对象时所产生的值
- type ：命令行参数应当被转换成的类型
- choices ：可选参数的容器
- required ：此命令行选项是否可省略（仅选项可用）
- help ：一个此选项作用的简单描述
- metavar ：在使用方法消息中使用的参数值示例
- dest ：被添加到parse_args() 所返回对象的属性名 """
# 参数有很多，这里我们只关注常用的几个。
"""-name or flags ：一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
- default ：当参数未在命令行出现并且也不存在于命名空间对象时所产生的值
    - 所有选项和一些位置参数可能在命令行中被忽略
- action ：指示如何处理命令行参数
- type ： 命令行参数应当被转换成的类型。
    - 默认情况下，解析器会将命令行参数当做简单字符串读入。
- choices：可用的参数的容器。
    - 某些命令行参数应当从一组受限值中选择
- help：一个此选项作用的简单描述 """
# 示例
# import argparse
# parse = argparse.ArgumentParser(description='add')  # 创建ArgumentParser对象
# # 添加参数
# parse.add_argument('--patch_size', type=int, default=100, help="patch size (default: 48)")
# parse.add_argument('--dataset', default="DRIVE", choices=['DRIVE', 'CHASE', 'STARE', 'HRF'])
# # 解析参数
# args = parse.parse_args()
# # 获得参数中的patch_size，dataset 的值
# print(args.patch_size, args.dataset)
# # 打印出所有的参数
# print(args)
# print(type(args))
# """可以发现，返回的是一个Namespace对象，我们需要继续将其转换为Python的字典类型，因为这样更容易保存！"""
# args_vars = vars(args)
# print(args_vars, type(args_vars))


"""python argparse模块用法实例详解 ,需要先在cmd模式，进入到对应的工作目录下：在命令行中输入python python_skill_arguments.py -h """
# 示例1 传入一个参数
# import argparse
# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# # type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('integers', type=str, help='传入的数字')
# args = parser.parse_args()
# # 获得传入的参数
# print(args)

# 操作args字典 其实得到的这个结果Namespace(integers='5')是一种类似于python字典的数据类型。我们可以使用 arg.参数名来提取这个参数
"""在命令行中输入python python_skill_arguments.py 5  命令行中给demo.py 传入一个参数5"""
# import argparse
# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# # type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('integers', type=str, help='传入的数字')
# args = parser.parse_args()
# # 获得传入的参数
# print(args)

# 示例2 传入多个参数
"""在命令行中输入python python_skill_arguments.py 1 2 3 4 """
# import argparse
# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# parser.add_argument('integers', type=str, nargs='+', help='传入的数字')
# args = parser.parse_args()
# print(args.integers)
"""nargs是用来说明传入的参数个数，'+' 表示传入至少一个参数。
这时候再重新在命令行中运行python demo.py 1 2 3 4得到 ['1','2','3','4']

参数nargs：
nargs='*' 　表示参数可设置零个或多个
nargs='+' 表示参数可设置一个或多个
nargs='?'　表示参数可设置零个或一个"""

# 示例3 改变数据类型 add_argument中有type参数可以设置传入参数的数据类型。我们看到代码中有type这个关键词，
"""在命令行中输入python python_skill_arguments.py 1 2 3 4"""
# 该关键词可以传入list, str, tuple, set, dict等。例如我们把上面的type=str，改成type=int,这时候我们就可以进行四则运算
# import argparse
# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# parser.add_argument('integers', type=int, nargs='+', help='传入的数字')
# args = parser.parse_args()
# 对传入的数据进行加总
# print(sum(args.integers))


# 示例4 位置参数 在命令行中传入参数时候，传入的参数的先后顺序不同，运行结果往往会不同，这是因为采用了位置参数
"""在命令行中输入python python_skill_arguments.py 李 四与在命令行中输入python python_skill_arguments.py 四 李
更换第三与第四行，在输入python python_skill_arguments.py 李 四与在命令行中输入python python_skill_arguments.py 四 李"""
# import argparse
# parser = argparse.ArgumentParser(description='姓名')
# parser.add_argument('param1', type=str, help='姓')
# parser.add_argument('param2', type=str, help='名')
# args = parser.parse_args()
# 打印姓名
# print(args.param1 + args.param2)

# 示例5 可选参数 为了在命令行中避免上述位置参数的bug（容易忘了顺序），可以使用可选参数，这个有点像关键词传参，但是需要在关键词前面加--，例如
"""命令行输入python python_skill_arguments.py --family=李 --name=四 """
# import argparse
# parser = argparse.ArgumentParser(description='姓名')
# parser.add_argument('--family', type=str, help='姓')
# parser.add_argument('--name', type=str, help='名')
# args = parser.parse_args()
# # 打印姓名
# print(args.family + args.name)

# 示例6 默认值 add_argument中有一个default参数。有的时候需要对某个参数设置默认值，即如果命令行中没有传入该参数的值，程序使用默认值。 如果命令行传入该参数，则程序使用传入的值。具体请看下面的例子
"""命令行输入python python_skill_arguments.py与python python_skill_arguments.py --family=王"""
# import argparse
# parser = argparse.ArgumentParser(description='姓名')
# parser.add_argument('--family', type=str, default='张', help='姓')
# parser.add_argument('--name', type=str, default='三', help='名')
# args = parser.parse_args()
# # 打印姓名
# print(args.family + args.name)

# 示例7 必需参数 add_argument有一个required参数可以设置该参数是否必需
"""命令行输入python python_skill_arguments.py --family=李 提示必填参数，因为可选参数name的required=True，所以必须要传入。如果我们将其更改为False，程序运行结果"""
# import argparse
# parser = argparse.ArgumentParser(description='姓名')
# parser.add_argument('--family', type=str, help='姓')
# parser.add_argument('--name', type=str, required=True, default='', help='名')
# args = parser.parse_args()
# # 打印姓名
# print(args.family + args.name)

# dest 绑定
import argparse
parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# type是要传入的参数的数据类型  help是该参数的提示信息
parser.add_argument('--param1', dest="xxx", type=str, default='zhang', help='xing')
parser.add_argument('--param2', dest="yyy", type=str, help='ming')
args = parser.parse_args()
# 获得传入的参数
print(args)
print(args.xxx + args.yyy)
print(args.yyy + args.xxx)