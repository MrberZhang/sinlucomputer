# Django 的使用
"""Django最初是被开发用来管理劳伦斯出版集团旗下一些以新闻内容为主的网站的，它以比 利时的吉普赛爵士吉他f- Django Reinhardt来命名，
它和Flask是使用最广泛的Python Web 框架—Django能如此知名很大程度上是因为提供了非常齐备的官方文档，它提供了一站式 的解决方案，
包含缓存、ORM、管理后台、验证、表单处理等，使得开发复杂的数据库驱 动的网站变得很简单但正因为它坚持自己对于Web框架的理解,系统耦合度太高，
替换 掉内置的功能往往需要花费一些功夫，所以学习曲线也相当陡峭。  """


import django
print(django.get_version())