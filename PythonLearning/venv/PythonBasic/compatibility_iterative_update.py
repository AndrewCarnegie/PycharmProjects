'''
module/function iterative update for compatible availability

two knowledge point:
    1. how to iterative update the existed module or function to ensure the compatibility
    2. how to declare the argument to be optional parameter

'''



'''
when you finish a module or function and find it very useful for world,
what we need to do is make a distribution of this module or function

for instance：
'''

def print_lol(the_list):
    # this is the first version, print metadata in the_list by recursion
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

'''

after the draft version/first version, we want to enhance this function or module

requirement: improve the function print_lol so that the nested list 
can be indented with specified number tab

improvement way: add new argument named indent_level:

indent_level <= 0 : no indentation
indent_level = 1 : there is indentation with one tab
indent_level = 2 : there is indentation with two tab

'''
def print_lol(the_list, indent_level):
    # this is the second version, print metadata in the_list by recursion with indentation
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item, indent_level + 1)
        else:
            for tap_stop in range(indent_level):
                print('/t', end='')
            print(each_item)


'''
After we complete the second version , another problem appears: the second version 
can't be compatible with the first version
especially when users already use the first version in their program. 
So we have to solve this compatibility problem

improvement way: change the newly added argument as optional parameter
How to: setting a default value for the argument in the argument list will 
make the argument to be optional argument

in this case, first version has no indentation, so the default value 
for indent_level should be zero
'''

def print_lol(the_list, indent_level = 0):
    # this is the third version, print metadata in the_list by recursion with indentation
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item, indent_level + 1)
        else:
            for tap_stop in range(indent_level):
                print('/t', end='')
            print(each_item)


'''
Although we use default value to avoid the indentation, the recursion print has been open

why we don't add a new optional argument to control whether opening the recursion print or not

improvement way: add new optional argument named is_indent

is_indent = True  : open the indentation feature
is_indent = False : close the indentation feature

'''


def print_lol(the_list, is_indent = False, indent_level = 0):
    # this is the fourth version, print metadata in the_list by recursion with indentation
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item, is_indent, indent_level + 1)
        else:
            if is_indent:
                for tap_stop in range(indent_level):
                    print('/t', end='')
            print(each_item)