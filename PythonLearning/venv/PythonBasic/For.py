# !/usr/bin/env python3

import sys

template = ['ham','spam','eggs','nuts','noodle','rice','apple']

for food in template:
	if food == 'spam':
		print('no more spam')
		continue
	print('The %s is very delicious'%(food))


# for i in range(len(template)):
# 	print(template[i])

it = iter(template)
while True:
	try:
		print(next(it), end = ' ')
	except StopIteration as e:
		print ('\niteration has been done')
		break

print('r\n')
it = iter(template)
for food in it:
	print(food, end = ' ')

print('r\n')

for food in template:
	print(food, end = ' ')
print('r\n')

def yield_test(test):
	while True:
		if n < len(test):
			yield test
			n= n + 1
yield_test(template)
print('r\n')


test = [8, 6, 1, 3, 5, 10]

def insert_sort(list):
    length=len(list)
    for i in range(1,length):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
test1 = insert_sort(test)

for x in test1:
	print(x, end = ' ')


# advance loop

a = [x for x in range(10)]

print('\n')
# 在迭代过程中修改迭代序列不安全，如果你想修改迭代序列，那么最好是迭代它的副本，使用切割标记可以做到迭代副本

for w in template[:]: # Loop over a slice copy of the entire list.
	if len(w) > 5:
		template.insert(0,w)

print(template)
