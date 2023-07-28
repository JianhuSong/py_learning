# 8.错误和异常

主要介绍两种错误：语法错误和异常

## 8.1.语法错误

语法错误又叫解析错误。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def func()
    print("xxxxxxxx")

#   File "D:\coding\py_learning\code\src.py", line 3   # 指明错误发生的文件以及语法错误的行号
#     def func()									   # 指明语法错误的位置
#               ^		
# SyntaxError: expected ':'							   # 什么样的语法错误
```

一般来说使用的编辑器会在编辑的时候就会将错误的地方用红色波浪线标识（vs code），比如说缺少：的这种情况，按下回车后，def func()的下一行都不会自动退格

## 8.2.异常

执行时检测到的错误称为 *异常*

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# print('2' + 2)
# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 3, in <module>  #指明文件名，异常发生行号
#     print('2' + 2)                                               #指明发生异常的代码
# TypeError: can only concatenate str (not "int") to str           #指明异常的类型，以及该异常的提示信息
```



## 8.3.异常的处理

可以编写程序处理选定的异常

try 语句的工作原理如下：

​	* 首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）。

​	* 如果没有触发异常，则跳过 except 子句，try 语句执行完毕。

​	* 如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。 如果异常的类型与 except 关键字后指定的异常相匹配，则会执行 except 子句，

​	   然后跳到try/except 代码块之后继续执行。

​	* 如果发生的异常与 except 子句 中指定的异常不匹配，则它会被传递到外部的 try 语句中；如果没有找到处理程序，则它是一个 未处理异常 且执行将终

​       止并输出如上所示的消息。

try 语句可以**有多个 except 子句** 来为不同的异常指定处理程序。 但**最多只有一个**处理程序会被执行。 处理程序只处理对应的 try 子句 中发生的异常，而不处理同一 try 语句内其他处理程序中的异常。 except 子句 可以用带圆括号的元组来指定多个异常

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    # 可以有多个 except 子句 来为不同的异常指定处理程序
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except (RuntimeError, TypeError, NameError): # except 子句 可以用带圆括号的元组来指定多个异常
        pass
```

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

# 派生类的 except 子句 与基类不兼容
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# 生的异常与 except 子句中的类是同一个类或是它的基类时，则该类与该异常相兼容
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")
```

```python
# 可以在except 中使用as来定义一个变量
# 可以通过直接打印该变量或者通过.arg方式来查看异常的内容。
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
    
```

```python
import sys

# 异常的 __str__（） 输出打印为未经处理的异常的消息的最后一部分（“详细信息”）。
# BaseException 是所有异常的公共基类。它的子类之一 Exception 是所有非致命异常的基类。通常不处理不是异常子类的异常，
# 因为它们用于指示程序应终止。它们包括由sys.exit（）引发的SystemExit和当用户希望中断程序时引发的KeyboardInterrupt。
# 异常可以用作捕获（几乎）所有内容的通配符。但是，最好尽可能具体地说明我们打算处理的异常类型，并允许任何意外异常传播。
# 处理异常的最常见模式是打印或记录异常，然后重新引发异常（允许调用方也处理异常）
# bing翻译
try:
    f = open('test.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

```python
# try ... except 语句具有可选的 else 子句，该子句如果存在，它必须放在所有 except 子句 之后。 
# 它适用于 try 子句 没有引发异常但又必须要执行的代码
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else: # 没有异常发生的时候才会执行这一句
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```



## 8.4.触发异常

```python
try:
    #强制触发异常
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    #在except中再次抛出捕获的异常,直接raise就行
    raise
```



## 8.5.异常链

如果在 except 部分中发生未经处理的异常，则会将正在处理的异常附加到该异常并包含在错误消息中：

```python
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")

# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 5, in <module>
#     open("database.sqlite")
# FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 7, in <module>
#     raise RuntimeError("unable to handle error")
# RuntimeError: unable to handle error
```



为了指示一个异常是另一个异常的直接结果，raise 语句允许一个可选的 from 子句：

```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 8, in <module>
#     func()
#   File "D:\coding\py_learning\code\src.py", line 5, in func
#     raise ConnectionError
# ConnectionError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 10, in <module>
#     raise RuntimeError('Failed to open database') from exc
# RuntimeError: Failed to open database
```

它还允许使用 From None 惯用语禁用自动异常链接：

```python
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 7, in <module>
#     raise RuntimeError from None
# RuntimeError
```

## 8.6.用户自定义异常

程序可以通过创建新的异常类命名自己的异常（Python 类的内容详见 类）。不论是以直接还是间接的方式，异常都应从 Exception 类派生。

```python
class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)

try:
    raise MyException("just test")
except MyException as erro:
    print(erro)

#just test
```

## 8.7.定义清理操作

try 语句还有一个可选子句，用于定义在**所有情况下都必须要执行的**清理操作

如果存在 finally 子句，则 finally 子句是 try 语句结束前执行的最后一项任务。不论 try 语句是否触发异常，都会执行 finally 子句。以下内容介绍了几种比较复杂的触发异常情景：

如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。如果该异常没有 except 子句处理，在 finally 子句执行后会被重新触发。

```python
times = 0
try:
    print("times  = ", times)
    times+=1
    f = open("dasdfsd")
finally:
    print("It is in finally.")
  
# times  =  0
# It is in finally.
# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 8, in <module>
#     f = open("dasdfsd")
# FileNotFoundError: [Errno 2] No such file or directory: 'dasdfsd'
```

except 或 else 子句执行期间也会触发异常。 同样，该异常会在 finally 子句执行之后被重新触发。

```python
try:
    raise OSError("Just test")
except OSError as error:
    print("OSError msg:", error)
    raise SyntaxError("OSError raise.")
finally:
    print("It is in finally.")

# OSError msg: Just test
# It is in finally.
# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 5, in <module>
#     raise OSError("Just test")
# OSError: Just test

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 8, in <module>
#     raise SyntaxError("OSError raise.")
# SyntaxError: OSError raise.
```

如果 finally 子句中包含 break、continue 或 return 等语句，异常将不会被重新引发。

```python
def func():
    try:
        raise OSError("Just test")
    except OSError as error:
        print("OSError msg:", error)
        raise SyntaxError("OSError raise.")
    finally:
        print("It is in finally.")
        return 0

func()
# OSError msg: Just test
# It is in finally.
```

如果执行 try 语句时遇到 break,、continue 或 return 语句，则 finally 子句在执行 break、continue 或 return 语句之前执行。

```python
def func():
    try:
        #raise OSError("Just test")
        print("It is in try")
        
        # 本来执行完这里就应该返回了，这里返回的话就无法执行finally的内容了。
        return 0
    except OSError as error:
        print("OSError msg:", error)
        raise SyntaxError("OSError raise.")
    finally:
        print("It is in finally.")

func()

# It is in try
# It is in finally.
```

如果 finally 子句中包含 return 语句，则返回值来自 finally 子句的某个 return 语句的返回值，而不是来自 try 子句的 return 语句的返回值。

```python
def func():
    try:
        #raise OSError("Just test")
        print("It is in try")
        
        # 本来执行到这里就应该返回了，这里返回的话就无法执行finally的内容了。
        return 0
    except OSError as error:
        print("OSError msg:", error)
        raise SyntaxError("OSError raise.")
    finally:
        print("It is in finally.")
        return 1

print(" func() = ", func())

# It is in try
# It is in finally.
# func() =  1
```



## 8.8.预定义的清理操作

某些对象定义了不需要该对象时要执行的标准清理操作

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

语句执行完毕后，即使在处理行时遇到问题，都会关闭文件 *f*。和文件一样，支持预定义清理操作的对象会在文档中指出这一点。

## 8.9 Raising and Handing Multiple Unrelated Exceptions

英文太长了：

简单意思就是：现在的python3.11可以支持将多个异常弄到一个列表中一起抛出。

```python
ExceptionGroup("error message?",exceptionlist)
```



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

try:
    f()
except Exception as e:
    print(f'caught {type(e)}: {e}')

# caught <class 'ExceptionGroup'>: there were problems (2 sub-exceptions)
```

ExceptionGroup 可以嵌套：嵌套在异常组中的异常必须是实例，而不是类型。这是因为在实践中，异常通常是程序已经引发并捕获的异常.

```python
ExceptionGroup("msg1",[exceptrion1,ExceptionGroup("msg2",[exception2])]) 
```

```python
excs = []
for test in tests:  #例子先敲在这里，多线程目前没学。先跳过了，在多线程的时候再完善
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)
```

想要匹配ExceptionGroup中的某一种异常，就使用except*

(个人理解：这个应该是解包的意思，先把ExceptionGroup解包，然后再匹配)

```python
def f():
    raise ExceptionGroup("group1",
                         [OSError(1),
                          SystemError(2),
                          ExceptionGroup("group2",
                                         [OSError(3), RecursionError(4)])])

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
# There were OSErrors
# There were SystemErrors
#   + Exception Group Traceback (most recent call last):
#   |   File "D:\coding\py_learning\code\src.py", line 11, in <module>
#   |     f()
#   |   File "D:\coding\py_learning\code\src.py", line 4, in f
#   |     raise ExceptionGroup("group1",
#   | ExceptionGroup: group1 (1 sub-exception)
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------
```



## 8.10 Enriching Exceptions with Notes

exception 有一个方法add_note(note)可以让我们为异常添加更多的错误信息（描述）

在异常发生的时候，traceback会把我们添加的所有错误描述按照添加的顺序打印出来。

```python
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

# Traceback (most recent call last):
#   File "D:\coding\py_learning\code\src.py", line 4, in <module>
#     raise TypeError('bad type')
# TypeError: bad type
# Add some information
# Add some more information

```

```python
def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)

#   + Exception Group Traceback (most recent call last):
#   |   File "D:\coding\py_learning\code\src.py", line 14, in <module>
#   |     raise ExceptionGroup('We have some problems', excs)
#   | ExceptionGroup: We have some problems (3 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | Traceback (most recent call last):
#     |   File "D:\coding\py_learning\code\src.py", line 9, in <module>
#     |     f()
#     |   File "D:\coding\py_learning\code\src.py", line 4, in f
#     |     raise OSError('operation failed')
#     | OSError: operation failed
#     | Happened in Iteration 1
#     +---------------- 2 ----------------
#     | Traceback (most recent call last):
#     |   File "D:\coding\py_learning\code\src.py", line 9, in <module>
#     |     f()
#     |   File "D:\coding\py_learning\code\src.py", line 4, in f
#     |     raise OSError('operation failed')
#     | OSError: operation failed
#     | Happened in Iteration 2
#     +---------------- 3 ----------------
#     | Traceback (most recent call last):
#     |   File "D:\coding\py_learning\code\src.py", line 9, in <module>
#     |     f()
#     |   File "D:\coding\py_learning\code\src.py", line 4, in f
#     |     raise OSError('operation failed')
#     | OSError: operation failed
#     | Happened in Iteration 3
#     +-----------------------------------
```

