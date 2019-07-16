## OOP in python
### 基础
"""
把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。

类是对象的蓝图和模板，而对象是类的实例。这个解释虽然有点像用概念在解释概念，但是从这句话我们至少可以看出，类是抽象的概念，而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。

"""

#### class关键字定义类
```python
class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))
    
    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def checkage(self):
    	if self.age < 18:
            print('%s<18' % self.name)
        else:
            print('%s18+.' % self.name)


#创建和使用对象
def test():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    
	# 给对象发study消息
	stu1.study('Python程序设计')
	
	stu1.checkage()
	stu2 = Student('王大锤', 15)
	stu2.study('思想品德')
	stu2.checkage()
```


#### 访问可见性问题

在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。

~~~python
class Test:
    def __init__(self, foo):
        self.__foo = foo

```
def __bar(self):
    print(self.__foo)
    print('__bar')
```

#测试私有类型
def test1():
	test = Test('hello')
    #test.__bar()  #AttributeError: 'Test' object has no attribute '__bar'
    test._Test__bar()  #Python并没有从语法上严格保证私有属性或方法的私密性
~~~


### 进阶

#### @property装饰器
之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，代码如下所示。

~~~python
class Person(object):

```
def __init__(self, name, age):
    self._name = name
    self._age = age

# 访问器 - getter方法
@property
def name(self):
    return self._name

# 访问器 - getter方法
@property
def age(self):
    return self._age

# 修改器 - setter方法
@age.setter
def age(self, age):
    self._age = age

def play(self):
    if self._age <= 16:
        print('%s正在玩飞行棋.' % self._name)
    else:
        print('%s正在玩斗地主.' % self._name)
```

def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute

if __name__ == '__main__':
    main()
	
~~~

#### \__slots__
"""
我们讲到这里，不知道大家是否已经意识到，Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义\__slots\__变量来进行限定。需要注意的是\__slots\__的限定只对当前类的对象生效，对子类并不起任何作用。
"""

~~~python
class Person(object):

```
# 限定Person对象只能绑定_name, _age和_gender属性
__slots__ = ('_name', '_age', '_gender')

def __init__(self, name, age):
    self._name = name
    self._age = age

@property
def name(self):
    return self._name

@property
def age(self):
    return self._age

@age.setter
def age(self, age):
    self._age = age

def play(self):
    if self._age <= 16:
        print('%s正在玩飞行棋.' % self._name)
    else:
        print('%s正在玩斗地主.' % self._name)
```

def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
~~~



    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True

"""
静态方法和类方法
之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题，代码如下所示。
"""

~~~python
from math import sqrt

class Triangle(object):

```
def __init__(self, a, b, c):
    self._a = a
    self._b = b
    self._c = c

@staticmethod
def is_valid(a, b, c):
    return a + b > c and b + c > a and a + c > b

def perimeter(self):
    return self._a + self._b + self._c

def area(self):
    half = self.perimeter() / 2
    return sqrt(half * (half - self._a) *
                (half - self._b) * (half - self._c))
```

def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')

if __name__ == '__main__':
    main()
~~~

和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。

和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。

~~~python
from time import time, localtime, sleep

class Clock(object):
    """数字时钟"""

```
def __init__(self, hour=0, minute=0, second=0):
    self._hour = hour
    self._minute = minute
    self._second = second

@classmethod
def now(cls):
    ctime = localtime(time())
    return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

def run(self):
    """走字"""
    self._second += 1
    if self._second == 60:
        self._second = 0
        self._minute += 1
        if self._minute == 60:
            self._minute = 0
            self._hour += 1
            if self._hour == 24:
                self._hour = 0

def show(self):
    """显示时间"""
    return '%02d:%02d:%02d' % \
           (self._hour, self._minute, self._second)
```

def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()
~~~

