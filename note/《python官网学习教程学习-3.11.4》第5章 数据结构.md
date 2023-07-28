[@TOC](文章目录)

---

## 5.1 列表详解

| 方法名称                              | 解释                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| list.append(x)                        | 在列表的末尾插入一个元素，相当于a[len(a):] = [x]             |
| list.extend(iterable)                 | 用可迭代对象元素扩展列表，相当于a[len(a):] = iterable        |
| list.insert(i,x)                      | 在指定位置插入元素，第一个参数时插入元素的索引，因此a.insert(0,x)在列表开头插入元素，a.insert(len(a),x)等同于a.append(x) |
| list.remove(x)                        | 从列表中删除第一个值为x的元素，未找到指定元素时触发ValueError异常 |
| list.pop([i])                         | 删除列表中指定位置的元素，并返回删除指定的元素。未指定位置时，a.pop()删除并返回列表最后一个元素。 |
| list.clear()                          | 删除列表中的所有元素相当于del a[:]                           |
| list.index(x[, start[,end]])          | 返回列表中第一个值为x的元素的index，未找到触发ValueError异常。start.end限定了查找范围 |
| list.count(x)                         | 返回列表中x元素出现的次数                                    |
| list.reverse()                        | 翻转列表中的元素                                             |
| list.copy()                           | 返回列表的浅拷贝。相当于a[:]                                 |
| list.sort(*,key=none,reverse = false) | 就排序类表中的元素。                                         |

不是所有数据都可以排序或比较

补充知识：

浅拷贝是创建原始对象内部属性的副本的过程，但是，对于新对象的属性，它们实际上只是指向原始对象的引用。这意味着如果您更改新对象的属性，这些更改将反映在原始对象中。

深拷贝是创建一个完全不同的副本对象的过程，该对象的所有属性都被复制，包括嵌套的对象和子对象。在深拷贝后，原始对象与新对象不再共享任何内容，也不再占用同一段内存空间

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
mylist = list(x for x in range(10))
print(mylist)
mylist[len(mylist):] = [11]
mylist.append(12)
print(mylist)

mylist.insert(0,133)
mylist.insert(1,'aaa')
mylist.insert(len(mylist),'xxxxx')
print(mylist)

mylist.remove('xxxxx')
print(mylist)

mylist.pop(0)
mylist.pop()
print(mylist)
print(mylist.count(1))
print(mylist.index(0))

#这个翻转是会影响原来的内容的。
mylist.reverse()
print(mylist)

mylist.clear()
mylist.append([2222,3333,444,555])
#列表的copy方法是对最外层copy的深拷贝，内层list的浅拷贝
mylist1 = mylist.copy()
mylist1.append("append")
print("mylist1 = ",mylist1)
print("mylist = ",mylist)
#mylist的第一个元素是个列表，列表就可以用列表的方法。
mylist[0].append(1111)
print("mylist1 = ",mylist1)
print("mylist = ",mylist)

del mylist[:]
mylist.extend(x for x in range(6))
mylist.reverse()
print("mylist = ",mylist)
mylist.sort(key=None, reverse=False)
print("mylist = ",mylist)

del mylist1[0]
mylist1.extend(range(6))
print("mylist1 = ",mylist1)
#不是所有都能排序，TypeError: '<' not supported between instances of 'int' and 'str'
mylist1.sort()

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
# [133, 'aaa', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 'xxxxx']
# [133, 'aaa', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
# ['aaa', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
# 1
# 1
# [11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 'aaa']
# mylist1 =  [[2222, 3333, 444, 555], 'append']
# mylist =  [[2222, 3333, 444, 555]]
# mylist1 =  [[2222, 3333, 444, 555, 1111], 'append']
# mylist =  [[2222, 3333, 444, 555, 1111]]
# mylist =  [5, 4, 3, 2, 1, 0]
# mylist =  [0, 1, 2, 3, 4, 5]
# mylist1 =  ['append', 0, 1, 2, 3, 4, 5]
# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 50, in <module>
#     mylist1.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
```

### 5.1.1 用列表实现堆栈

堆栈的特性：后进先出

后进： 使用list的append保证每次都是在列表的尾部加入

先出：从尾部取出元素，使用list.pop() 

栈顶：有元素进/出的

栈底：没有元素进/出

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
my_stack = []

for i in range(10):
    print(f"push str({i}) into my_stack.")
    my_stack.append(str(i))

for i in range(len(my_stack)):
    print("Pop {0} from my_stack.".format(my_stack.pop()))
```



### 5.1.2 用列表实现队列

队列的特性：先进先出

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque as que
#先用自己的想法实现一遍，然后用官方例子

class MyQue:
    def __init__(self, *args):
        self.my_list = []
        self.my_list.extend(list(*args));
    def __str__(self):
        return self.my_list.__str__()
    def que_in(self, value):
        self.my_list.append(value)
    def que_out(self):
        if not len(self.my_list):
            print("It is a empty queue.")
        else:
            return self.my_list.pop(0)

myqueue1 = MyQue()
myqueue2 = MyQue(x for x in range(10))

print("myqueue1: ",myqueue1)

print("myqueue2",myqueue2)
print(myqueue2.que_out())
print(myqueue2.que_out())
print(myqueue2.que_out())
print(myqueue2.que_out())
print("myqueue2",myqueue2)

queue = que(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)

print(f"{queue.popleft()} left.")
print(f"{queue.popleft()} left.")
print(f"{queue.popleft()} left.")
print(f"{queue.popleft()} left.")


# myqueue1:  []
# myqueue2 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 0
# 1
# 2
# 3
# myqueue2 [4, 5, 6, 7, 8, 9]
# deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
# Eric left.
# John left.
# Michael left.
# Terry left.
```



### 5.1.3 列表推导式

用列表推导式创建列表的方法更简洁

列表推导式的方括号内包含以下内容：一个表达式，后面为一个 `for` 子句，然后，是零个或多个 `for` 或 `if` 子句。结果是由表达式依据 `for` 和 `if` 子句求值计算而得出一个新列表。 

列表推导式可以用复杂的表达式和嵌套函数

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#一个表达式，后面为一个 for 子句，然后，是零个或多个 for 或 if 子句
my_list1 = [x**2 for x in range(10) if x % 2 == 0]
print(f"my_list1 = {my_list1}")

my_list1 = [x*2 for x in range(10) for a in [2,3,4,5,6,8,10] if x == a]
print(f"my_list1 = {my_list1}")

#表达式是元组（例如 (x, y)）时，必须加上括号：
my_list1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(f"my_list1 = {my_list1}")

#列表推导式中的初始表达式可以是任何表达式，甚至可以是另一个列表推导式。
my_list1 = [[x for x in range(3)] for i in range(10)]
print(f"my_list1 = {my_list1}")

#不用自己写那么复杂，python 提供了zip
my_list1 = list(zip([x for x in range(5)], [a for a in range(1,5)]))
print(f"my_list1 = {my_list1}")
```

## 5.2 del 语句

del 语句按索引，而不是值从列表中移除元素。

`del` 语句也可以从列表中移除切片

del 清空整个列表

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#一个表达式，后面为一个 for 子句，然后，是零个或多个 for 或 if 子句
my_list1 = [x**2 for x in range(20) if x % 2 == 0]
print(f"my_list1 = {my_list1}")

#删除一个元素
del my_list1[0]
print(f"del my_list1[0] = {my_list1}")

#移除一段范围内的元素
del my_list1[1:5]
print(f"del my_list1[1:5] = {my_list1}")

#移除所有元素
#还可以使用del my_list1
del my_list1[:]
print(f"del my_list1[:] = {my_list1}")
```

## 5.3 元组和序列

输出时，元组都要由圆括号标注，这样才能正确地解释嵌套元组

输入时，圆括号可有可无，不过经常是必须的（如果元组是更大的表达式的一部分）。

构造 0 个或 1 个元素的元组比较特殊：为了适应这种情况，对句法有一些额外的改变。用一对空圆括号就可以创建空元组；只有一个元素的元组可以通过在这个元素后添加逗号来构建（圆括号里只有一个值的话不够明确）。丑陋，但是有效

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
my_tuple = (1,2,3,4)
print(f"my_typle = {len(my_tuple)}, type = {type(my_tuple)}")

my_tuple = (1,)
print(f"my_typle = {len(my_tuple)}, type = {type(my_tuple)}")

my_tuple = 1,
print(f"my_typle = {len(my_tuple)}, type = {type(my_tuple)}")

my_tuple = ()
print(f"my_typle = {len(my_tuple)}, type = {type(my_tuple)}")

my_tuple = (1,2.22,"hello world",[1,3,4],(1,3,4,5))
print(f"my_typle = {len(my_tuple)}, type = {type(my_tuple)}")

# 序列解包时，左侧变量与右侧序列元素的数量应相等
my_list = [(1,2,3),(4,5,6),(7,8,9),(11,12,13)]

for a in my_list:
    x, y,z = a
    print(f'{x},{y},{z}')

```

## 5.4 集合

集合是由不重复元素组成的无序容器

创建空集合只能用 `set()`

本用法包括成员检测、消除重复元素。集合对象支持合集、交集、差集、对称差分等数学运算。

 列表推导式 类似，集合也支持推导式

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
my_set = set()
print(f"my_set type = {type(my_set)}, my_set = {my_set}")

my_set = set([1,2,3,4])
print(f"my_set type = {type(my_set)}, my_set = {my_set}")

my_set = set("1234123412q")
print(f"my_set type = {type(my_set)}, my_set = {my_set}")

my_set = set((1,3,4,5,6))
print(f"my_set type = {type(my_set)}, my_set = {my_set}")

my_set = {x for x in 'asdgakalsjdfjas' if x not in "abc"}
print(f"my_set type = {type(my_set)}, my_set = {my_set}")

my_set = {x for x in range(4)}
print(f"my_set type = {type(my_set)}, my_set = {my_set}")
```

## 5.5 字典

与以连续整数为索引的序列不同，字典以 *关键字* 为索引，关键字通常是字符串或数字，也可以是其他任意不可变类型

只包含字符串、数字、元组的元组，也可以用作关键字。但如果元组直接或间接地包含了可变对象，就不能用作关键字

列表不能当关键字

可以把字典理解为 *键值对* 的集合，但字典的键必须是唯一的。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_dict = {1:123, 2:2344, 5:1234}
print(f" my_dict type = {type(my_dict)}, my_dict = {my_dict}")

my_dict = {}
print(f" my_dict type = {type(my_dict)}, my_dict = {my_dict}")

my_dict =  dict()
print(f" my_dict type = {type(my_dict)}, my_dict = {my_dict}")

my_dict = dict(zip([1,2,3,4,5],"asdlfkjaslkj"))
print(f" my_dict type = {type(my_dict)}, my_dict = {my_dict}")

my_dict = dict([(1,3),(2,4),(1,666),(333,333333)])
print(f" my_dict type = {type(my_dict)}, my_dict = {my_dict}")

#这里可以看出，只有第一个for决定了项的熟练，第二个循环看作条件（一次执行完），循环到最后就是ｋ,所以value永远是k
my_dict = {x:y for x in range(1,5) for y in "asdfasjdlfjask"}
print(f" my_dict type = {type(my_dict)}, my_dict = {my_dict}")

my_dict = {x:x**2 for x in range(1,5)}
print(f" my_dict type = {type(my_dict)}, my_dict = {my_dict}")
```

## 5.6 循环的技巧

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

# 在字典中循环时，用items()方法可以同时取出键和关键字
my_dict = {x:x+x**2 for x in range(1,5)}

for x,y in my_dict.items():
    print(f"key = {x}, value = {y}")
    
# 在序列中循环时，用enumerate()函数可以同时取出index和value
for index,value in enumerate("abcd"):
    print(f"index = {index}, vlaue = {value}")
    
# 同时循环两个或者多个序列时，用zip()函数可以将期内的元素一一匹配
for value1,value2,value3 in zip([1,3,4,5,6],(11,55,66),'asdfasdfasd'):
    print(f" value1 = {value1}, value2 = {value2}, value3 = {value3}")
    
# 逆向循环时，先正向定位序列，然后用reversed()函数
for i in reversed(range(1,4,1)):
    print(f"i = {i}")
    
# 按指定顺序循环列表时, 可以用sorted()函数，在不改动原序列的基础上，返回一个新的序列
for x in sorted("abcdefgabc"):
    print(f"x = {x}")
    
# 可以使用set取出序列中重复的元素
my_list = list(set((1,1,2,33,33,33,44,123))) 
my_tuple = tuple(set([2,2,2,2,2,3,4,3,5]))
my_str = str(set('adasdfasjdfklsajdfkja'))

print(f"my_list = {my_list}")
print(f"my_tuple = {my_tuple}")
print(f"my_str = {my_str}")

# 一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全：
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data
```

## 5.7 深入控制条件

`while` 和 `if` 条件句不只可以进行比较，还可以使用任意运算符。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#比较运算符 in 和 not in 用于执行确定一个值是否存在（或不存在）于某个容器中的成员检测
my_list = list(range(2,5))
if 3 in my_list:
    print("3 is in range(2,5)")

if 11 not in my_list:
    print("3 not in range(2,5)")
    
# 运算符 is 和 is not 用于比较两个对象是否是同一个对象
my_list1 = my_list
my_list2 = [0,1]
if my_list1 is my_list:
    print("my_list1 == my_list")
    
if my_list2 is not my_list:
    print("my_list2 != my_list")
    
# 所有比较运算符的优先级都一样，且低于任何数值运算符。
a = 1
b = 2
c = 11

if a + b < c:
    print("a + b < c")

if c > a+b:
    print("c > a + b")
    
# 比较操作支持链式操作
if a < b < c:
    print("a < b < c")
    
# 比较操作可以用布尔运算符 and 和 or 组合，并且，比较操作（或其他布尔运算）的结果都可以用 not 取反。
# 这些操作符的优先级低于比较操作符；not 的优先级最高， or 的优先级最低 
# 布尔运算符 and 和 or 也称为 短路 运算符：其参数从左至右解析，一旦可以确定结果，解析就会停止
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
```

## 5.8 序列和其它类型的比较

序列对象可以与相同序列类型的其他对象比较。首先，比较前两个对应元素，如果不相等，则可确定比较结果；如果相等，则比较之后的两个元素，以此类推，直到其中一个序列结束。

对不同类型的对象来说，只要待比较的对象提供了合适的比较方法，就可以使用 `<` 和 `>` 进行比较

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 只要有一个元素大，那么拥有较大元素值的序列大于较小值序列。
# 值都相等的两个序列才叫相等
list1 = [1,2,3,4,5]
list2 = [1,2,555,4]

if list1 > list2:
    print("list1 > list2")
else:
    print("list1 < list2")
```

