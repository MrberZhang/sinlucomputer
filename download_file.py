#!C:/Users/xinlu/AppData/Local/Programs/Python/Python39/python.exe

# HTTP 头部
print('Content-Disposition: attachment; filename=\"foo.txt\"')
print()

# 打开文件
fo = open("E:/foo.txt", "r")  # "E:/foo.txt" 为文件路径path

str1 = fo.read();
print(str1)

# 关闭文件
fo.close()
