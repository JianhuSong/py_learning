@[TOC](文章目录)

---

# 前言

关于字典：

​		怎么创建 字典

​		怎么往字典里添加元素

​		怎么修改字典的元素的值

​		怎么删除字典的元素/字典

关于集合

​		怎么创建集合

​		怎么往集合里添加元素

​		怎么修改集合元素的值

​		怎么删除集合元素/集合

# 1. 字典

python的字典的元素是键-值对（key-value）

python的字典在有些地方称为哈斯（hash）,在有些地方又称为关系数组

字典是python中唯一的映射类型（两个元素之间的相互对应关系称为映射）

字典是另外一种可变容器类型，且可存储任意类型的对象

值可以取任何数据类型，但是键必须是不可变的

每一对键值组合称为项

字典的键必须独一无二

要声明一个空的字典，直接用大括号就行（{}）

## 1.1创建字典

```python
#通过关键字dict和二元序列来创建
dict1 = dict((('a',10),('b',11)))
dict2 = dict([('A',10),('B',11)])
#通过dict和具有映射关系的参数来创建
dict3 = dict(a=10,b=11)
#创建一个空的字典，然后通过[]来添加元素
dict4 = {}
dict4["asdasdasd"] = 11
#直接赋值创建
dict5 = {'a':2123, 'b':1234}
#通过关键字dict和zip来创建
dict6 = dict(zip('abcdef',[1,2,3,4,5]))
#通过推导来创建（网上查到的）
dict7 = {i:i ** 2 for i in range(1,5)}
#通过dict.fromkeys()来创建
#第二个参数看作是一个整体
dict8=dict.fromkeys(range(4))
dict9=dict.fromkeys(range(4),'aaaaa')
print("dict1:",dict1)
print("dict2:",dict2)
print("dict3:",dict3)
print("dict4:",dict4)
print("dict5:",dict5)
print("dict6:",dict6)
print("dict7:",dict7)
print("dict8:",dict8)
print("dict9:",dict9)
	
#输出结果：
#dict1: {'a': 10, 'b': 11}
#dict2: {'A': 10, 'B': 11}
#dict3: {'a': 10, 'b': 11}
#dict4: {'asdasdasd': 11}
#dict5: {'a': 2123, 'b': 1234}
#dict6: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#dict7: {1: 1, 2: 4, 3: 9, 4: 16}
#dict8: {0: None, 1: None, 2: None, 3: None}
#dict9: {0: 'aaaaa', 1: 'aaaaa', 2: 'aaaaa', 3: 'aaaaa'}
```



## 1.2 访问/添加元素

```python
#访问字典的方法
dict1 = dict.fromkeys(range(3), "AaBbCc")
print("keys:", dict1.keys())
print("values:", dict1.values())
print("items", dict1.items())

#若指定的key在字典中没有，给这个key关联一个value的时候就会往字典里添加一个键值对
dict1[100] = "aaaaaaa"
print("keys:", dict1.keys())
print("values:", dict1.values())
print("items", dict1.items())

# 结果输出
# keys: dict_keys([0, 1, 2])
# values: dict_values(['AaBbCc', 'AaBbCc', 'AaBbCc'])
# items dict_items([(0, 'AaBbCc'), (1, 'AaBbCc'), (2, 'AaBbCc')])
# keys: dict_keys([0, 1, 2, 100])
# values: dict_values(['AaBbCc', 'AaBbCc', 'AaBbCc', 'aaaaaaa'])
# items dict_items([(0, 'AaBbCc'), (1, 'AaBbCc'), (2, 'AaBbCc'), (100, 'aaaaaaa')])
```

```python
# 还可以通过[]/get()访问字典
dict1 = dict.fromkeys(range(20), "AaBbCc")
print("dict1[0] = ", dict1[0])
print("dict1.get(0) = ", dict1.get(0))
# 输出结果：
# dict1[0] = AaBbCc
# dict1.get(0) = AaBbCc
```

字典的拷贝

```python
# 字典拷贝：
# =/copy()
# 通过'='看起来像是赋值，其实就是给原来的字典起了另外一个名字。
# 使用copy(),将原有字典拷贝了一份存在了别的地方。
dict1 = dict.fromkeys(range(2), "AaBbCc")
dict2 = dict1
dict3 = dict1.copy()
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3", dict3)
print("id(dict1)", id(dict1))
print("id(dict2)", id(dict2))
print("id(dict3)", id(dict3))
# 输出结果：
# dict1: {0: 'AaBbCc', 1: 'AaBbCc'}
# dict2: {0: 'AaBbCc', 1: 'AaBbCc'}
# dict3 {0: 'AaBbCc', 1: 'AaBbCc'}
# id(dict1) 1664347081152
# id(dict2) 1664347081152
# id(dict3) 1664346754752
```



## 1.3 修改字典元素的值

```python
# 更新字典的内容
# []/update()
# 若字典存在对应的key,那就是更新。若不存在那就是添加key-value

dict1 = dict.fromkeys(range(2), "AaBbCc")
print("dict1:", dict1)
dict1[1] = "Hello"
dict1["aaa"] = 'AAAAAA'
print("dict1:", dict1)
dict2 = dict.fromkeys(range(2), 'AAAAAAAA')
print("dict2:", dict2)
dict2.update({3: 1, 2: 3})
print("dict2:", dict2)
dict2.update((("aaa", 2), ("ccc", 3)))
print("dict2:", dict2)
dict2.update([(11, 'aa'), ('vvvv', "aaaa")])
print("dict2:", dict2)
dict2.update(zip((0, 1, 2), ["test1", "test2", 'test3']))
print("dict2:", dict2)
# 目前这个已经不能用了
# dict2.update('aaaaa'=444)
# 输出结果：
# dict1: {0: 'AaBbCc', 1: 'AaBbCc'}
# dict1: {0: 'AaBbCc', 1: 'Hello', 'aaa': 'AAAAAA'}
# dict2: {0: 'AAAAAAAA', 1: 'AAAAAAAA'}
# dict2: {0: 'AAAAAAAA', 1: 'AAAAAAAA', 3: 1, 2: 3}
# dict2: {0: 'AAAAAAAA', 1: 'AAAAAAAA', 3: 1, 2: 3, 'aaa': 2, 'ccc': 3}
# dict2: {0: 'AAAAAAAA', 1: 'AAAAAAAA', 3: 1, 2: 3, 'aaa': 2, 'ccc': 3, 11: 'aa', 'vvvv': 'aaaa'}
# dict2: {0: 'test1', 1: 'test2', 3: 1, 2: 'test3', 'aaa': 2, 'ccc': 3, 11: 'aa', 'vvvv': 'aaaa'}
```



## 1.4删除字典元素/字典

```python
# pop()和popitem()
# 1.这两个都会减少字典中的项

dict1 = dict.fromkeys(range(2), "AaBbCc")
dict2 = dict.fromkeys(range(2), 'AAAAAAAA')
print("Before dict1:", dict1)
print("Before dict2:", dict2)
print("dict1.pop(1)", dict1.pop(1))
print("dict2.popitem()", dict2.popitem())
print("after dict1:", dict1)
print("after dict2:", dict2)
# popitem弹出目前dict中最后存入的项？？
dict3 = {i: i ** 2 for i in range(1, 10)}
print("dict3:", dict3)
for i in range(1, 4):
	dict3.popitem()
	print("After popitem dict3:", dict3)
# 输出结果：
# Before dict1: {0: 'AaBbCc', 1: 'AaBbCc'}
# Before dict2: {0: 'AAAAAAAA', 1: 'AAAAAAAA'}
# dict1.pop(1) AaBbCc
# dict2.popitem()(1, 'AAAAAAAA')
# after dict1: {0: 'AaBbCc'}
# after dict2: {0: 'AAAAAAAA'}
# dict3: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# After popitem dict3: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# After popitem dict3: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
# After popitem dict3: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
```



#  2. 集合

如果用大括号括起来的一堆数字但是没有体现映射关系，那么python就会认为这堆玩意儿就是集合

集合中的元素是唯一的

集合中的元素是无序的

不能通过索引取访问集合中的任一元素

## 2.1创建集合

```python
#使用{}直接定义
myset1 = {1, 3, 4, 5, 6, 6, 6}

#通过关键字set()定义
myset2 = set([1, 2, 34, 5, 6])
myset3 = set((1, 2, 4, 5, 6))
myset4 = set("sajdlfkjas")
myset5 = set(x for x in range(2, 10))
print("myset1", myset1)
print("myset2", myset2)
print("myset3", myset3)
print("myset4", myset4)
print("myset5", myset5)
# 输出结果：
# myset1 {1, 3, 4, 5, 6}
# myset2 {1, 2, 34, 5, 6}
# myset3 {1, 2, 4, 5, 6}
# myset4 {'s', 'f', 'a', 'd', 'k', 'l', 'j'}
# myset5 {2, 3, 4, 5, 6, 7, 8, 9}
```



## 2.2 添加元素

```python
# add()
# 若元素存在于集合中，无影响
# 若元素不存在于集合中，往集合里面添加
myset5 = set(x for x in range(2, 10))
print("myset5", myset5)
myset5.add(2)
myset5.add(1100)
print("myset5", myset5)
# 输出结果：
# myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# myset5 {2, 3, 4, 5, 6, 7, 8, 9, 1100}
```



## 2.3 修改集合元素的值

```python
#update()
myset5 = set(x for x in range(2, 10))
print("myset5", myset5)
myset5.update([2, 4, 5, 100, 200])
myset5.update((2, 4, 5, 100, 200, 300))
myset5.update(x for x in range(1000, 1010))
myset5.update('abcdefg')
print("myset5", myset5)
# 输出结果 ：
# myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# myset5 {2, 3, 4, 5, 6, 7, 8, 9, 'g', 'f', 300, 'a', 'd', 'c', 'b', 200, 'e', 100, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009}
```



```python
myset5 = set(x for x in range(2, 10))
print("myset5", myset5)
myindex = 0
for x in myset5:
	print("member %d value is %d" % (myindex, x))
	myindex += 1
	if 2 in myset5:
	    print("2 is in set.")
	if 100 not in myset5:
	    print("100 is not in set.")

# 输出结果：
# myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# member 0 value is 2
# member 1 value is 3
# member 2 value is 4
# member 3 value is 5
# member 4 value is 6
# member 5 value is 7
# member 6 value is 8
# member 7 value is 9
# 2 is in set.
# 100 is not in set.
```



## 2.4 删除集合元素/集合

```python
# remove()
# 参数必须是集合的成员
myset5 = set(x for x in range(2, 10))
print("myset5", myset5)
myset5.remove(2)
# myset5.remove(1100) #这句会报错
print("myset5", myset5)

#如果不想修改集合元素，那么使用frozenset()创建集合
myset6 = frozenset(x for x in range(1,3))
#AttributeError: 'frozenset' object has no attribute 'add'
#myset6.add()
print(myset6)
del myset6
# 输出结果：
# myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# myset5 {3, 4, 5, 6, 7, 8, 9}
# frozenset({1, 2})
```

