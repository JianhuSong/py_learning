# 11. 标准库简介 —— 第二部分

第二部分涵盖了专业编程所需要的更高级的模块

## 11.1. 格式化输出

reprlib模块提供了一个定制化版本的rper()函数，用于缩略显示大型或嵌套的容器对象

```python
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))
```

pprint模块提供了更加复杂的打印控制，其输出的内置对象和用户定义能够被解释器直接读取。当输出结果过长时，会添加换行符和缩进。

```python
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t,width=20)
```

textwrap模块能够格式化文本段落，以适应给定的屏幕宽度

```python
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=20))
```

locale模块处理于特定地域文化相关的数据格式。locale模块的format函数包含了一个grouping属性，可以直接将数字格式化为带组分隔符的格式

```python
import locale
print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.89

# locale.format()会有提示
# This method will be removed in a future version of Python. Use 'locale.format_string()' instead.
# locale.format("%d", x, grouping=True)
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True))
```

## 11.2. 模板

string模块包含一个通用的Template类，具有适用最终用户的简化语法。它允许用户在不更改应用逻辑的情况下定制自己的应用。

格式化操作通过占位符实现，占位符：$Python标识符， python标识符只能包含字母、数字和下划线。$$被转义成$

```python
from string import Template
t = Template('${asdjfalsd}flok send $$10 to $case')
print(t.substitute(asdjfalsd="asdaasd", case = 'xxxxxxx'))
```

如果字典或关键字参数没有提供某个占位符的值，substitute抛出KeyError。可以使用safe_subsitute(),没有提供占位符的值时原样保留。

```python
from string import Template
t = Template('${asdjfalsd}flok send $$10 to $case, $xxxxxx')
print(t.safe_substitute(asdjfalsd="asdaasd", case = 'xxxxxxx'))

dict1 = {'asdjfalsd':'asdjfalsd','case':'case','xxxxxx':'xxxxxx'}
print(t.safe_substitute(dict1))
```

Template的子类可以自定义分隔符

```python
import time, os.path
from string import Template
photofiles = ['hello.jpg','world.jpg']
class BatchRename(Template):
    delimiter = "%"
fmt = '%d-%n%f)'
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d = date, n=i, f=ext)
    print('{} --> {}'.format(filename, newname))
```

## 11.3. 使用二进制的数据记录格式

struct模块提供了pack()和unpack()函数，用于处理不定长度的二进制记录格式。

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```



## 11.4. 多线程 

```python
# 以下代码展示了高阶的 threading 模块如何在后台运行任务，且不影响主程序的继续运行:
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('test.txt', 'myfile.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

## 11.5. 日志记录

```python
# logging 模块提供功能齐全且灵活的日志记录系统。在最简单的情况下，日志消息被发送到文件或 sys.stderr
import logging
# 将日志记录到文件中
logging.basicConfig(filename='test.txt',format="%(asctime)s|%(levelname)s|%(filename)s|%(message)s", datefmt="%Y-%m-%d %H-%M-%S")
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
# 默认情况下，informational 和 debugging 消息被压制，输出会发送到标准错误流。其他输出选项包括将消息转发到电子邮件，数据报，套接字或 HTTP 服务器。
# 新的过滤器可以根据消息优先级选择不同的路由方式：DEBUG，INFO，WARNING，ERROR，和 CRITICAL。
# 日志系统可以直接从 Python 配置，也可以从用户配置文件加载，以便自定义日志记录而无需更改应用程序。
```

## 11.6. 弱引用

Python中的弱引用是一种特殊类型的引用，它不会增加对象的引用计数，也不会阻止对象被垃圾回收器回收。

Python 会自动进行内存管理（对大多数对象进行引用计数并使用 garbage collection 来清除循环引用）。 当某个对象的最后一个引用被移除后不久就会释放其所占用的内存。

此方式对大多数应用来说都适用，但偶尔也必须在对象持续被其他对象所使用时跟踪它们。 不幸的是，跟踪它们将创建一个会令其永久化的引用。 weakref 模块提供的工具可以不必创建引用就能跟踪对象。 当对象不再需要时，它将自动从一个弱引用表中被移除，并为弱引用对象触发一个回调。 典型应用包括对创建开销较大的对象进行缓存:

```python
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
print(d['primary'])         # fetch the object if it is still alive
del a                       # remove the one reference
print(gc.collect()  )       # run garbage collection right away
print(d['primary']) 
```

## 11.7. 用于操作列表的工具

许多对于数据结构的需求可以通过内置列表类型来满足。 但是，有时也会需要具有不同效费比的替代实现。

```python
# array 模块提供了一种 array() 对象，它类似于列表，但只能存储类型一致的数据且存储密集更高。 
# 下面的例子演示了一个以两个字节为存储单元的无符号二进制数值的数组 (类型码为 "H")，而对于普通列表来说，
# 每个条目存储为标准 Python 的 int 对象通常要占用16 个字节:

from array import array
# H unsigned short
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])
```

```python
# collections 模块提供了一种 deque() 对象，它类似于列表，但从左端添加和弹出的速度较快，
# 而在中间查找的速度较慢。 此种对象适用于实现队列和广度优先树搜索:
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
```

```python
#  bisect 模块具有用于操作有序列表的函数:
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(data)
heapify(data)                             # rearrange the list into heap order
heappush(data, -5)                        # add a new entry
print(data)
print([heappop(data) for i in range(3)])  # fetch the three smallest entries
```

## 11.8. 十进制浮点运算

```python
# decimal 模块提供了一种 Decimal 数据类型用于十进制浮点运算。 相比内置的 float 二进制浮点实现，该类特别适用于
#   财务应用和其他需要精确十进制表示的用途，
#   控制精度，
#   控制四舍五入以满足法律或监管要求，
#   跟踪有效小数位，或
#   用户期望结果与手工完成的计算相匹配的应用程序。

# 使用十进制浮点和二进制浮点数计算70美分手机和5％税的总费用，会产生的不同结果。如果结果四舍五入到最接近的分数差异会更大:
from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))


# Decimal 表示的结果会保留尾部的零，并根据具有两个有效位的被乘数自动推出四个有效位。 
# Decimal 可以模拟手工运算来避免当二进制浮点数无法精确表示十进制数时会导致的问题。
# 精确表示特性使得 Decimal 类能够执行对于二进制浮点数来说不适用的模运算和相等性检测:
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)
print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10) == 1.0)

# decimal 模块提供了运算所需要的足够精度:
getcontext().prec = 36
print(Decimal(1) / Decimal(7))
```