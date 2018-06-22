list_test = []
a = 0
b = 1
for i in range(1, 10):
    a, b = b, a + b
    list_test.append(b)
print(list_test)