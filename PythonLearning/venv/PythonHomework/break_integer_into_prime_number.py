"""

first part: written by myself
"""

input_number =int(input('Please enter one integer: '))
list_ = []
for i in range(2, input_number+1):
    while input_number != i:
        if input_number % i == 0:
            list_.append(i)
            input_number = input_number / i
        else:
            break
list_.append(int(input_number))
print(list_)


"""

second part: got from network
"""
from sys import stdout
n = int(input("input number:\n"))
print("n = %d" % n)

for i in range(2,n + 1):
    while n != i:
        if n % i == 0:
            stdout.write(str(i))
            stdout.write("*")
            n = n / i
        else:
            break
print("%d" % n)