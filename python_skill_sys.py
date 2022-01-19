# python sys 模块

"""Python的sys模块提供访问由解释器使用或维护的变量的接口，并提供了一些函数用来和解释器进行交互，操控Python的运行时环境"""

"""一、 动态对象"""
# 1 sys.argv 传递给程序的命令行参数列表；其中，sys.argv[0]表示脚本名称，各个参数均为字符串类型
import sys
for i in range(len(sys.argv)):
    print("argv{0}:type is {1} , valus is {2}".format(i, type(sys.argv[i]), sys.argv[i]))


# 2 sys.path 模块的搜索路径；sys.path[0] 表示当前脚本所在目录
import sys
print(sys.path)
print(sys.path[0])

# 3 sys.modules 已加载的模块的字典； 可以像一般的字典一样进行各种字典操作。
import sys
print(sys.modules.keys())

# 4 sys.exc_info 获取正在处理的异常的相关信息. 返回值为一个包含异常类、异常实例和异常回溯信息的元组

# 5 sys.last_type 返回最近一次捕获的异常的类型（只在交互式环境下可用）

# 6 sys.last_value 返回最近一次捕获的异常的值（只在交互式环境下可用）

# 7 sys.last_traceback 返回最近一次捕获的异常的追踪信息（只在交互式环境下可用）

"""二、静态对象"""

# sys.builtin_module_names  当前解释器所有内置模块的名称

# sys.copyright  包含解释器版权相关信息的字符串

# sys.exec_prefix  用于查找特定于当前机器的python库的路径前缀

# sys.executable  Python解释器可执行文件的绝对路径

# sys.float_info  包含有关浮点数实现的信息的结构序列

# sys.float_repr_style  表示浮点数的repr()方法的输出样式的字符串

# sys.hash_info  包含哈希算法相关信息的结构序列

# sys.hexversion  对sys.version_info中包含的版本信息进行编码后使用十六进制表示的整数

# sys.implementation 包含有关Python实现的相关信息

# sys.int_info 包含有关整形实现的信息的结构序列

# sys.maxsize 返回字符串、列表、字典和其他内置类型的最大长度

# sys.maxunicode 返回能够表示的最大Unicode码点的整数值

# sys.platform 返回平台标识符字符串

# sys.prefix 返回安装平台无关Python文件的目录

# sys.thread_info 包含有关线程实现的信息的结构序列

# sys.version 表示当前解释器版本的字符串

# sys.version_info 当前解释器版本的命名元组

# sys.byteorder 本机的字节排序方式，little表示小尾，big表示大尾

# sys.api_version 返回表示Python解释器的C语言版本API的整数


"""三 方法"""

# sys.displayhook(p_object) 解释器以交互模式运行时，调用该函数会打印表达式的结果

# sys.excepthook(type, value, traceback) 发生未捕获的异常时将调用该函数
""" 其中，type是异常类，value是异常的实例，traceback是回溯对象。默认行为是打印该异常并回溯到标准错误。
不过，可以重新定义该函数来实现另一种处理未捕获异常的方法（在诸如调试器或者CGI脚本这样的专门的应用程序中可能会用到）"""

# sys.exit(n) 通过引发SystemExit异常来退出当前程序
"""n是一个表示状态码的整数退出码。0值表示正常（默认值），非零值表示异常。如果n指定为一个非整数值，则将它打印到sys.stderr并使用退出码1退出"""

# sys.getdefaultencoding() 返回Unicode实现所使用的默认字符串编码格式

# sys.getfilesystemencoding 返回用于将Unicode文件名转换成操作系统使用的文件名时所用的编码格式

# sys.getfilesystemencodeerrors() 返回将Unicode文件名转换成操作系统使用的文件名时的错误模式

# sys.getdlopenflags() 返回调用C函数 dlopen 时使用的标志参数的值。

# sys.getprofile() 返回由sys.setprofile(function)设置的系统配置函数

# sys.getcheckinterval() 返回由sys.setcheckinterval()函数设置的检查异步事件的频率

# sys.getrefcount(obj) 返回对象obj的引用计数

# sys.getrecursionlimit() 返回解释器的最大递归深度

# sys.getsizeof() 获取对象占用的内存大小（用字节表示）

# sys.gettrace() 返回由sys.settrace(function)设置的跟踪函数

# sys.setcheckinteral(n) 设置python解释器每n条指令执行一次异步事件的检查。这个设置会影响线程切换的频率

# sys.setdlopenflags(n) 设置调用C函数 dlopen 时使用的标志参数的值

# sys.setprofile(function) 设置系统配置函数，用于实现源代码配置程序

# sys.setrecursionlimit(n) 设置解释器的最大递归深度

# sys.settrace(tfunc) 设置系统跟踪函数，用于实现调试器
