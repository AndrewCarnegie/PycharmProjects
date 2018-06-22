"""
research description:

    There is one int number. after plus it with 100 or 268, it will be perfect square number

question:

    how many numbers there is between 1 and 10000?

"""

import math

# correct method
for i in range(1, 10000):
    a = int(math.sqrt(i + 100))
    b = int(math.sqrt(i + 268))
    if (a * a == i + 100) and (b * b == i + 268):
        print(i)

# wrong method
"""
Why here it's wrong, sqrt method always return float number but not int number, 
so isinstance() and isdigit() can't be used here to judge

practice:
int()
sqrt()
isinstance()
isdigit()


"""
for i in range(1, 10000):
    a1 = math.sqrt(i + 100)
    b1 = math.sqrt(i + 268)
    while isinstance(a1, int) and isinstance(b1, int):
        print(i)
