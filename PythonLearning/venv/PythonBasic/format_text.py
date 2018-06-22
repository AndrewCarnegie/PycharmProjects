"""

How to escape character

"""


# use ESC

print('%s is a good student' %('Andy'))


# use format {0} method
print('Both {0} and {1} are good students\n'.format('Andy', 'Grace'))


'''
 use format {0:30s} method
 
 {0:30s} has two parts: 
 before the colon, the 0 represent positional placeholder for variables;
 After the colon, the 30s represent 30 strings placeholder(blank space) between variables
 
'''
builtin = dir(__builtins__)

for i in range(len(builtin)):
    print('{0:30s}'.format(builtin[i]), end='')
    if i%5 ==0:
        print('\n')