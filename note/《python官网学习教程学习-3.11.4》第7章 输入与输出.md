# 7.输入与输出

数据既可以输出供人阅读的形式

## 7.1. 更复杂的输出格式

三种写入值的方法：

表达式语句和print()函数，文件对象的write方法

标准输出文件为sys.stdout

格式化输出包括以下几种方式：

1.使用格式化字符串字面值，要在字符串的引号/三引号前加f/F。在{}中间输入引用的变量，或字面值的Python表达式

```python
str1 = 'Hello'
str2 = 'world!!!'
print(f"{str1} {str1}")

int1 = 1234
float1 = 11.22222
print(f"{int1}-----{float1:2.3f}")
```

2.字符串的str.format()

```python
int1 = 1234
float1 = 11.22222
print("{}.....---{:3.4f}".format(int1, float1))
```

3.还可以用字符串的切片和合并操作完成字符串处理操作，创建任何排版布局。

```python
str1="Helloworld"
str1 = str1[:5] + " " + str1[5:]
print(str1)
```

### 7.1.1. 格式化字符串字面值

格式化字符串字面值 （简称为 f-字符串）在字符串前加前缀 f 或 F，通过 {expression} 表达式，把 Python 表达式的值添加到字符串内。

格式说明符是可选的，写在表达式后面，可以更好地控制格式化值的方式

| 修饰符名称 | 作用       |
| ---------- | ---------- |
| !a         | 应用ASCII  |
| !s         | 应用str()  |
| !r         | 应用repr() |

```python
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
    
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

str1 = 'a'
print(F'a = {str1!a}')
```

### 7.1.2. 字符串format()方法

花括号及之内的字符（称为格式字段）被替换为传递给 str.format() 方法的对象。花括号中的数字表示传递给 str.format() 方法的对象所在的位置。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用位置参数
print("{} {}".format("Hello","world"))
print("{0} {1}".format("Hello","world"))

# str.format() 方法中使用关键字参数名引用值。
print("{hello} {world}".format(hello = "Hello",world = "world"))

# 位置参数和关键字参数可以任意组合
print("{} {world}".format("Hello",world = "world"))

# SyntaxError: positional argument follows keyword argument 位置参数不能在关键字参数之后
#print("{hello} {}".format(hello = "Hello","world"))

# 不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; '
      'Dcab: {Dcab:d}'.format(**table))
```

### 7.1.3. 手动格式化字符串

每列之间的空格是通过使用 print() 添加的：它总在其参数间添加空格。

字符串对象的 str.rjust() 方法通过在左侧填充空格，对给定宽度字段中的字符串进行右对齐。同类方法还有 str.ljust() 和 str.center() 

 str.zfill() ，该方法在数字字符串左边填充零，且能识别正负号

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
for x in range(1, 11):
    print(repr(x).zfill(2), repr(x*x).zfill(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).zfill(4))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
```

### 7.1.4. 旧式字符串格式化方法

% 运算符（求余符）也可用于字符串格式化。给定 'string' % values，则 string 中的 % 实例会以零个或多个 values 元素替换。此操作被称为字符串插值

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("hello %s" %"world")
print("%s %s" % ("hello", "world"))

my_list = ["hello","world"]
#这样是不行的，cannot use starred expression here
#print("%s %s" %(*my_list))
```

## 7.2 读写文件

open() 返回一个 file object ，最常使用的是两个位置参数和一个关键字参数：open(filename, mode, encoding=None)

第一个实参是文件名字符串。第二个实参是包含描述文件使用方式字符的字符串。

mode 的值包括：

​	 'r' ，表示文件只能读取；

​	'w' 表示只能写入（现有同名文件会被覆盖）；

​	'a' 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。

​	'r+' 表示打开文件进行读写。

mode 实参是可选的，省略时的默认值为 'r'。

通常情况下，文件是以 text mode 打开的，也就是说，你从文件中读写字符串，这些字符串是以特定的 encoding 编码的。如果没有指定 encoding ，默认的是与平台有关的（见 open() ）

除非你知道你需要使用一个不同的编码，否则建议使用 encoding="utf-8" 

在二进制模式下打开文件时，你不能指定 *encoding* 

在文本模式下读取文件时，默认把平台特定的行结束符（Unix 上为 `\n`, Windows 上为 `\r\n`）转换为 `\n`。在文本模式下写入数据时，默认把 `\n` 转换回平台特定结束符。这种操作方式在后台修改文件数据对文本文件来说没有问题，但会破坏 `JPEG` 或 `EXE` 等二进制文件中的数据。注意，在读写此类文件时，一定要使用二进制模式。

在处理文件对象时，最好使用 with 关键字

### 7.2.1.文件对象的方法

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
    
# 在处理文件对象时，最好使用 with 关键字。优点是，子句体结束后，文件会正确关闭，即便触发异常也可以
with open("./test.txt", "a+", encoding='utf-8') as f:
    
    # f.read(size) 可用于读取文件内容，它会读取一些数据，并返回字符串（文本模式），或字节串对象（在二进制模式下）。 
    # size 是可选的数值参数。省略 size 或 size 为负数时，读取并返回整个文件的内容；文件大小是内存的两倍时，会出现问题。
    # size 取其他值时，读取并返回最多 size 个字符（文本模式）或 size 个字节（二进制模式）。如已到达文件末尾，f.read() 返回空字符串（''）。
    print(f.read())
    f.seek(0,0)
    
    # f.readline() 从文件中读取单行数据；字符串末尾保留换行符（\n），只有在文件不以换行符结尾时，文件的最后一行才会省略换行符。
    # 这种方式让返回值清晰明确；只要 f.readline() 返回空字符串，就表示已经到达了文件末尾，空行使用 '\n' 表示，该字符串只包含一个换行符。
    print(f.readline())
    f.seek(0,0)
    
    # 从文件中读取多行时，可以用循环遍历整个文件对象。这种操作能高效利用内存，快速，且代码简单：
    for line in f:
        print(line)
    f.seek(0,0)
    
    # 如需以列表形式读取文件中的所有行，可以用 list(f) 或 f.readlines()。
    print(list(f))
    f.seek(0,0)
    print(f.readlines())
    f.seek(0,0)
    
    # f.write(string) 把 string 的内容写入文件，并返回写入的字符数。
    print(f.write("This is a test\n"))
    f.seek(0)
    # f.tell() 返回整数，给出文件对象在文件中的当前位置，表示为二进制模式下时从文件开始的字节数，以及文本模式下的意义不明的数字。
    print(f.tell())
    
    # f.seek(offset, whence) 可以改变文件对象的位置。通过向参考点添加 offset 计算位置；参考点由 whence 参数指定。 
    # whence 值为 0 时，表示从文件开头计算，1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。
    # 省略 whence 时，其默认值为 0，即使用文件开头作为参考点。
    print(f.readline())
    print(f.tell())
    f.seek(0,1)
    print(f.tell())
    f.seek(0,2)
    print(f.tell())
    f.seek(0,0)
    print(f.tell())
    # 在文本文件（模式字符串未使用 b 时打开的文件）中，只允许相对于文件开头搜索（使用 seek(0, 2) 搜索到文件末尾是个例外），
    # 唯一有效的 offset 值是能从 f.tell() 中返回的，或 0。其他 offset 值都会产生未定义的行为。
```

### 7.2.2.使用json保存结构化数据

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

# 将对象序列化为 text file
x = [1,"simple","list"]
with open('test.txt', 'w+', encoding="utf-8") as f:
    json.dump(x,f)

# 解码对象，如果 f 是已打开、供读取的 binary file 或 text file 对象
with open('test.txt', 'r', encoding="utf-8") as f:
    x1 = json.load(f)
    print(x1)    

# 查看某个对象的 JSON 字符串表现形式
json_str = json.dumps(x)

# 从JSON字符串中解码出对象
x2 = json.loads(json_str)
print(x2)
```

