"""
Python的优点很多，简单的可以总结为以下几点。

1.简单和明确，做一件事只有一种方法。
2.学习曲线低，跟其他很多语言相比，Python更容易上手。
3.开放源代码，拥有强大的社区和生态圈。
4.解释型语言，天生具有平台可移植性。
5.支持两种主流的编程范式（面向对象编程和函数式编程）都提供了支持。
6.可扩展性和可嵌入性，可以调用C/C++代码，也可以在C/C++中调用Python。
7.代码规范程度高，可读性强，适合有代码洁癖和强迫症的人群。

Python的缺点主要集中在以下几点。

1.执行效率稍低，因此计算密集型任务可以由C/C++编写。
2.代码无法加密，但是现在很多公司都不销售卖软件而是销售服务，这个问题会被淡化。
3.在开发时可以选择的框架太多（如Web框架就有100多个），有选择的地方就有错误。

Python的应用领域
目前Python在Web应用开发、云基础设施、DevOps、网络爬虫开发、数据分析挖掘、机器学习等领域都有着广泛的应用，因此也产生了Web后端开发、数据接口开发、自动化运维、自动化测试、科学计算和可视化、数据分析、量化交易、机器人开发、图像识别和处理等一系列的职位。
"""

### 确认Python的版本

```python
import sys
print(sys.version_info)
print(sys.version)

#print
print("hello world")
print('hello', 'world', sep=', ', end='!')
print('good, world', end='!\n')
```

### python之禅

```python
import this
```

"""
Beautiful is better than ugly. （优美比丑陋好） Explicit is better than implicit.（清晰比晦涩好） Simple is better than complex.（简单比复杂好） Complex is better than complicated.（复杂比错综复杂好） Flat is better than nested.（扁平比嵌套好） Sparse is better than dense.（稀疏比密集好） Readability counts.（可读性很重要） Special cases aren't special enough to break the rules.（特殊情况也不应该违反这些规则） Although practicality beats purity.（但现实往往并不那么完美） Errors should never pass silently.（异常不应该被静默处理） Unless explicitly silenced.（除非你希望如此） In the face of ambiguity, refuse the temptation to guess.（遇到模棱两可的地方，不要胡乱猜测） There should be one-- and preferably only one --obvious way to do it.（肯定有一种通常也是唯一一种最佳的解决方案） Although that way may not be obvious at first unless you're Dutch.（虽然这种方案并不是显而易见的，因为你不是那个荷兰人^这里指的是Python之父Guido^） Now is better than never.（现在开始做比不做好） Although never is often better than *right* now.（不做比盲目去做好^极限编程中的YAGNI原则^） If the implementation is hard to explain, it's a bad idea.（如果一个实现方案难于理解，它就不是一个好的方案） If the implementation is easy to explain, it may be a good idea.（如果一个实现方案易于理解，它很有可能是一个好的方案） Namespaces are one honking great idea -- let's do more of those!（命名空间非常有用，我们应当多加利用）
"""

#### turtle 绘制图像
```python
import turtle

turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
```


### 变量命名
​    对于每个变量我们需要给它取一个名字，就如同我们每个人都有属于自己的响亮的名字一样。在Python中，变量命名需要遵循以下这些必须遵守硬性规则和强烈建议遵守的非硬性规则。

硬性规则：
	变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
	大小写敏感（大写的a和小写的A是两个不同的变量）。
	不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
PEP 8要求：
	用小写字母拼写，多个单词用下划线连接。
	受保护的实例属性用单个下划线开头（后面会讲到）。
	私有的实例属性用两个下划线开头（后面会讲到）。



### 运算符表格

| py运算符 | 描述 |
| -------- | ---- |
|[] [:]		| 下标，切片|
|**		|			指数|
|~ + -		|		按位取反, 正负号|
|*  /  %  //	      |		乘，除，模，整除|
|+ -				|	加，减   |
|>>  <<	 |			右移，左移|
|&			|		按位与|
|^ |			|
|<=  <  >   >=			|小于等于，小于，大于，大于等于|
|== !=			|	等于，不等于|
|is is not		|	身份运算符|
|in not in			|成员运算符|
|not or and		|	逻辑运算符|


```python
#从键盘读入并输出计算结果
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)

#type() 
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
```


#### type transform
​	int()：将一个数值或字符串转换成整数，可以指定进制。
​	float()：将一个字符串转换成浮点数。
​	str()：将指定的对象转换成字符串形式，可以指定编码。
​	chr()：将整数转换成该编码对应的字符串（一个字符）。
​	ord()：将字符串（一个字符）转换成对应的编码（整数）。

