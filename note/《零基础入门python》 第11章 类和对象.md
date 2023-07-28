@[TOC](文章目录)

---

# 前言

直接跳过第10章

起始写这张的时候，有点纠结，因为还是有点编程基础。所以关于python对象和类的概念理解起来还算轻松。

想在这章节把这些概念阐述清楚，发现自己不能阐述清楚。索性就算了。那就直接照本宣科了。

最最直接的方法就是：不懂可以先硬记下来，在慢慢理解。

# 1.对象 = 属性 + 方法

对象的特征称为属性， 对象的特征在变量层面就是变量

对象的行为称为方法，方法其实就是函数

类

​	是创建对象的蓝图，对象是通过类创建的。使用某一个类来创建了一个对象，这个对象叫做这个类的一个实列，也叫实例对象。

```python
#类
class MyPythonClass:
    #定义属性，也就是变量
    name = "mypythonclass"
    #定义动作，也就是函数
    #这样定义倒也不会报错，但是这样无法使用属性的内容
    def printName1(name):
        print(name)

    #类里的函数定义一般是特殊的参数列表, self放在其它参数前面（self放在第一个）
    #方法的第一个参数常常被命名为 self。 这也不过就是一个约定: self 这一名称在 Python 中绝对没有特殊含义。 
    #但是要注意，不遵循此约定会使得你的代码对其他 Python 程序员来说缺乏可读性。---这部分来自官网
    def printName(self):
        print(self.name)
    def printName2(self, name):
        print(self.name, name)

#这个倒也能执行，其实就是个普通的函数
MyPythonClass.printName1("xxxxxxx")

#这一句会报错，
#MyPythonClass.printName()

#实例对象会作为函数的第一个参数被传入
mpc = MyPythonClass()
#这个明面上看起来什么参数都没有，那是python帮你做了，把mpc作为参数传递为了printName
mpc.printName()
#换个调用方式,同样会正常输出
MyPythonClass.printName(mpc)
```

# 2.公有和私有

​	默认上对象的属性和方法都是公开的，可以直接通过点操作符(.)进行访问

​	那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。

​	大多数 Python 代码都遵循这样一个约定：带有一个下划线的名称 (例如 `_spam`) 应该被当作是 API 的非公有部分 (无论它是函数、方法或是数据成员)。

​	由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种机制的有限支持，称为 *名称改写*。 任何形式为    `__spam` 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 `_classname__spam`，其中 `classname` 为去除了前缀下划线的当前类名称。 这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。

​	访问或修改被视为私有的变量仍然是可能的

```python
class Person:
    __name_ = "xxxxxx"
    __high  = "asdas"
    #__init__在实例化对象的时候自动调用
    def __init__(self, name, high):
        self.__high = high
        self.__name_= name
    def getName(self):
        return self.__name_
    def __getHigh(self):
        return self.__high
    
me = Person("xxx", "183")
#这样会报错'Person' object has no attribute '__name_'
# print(me.__name_)
# print(me.__high)
#这样就对了
print(me._Person__name_)
print(me._Person__high)

#AttributeError: 'Person' object has no attribute '__getHigh'
#me.__getHigh()
me._Person__getHigh()
```

# 3.继承

基本格式：

​	class 类名字(父类的名字):

​		...

被继承的类称为基类、父类或超类

继承者称为子类

一个子类可以继承它的父类的任何属性和方法

如果子类中有与父类同名的变量或方法，则会自动覆盖父类的变量或方法

```python
class Base:
    name = "base"
    def printBase(self):
        print(" i am base")
        
class A(Base):
    pass
    pass

a = A()
a.printBase()    
print(A.name) 
print(a.name)
```

在子类中调用父类的方法
调用未绑定的父类方法：

​	未绑定是指并不需要绑定父类的实例对象，使用子类的实例对象代替即可

使用super函数

​	super函数能够帮我们自动找到基类的方法，而且还为我们传入了self参数。

```python
class Base:
    name = "base"
    def __init__(self, name):
        print("i am base __init__, name = ", name)
        self.name = name
    def printBase(self):
        print(" i am in base printBase, ", self.name)
        
class A(Base):
    def __init_(self, name):
        print("i am A __init__")
        #用子类的实例化对象self代替Base的实例化对象。
        #Base.__init__(self, name)
        
        #用super,用的self也是子类的实例化对象，而不是基类Base的实例化对象
        super().__init__(self, name)
        
        #这样写也不会报错
        #super().__init__(name)

a = A("XXXXX")
a.printBase()    
print(a.name)
#super的使用方法，这里不细讲。感兴趣自己搜以下吧
```

多重继承

​	python支持多重继承

​	格式：

​		class 类名(父1,父2,...):

​			...

​	**多重继承谨慎使用**

组合

​	直接把需要的类放进去实例化就行

```python
class BaseA:
    name = "xxxx"
    def __init__(self, name):
        self.name = name
        print("BaseA __init__")

class BaseB:
    school = "xxxx"
    def __init__(self, school):
        self.school = school
        print("BaseB __init__")

class BaseC:
    phone = "xxxx"
    def __init__(self, phone):
        self.phone = phone
        print("BaseC __init__")

class Student:
    address = "xxx"
    def __init__(self, name, school, phone, address):
        self.name = BaseA(name)
        self.school = BaseB(school)
        self.phone = BaseC(phone)
        self.address = address

    def printStudentInfo(self):
        print("\nname: %s\nschool: %s\nphone: %s\naddress: %s"
              % (self.name.name, self.school.school, self.phone.phone, self.address))

stu = Student("sam", "mid", "123131", "asdfas")
stu.printStudentInfo()

```

类/类对象和实例对象

类中定义的属性是静态变量

类的属性是与类对象进行绑定，并不会依赖任何它的实例对象。

如果类的属性和方法同名，属性会覆盖方法。

```python
class BB:
    # def printBB()
    def printBB(self):
        print("This is BB")

bb = BB()
bb.printBB()
#报错的原因是:使用实例对象调.方法的时候，python会把当前实例化的对象的地址当作第一个参数给方法
#我们定义printBB的时候没有定义参数,

#当printBB()加上self以后，BB.printBB() missing 1 required positional argument: 'self'
#BB.printBB()
#当printBB有参数self的时候，直接用类名.方法()的方式不行了，要求有一个self，而调用的时候没有
BB.printBB(bb)  #这样就可以了
```

