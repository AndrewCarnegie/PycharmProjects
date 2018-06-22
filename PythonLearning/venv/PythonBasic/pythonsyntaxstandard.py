'''Best practice for naming in Python'''

#Pylint is a very flexible source code analyzer


"""
#constant   uppercase with underscores

1. all constants in same module should be list at the top of the module; 
2. if necessary they should be combined into new variables for operation
3. gather all constants in a single file in the package, such as settings.py; or use a configuration file can be parsered by ConfigParser...

"""



"""
#variables   lowercase with underscores

1. private variables, perfix should be an underscore; for instance, _private_variable
2. private variable in module/class/functions/method should be accessed by getters and setters
3. double underscores as prefix is used for special methods, such as operator overloading/container definitions; these special mehtod should be
   gathered at the beginning of the class definitions. normal methods should never user double underscores as prefix
4. pubulic variables should be named by lowercase with underscores, for example, public_variable
5. variables represent collections should use plurals, for instance, users = ['Andy']
6. variables represent dictionaries should have explicit names, for instance, 
   persons_addresses = {'Bill': '6565 Monty Road','Pamela': '45 Python street'}
7. variables' name should avoid retained name by system or existing name defined by user

"""


"""
#arguments   lowercase with underscores

1. follow the same rule as variables
2. arguments should be used carefully through below rules:
    a. Build arguments by iterative design; 
        a1. arguments should have default values as much as possible to aviod regression
        a2. When the argument of a public element has to be changed, a deprecation process is to be used
    b. Trust the arguments and your tests
        b1. assertion should be used carefully since it will be made on each call
        b2. assertion can be removed with the "-O" option of interpreter
        b3. obey test-driven development style to avoid the usage of assertion
        b4. assertion should be used when code in library is used by external elements because incoming data may break things up
    c. Use *args and **kwargs magic arguments carefully
        c1. Using *args and **kwargs can break the robustness of function or method
        c2. Since argument list gets long and complex, function or method will become week, it's better to break it into pieces or refactored
        c3. Once *args/**kwargs deal with a sequence of elements that are treated the same way in the function, 
            container argument should be used such as iterator

"""



"""
#properties   lowercase with underscores

follow the same rule as variables
"""



"""
#class   CamelCase/mixedCase

1. class in module should be named in camel case, for instance, MyClass
2. private class in module should be named with leading underscore, for instance, _MyClass
3. since class name should be concise,presice, suffix should be used to inform about its type and nature for best practice
4. a Base or Abstract prefix can be used for base class and abstract class
"""



"""
# Modules and packages     lowercase

1. module should always use lowercase without underscore.
2. private module in package should be named with leading undrescore, ofr instance, _module
3. package has the same rule
4. module name are often suffixed with lib while it implements a protocol such as smtplib/urllib/telnetlit
5. 
"""



"""
# Boolean elements     lowercase with underscores and prefix is or has

1. boolean variables should be named with prefix is or has, for instance, is_boolean or has_boolean
"""
