

print('Comprehension template:\n')

#--list comprehension
'''general list comprehension'''
list_ = [i*2 for i in range(10) if i % 2 == 0]
print(list_)
print(type(list_))


# The difference between list comprehension and generator expression is only the
# parenthesis and the brackets

'''generator expression'''
generator_ = (i*2 for i in range(10) if i % 2 == 0)
print([i for i in generator_])
print(type(generator_))

'''enumerate'''
for i, element in enumerate(['one', 'two', 'three']):
    print(i,element)

'''zip'''
for item in zip([1, 2, 3], [4, 5, 6]):
    print(item)

'''zip() for reverse'''
for item in zip(*zip([1, 2, 3], [4, 5, 6])):
    print(item)

'''dictionary comprehension'''
dict_={"a":1, "b":2, "c":3, "d":4}
dicts={v:k for k,v in dict_.items()}


dict_.update({k:v for k,v in {"e":1, "f":2, "g":3, "h":4}.items()})
print(dict_)


mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    if k.lower() in ['a','b']
}


#sets comprehension

