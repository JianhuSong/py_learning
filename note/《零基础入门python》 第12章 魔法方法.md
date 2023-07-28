@[TOC](文章目录)

---

# 前言

这章内容有点多

# 1. 魔法方法

​	什么是魔法方法：

​		魔法方法总是被双下划线包围

​		魔法方法是面向对象的python的一切

​		魔法方法总能在适当的时候被调用

# 2. 构造和析构

| 函数                    | 解释                                                         |
| ----------------------- | ------------------------------------------------------------ |
| \__init__(self[, ...])\ | 1.不是必须要有，根据需求来.2.实例化对象的时候自动调用。3.重写的话注意返回值必须是None |
| \__new__(cls[,...])     | 1.一般不重写。 2.当继承一个不可变的类型的时候，需要重写      |
| \__del__(self)          | 1.当垃圾回收机制回收这个对象的时候调用。                     |

# 3. 算术运算

| 魔法方法                       | 含义                                |
| ------------------------------ | ----------------------------------- |
| \__add__(self, other)          | 定义加法的含义：+                   |
| \__sub__(self, other)          | 定义减法的行为:+                    |
| \__mul__(self, other)          | 定义乘法的行为：*                   |
| \__truediv__(self, other)      | 定义真除法的行为：/                 |
| \__floordiv__(self, other)     | 定义整数除法的行为：//              |
| \__mod__(self, other)          | 定义取模运算的行为：%               |
| \__divmod__(self, other)       | 定义当被divemod()调用时的行为       |
| \__pow__(self, other[,modulo]) | 定义当被power()调用或**运算时的行为 |
| \__lshift__(self, other)       | 定义按位左移的行为：<<              |
| \__rshift__(self, other)       | 定义按位右移的行为：>>              |
| \__and__(self, other)          | 定义按位操作的行为: &               |
| \__xor__(self, other)          | 定义按位异或操作的行为：^           |
| \__or__(self, other)           | 定义按位或操作的行为：\|            |

```python
# 调用int的魔法方法实现自己的魔法方法
class MyInt(int):
    def __add__(self, other):
        return int.__add__(self, other)

#不调用int的魔法方法实现自己的魔法方法 
class MyInt1(int):
    def __add__(self, other):
        return int(self) + int(other)
    
a = MyInt(2)
b = MyInt(2)

print(a + b)
print(MyInt1(5) + MyInt1(6))
```

# 4. 一元操作符

一元操作符就是只有一个操作符的意思

| 操作符        | 说明                                |
| ------------- | ----------------------------------- |
| \__neg__()    | 表示正号行为                        |
| \__pos__()    | 负号行为                            |
| \__abs__()    | 当被abs()调用的时就是取绝对值的意思 |
| \__invert__() | 按位取反                            |

```python
#写出自己的
import time
class MyTimer:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.total = 0
    def _calc(self):
        if not self.begin > 0:
            print("计时器并未开始")
            return None
        if not self.end > 0:
            print("计时器并未停止")
            return None
        seconds = self.end - self.begin
        if seconds:
            print("总耗时: {0:.2f}s.".format(seconds))
            self.total = seconds
        else:
            print("计时出错了")
        self.begin = self.end = 0

    def start(self):
        self.begin = time.time()
        print(time.strftime("开始计时时间:%Y-%m-%d %H:%M:%S", time.localtime(self.begin)))
        
    def stop(self):
        if not self.begin:
            print("未开始计时")
            return None
        self.end = time.time()
        print(time.strftime("开始计时时间:%Y-%m-%d %H:%M:%S", time.localtime(self.end)))
        self._calc();
        
    def __add__(self, other):
        print("add: {0:.2f}s.".format(self.total + other.total))
    def __str__(self):
        return ("__str__: {0:.2f}s.".format(self.total))
    def __repr__(self):
        return ("__repr__: {0:.2f}s.".format(self.total))
        
t1 = MyTimer()
t2 = MyTimer()
def runTimer(t1):
    while True:
        t1.start()
        a = 100
        for i in range(100*1000):
            a += 1000
            a *= 100
            a -= 2000
        t1.stop()
        break
    
runTimer(t1)
runTimer(t2)
print(t1)
print(t2)
t1 + t2
#还有需要完善的地方
```

# 5. 属性访问

| 魔法方法                      | 含义                                       |
| ----------------------------- | ------------------------------------------ |
| \__getattr__(self, name)      | 定义当用户试图获取一个不存在的属性时的行为 |
| \__getattribute__(self, name) | 定义当该类的属性被访问时的行为             |
| \__setattr__(self, name)      | 定义当一个属性被设置时的行为               |
| \__delattr__(self, name)      | 定义当一个属性被删除时的行为               |

python中的所有类都有一个默认的基类object

类的属性都存在于\__dict__中(键值对的形式，字典)

上述魔法方法在使用的时候容易死循环

```python
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        print("__init__")
    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
            print("__setattr__ if")
        else:
            self.name = value
            print("__setattr__ else")
    def getArea(self):
        return self.width * self.height
    
r1 = Rectangle(4,5)
#__setattr__(self, name, value)
#其中的name是实例属性名。
#错误信息
# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\test.py", line 1280, in <module>
#     r1 = Rectangle(4,5)
#   File "D:\coding\py_learning\code\test.py", line 1266, in __init__
#     self.width = width
#   File "D:\coding\py_learning\code\test.py", line 1275, in __setattr__
#     self.name = value
#   File "D:\coding\py_learning\code\test.py", line 1275, in __setattr__
#     self.name = value
#   File "D:\coding\py_learning\code\test.py", line 1275, in __setattr__
#     self.name = value
#   [Previous line repeated 993 more times]
#   File "D:\coding\py_learning\code\test.py", line 1270, in __setattr__
#     if name == 'square':
# RecursionError: maximum recursion depth exceeded in comparison
```

原因：

  在定义的方法中只要有 sefl.属性 = value，这种样式的语句，就会触发\__setattr__, 

在例子中在__init__阶段给width赋值时触发，然后在\__setattr__中再次触发。 从而导致死循环。

解决方法：

1.通过supper调用基类的\__settattr__

```python
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        print("__init__")
    def __setattr__(self, name, value):
        if name == 'square':
            super().__setattr__('width', value)
            super().__setattr__('height', value)
            print("__setattr__ if")
        else:
            super().__setattr__(name, value)
            print("__setattr__  var = ", name, ", value = ", value)
    def getArea(self):
        return self.width * self.height
    
r1 = Rectangle(4,5)
```

2.通过\__dict__给属性赋值

```python
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        print("__init__")
    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__["width"] = value
            self.__dict__["height"] = value
            print("__setattr__ if")
        else:
            self.__dict__[name] = value
            print("__setattr__  var = ", name, ", value = ", value)
    def getArea(self):
        return self.width * self.height
    
r1 = Rectangle(4,5)
```

property的原理

property本质上是一个描述符类，描述符就将某种特殊类型的类的实列指派给另一个属性的类。

特殊性：

​	在该类中至少要定义下表中的一个。

| 魔法方法                        | 含义                                     |
| ------------------------------- | ---------------------------------------- |
| \__get__(self, instance, owner) | 用于访问属性， 它返回属性的值            |
| \__set__(self, instance, value) | 将在属性分配操作中的调用，不返回任何内容 |
| \__delete__(self, instance)     | 控制删除操作，不做任何操作               |

```python
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x
    x = MyProperty(getX, setX, delX)

c = C()
c.x = 'X-man'
print(c.x)
print(c._x)
del c.x
print(c._x)

```

# 6. 定制序列

定制序列的以下协议：

```
如果说你希望定制的容器不可变的话，你只需要定义__len__()和__getitem__()方法
​如果希望定制的容器是可变的话，除了定义__len__()和__getitem__()以外，还需要定义__setitem__()和__delitem()__两个方法
```

定制容器的魔法方法

| 魔法方法                       | 含义                                                    |
| ------------------------------ | ------------------------------------------------------- |
| \__len__(self)                 | 定义当被len()函数调用时候的行为（返回容器中元素的个数） |
| \__getitem__(self, key)        | 定义获容器中指定元素的行为，相当于self[key]             |
| \__setitem__(self, key, value) | 定义设置容器中元素的行为，相当于self[key] = value       |
| \__delitem__(self, key)        | 定义删除容器中指定元素的行为，相当于del self[key]       |
| \__iter__(self)                | 定义当迭代容器中的元素的行为                            |
| \__reversed__(self)            | 定义当被reversed()函数调用时候的行为                    |
| \__contains__(self, item)      | 定义当是哟个成员测算函数(in 或 not in)时的行为          |

```python
#不可变的
class MyConstList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]
    def __str__(self):
        return str(self.values)
    
c1 = MyConstList(1,3,5,7,9)
c2 = MyConstList(2,4,6,8,10)

#模仿列表的行为，打印列表名字，就是打印整个列表
print(c1)
print(c2)

print(c1[1])
print(c2[1])
print(c1.count)
print(c2.count)  

#这一句会报错 TypeError: 'MyConstList' object does not support item assignment
#c1[1] = 22
```

```python
class MyConstList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

    def __str__(self):
        return str(self.values)

    def __setitem__(self, key, value):
        self.values[key] = value

    # 定义删除行为的时候这个有点异常,删除异常后，但是记录没有删除。
    # 两个思路：1.用新的self.values生成一个新的访问记录字典，然后把旧字典改成新的
    # 2.根据删除的key找到字典中比key大的，然后值都往前挪动，把最后一个键值对删除就行
    # def __delitem__(self, key):
    #     del self.values[key]
    #     del self.count[key]
    #     tmp = {}
    #     time = 0
    #     for x, y in self.count.items():
    #         tmp[time] = y
    #         time +=1
    #     self.count = tmp

    # 方案2
    def __delitem__(self, key):
        old_values_size = len(self.values)
        for i in range(key, old_values_size):
            if key == old_values_size - 1:
                break
            else:
                self.count[key] = self.count.get(key + 1)

        self.count.popitem()
        self.values.pop(key)

c1 = MyConstList(1, 3, 5, 7, 9)

# 模仿列表的行为，打印列表名字，就是打印整个列表
print(c1)

print(c1[1])

print(c1.count)

c1[1] = 22
print(c1)
del c1[1]
# //c1[100] = 23
print(c1)

# 不能直接用c1会报错，不能直接用c1.values这样c1.count里面无计数
for each in range(len(c1.values)):
    print(c1[each])
print(c1.count)
```

迭代器

```
关于迭代器的两个关键魔法
	__iter()__
		这个返回迭代器本身
	__next()__
		这个决定了迭代的规则
```

```python
class IterTest:
    def __init__(self, n = 20):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a >  self.n:
            raise StopIteration
        return self.a


test = IterTest()
for each in test:
    print(each)
```

生成器	

​	生成器是迭代器的一种实现

​	生成器可以暂时挂起函数，并保留函数的局部变量等数据

```python
def myGen():
    print("生成器被执行")
    yield 1
    yield 2
    yield 3
    
for each in myGen():
    print(each)
```

推导式：

```python
#列表推导式
a = [i for i in  range(100) if not (i % 2) and i % 3]
print(a)

#字典推导式
b = {i:i%2 == 0 for i in range(10)}
print(b)

#用普通小括号括起来的就是生成器推导器
e = (i for i in range(20))
for each in  e:
    print(each)
    
#生成器还有一个特点如果作为函数参数，可以直接写推导式，而不用加小括号
print(sum(i for i in range(100) if i % 2))
```

