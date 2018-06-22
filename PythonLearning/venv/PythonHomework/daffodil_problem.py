"""
First realization: the function part written by myself
"""

def break_number(number):
    list_number = []
    if number >= 100 and number <= 999:
        list_number.append(int(number / 100))
        list_number.append(int((number - int(number / 100) * 100) / 10))
        list_number.append((number - int(number / 100) * 100 - int((number - int(number / 100) * 100) / 10) * 10))
    return list_number

def sum_number(list_):
    sum_ = 0
    for i in list_:
        sum_ += i ** 3
    return sum_

final_list = []

for i in range(100, 1000):
    if sum_number(break_number(i)) == i:
        final_list.append(i)

print(final_list)


"""
Second realization: got from network
"""

for n in range(100,1000):
    i = int(n / 100)
    j = int(n / 10 % 10)
    k = int(n % 10)
    if n == i ** 3 + j ** 3 + k ** 3:
        print(n, end=' ')





