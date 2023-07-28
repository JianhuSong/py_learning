@[TOC](文章目录)

---

# 前言

主要是了解文件的打开，读取，写入，文件夹的相关内容

# 1.打开文件

​	

```python
open(file,mode = 'r', buffering = -1, encoding = None, errors = None, newline = None, closefd = True, opener = None)
#像关注前两个参数，后面的以后再说
```

open函数的第二个参数就是文件的开模式，如下表

| 打开模式 | 执行操作                                                     |
| -------- | ------------------------------------------------------------ |
| ‘r’      | 以只读的方式打开（默认 ）                                    |
| 'w'      | 以写入的方式打开我呢见，会覆盖已经存在的文件                 |
| 'x'      | 如果文件已经存在，使用此模式打开会引发异常                   |
| 'a'      | 以写入模式打开，如果文件存在，在文件末尾追加写入             |
| 'b'      | 以二进制模式打开文件                                         |
| 't'      | 以文本的方式打开                                             |
| '+'      | 可读可写模式（可添加到其它模式中使用）                       |
| 'U'      | 通用换行符支持（将文本模式下的换行符 `\r\n` 或 `\r` 转换为 `\n`。） |

使用open打开文件后，我们就获取了一个文件对象，文件对象提供了很多方法去对文件进行读取或修改等操作。

| 文件对象的方法       | 执行操作                                                     |
| -------------------- | ------------------------------------------------------------ |
| close()              | 关闭文件                                                     |
| read(size = -1)      | 从文件中读取size个字符，当未给定size或给定负值的时候，读取剩余的所有字符，然后作为字符串返回 |
| readline()/readlines | 一次读取一行/一次读取所有行                                  |
| write(str)           | 将字符串str写入文件                                          |
| writelines(seq)      | 向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象 |
| seek(offset, from)   | 在文件中移动文件指针，从from（0-起始，1-当前，2-末尾）偏移offset个字节 |
| tell()               | 返回当前在文件中的位置                                       |

**注意事项：养成文件使用完毕后就关闭的习惯**

```python
#'r',文件默认以r模式打开
f = open('test.txt')
print(f.read())
f.close()

#用模式w打开的文件，以替换原有内容的方式写入。单纯使用w打开的文件无法读取，想要读取可以w+模式打开
f = open('test.txt', 'w')
#r和w模式不能混用，直接报错
#f = open('test.txt', 'rw')

#w模式的时候，不能读取文件内容，只能往里写
#print(f.read())
f.close()

#用模式x打开已经存在的文件会报错，打开不存在的文件会直接创建一个文件
f = open('test1.txt','x')
#单纯用x模式打开的文件不能读和写
# f.read()
# f.write("xxxxxxxxxxxxxx")
f.close()

#用模式a打开的文件，在写入的时候在文件末尾写入.只以a模式打开的文件，是无法读取的，可以使用a+模式打开
f = open('test.txt','a')
f.close()

#b/t这两个模式不能单独使用，需要指明文件读写模式后才能加上. t以文本的方式打开，b以二进制文件的方式打开
# t：
#     1、读写都是以字符串（Unicode）为单位
#     2、只能针对文本文件
#     3、必须制定字符编码
# b: binary模式
#     1、读写都是以bytes为单位
#     2、可以针对所有文件
#     3、一定不能指定字符串编码
# 总结：
# 1、在操作纯文本文件方面t模式帮我们省去了编码和解码的环节，b模式则需要手动编码和解码
# 2、针对非文本文件（如视频，图片、音频等），只能使用b模式
f = open('test.txt', 'at+')
f.close()

#+模式不能单独使用，需要和别的模式一起使用
f = open('test.txt','r+')
f.close()
f = open('test.txt', 'w+')
f.close()
f = open('test.txt', 'a+')
f.close()

#模式U,不用了。使用的话会提示'U' mode is deprecated
```



# 2.读取文件

```python
# read()
# 少量读取/读取全部/超量读取
f = open('test.txt')
read_200 = f.read(200)
print("read_200.size = ", len(read_200))
print(f.tell())

# 重置文件指针，保证每次的读取都是从文件起始位置开始的
f.seek(0, 0)
read_all = f.read()
print("read_all.size = ", len(read_all))
print(f.tell())
f.seek(0, 0)
read_10000 = f.read(10000)
print("read_10000.size = ", len(read_10000))

# readline()
# 读取一行，并指定读取的字节数
f.seek(0, 0)
readline_10 = f.readline(10)
print("readline_10", len(readline_10))
f.seek(0, 0)
readline_all = f.readline()
print("readline_all", len(readline_all))
f.seek(0, 0)
readline_1000 = f.readline(1000)
print("readline_1000", len(readline_1000))

# readlines()
# readlines()方法可以使用一个可选参数sizehint，它指定要读取的字节数。
# 如果指定了sizehint，则readlines()方法将读取尽可能多的字节，
# 直到读取的字节数达到或超过sizehint(如果到某一行的中间就超了，会完整的读完这一行，然后结束)，然后返回读取的行列表。
f.seek(0, 0)
readlines_all = f.readlines(100)
print("readlines_all", len(readlines_all))

#文件使用完毕一定要记得关闭
f.close()
```



# 3.写入文件

```python
f = open('test.txt','at+')
f.write("askjdflkjasjdfkljasdj\n")
# flush() 是文件对象的一个方法，用于刷新文件缓冲区并将数据立即写入磁盘。
# 在默认情况下，Python 会将数据存储在缓冲区中，并在缓冲区满或关闭文件时将数据写入磁盘。
# 但是，有时候我们需要立即将数据写入磁盘，而不是等待缓冲区满或文件关闭。
# 这时，就可以使用 flush() 方法将缓冲区中的数据写入磁盘。
f.flush()

#writelines()将字符串序列写入文件
#不要被其名字欺骗，字符串序列的所有元素都写入同一行，并不是一个元素一行
f.writelines(['aaa','bbb'])
f.writelines(('cc','dd'))

#文件使用完毕一定要关闭
f.close()
```

python提供了pickle模块方便将列表、字典这类复杂数据存储为文件

pickle写入时都是以二进制的格式写入

```python
mport pickle
my_list = list(range(5))
my_tuple = tuple(range(5, 10))
my_dict = dict.fromkeys(range(5), 'xxxxxx')
my_set = set(x for x in range(7, 11))

with open('my_list.pick', "wb") as list_file:
    pickle.dump(my_list, list_file)

with open('my_tuple.pick', "wb") as tuple_file:
    pickle.dump(my_tuple, tuple_file)

with open('my_dict.pick', "wb") as dict_file:
    pickle.dump(my_dict, dict_file)

with open('my_set.pick', "wb") as set_file:
    pickle.dump(my_set, set_file)

with open('my_list.pick', "rb") as my_list_file:
    print(pickle.load(my_list_file))

with open('my_tuple.pick', "rb") as my_tuple_file:
    print(pickle.load(my_tuple_file))

with open('my_dict.pick', "rb") as my_dict_file:
    print(pickle.load(my_dict_file))

with open('my_set.pick', "rb") as my_set_file:
    print(pickle.load(my_set_file))
```



# 4.文件系统

OS模块，有了OS模块，不需要关心什么操作系统下使用什么模块，OS模块会帮助选择正确的模块并调用

OS模块中关于文件/目录常用的函数

| 函数名                       | 使用方法                                     |
| ---------------------------- | -------------------------------------------- |
| getcwd()                     | 返回当前的工作目录                           |
| chdir()                      | 改变工作目录                                 |
| listdir(path='.')            | 列举指定目录中的文件名                       |
| makedir(path)                | 创建单层目录，目录已经存在就抛异常           |
| makedirs(path)               | 递归创建目录，如果该目录已经存在就抛异常     |
| remove(path)                 | 删除文件                                     |
| rmdir(path)                  | 删除单层目录，如果该目录非空抛异常           |
| removedirs(path)             | 递归删除目录，从子到父，遇到目录非空就抛异常 |
| rename(old, new)             | 将文件old重命名为new                         |
| system(command)              | 运行系统的shell命令                          |
| 以下是路径操作常用的一些操作 |                                              |
| os.curdir                    | 代指当前目录                                 |
| os.pardir                    | 代指上一级目录                               |
| os.sep                       | 输出操作系统中的路径分隔符                   |
| os.linesep                   | 当前系统的行中止符                           |
| os.name                      | 代指当前的操作系统                           |

```python
import os

print(os.getcwd())
print(os.chdir(r"D:\coding\py_learning"))
print(os.getcwd())
print(os.chdir(r"D:\coding\py_learning\code"))
print(os.getcwd())
print(os.listdir())
print(os.listdir(r"D:\coding\py_learning"))
os.mkdir("TEST")
os.rmdir("TEST")
os.makedirs(r'a\b\c')
os.removedirs(r'a\b\c')
open(r"test1.txt", 'x')
os.remove(r'test1.txt')
os.rename(r'test.txt', r'test1.txt')
os.rename(r'test1.txt', r'test.txt')
os.system(r'ls -alh')
print("os.listdir(os.curdir) = ",os.listdir(os.curdir))
print("os.listdir(os.pardir) = ", os.listdir(os.pardir))
print("os.sep = ", os.sep)

#这个输出看不见明显的字符，能看到换行了
print("os.linesep = ", os.linesep)
print("os.name = ", os.name)

#walk(top) 遍历top下的所有字母，并将结果返回一个三元组(路径,[包含目录],[包含文件])
for each in os.walk(r'D:\coding\py_learning'):
    print(each)
```

​	

还有一个强大的模块os.path 可以完成一些针对路径名的操作

| 函数名                     | 使用方法                                                     |
| -------------------------- | ------------------------------------------------------------ |
| basename(path)             | 去掉目录路径，返回文件名                                     |
| dirname(path)              | 去掉文件名，返回目录路径                                     |
| join(path1[, path2[,...]]) | 将path1和path2各部分组合成一个路径名                         |
| split(path)                | 分割文件名与路径名，返回（f_path, f_name）元组。如果完全使用目录，他也会将最后一个目录作为文件名分离 |
| splitext(path)             | 分离文件名与扩展名，返回（f_name, f_extension）              |
| getsize(file)              | 返回指定文件的尺寸，单位是字节                               |
| getatime(file)             | 返回指定文件最近的访问时间（浮点的秒数，可用time模块的gmtime()或localtime函数换算） |
| getctime(file)             | 返回指定文件的创建时间（浮点的秒数，可用time模块的gmtime()或localtime函数换算） |
| getmtime(file)             | 返回指定文件的最新的修改时间（浮点的秒数，可用time模块的gmtime()或localtime函数换算） |
| 以下函数返回True或False    |                                                              |
| exists(file)               | 判断指定的文件/目录是否存在                                  |
| isabs(path)                | 判断指定路径是否为绝对路径                                   |
| isdir(path)                | 判断指定路径是否存在且是一个目录                             |
| isfile(path)               | 判断指定路径是否存在且是一个文件                             |
| islink(path)               | 判断指定路径是否存在且是一个符号链接                         |
| ismount(path)              | 判断指定路径是否存在且是一个挂载点                           |
| samefile(path1, path2)     | 判断path1和path2是否指向同一个文件                           |

```python
import os
import time
print(os.path.basename(r'D:\coding\py_learning\code\test.txt'))
print(os.path.dirname(r'D:\coding\py_learning\code\test.txt'))

#这个join有点好玩
print(os.path.join(r'D:\coding\py_learning', r'code\test.txt'))
print(os.path.join(r'D:\coding\py_learning\text.txt', r'code\test.txt'))
print(os.path.join(r'D:\coding\py_learning', r'D:\code\test.txt'))
print(os.path.join(r'\coding\py_learning', r'd:\code\test.txt'))

print(os.path.split(r'D:\coding\py_learning\code\test.txt'))
print(os.path.splitext(r'D:\coding\py_learning\code\test.txt'))
print(os.path.splitext(r'D:\coding\py_learning\code\test.txt.exe'))
print(os.path.getsize(r'D:\coding\py_learning\code\test.py'))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getatime(r'D:\coding\py_learning\code\test.py'))))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(r'D:\coding\py_learning\code\test.py'))))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(r'D:\coding\py_learning\code\test.py'))))

my_dir = r"D:\coding\py_learning\code"
my_file = r"test.py"

if os.path.exists(my_file):
    print("file exists:", my_file)
if os.path.isabs(my_dir):
    print("path is abs:", my_dir)
if os.path.isdir(my_dir):
    print("path is dir:", my_dir)
if os.path.isfile(my_file):
    print(my_file, "is file")
if not os.path.islink(my_file):
    print(my_file, "is not a link.")
if not os.path.ismount(my_dir):
    print(my_dir, "is not a mount.")
if os.path.samefile(os.path.join(my_dir, my_file), my_file):
    print(os.path.join(my_dir, my_file), " and ", my_file, "is same.")
```

