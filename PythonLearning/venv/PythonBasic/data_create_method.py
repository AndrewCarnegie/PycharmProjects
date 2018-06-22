
# 方法一： 使用括号创建
test1 = ()
print(type(test1))
test2 =[]
print(type(test2))
test3 = {}
print(type(test3))


# 方法二： 使用工厂函数创建,工厂函数也可以用来数据类型之间的转换
test4 = tuple()
print(type(test4))
test5 = list()
print(type(test5))
test6 = dict()
print(type(test6))