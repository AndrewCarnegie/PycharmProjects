'''nested data structure operation'''

'''
it must be careful for using nested data structure
because the result is unpredictable
So the unit test must be done when use its

'''
nested_list =[['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3']]
print([y for x in nested_list for y in x[1:2]])
print([a[1] for a in nested_list])
print([z for z in nested_list[:1]])