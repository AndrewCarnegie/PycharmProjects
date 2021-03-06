'''
递归:在调用一个函数的过程中，直接或间接地调用了函数本身这个就叫递归

#直接调用自己：
def func():
    print('from func')
    func()

#间接调用自己
def func1():
    print('from func1')
    func2()

def func2():
    print('from func2')
    func1()

func1()

递归分两部分：回溯与递推

递推：像上边递归实现所拆解，递归每一次都是基于上一次进行下一次的执行，这叫递推
回溯：则是在遇到终止条件，则从最后往回返一级一级的把值返回来，这叫回溯


递归和循环的比较：

递归可以减少变量定义，但是占用内存空间会相对较多
循环可以减少运行空间的占用，但是增加了很多变量的定义
从性能上来说没有谁有绝对的优势，使用场景需要视情况而定

'''

def age(n):
    if n == 1:
        return 18
    return age(n-1)+2

print(age(5))