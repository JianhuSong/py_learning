@[TOC](文章目录)

___

# 1.模块

模块就是程序

在python中，每个模块都会维护一个独立的命名空间，在使用模块中的内容的时候应该把模块名加上

## 1.1导入模块的方法

```python
#imort 模块名
#在使用的时候加上模块名
import my_module
my_module.myAdd(3,3)
```

```python
#from 模块名字 import 函数名 或者 from 模块名字 import *
#第二种不建议使用，这样可能存在名字冲突
from my_module import myAdd
myAdd(2,3)
```

```python
# import 模块名字 as 新名字
import my_module as md
md.myAdd("hello ", "world")
```

## 1.2 避免在导入模块的时候执行模块中的函数

```python
#my_module.py
def myAdd(a, b):
    print(a + b)
    

print(__name__)
#加上这个以后，只有在单独执行my_module.py的时候，myAdd(3,3000)才会执行
if __name__ == '__main__':
    myAdd(3, 3000)  
```

```python
#test.py
print(__name__)
import my_module as md
md.myAdd("hello ", "world")
```



# 2.搜索路径

## 2.1搜索路径配置

```python
#以下语句执行时可以查看python导入模块时候的搜索路径
import sys
print(sys.path)
#结果中的site-packages是最佳的模块存放路径

```

## 2.2包

如何创建一个包

（1）创建一个文件夹，用于存放相关的模块，文件夹的名字即包的名字

（2）在文件夹中创建一个\__init__.py的模块文件，内容可以为空

（3）将相关文件放入文件夹

```python
import MD.my_module as mmd
mmd.myAdd(123,456)
```