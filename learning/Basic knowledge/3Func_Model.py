"""
定义函数
在Python中可以使用def关键字来定义函数，和变量一样每个函数也有一个响亮的名字，而且命名规则跟变量的命名规则是一致的。在函数名后面的圆括号中可以放置传递给函数的参数，这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数的自变量，而函数执行完成后我们可以通过return关键字来返回一个值，这相当于数学上说的函数的因变量。
"""

from random import randint

def roll_dice(n=2):
    """
    摇色子
    
    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a=0, b=0, c=0):
    return a + b + c
	
# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))

"""
---------------------
"""

"""
#module1.py
def foo():
    print('hello, world!')

#module2.py
def foo():
    print('goodbye, world!')


#test.py
from module1 import foo
# 输出hello, world!
foo()

from module2 import foo
# 输出goodbye, world!
foo()
也可以按照如下所示的方式来区分到底要使用哪一个foo函数。

test.py
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()


但是如果将代码写成了下面的样子，那么程序中调用的是最后导入的那个foo，因为后导入的foo覆盖了之前导入的foo。
test.py
from module1 import foo
from module2 import foo
# 输出goodbye, world!
foo()

test.py
from module2 import foo
from module1 import foo
# 输出hello, world!
foo()

需要说明的是，如果我们导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“__main__”。

module3.py
def foo():
    pass

def bar():
    pass
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
	
test.py
import module3
# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
