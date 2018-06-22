import re
import sys
def bonus(benefit):
    if benefit <=0:
        return 0
    elif benefit > 0 and benefit <= 10:
        return benefit * 0.1
    elif benefit >10 and benefit <= 20:
        return 10 * 0.1 + (benefit -10) * 0.075
    elif benefit >20 and benefit <= 40:
        return 10 * 0.1 + 10 * 0.075 + (benefit -20) * 0.05
    elif benefit >40 and benefit <= 60:
        return 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (benefit -40) * 0.03
    elif benefit >60 and benefit <= 100:
        return 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (benefit -60) * 0.015
    else:
        return 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (benefit -100) * 0.01


input_value = input('Please enter the benefit: ')
input_rule = re.compile(r'[0-9]+') #this regular expression didn't work yet
result = input_rule.match(input_value)

while True:
    while result:
        try:
            input_value = int(input_value)
        except:
            input_value = input('Please enter the number for the benefit but not string: ')
            result = input_rule.match(input_value)
        else:
            print('Your bonus should be {0} after calculation with benefit {1}'.format(bonus(input_value) * 10000, input_value * 10000))
            input_value = input('Please enter the benefit: ')
            result = input_rule.match(input_value)
    else:
        input_value = input('Please enter the number for the benefit but not string: ')
        result = input_rule.match(input_value)