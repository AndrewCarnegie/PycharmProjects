"""
first method:
written by myself

"""
list_test = [5, 3, 10, 71]
list_test1 = []
list_test2 = list_test
for i in list_test:
    list_test1.append(i)
print(list_test1)

#函数id()查看对象的十进制内存地址，可以看到list_test2和list_test指向同一片内存，而list_test1指向新地址
print(id(list_test))
print(id(list_test1))
print(id(list_test2))

"""
second method:
got from network

"""
list_test_a = [5, 3, 10, 71]
list_test_b = list_test_a [:]
print(list_test_b)
