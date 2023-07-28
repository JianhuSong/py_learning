# 9.类

类把数据与功能绑定在一起。创建新的类就是创建新的对象类型，从而创建该类型的新实例。类实例支持维持自身状态的属性，还支持（由类定义）修改自身状态的方法。

## 9.1.名称和对象

对象之间相互独立，多个名称（在多个作用域内 ）可以绑定到同一个对象。

## 9.2. Python 作用域和命名空间 

namespace(命名空间)是映射到对象的名称。

大多数命名空间都使用python字典实现，但除非涉及到优化性能，一般不关注。以后可能改变方式。

常见的几种命名空间：

​	abs()函数、内置异常等的内置函数集合；

​	模块中的全局名称

​	函数调用中的局部名称

​	对象的属性集合也算是一种命名空间

不同命名空间中的名称之间绝对没有关系

命名空间在不同时刻创建的，且拥有不同的声明周期：

​	内置名称的命名空间是在Python解释器启动的时候创建的，永远不会被删除。

​	模块的全局命名空间在读取模块定义时创建，通常持续到解释器退出

​	函数的本地命名空间在调用该函数的时候创建，并在函数返回或者抛出不在函数内部处理的错误时被删除。

作用域是命名空间可直接访问的Python程序的文本区域。“可直接访问”的意思是，对名称的非限定引用会在命名空间中查找名称。

作用域虽然是静态确定的，但会被动态使用。执行期间的任何时刻，都会有3或4个命名空间可被直接访问的嵌套作用域：

​	最内层作用域，包含局部名称，并首先在其中搜索。

​	the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names

​	倒数第二个作用域，包含当前模块的全局名称

​	最外层的作用域，包含内置名称的命名空间，最后搜索。

通常，当前局部作用域将（按字面文本）引用当前函数的局部名称。在函数之外，局部作用域引用与全局作用域一致的命名空间：模块的命名空间。 类定义在局部命名空间内再放置另一个命名空间。

划重点，作用域是按字面文本确定的：模块内定义的函数的全局作用域就是该模块的命名空间，无论该函数从什么地方或以什么别名被调用。另一方面，实际的名称搜索是在运行时动态完成的。但是，Python 正在朝着“编译时静态名称解析”的方向发展，因此不要过于依赖动态名称解析！（局部变量已经是被静态确定了。）

Python 有一个特殊规定。如果不存在生效的 global 或 nonlocal 语句，则对名称的赋值总是会进入最内层作用域。赋值不会复制数据，只是将名称绑定到对象。删除也是如此：语句 del x 从局部作用域引用的命名空间中移除对 x 的绑定。所有引入新名称的操作都是使用局部作用域：尤其是 import 语句和函数定义会在局部作用域中绑定模块或函数名称。

global 语句用于表明特定变量在全局作用域里，并应在全局作用域中重新绑定；nonlocal 语句表明特定变量在外层作用域中，并应在外层作用域中重新绑定

### 9.2.1.作用域和命名空间示例

nonlocal 和global 的声明出现在内层空间的第一次使用之前

```python
# 在没有使用nonlocal 情况下在内嵌函数中修改函数中变量的值不会生效
def scope_test():
    def do_local():
        spam = "local spam"
    spam = "test"
    print("Before do_local, spam = ", spam)
    do_local()
    print("After do_local, spam = ", spam)

scope_test()
```

```python
# nonlocal的用法
# 用于在内嵌函数中修改外部函数的变量值
# 官方说法：nonlocal 语句表明特定变量在外层作用域中，并应在外层作用域中重新绑定。
def scope_test():
    def do_local():
        nonlocal spam
        spam = "local spam"
    
    spam = "test"
    print("Before do_loacal(), spam = ", spam)
    do_local()
    print("After do_loacal(), spam = ", spam)

scope_test()
```

```python
# global的用法

# 在函数中修改外部命名空间中的变量
# 在全局空间中使用函数内部定义的变量
def scope_test():
   
    def do_without_global():
        spam1 = "global spam1"


    def do_global():
        global spam
        spam = "global spam"
    def do_local():
        # nonlocal 无法让内嵌函数的变量在外层函数中使用
        # nonlocal spam4
        # spam4 = "define in do_local"
        pass
        
       
    do_global()
    do_without_global()
    do_local()
    global spam2
    spam2 = "define in function."
    # print("after do_local spam4 = ", spam4)
    
spam = "test spam"
spam1 = "test spam1"

print("In global scope spam:", spam)
print("In global scope spam1:", spam1)

# 在函数调用前不能使用 spam2, 函数的命名空间在函数调用时创建
# print("In global scope spam2:", spam2)
scope_test()
print("After spam ", spam)
print("After spam1:", spam1)
print("After spam2:", spam2)
```

## 9.3.初探类

### 9.3.1.类定义语法

最简单的类定义的形式如下：

```
lass ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

与函数定义(def语句)一样，类定义必须先执行才能生效。

在实践中，类定义内的语句通常都是函数定义，但也可以是其他语句

类里的函数定义一般是特殊的参数列表，这是由方法调用的约定规范所指明的

当进入类定义时，将创建一个新的命名空间，并将其用作局部作用域 --- 因此，所有对局部变量的赋值都是在这个新命名空间之内。 特别的，函数定义会绑定到这里的新函数名称。

当（从结尾处）正常离开类定义时，将创建一个 *类对象*。 这基本上是一个包围在类定义所创建命名空间内容周围的包装器；

原始的（在进入类定义之前起作用的）局部作用域将重新生效，类对象将在这里被绑定到类定义头所给出的类名称 (在这个示例中为 `ClassName`)。

### 9.3.2.Class对象

类对象支持两种操作：属性引用和实例化。

*属性引用* 使用 Python 中所有属性引用所使用的标准语法: `obj.name`。 有效的属性名称是类对象被创建时存在于类命名空间中的所有名称。

```python
class MyCLass:
    i = 1234
    def func(self):
        print("hello world")

#属性引用：
print(MyCLass.i)

# 返回一个函数对象
MyCLass.func
```

类的 *实例化* 使用函数表示法。 可以把类对象视为是返回该类的一个新实例的不带参数的函数

实例化操作（“调用”类对象）会创建一个空对象。 许多类喜欢创建带有特定初始状态的自定义实例。 为此类定义可能包含一个名为 `__init__()` 的特殊方法

当类定义了`__init__()`时，类实例化会自动为新创建的类实例调用`__init__()`

当然，`__init__()` 方法还可以有额外参数以实现更高灵活性。 在这种情况下，提供给类实例化运算符的参数将被传递给 `__init__()`

```python
class MyCLass:
    def __init__(self,*arg):
        print("__init__ len(arg) = ", len(arg))
        self.data = list(arg)
    def func(self):
        print(self.data)

x = MyCLass(*[1,2,3,4,5])
x.func()
```

### 9.3.3.实例对象

实例对象所能理解的唯一操作是属性引用。 有两种有效的属性名称：数据属性和方法。

 数据属性不需要声明；像局部变量一样，它们将在第一次被赋值时产生。

另一类实例属性引用称为 *方法*。 方法是“从属于”对象的函数。

实例对象的有效方法名称依赖于其所属的类

### 9.3.4.方法对象

方法在绑定后立即被调用:

方法对象可以被保存起来以后再调用

方法的特殊之处就在于实例对象会作为函数的第一个参数被传入

当一个实例的非数据属性被引用时，将搜索实例所属的类。 如果被引用的属性名称表示一个有效的类属性中的函数对象，会通过打包（指向）查找到的实例对象和函数对象到一个抽象对象的方式来创建方法对象：这个抽象对象就是方法对象。 当附带参数列表调用方法对象时，将基于实例对象和参数列表构建一个新的参数列表，并使用这个新参数列表调用相应的函数对象。

### 9.3.5.类和实例变量

一般来说，实例变量用于每个实例的唯一数据，而类变量用于类的所有实例共享的属性和方法

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)                  # shared by all dogs
print(e.kind)                  # shared by all dogs
print(d.name)                  # unique to d
print(e.name) 

```

正如 名称和对象 中已讨论过的，共享数据可能在涉及 mutable 对象例如列表和字典的时候导致令人惊讶的结果。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Dog:
    
    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs
```

正确的类设计应该使用实例变量

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print("d.tricks = ", d.tricks)
print("e.tricks = ", e.tricks)
```

## 9.4.补充说明

如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例

```python
class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

# storage west
# storage east
```

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class A:
    a = 1234
def fun(a):
    print(a.test)
a = A()
b = A()
#可以在类外为实例对象定义一个独属于实例对象的数据属性？？？
a.test = 11
print(a.test)
fun(a)
#fun(b) #这样不行要报错 'A' object has no attribute 'test'
# 11
# 11

```

据属性可以被方法以及一个对象的普通用户（“客户端”）所引用。 换句话说，类不能用于实现纯抽象数据类型。 实际上，在 Python 中没有任何东西能强制隐藏数据 --- 它是完全基于约定的。而在另一方面，用 C 语言编写的 Python 实现则可以完全隐藏实现细节，并在必要时控制对象的访问；此特性可以通过用 C 编写 Python 扩展来使用。）

客户端应当谨慎地使用数据属性 --- 客户端可能通过直接操作数据属性的方式破坏由方法所维护的固定变量。 请注意客户端可以向一个实例对象添加他们自己的数据属性而不会影响方法的可用性，只要保证避免名称冲突 --- 再次提醒，在此使用命名约定可以省去许多令人头痛的麻烦。

方法的第一个参数常常被命名为 `self`。 这也不过就是一个约定: `self` 这一名称在 Python 中绝对没有特殊含义。 但是要注意，不遵循此约定会使得你的代码对其他 Python 程序员来说缺乏可读性，而且也可以想像一个 *类浏览器* 程序的编写可能会依赖于这样的约定。

任何一个作为类属性的函数都为该类的实例定义了一个相应方法。 函数定义的文本并非必须包含于类定义之内：将一个函数对象赋值给一个局部变量也是可以的

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'
```

方法可以通过与普通函数相同的方式引用全局名称。 与方法相关联的全局作用域就是包含其定义的模块。 （类永远不会被作为全局作用域。） 虽然我们很少会有充分的理由在方法中使用全局作用域，但全局作用域存在许多合理的使用场景：举个例子，导入到全局作用域的函数和模块可以被方法所使用，在其中定义的函数和类也一样。 通常，包含该方法的类本身是在全局作用域中定义的，而在下一节中我们将会发现为何方法需要引用其所属类的很好的理由。

每个值都是一个对象，因此具有 *类* （也称为 *类型*），并存储为 `object.__class__` 。

## 9.5.继承

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

名称 `BaseClassName` 必须定义于包含派生类定义的作用域中。 也允许用其他任意表达式代替基类名称所在的位置。

```python
class DerivedClassName(modname.BaseClassName):
```

当构造类对象时，基类会被记住。 此信息将被用来解析属性引用：如果请求的属性在类中找不到，搜索将转往基类中进行查找。 如果基类本身也派生自其他某个类，则此规则将被递归地应用。

派生类的实例化没有任何特殊之处: `DerivedClassName()` 会创建该类的一个新实例。 方法引用将按以下方式解析：搜索相应的类属性，如有必要将按基类继承链逐步向下查找，如果产生了一个函数对象则方法引用就生效

派生类可能会重写其基类的方法。 因为方法在调用同一对象的其他方法时没有特殊权限，所以调用同一基类中定义的另一方法的基类方法最终可能会调用覆盖它的派生类的方法。

在派生类中的重载方法实际上可能想要扩展而非简单地替换同名的基类方法。 有一种方式可以简单地直接调用基类方法：即调用 `BaseClassName.methodname(self, arguments)`。 有时这对客户端来说也是有用的。 （请注意仅当此基类可在全局作用域中以 `BaseClassName` 的名称被访问时方可使用此方式。）

Python有两个内置函数可被用于继承机制：

​		使用 isinstance() 来检查一个实例的类型: isinstance(obj, int) 仅会在 obj.__class__ 为 int 或某个派生自 int 的类时为 True。

​		使用 issubclass() 来检查类的继承关系: issubclass(bool, int) 为 True，因为 bool 是 int 的子类。 但是，issubclass(float, int) 为 False，

​		因为 float 不是 int 的子类。

### 9.5.1. 多重继承

Python 也支持一种多重继承。 带有多个基类的类定义语句如下所示:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

对于多数应用来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左至右的，当层次结构中存在重叠时不会在同一个类中搜索两次。 因此，如果某一属性在 `DerivedClassName` 中未找到，则会到 `Base1` 中搜索它，然后（递归地）到 `Base1` 的基类中搜索，如果在那里未找到，再到 `Base2` 中搜索，依此类推。

真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 [`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 的协同调用。 这种方式在某些其他多重继承型语言中被称为后续方法调用，它比单继承型语言中的 super 调用更强大。

## 9.6.私有变量

**那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在**。

大多数 Python 代码都遵循这样一个约定：带有一个下划线的名称 (例如 `_spam`) 应该被当作是 API 的非公有部分 (无论它是函数、方法或是数据成员)。 这应当被视为一个实现细节，可能不经通知即加以改变。

由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种机制的有限支持，称为 *名称改写*。 任何形式为 `__spam` 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 `_classname__spam`，其中 `classname` 为去除了前缀下划线的当前类名称。 这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。

名称改写有助于让子类重载方法而不破坏类内方法调用

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```



## 9.7.杂项说明

有时，拥有类似于 Pascal “record” 或 C“struct” 的数据类型很有用，将几个命名数据项捆绑在一起。惯用方法是为此目的使用数据类：

一段需要特定抽象数据类型的 Python 代码往往可以被传入一个模拟了该数据类型的方法的类作为替代

```python
from dataclasses import dataclass

@dataclass   #这是一个装饰器，这个东西目前没有学，知道个名字就行
class Employee:
    name: str
    dept: str
    salary: int
```

## 9.8.迭代器

 迭代器的使用非常普遍并使得 Python 成为一个统一的整体

```python
# 迭代器的使用非常普遍并使得 Python 成为一个统一的整体。 在幕后，for 语句会在容器对象上调用 iter()。 
# 该函数返回一个定义了 __next__() 方法的迭代器对象，此方法将逐一访问容器中的元素。 
# 当元素用尽时，__next__() 将引发 StopIteration 异常来通知终止 for 循环。 你可以使用 next() 内置函数来调用 __next__() 方法
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    # 定义一个__iter__（）方法来返回一个带有__next__()方法的对象，如果已经定义了__next__()可以简单返回self
    def __iter__(self):
        return self

    # 当元素用尽时，引发StopIteration,没有用尽那就返回下一个元素
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char)
```

```python
class Myclass:
    def __init__(self, *arg):
        self.data = list(arg)
        self.index = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.data):
            # 重置index,方便以后的循环
            self.index = 0;
         
            # 抛出StopIteration，结束循环
            raise StopIteration
        
        tmp = self.data[self.index]
        self.index += 1
        return tmp

# 不加* "hello"被当作一个整体加入到self.data中作为一个元素。       
my_class = Myclass(*"hello")
for char in my_class:
    print(char)
    
# h
# e
# l
# l
# o
```

## 9.9.生成器

生成器 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似于标准的函数，但当它们要返回数据时会使用 yield 语句。 每次在生成器上调用 next() 时，它会从上次离开的位置恢复执行（它会记住上次执行语句时的所有数据值）

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
```

它会自动创建 `__iter__()` 和 `__next__()` 方法

一个关键特性在于局部变量和执行状态会在每次调用之间自动保存

当生成器终结时，它们还会自动引发 `StopIteration`

## 9.10.生成器表达式

某些简单的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，但外层为圆括号而非方括号

```python
sum(i*i for i in range(10))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product
```