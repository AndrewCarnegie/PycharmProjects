import re
def bonus(benefit):
    arr =[100, 60, 40, 20, 10, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    bonus_ = 0
    for index in range(0,6):
        if benefit > arr[index]:
            bonus_ += (benefit - arr[index]) * rat[index]
            benefit = arr[index]
    return bonus_


input_value = input('Please enter the benefit: ')
input_rule = re.compile(r'[0-9]+')
result = input_rule.match(input_value) #this regular expression didn't work yet
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