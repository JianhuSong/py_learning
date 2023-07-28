# 10. 标准库简介

内如入名称，叫简介。每个都讲点，但是都不详细。知道有这么个东西，到时候查的时候方便。

## 10.1. 操作系统接口

os模块提供了许多与操作系统交互的函数

一定要使用import os 不要使用from os import *。避免内建的open()函数被os.open()隐式替换掉。

```python
import os
print("current work dir :", os.getcwd())
os.chdir(r'D:\coding\py_learning')
print("current work dir :", os.getcwd())
os.chdir(r"D:\coding\py_learning\code")
print("current work dir :", os.getcwd())
os.system(r'dir')
```

内置的dir()和help()函数可作为交互辅助工具，用于处理大型模块

```python
import os

# returns a list of all module functions
print(dir(os))

# returns an extensive manual page created from the module's docstrings
print(help(os))
```

对于日常文件和目录的管理，shutil提供了更易于使用的更高级别的接口

```python
import shutil

# 如其名
shutil.copyfile("test.txt", "test_copy.txt")

# 移动文件或者文件夹
shutil.move("test_copy.txt", "..")
```

## 10.2.文件通配符

```python
import glob

# glob模块提供了一个在目录中使用通配符搜索创建文件列表的函数
print(glob.glob('*.py'))
```

## 10.3.命令行参数

通用实用程序脚本通常需要处理命令行参数。这些参数作为列表存储在 sys 模块的 argv 属性中

```python
import sys

print(sys.argv)
print(len(sys.argv))
```

argparse 模块提供了一种更复杂的机制来处理命令行参数。

```python
# argparse 使用的标准流程
import argparse    # 导入argparse 模块

# 定义一个参数解析对象
parser = argparse.ArgumentParser(
    prog='src',
    description='Show top lines from each file')

# 添加解析的参数flag/option

# name or flags : name 前面没有-/--，flags 前面有-/--

#name 每次只能传入一个
parser.add_argument('filenames', nargs='+')

# flags 可以传入一系列的flag
parser.add_argument('-l', '--lines', type=int, default=10)

# 获取参数
args = parser.parse_args()
print(args)

# 这里不展开，可以自行搜索
```



## 10.4.错误输出重定向和程序终止

 sys 还有stdin, stdout,stderr

```python
import sys
sys.stderr.write("stderr test.")
sys.stdout.write("stdout test")
```

直接使用sys.exit() 就可以退出脚本

## 10.5.字符串匹配

re模块为高级字符串处理提供了正则表达式工具。

当只需要简单的功能时，首选字符串方法。

```python
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print('tea for too'.replace('too', 'two'))
```



## 10.6.数学

math模块提供对浮点数学的底层C库函数的访问

random模块提供了惊醒随机选择的工具

statistics模块计算数值数据的基本统计属性（均值，中位数，方差等）

```python
import math
import random
import statistics
print(math.cos(math.pi/4))

# 从指定的序列中获取一个随机元素
print(random.choice([1,2,'asdfas',3.14]))

# 用于从指定序列中随机获取指定长度的片段，sample()函数不会修改原有序列。
print(random.sample(range(1000),10))

# 返回随机生成的一个浮点数，范围在[0,1)之间
print(random.random())

# 用于从指定范围内按指定基数递增的集合中获取一个随机数。 
print(random.randrange(10))

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

# 数据的算术平均数(“平均数”)
print(statistics.mean(data))

# 中位数
print(statistics.median(data))

# 方差
print(statistics.variance(data))
```

## 10.7.互联网访问

有许多模块用于访问互联网和处理互联网协议。

```python
# urllib.request 用于从URL检索数据
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline
```

## 10.8.日期和时间

datetime模块提供了以简单和复杂方式操作日期和时间的类，虽然支持日期和时间算法，但实现的重点是有效的成员提取以进行输出格式化和操作。该模块还支持可感知时区的对象。

```python
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
```

## 10.9.数据压缩

常见的数据存档和压缩格式由模块直接支持，包括：zlib, gzip, bz2, lzma, zipfile 和 tarfile。

```python
import zlib
s = b'witch which has which witches wrist watch'
print("len(s) = ", len(s))
t = zlib.compress(s)
print("len(t) = ", len(t))

print("zlib.decompress(t) = ", zlib.decompress(t))
print("zlib.crc32(s) = ", zlib.crc32(s))
```

## 10.10.性能测量

一些Python用户对了解同一问题的不同方法的相对性能产生了浓厚的兴趣。 Python提供了一种可以立即回答这些问题的测量工具。

```python
from timeit import Timer
t1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print("t1",t1)
print("t2",t2)
```

## 10.11.质量控制

doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试

```python
# Doctest的测试原理就是把我们在python控制台中输入输出记录保存到函数docstring里，
# 然后--把这些输入到解析器里对比输出是否一致用来确定测试结果是否通过。
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    Args:
        values (values): It must be a number.
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod() # automatically validate the embedded tests
```

unittest模块不像doctest那样易用，但它允许在一个单独的文件中维护更全面的测试集

```python
import unittest
def average(values):
    """Computes the arithmetic mean of a list of numbers."""
    return sum(values) / len(values)

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```



## 10.12.自带电池

Python有“自带电池”的理念。通过其包的复杂和强大功能可以最好地看到这一点。例如:

xmlrpc.client 和 xmlrpc.server 模块使得实现远程过程调用变成了小菜一碟。 尽管存在于模块名称中，但用户不需要直接了解或处理 XML。

 email 包是一个用于管理电子邮件的库，包括MIME和其他符合 RFC 2822 规范的邮件文档。与 smtplib 和 poplib 不同（它们实际上做的是发送和接收消息），电子邮件包提供完整的工具集，用于构建或解码复杂的消息结构（包括附件）以及实现互联网编码和标头协议。

 json 包为解析这种流行的数据交换格式提供了强大的支持。 csv 模块支持以逗号分隔值格式直接读取和写入文件，这种格式通常为数据库和电子表格所支持。 XML 处理由 xml.etree.ElementTree ， xml.dom 和 xml.sax 包支持。这些模块和软件包共同大大简化了 Python 应用程序和其他工具之间的数据交换。

 sqlite3 模块是 SQLite 数据库库的包装器，提供了一个可以使用稍微非标准的 SQL 语法更新和访问的持久数据库。

国际化由许多模块支持，包括 gettext ， locale ，以及 codecs 包。

Python 自带电池,也被称为标准库。它是 Python 非常重要的组成部分,提供了众多常见任务的功能,使得开发者在编写复杂的 Python 程序时能够更加高效地工作。