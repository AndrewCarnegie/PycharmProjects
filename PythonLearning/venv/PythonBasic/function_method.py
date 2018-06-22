'''

函数：存在于模块之中，类之外的程序片段，使用def定义
方法：存在于类之中的程序片段，使用def定义,在Python中称为成员方法或者成员函数

使用方式：

函数和方法都是可以串联使用的，这种串联称为串链，但是调用的先后顺序却不同

函数串链(function chaining)的invoke顺序：从右向左
方法串链(method chaining)的invoke顺序：从左向右
'''

#方法串链 下面的strip()和split()方法都是str对象的成员方法
text_content = '    Hi, What are you doing '
test_list =text_content.strip().split(',')
print(test_list)

#函数串链 下面的print()和sorted()都是BIF

test_list=[21, 11, 8, 19]
print(sorted(test_list))

