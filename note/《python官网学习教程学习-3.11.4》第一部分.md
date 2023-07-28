@[TOC](文章目录)

---

前言

如果英语水平允许的话，建议看英文版。我英语水平有限，看得是简体中文版的教程

引用官网上对教程的描述和后续的学习内容建议

“*本教程对每一个功能的介绍并不完整，甚至没有涉及全部常用功能，只是介绍了 Python 中最值得学习的功能，旨在让读者快速感受一下 Python 的特色。学完本教程的读者可以阅读和编写 Python 模块和程序，也可以继续学习 Python 标准库。*”

# 1.源文件的特殊开头

## 1.1指定解释器

​	#！这个官方的叫法叫shebang,后面可以有一个或数个空格

如果脚本中没有这一行，那么执行时会选用默认的解释器

如果#!之后指定的解释程序没有可执行权限，会报错。

如果#!之后指定的解释程序不是一个可执行文件，那么就忽略

如果#!之后指定的解释程序不存在，会报错。

小事情：

​	在练习的时候，习惯使用 python test.py 这样的操作会直接忽略第一行。

   用法1：#! /usr/bin/env 解释器名称

```python
#! /usr/bin/env python
```

​	用法2：#! 解释器的绝对路径

```python
#! /usr/bin/python
```

两种用法有什么不同？

​	用法1：不会随着python的安装路径的不同而出现问题。一般情况下，env都在/usr/bin目录下。这样写比较通用一些，在不同的机器上不用特意修改

​	用法2：随着机器的不同，解释器的绝对路径可能不同。用在不同的机器上可能需要修改。

关于#!的介绍就到这里，感兴趣可自行搜索。

## 1.2 指定文件编码

python3默认的编码格式是UTF-8

指定文件编码方式

在源文件中配置, 放在文件的第一行或者第二行（若指定了解释器，那就放第二行）。

```
# -*- coding: UTF-8 -*-
```

# 2.流程控制工具

### 2.1 if

if语句包含零个或多个elif子句和可选的else子句

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = int(input("Please enter an integet: "))
if x < 0:
    x = 0
    print('Nagetive changed to zero.')
elif x == 0:
    print("Zero")
elif x == 1:
    print('Single')
else:
    print('More')
```

### 2.2 循环（while/for）

python的for语句不迭代算术递增数值，或是给予用户定义迭代步骤或暂停条件的能力。而是迭代列表或字符串等任意序列，元素的迭代顺序于在序列中的顺序一致。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

while 2 < 10:
    for i in range(10):
        x = int(input("Please enter an integet: "))
        if x < 0:
            x = 0
            print('Nagetive changed to zero.')
        elif x == 0:
            print("Zero")
        elif x == 1:
            print('Single')
        else:
            print('More')
    break
```

### 2.3 range()

常用于遍历数字序列，该函数可以生成算术级数。

生成的是一个序列，生成的序列中的元素不包含结束位置的数

其有三个参数range(start, stop[, step])

只赋值一个参数的时候，作为该序列的中止位置

赋值两个参数的时候，第一个参数作为生成序列的起始位置，第二个参数作为生成序列的结束位置(不包含)

赋值三个参数的时候,相当于指定了生成序列的起始位置，结束位置，元素间的步进。

特别说明：step可以为负数。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,2)))

#step可以看作是从start怎么样到stop位置
print(list(range(10,1,-1)))
print(list(range(-10,-70,-20)))
```

### 2.4 循环中的break,continue以及else子句

break语句：用于跳出最近的for或者while循环。（循环结束了）

continue语句：跳出本次（轮）循环，直接执行下一次循环。

else子句：

​	1.与if搭配，表示不满足if/elif条件时执行

​	2.与while搭配，不满足while条件时执行

​	3.与for搭配，当for的循环列表中的元素遍历完后执行。（break退出循环不算）

​	4.与try搭配，没有触发异常时执行。

2.5 pass语句

​	pass语句不执行任何操作，当语法上需要，但实际无操作时使用。

2.6 match语句

match功能很多，感觉有点复杂。目前是这样理解的，也不知道对不对：

match 从哪里以什么方式捕获值

match 如何匹配捕获的值

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# match中的case只会执行一句。只要匹配上一句，后面的就不再执行了
a = ["red", "blue", "green", "yellow", 1,2,3,4,55.001]
for element in a:
    print("current is ", element)
    match element:
        case 'red':
            print("got the red color.")
        case 'blue':
            print("got the blue color.")
        #匹配多个值中的任意一个（）
        case "green" | "yellow":
            print("red or blue")
        # 可以将得到的值赋值给一个变量，然后还可以操作
        case x if x > 2 and x < 6:
            print("It is a integer:", x)
        # _是通配符，匹配任意内容
        case _:
            print("xxxxxxx")
points = [(0,0),(0,1),(1,0),(1,1),(1,2)]
for x,y in points:
    print("current point({0},{1})".format(x, y))
    match (x,y):
        #x y 的值都匹配都必须是0
        case (0,0):
            print("is origin")
        #只匹配X的值，y任意
        case (0, y):
            print(f"on x point({x},{y})")
        #甚至可以不关心x,y具体是多少，只要满足条件就行，if x==y 称为守护项的if子句
        case (x,y) if x == y:
            print(f"x == y  point({x},{y})")
        #可以使用通配符，表示至少
        case (x,*_):
            print("匹配任意一个点")
        
points = [(0,0,1),(0,1,1),(1,0,2),(1,1,'test'),(1,2,5.44)] 
for point in points:
    match point:
        case (x,0,z):
            print("xxxxx")  
        case (0,1,z):
            print("zzzzzz", z)
        case (x,y,z) if x > 0 and y > 0:
            print(f"{x},{y},{z}")
```



# 3.函数

格式： def 函数名([形参列表])  

解释：[形参列表]  表示形参列表是可选的

函数内的第一条语句是字符串时，该字符串就是文档字符串

函数在执行时使用局部符号表，所有函数变量赋值都存在于局部符号表中。引用变量时，首先在局部符号变量表中查找，然后是外层函数局部符号表，再是全局符号表，最后是内置名称符号表。

尽管可以引用全局变量和外层函数的变量，但最好不要直接赋值（除非是global或是nonglobal）

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
global_name = "global"
def myFunction(arg):
    out_func_arg = "out"
    out_arg = 0
    global global_name 
    global_name = "global + myFunction"
    def func(arga):
        nonlocal out_func_arg
        out_func_arg = "out + in"
        arga = "test"
    print("before out_func_arg = ", out_func_arg)
    func(out_arg)
    print("after out_func_arg = ", out_func_arg)

print("before global_name = ", global_name)
myFunction("testsaetasste")
print("after global_name = ", global_name)
```

### 3.1 位置或关键字参数

函数定义中未使用/和*时候，参数可以按位置或关键字传递给函数

函数定义中若使用了/表示该位置前仅限位置形参

函数定义中若使用了*表示该位置后仅限关键字形式传递该形参

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#位置参数:
#在调用的时候实参的数量和位置必须和形参的数量和位置一致。
#数量一致好理解，那么位置一致可以理解为，在调用过程中与形参处于同样位置的实参总是于对应位置的形参绑定

#普通的定义
def func(x,y,z):
    print(f"x = {x}, y = {y}, z = {z}")

#仅限位置参数
def func1(x,y,z,/):
    print(f"x = {x}, y = {y}, z = {z}")

#仅限关键字参数
def func2(*,x,y,z):
    print(f"x = {x}, y = {y}, z = {z}")
    
#没有加限制的函数，在调用时
func(1,2,3)
func(x = 1, z = 2,y = 3)

#仅限位置参数的函数在调用时
func1(1,2,3)
#下面这样调用会报错：func1() got some positional-only arguments passed as keyword arguments: 'x, y, z'
#func1(x = 2, y = 3, z = 4)

#仅限关键字参数的函数在调用时
func2(y = 1, x = 2, z=4)
# 下面这样调用会报错：func2() takes 0 positional arguments but 3 were given
# func2(5,6,7)

#可以混用
#这样中不行，它们两个的生效区间不能完全一样
# def func3(*,x,y,z,/):
#     print(f"x = {x}, y = {y}, z = {z}")

def func4(x,y,/,z,*,f,g):
     print(f"x = {x}, y = {y}, z = {z},f = {f}, g = {g}")
     
func4(111,222,333,g = 444,f = "zzzz")
func4(666,6666,z = 666666, f = 666666, g = 6666666)
```

### 3.2  任意实参列表

调用函数时，使用任意数量的实参时最少见的选项。这些实参包含在元组中。在可变数量的实参前，可能有若干个普通的参数。

*arg形参后的任何形式参数只能时仅限关键字参数。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def funcArgs(one, two, *args, three):
    print(f"{one}-{two}-{three} args length:", len(args))
    
funcArgs(1,2,3,4,5,6,three= 3333)
```

### 3.3 解包实参列表

用*把实参从列表或元组解包出来

字典可以用**操作符传递关键字参数

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def myFunc(one, two, three):
    print(f"one = {one}, two = {two}, three = {three}")
    
aaa = [1,2,3]
bbb = ("one", "two", "three")
ccc = {'one': "Hello", 'two':'world', 'three':'!!!!'}

myFunc(*aaa)
myFunc(*bbb)
myFunc(**ccc)
```

### 3.4 Lambda表达式

lambda关键字用于创建小巧的匿名函数。

格式： lambda 参数列表:返回值

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = lambda a,b,c:a+a + b *c
print(f(1,2,3))
```

### 3.5 文档字符串

第一行应为对象用途的间段摘要。大写字母开头，以句点结尾。

第二行为空白行

第一行之后的第一个非空行决定了文档的字符串的缩进量

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def my_function():
    """Do nothing, but ducment it.
    No, really, it doesn't to anything.
    """
    pass

print(my_function.__doc__)
```
