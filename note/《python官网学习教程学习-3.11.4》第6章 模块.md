# 6. 模块

python 把各种定义存入一个文件，在脚本或解释器的交互实例中使用，这个文件就是模块

模块是包含Python 定义和语句的文件。在模块内部可以通过\__name__获取模块的名字

## 6.1. 模块详解

模块包含可执行语句及函数定义。这些语句用于初始化模块，且仅在 import 语句 *第一次* 遇到模块名时执行。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 几种模块的导入方式

# import 模块名 [as newname]
# import fibo
# import fibo as fib

# from 模块名 import 函数/类/... [as newname]
# from fibo import fib, fib2
# from fibo import *   
# from fibo import fib as fibonacci
```

### 6.1.1. 以脚本的方式运行模块

解析命令行的代码只有在模块以“main”文件执行时才运行

```python
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

### 6.1.2 . 模块的搜索路径

当一个名为 spam 的模块被导入时，解释器首先搜索具有该名称的内置模块。这些模块的名字被列在 sys.builtin_module_names 中。如果没有找到，它就在变量 sys.path 给出的目录列表中搜索一个名为 spam.py 的文件， sys.path 从这些位置初始化:

输入脚本的目录

PYTHONPATH（目录列表，与shell变量PATH的语法一样）

依赖于安装的默认值（按照惯例包括一个site-packages目录，有site模块处理）



### 6.1.3. “已编译的”Python文件

为了快速加载模块，python把模块的编译版缓存在\_pycache_目录中，文件名为module.version.pyc,version对编译文件的格式进行编码，一般是python的版本号。

编译模块与平台无关

## 6.2. 标准模块

Python 自带一个标准模块的库，它在 Python 库参考（此处以下称为"库参考" ）里另外描述。 一些模块是内嵌到编译器里面的， 它们给一些虽并非语言核心但却内嵌的操作提供接口，要么是为了效率，要么是给操作系统基础操作例如系统调入提供接口。 这些模块集是一个配置选项， 并且还依赖于底层的操作系统。 例如，winreg 模块只在 Windows 系统上提供。一个特别值得注意的模块 sys，它被内嵌到每一个 Python 编译器中。sys.ps1 和 sys.ps2 变量定义了一些字符，它们可以用作主提示符和辅助提示符:

只有解释器用于交互模式时，才定义两个变量

sys.path是字符串列表，用于确定解释器的模块搜索路径

## 6.3. dir()函数

内置函数 dir()用于查找模块定义的名称。返回结果是经过排序的字符串列表

没有参数时，dir() 列出当前定义的名称

dir()不会列出内置函数和变量的名称

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fibo

a = [1, 2, 3, 4, 5]
fib = fibo.fib
print(f"dir(fibo) = {dir(fibo)}")
print(f"dir() = {dir()}")
# dir(fibo) = ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
# dir() = ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'fib', 'fibo']
```

## 6.4. 包

包是一种用“点式模块名”构造 Python 模块命名空间的方法

导入包时，Python 搜索 sys.path 里的目录，查找包的子目录。

### 6.4.1. 从包中导入*

记住，使用 `from package import specific_submodule` 没有任何问题！ 实际上，除了导入模块使用不同包的同名子模块之外，这种方式是推荐用法。

### 6.4.2. 子包参考

包中含有多个子包时（与示例中的 `sound` 包一样），可以使用绝对导入引用兄弟包中的子模块

可以用 `from sound.effects import echo` 导入。

还可以用 import 语句的 `from module import name` 形式执行相对导入

### 6.4.3. 多目录中的包

这个功能虽然不常用，但可用于扩展包中的模块集。

