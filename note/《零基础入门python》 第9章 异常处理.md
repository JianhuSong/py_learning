@[TOC](文章目录)

---

# 前言

主要是学习异常处理的格式

# 1.为什么要异常处理

程序出现逻辑错误或者用户的输入不合法都会引发异常，一旦发生异常，我们又没有异常处理机制的话，程序就会崩溃死掉。任何情况下的异常，都需要用程序崩溃来引起使用者注意么？显然并不是

python提供了异常处理机制来帮助我们处理那些没必要引起程序崩溃的异常。

# 2.异常的种类

| 异常名称          | 解释                                           |
| ----------------- | ---------------------------------------------- |
| AssertionError    | 当assert这个关键字后面的条件为假时抛出         |
| AttributeError    | 当访问的对象属性不存在的时候抛出               |
| IndexError        | 索引超出序列范围时抛出                         |
| KeyError          | 当试图在字典中查找一个不存在的关键字的时候抛出 |
| NameError         | 当试图访问一个不存在的变量的时候抛出           |
| OSError           | 操作系统产生的异常                             |
| SyntaxError       | 有语法错误时抛出                               |
| TypeError         | 不同类型间的无效操作时抛出                     |
| ZeroDivisionError | 除数为0时抛出                                  |

# 3.异常处理的格式

有两种格式：

try-except和try-finally

## 3.1 try-except

捕获一个异常

try:

​	异常检测范围

except exception[as reason]:

​	出现异常后的处理

捕获多个异常

try:

​	异常检测范围

except exception1[as reason]:

​	出现异常后的处理

except exception2[as reason]:

​	出现异常后的处理

except exception3[as reason]:

​	出现异常后的处理

多个异常合并处理

try:

​	异常检测范围

except (Exception1,Exception2,...):

​	出现异常后的处理

捕获所有异常

try:

​	异常检测范围

except:

​	出现异常后的处理

## 3.2 try-finally

这个也有两种格式

try:

​	异常检测范围

except exceptrion as reason:

​	异常处理

```python
try:
    f = open("这个文件不存在.txt",'rt')
except OSError as reason:
    print(reason)
    
try:
    f = open("这个文件不存在.txt",'rt')
except TypeError as reason:
    print(reason)
except OSError as reason:
    print(reason)
    
try:
    f = open("这个文件不存在.txt",'rt')
except (TypeError, OSError,SyntaxError) as reason:
    print(reason)
    


try:
    f = open("这个文件不存在.txt",'rt')
except OSError as reason:
    print(reason)
finally:
    #这里是没有办法访问try中的f，如果f在外面定义的话可能可以
    #f.close() #NameError: name 'f' is not defined
    print("不管怎样，这个都要执行")
    
#with...[as var]
#并不是所有的对象都支持with语句这一新的特性。只有支持上下文管理协议的对象才能使用with语句。

try:
    with open("这个文件不存在.txt",'rt') as f:
        pass
except OSError as reason:
    print(reason)

#可以主动抛出异常
try:
    x = 2
    y = 3
    if x < y:
        raise OSError("这是主动抛出的")
except OSError as reason:
    print(reason)
    
try:
    pass
finally:
    print("try-finally 是可以省略异常处理过程的")
```

# 4.丰富的else子句

else可以和if搭配形成 if....else

else可以和循环语句搭配

​	else 和while搭配，当循环条件不成立的时候执行else

​	else 和for搭配，当遍历完循环列表中的所有元素后执行

else可以和try搭配

​	当try的检测范围中没有任何异常的时候执行

```python
x = 3
y = 4

if x > y:
    print("x > y")
else:
    print("x <= y, 这个if....else...结构")

for x in range(5):
    my_index = 5
    while x > 3 and my_index > 3:
        print("while 循环条件满足 x = ", x, " ,my_index = ", my_index)
        my_index -= 1
    else:
        print("while 循环的条件不满足 x = ", x, " ,my_index = ", my_index)
else:
    print("for 循环的循环列表遍历完毕，才执行")


for x in range(5):
    if x > 2:
        print("for 循环break以后是不会再执行for搭配的else")
        break
else:
    print("for 循环的循环列表遍历完毕，才执行")

for x in range(4):
    if x < 5:
        continue
else:
    print("for循环continue以后，会遍历完所有元素，所以这个会执行")

try:
    with open("这个文件不存在.txt", 'rb'):
        pass
except OSError as reason:
    print("有异常发生，与try配对的else不会执行了")
else:
    pass

try:
    pass
    pass
except:
    pass
else:
    print("没有异常发生, 与try配对的else执行")
```



​	