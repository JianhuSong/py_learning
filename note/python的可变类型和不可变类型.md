# 1. 解释

## 1.1 不可变类型

​	在id不变的情况下，value可以改变

​	在熟知的类型中，整数，浮点数，复数，布尔值，字符串，元组和冻结集合属于不可变类型

​	对不可类型的变量重新赋值，实际上是重新创建一个不可变类型的对象，并将原来的变量重新指向新创建的对象

## 1.2 可变类型

​	value一旦改变，id也跟着改变

​	在熟知的类型中，列表，字典，集合属于可变类型

# 2. 举例

会通过大量的例子来帮助自己记忆。

## 2.1 不可变类型举例

### 2.1.1 数字举例

```python
# 数字举例
a = 11
print(id(a))
a +=1
print(id(a))
# 140729053930600

# 140729053930664
```

### 2.1.2 字符串举例

```python
# 字符串举例
str1 = 'abcdef'
print(f'{str1} id = {id(str1)}')
str1 = str1[4:]
str1 += 'hello world'
print(f'{str1} id = {id(str1)}')
```

### 2.1.3 元组举例

```python
# 元组
# 在 Python 中，元组是一种不可变序列，即元组一旦被创建就不能更改它的内容。这表明在原有的元组上新增元素是不允许的
my_tuple = (1,2,3,4)
my_tuple1 = my_tuple
print(f'value = {my_tuple}, id = {id(my_tuple)}')
print(f'value1 = {my_tuple1}, id = {id(my_tuple1)}')

# 通过+ 将旧有元组与需要添加的值拼接形成新的元组
my_tuple = my_tuple + (11,22)
print(f'value = {my_tuple}, id = {id(my_tuple)}')

# 通过*解包旧有元组，然后和新的元素组成新的元组
my_tuple = (*my_tuple, 33)
print(f'value = {my_tuple}, id = {id(my_tuple)}')

# 值发生改变同时id也发生改变。
```

### 2.1.4 冻结集合举例

```python
# 冻结集合
# 冻结集合是不可变的，冻结集合在被定义后我们就不能再修改里面的元素了。冻结集合除了不能修改元素以外，其他的性质和集合一样。
my_f_set = frozenset(range(3))
print(f'value={my_f_set},id={id(my_f_set)}')
# 冻结集合的其它操作就不介绍了
```

# 2.2 可变类型举例

### 2.2.1 列表举例

```python
# 列表
# 列表是一个可以包含任何类型数据的有序集合，比如数字、字符串甚至是其他列表。
# 列表是可变的，也就是说你可以改变一个列表的内容。
# 创建一个列表很简单，只需要将一些值用逗号隔开，然后用方括号括起来即可
# 常用的三种列表的创建方式
my_list = [1,2,3,4]
my_list1 = list(range(5))
my_list2 = [x for x in range(3)]
print(f'value = {my_list}, id = {id(my_list)}')
my_list.insert(0,11)
print(f'value = {my_list}, id = {id(my_list)}')
my_list.append(22)
print(f'value = {my_list}, id = {id(my_list)}')
my_list.remove(11)
print(f'value = {my_list}, id = {id(my_list)}')

# 可以看到我们向列表添加元素和删除元素（改变列表的内容），id均未发生变化
# value = [1, 2, 3, 4], id = 1181715063808
# value = [11, 1, 2, 3, 4], id = 1181715063808
# value = [11, 1, 2, 3, 4, 22], id = 1181715063808
# value = [1, 2, 3, 4, 22], id = 1181715063808
```

### 2.1.2 字典举例

```python
# 字典
# 字典是python当中的一种数据类型，字典内部是一个一对一映射的数据关系。
import itertools
my_dict = {'1':1, '2':2}
my_dict1 = {x:x**2 for x in range(4)}
my_dict2 = dict(zip([1,2,3,4,5],[chr(x) for x in range(97,102)]))
my_dict3 = dict(itertools.product(range(3), range(3)))
print(f'value = {my_dict}')
print(f'value = {my_dict1}')
print(f'value = {my_dict2}')
print(f'value = {my_dict3}')
print(f'value = {my_dict},id = {id(my_dict)}')
my_dict['key'] = 'value'
print(f'value = {my_dict},id = {id(my_dict)}')

del my_dict['1']
print(f'value = {my_dict},id = {id(my_dict)}')

# 我们往字典里添加元素和从字典里删除元素，字典的id均未发生改变
# value = {'1': 1, '2': 2}
# value = {0: 0, 1: 1, 2: 4, 3: 9}
# value = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# value = {0: 2, 1: 2, 2: 2}
# value = {'1': 1, '2': 2},id = 1497832590976
# value = {'1': 1, '2': 2, 'key': 'value'},id = 1497832590976
# value = {'2': 2, 'key': 'value'},id = 1497832590976
```

### 2.1.3 集合举例

```python
# 集合
# 集合是python当中一种无序的、不重复的数据序列

my_set = {1,2,3,4}
my_set1 = set(range(5))
print(f'value = {my_set}')
print(f'value = {my_set1}')

print(f'value = {my_set}, id = {id(my_set)}')
my_set.add(12)
print(f'value = {my_set}, id = {id(my_set)}')

my_set.remove(12)
print(f'value = {my_set}, id = {id(my_set)}')

# value = {1, 2, 3, 4}
# value = {0, 1, 2, 3, 4}
# value = {1, 2, 3, 4}, id = 2059410018752
# value = {1, 2, 3, 4, 12}, id = 2059410018752
# value = {1, 2, 3, 4}, id = 2059410018752
```

2.1. 4 可变类型参数

```python
# 不可变类型参数
# 函数内部修改参数的值，只是修改另一个复制对象，不会影响变量本身
# 可变类型参数
# 函数将实参本体传递过去，修改后函数外部的变量也会受到影响

def my_func(list1:list,dict1:dict, set1:set):
    list1.pop()
    dict1.pop(1)
    set1.remove(22)

def my_func1(list1:list,dict1:dict, set1:set):
    list1 = list1[1:]
    dict1 = dict(zip(range(3),range(3)))
    set1 = set(range(3))    
my_list = list(range(4))
my_dict = {x:x**2 for x in range(1,4)}
my_set = set(range(20,24))

print(f'value = {my_list}, id = {id(my_list)}')
print(f'value = {my_dict}, id = {id(my_dict)}')
print(f'value = {my_set}, id = {id(my_set)}')

my_func(my_list, my_dict, my_set)
print(f'value1 = {my_list}, id = {id(my_list)}')
print(f'value1 = {my_dict}, id = {id(my_dict)}')
print(f'value1 = {my_set}, id = {id(my_set)}')

# 这样操作，没有影响到外面
# 尝试这样解释，由于在函数内使用了等号，相当远新建了一个变量，而局部变量在函数结束时就已经无了
my_func1(my_list, my_dict, my_set)
print(f'value2 = {my_list}, id = {id(my_list)}')
print(f'value2 = {my_dict}, id = {id(my_dict)}')
print(f'value2 = {my_set}, id = {id(my_set)}')

# value = [0, 1, 2, 3], id = 3112078428416
# value = {1: 1, 2: 4, 3: 9}, id = 3112077352960
# value = {20, 21, 22, 23}, id = 3112078346944
# value1 = [0, 1, 2], id = 3112078428416
# value1 = {2: 4, 3: 9}, id = 3112077352960
# value1 = {20, 21, 23}, id = 3112078346944
# value2 = [0, 1, 2], id = 3112078428416
# value2 = {2: 4, 3: 9}, id = 3112077352960
# value2 = {20, 21, 23}, id = 3112078346944
```

