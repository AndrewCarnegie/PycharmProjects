test_list = []
flag = True

for i in range(101,201):
    for j in range(2,i):
        if i%j != 0:
            flag =True
        else:
            flag =False
            break
    if flag == True:
        test_list.append(i)
print('The prime numbers between 101 and 200 are: \n' + str(test_list))
print('\nThe total number of these prime numbers is: \n' + str(len(test_list)))