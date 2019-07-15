#在Python中，要构造分支结构可以使用if、elif和else关键字。

print("example1:")
"""
分段函数求值

       | 3x - 5  (x > 1)
f(x) = | x + 2   (-1 <= x <= 1)
       | 5x + 3  (x < -1)
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

#在Python中构造循环结构有两种做法，一种是for-in循环，一种是while循环。

#for-in循环
#如果明确的知道循环执行的次数或者要对一个容器进行迭代，那么我们推荐使用for-in循环
"""
range usage
range(101)可以产生一个0到100的整数序列，从0开始。
range(1, 100)可以产生一个1到99的整数序列,左闭右开。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
"""
print("example2:")
#sigma(1->100)
sum = 0
for x in range(101):
    sum += x
print(sum)



"""
while循环
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True循环继续，表达式的值为False循环结束。
"""
print("example3:")
#Guess number
import random
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)

#循环嵌套
#乘法表
print("example4:")
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

"""
构造程序逻辑
分支和循环结构会帮助我们将程序中逻辑建立起来，将来我们的程序无论简单复杂，都是由顺序结构、分支结构、循环结构构成的。对于编程语言的初学者来说，首先要锻炼的是将人类自然语言描述的解决问题的步骤和方法翻译成代码的能力，其次就是熟练的运用之前学过的运算符、表达式以及最近的两个章节讲解的分支结构和循环结构的知识。有了这些基本的能力才能够通过计算机程序去解决各种各样的现实问题。所以，开始做练习吧！
	
"""