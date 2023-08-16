# favourite = "FishC"
# for each in favourite:
#     print(each, end = ' ')
# print("\n")

# for i in range(5):
#     print(i)

# print("\n")
# for i in range(2, 9):
#     print(i)
# print("\n")

# bingo = "1111222"
# answer = input("Please input a number:")
# while  True:
#     if answer == bingo:
#         break
#     else:
#         answer = input("Plese input a number: ")
# print("congrations!!!!!")


# for i in range(10):
#     if i%2 != 0:
#         print(i)
#         continue
#     i += 2
# print(i)

# x = 11
# y = 22
# 三元表达式，但是看起来不是很好理解的样子。样子有点怪异，可能是受到了C语言中的?:运算符的影响
# a = x if x < y else y
# print(x)

# assert 3 < 4
# assert 4 > 5

# number = []
# number.insert(0, 0)
# number.insert(1, 1)
# number.insert(2, 3)
# number.insert(4, 5)
# number.insert(5, 6)

# print(number)
# number[1], number[3] = number[3], number[1]
# print(number)
# print("hello word!\n" * 3)

# number.remove(0)
# print(number)
# number.pop(3)
# print(number)
# del number[2]
# print(number)

# number.append(11)
# number.append(12)
# number.append(13)
# number.append(14)
# print(number)
# print(number[0:1])
# print(number[1:3])
# print(number[:2])
# print(number[:])
# print(number[::2])
# print(number[::-1])
# print(number * 3)
# print(number)

# orinumber = ()
# orinumber1 = 1, 2
# orinumber2 = orinumber + orinumber1
# print(orinumber2)
# print(type(orinumber))
# print(type(orinumber1))
# print(type(orinumber2))

# str = "I love Python!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
# print(type(str))
# print(str.count("!",0, 20))
# print(str.count("!",0, 20))

# def myFirstFunction(name):
#     """This is my first python function.""" #python 函数的注释，其实就是使用指南，定义在里面才能被识别？
#     print(name + " word!!!!")

# """ This is my second function."""
# def myFirstFunction1(name):
#     print(name)

# myFirstFunction("Hello")
# help(myFirstFunction)
# print(myFirstFunction.__doc__)

# myFirstFunction1("Hello")
# help(myFirstFunction1)
# print(myFirstFunction1.__doc__)


# def printName(name1, name2):
#     print(name1 + "->" + name2)

# #理想的时name1->name2
# #常规的按照形参顺序赋值
# printName("name1","name2")

# #不按照形参顺序赋值
# printName("name2", "name2")

# #不按照形参顺序赋值，但是由特殊处理
# printName(name2="name2", name1="name1")

# 可变参数的函数定义(收集参数)
# def myFunction( *params):
#     print("Params number is ", len(params))

# myFunction("name", 1, 2,2,2,3,3,3)


# def myFunc1(*args, extra):
#     print("variable arg number is ", len(args))
#     print("extra param:", extra)

# myFunc1(1,2,3,3,4,extra="This is test")

# num=[1,2,3,4,5,6,6]
# print(num)
# num.reverse()
# print(num)
# print(3**-2)  #这个 1/9

# print("%c" % (97))
# print("%s world %s" %("Hello","!!!!!!!!!!!!"))
# print("%g" %(14500000000000000000000))
# print("%g" %(0.123456789))
# print("%04.2f" % 2.1234123)
# print(' %010d' % 10)

# print(' % #X' %100000)

# num=list((1,2,3,5,6,666,34,45))
# num=list("hello world")
# num=list([1,2,3,4,5])
# print(num)
# num=tuple("asdfasdfasdfasdf")
# num=tuple([1,2,3,4,5,6])
# print(num)
# name=str([1,23,4,5,6,66,66])
# name=str(64)
# name=str(66.12316546546546)
# name=str(0xa)
# print(name)

# name="hello"
# num=[1,2,3,4,5,1,2,23,234]
# num1=1,2,3,4,6,7,7,8,67
# for each in zip(num1, name, num1):
#     print(each)

# def myFirstFunc(name1, name2="aaa"):
#     print(name1 + str(name2))

# def func(*name):
#     print("params number:", len(name))

# func(1,2,3,4,5)
# name = "111111"
# def func1(* names, extra = "XXXXX"):

#     print(len(names))
#     global name
#     print(name)
#     name = "2222222222"
#     print(extra)
# func1("xiaowang","xiaoming","xiaogou",extra="Hello world!!!!")
# print(name)

# x = "hello"
# y = " world"
# name = lambda x, y:x + y
# print(name(x,y))

# temp = filter(None,[1,2,3,0,0,False, True])
# print(list(temp))

# temp1=filter(lambda x:x%2, range(20))
# print(list(temp1))
# temp = map(lambda x:x *100,[1,2,3,4])
# print(tuple(temp))
# def normalFab(n):
#     a1 = 1
#     a2 = 1
#     a3 = 1
#     if n < 1:
#         print("Wrong number:", n)
#     while (n - 2) > 0:
#         a3 = a1 + a2
#         a1 = a2
#         a2 = a3
#         n -= 1while
#     return a3

# def fab(n):
#     if n < 1:
#         print("wrong number : ", n)
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fab(n-1) + fab(n-2)

# print("total %d" % fab(20))
# print("total %d" % normalFab(20))
# import os
# print(os.listdir())

# num =
# print(num)import
# #通过关键字dict和二元序列来创建
# dict1 = dict((('a',10),('b',11)))
# dict2 = dict([('A',10),('B',11)])

# #通过dict和具有映射关系的参数来创建
# dict3 = dict(a=10,b=11)

# #创建一个空的字典，然后通过[]来添加元素
# dict4 = {}
# dict4["asdasdasd"] = 11

# #直接赋值创建
# dict5 = {'a':2123, 'b':1234}

# #通过关键字dict和zip来创建
# dict6 = dict(zip('abcdef',[1,2,3,4,5]))

# #通过推导来创建（网上查到的）
# dict7 = {i:i ** 2 for i in range(1,5)}

# #通过dict.fromkeys()来创建
# #第二个参数作为一个看作是一个整体
# dict8=dict.fromkeys(range(4))
# dict9=dict.fromkeys(range(4),'aaaaa')
# print("dict1:",dict1)
# print("dict2:",dict2)
# print("dict3:",dict3)
# print("dict4:",dict4)
# print("dict5:",dict5)
# print("dict6:",dict6)
# print("dict7:",dict7)
# print("dict8:",dict8)
# print("dict9:",dict9)

# def myFunc(**params):
#     print("params num:", len(params))
#     print("member:", params)

# mydict = dict(zip(("1",'3',"5",'7',"9"),[1,2,3,4,5,5,6,6,7]))
# myFunc(**mydict)
# myFunc(a=1,b=2,c=3,d=4)


# myset5 = set(x for x in range(2,10))
# print("myset5", myset5)
# myindex = 0
# for x in myset5:
#     print("member %d value is %d" %(myindex, x))
#     myindex += 1
# if 2 in myset5:
#     print("2 is in set.")
# if 100 not in myset5:
#     print("100 is not in set.")
# words = ['cat','window','defenestrate']
# for w in words:
#     print(w, len(w))

# for n in range(2,10):
#     for x in range(2,n):
#         if n %x == 0:
#             print(n, " equals ", x , "*", n//x)
#             break
#     else:
#         print(n, 'is a prime number.')

# x = 0
# while x < 9:
#     print(x)
#     x +=1
# else:
#     print("while 条件不成立时执行。")

# for i in range(10):
#     if i > 100:
#         break
# else:
#     print("所有元素都遍历完，就执行")

# for i in range(4):
#     if i == 2:
#         print("value == 2,本次迭代即将结束，进入下一次迭代")
#         continue
#     print(i)
# users = {"Hans":"active", "eleonere": "inactive","景太郎":"active"}

# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)

# active_users = {}
# for user,status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)

# #range()
# print("range(10) ",       list(range(10)))
# print("range(1,10) ",     list(range(1,10)))
# print("range(1,10,2) ",   list(range(1,10,2)))
# print("lrange(1,10,-1) ", list(range(10,1,-1)))

# errors = (400,401,402,403,405,418,420)
# for status in errors:
#     match status:
#         case 400|401|402:
#             print("Bad request")
#         case 404:
#             print('Not found')
#         case 418:
#             print("I'm a teapot")
#         case _:
#             print("Something's wrong with the internet.")

# points = {1:(0,0),2:(0,2),3:(1,0),4:(3,4),5:"xxxxxxxx"}
# for index, point in points.items():
#     match point:
#         case(0,0):
#             print("origin point ", point)
#         case(0,y):
#             print(f"Y={y}")
#         case(x,0):
#             print(f"X={x}")
#         case(x,y):
#             print(f"X={x}, Y={y}")
#         case _:
#             raise ValueError("not a point")

# import pickle
# my_list = ["hello world"]
# pickle_file = open('pickle_file.pick', 'wb')
# pickle.dump(my_list, pickle_file)
# pickle_file.close()

# pickle_file = open('pickle_file.pick', 'rb')
# my_list=pickle.load(pickle_file)
# print(my_list)
# pickle_file.close()

# import os
# os.remove("pickle_file.pick")

# my_file = open('测试一下1.txt')
# print(my_file.read())
# my_file.close()


# try:
#     with open('测试一下1.txt') as my_file:
#         print(my_file.read())
# except OSError:  #不知道有没有通用的， 不然还要记住每种异常类型
#     print("打开文件失败！！！！！")
# finally:
#     print("不管有没有出错，这个都要执行")

# try:
#     name = 1
#     name = 1 + '1'
#     with open("test.txt") as my_file1:
#         pass
# except (OSError, TypeError) as reason:
#     print("打开文件时出错", reason)
# finally:
#     print("省略中间的except")

# class Myclass:
#     __name = 'myclass'
#     __x = 1
#     __y = 1
#     #参数中不加self会报错
#     def __init__(self, name):
#         print("class ", name ," created.")
#         self.__name = name

#     # 这个函数的名字颜色都变了
#     def __inClass(self, name, x, y):
#         pass
#     def setName(self, name):
#         """reset the object name."""
#         self.__name = name

#     def setPositon(self, x, y):
#         self.__x = x
#         self.__y = y


#     def justPrint(self):
#         print(self.__name, self.__x, self.__y)

# a = Myclass('aaaaaaaaaaaa')
# a.__name = "XXXXXXXXXXXX"  #这样是不会生效，但是不会报错

# a.setName("MyClass")
# a.setPositon(12,13)
# a.justPrint()

# #其实类外还是有办法访问，定义成私有的变量 对象名._类名私有变量名
# print("MyClass name is ", a._Myclass__name)

# num1=3000
# num2=3000.555555555555
# num3=3000.111111111111
# str1="3000"
# BooL=False
# print(type(num1), " value ", num1, " to float ", float(num1))
# print(type(num2), " value ", num2, "to int ", int(num2))
# print(type(num3), " value ", num3, "to str ", str(num3))
# print(type(str1), " value ", str1, "to int ", int(str1))
# print(type(BooL), " value ", BooL, "to int ", int(BooL))

# # <class 'int'>  value  3000  to float  3000.0
# # <class 'float'>  value  3000.555555555555 to int  3000
# # <class 'float'>  value  3000.111111111111 to str  3000.111111111111
# # <class 'str'>  value  3000 to int  3000
# # <class 'bool'>  value  False to int  0

# print('3/2 = ',3/2)
# print('3//2 = ', 3//2)
# print('2*2 = ', 3*2)
# print('3**2 = ', 3**2)
# print('3%2 = ', 3%2)
# # 3/2 =  1.5
# # 3//2 =  1
# # 2*2 =  6
# # 3**2 =  9
# # 3%2 =  1

# if 4 > 3 > 2:
#     print("Hello world!!!!")

# if 1 > 0 and 1 < 2:
#     print("1 > 0 and 1 < 2")
# else:
#     print("Hello World!!!")

# #其实没有学过其它语言，这里根本不需要说什么悬挂。 看对齐方式就知道
# x = 3
# if x > 2:
#     if x == 1:
#         print("XXXXX")
# else:
#     print("AAAAAAA")
# list0 = []
# lista = [1, 2, 3]
# listb = [1.0, 2.0]
# listc = ['aaa', 'bb', 'cc']
# listd = [1, 1.0, 'aa', [1, 2, 3]]
# liste = list(range(4))
# print("list0", type(list0))
# print("lista", type(lista))
# print("listb", type(listb))
# print("listc", type(listc))
# print("listd", type(listd))
# print("listd", type(liste))


# # list0 <class 'list'>
# # lista <class 'list'>
# # listb <class 'list'>
# # listc <class 'list'>
# # listd <class 'list'>
# # listd <class 'list'>

# mylist = list(range(3))

# print(mylist)
# mylist.append("aaaxx")  # 往尾部添加个元素
# print(mylist)
# mylist.extend(list(range(2, 10, 2)))  # extend的参数是一个列表，在尾部添加
# print(mylist)
# mylist.insert(1, "xaxaxa")  # 第一个参数是index,第二个参数为value
# print(mylist)


# # [0, 1, 2]
# # [0, 1, 2, 'aaaxx']
# # [0, 1, 2, 'aaaxx', 2, 4, 6, 8]
# # [0, 'xaxaxa', 1, 2, 'aaaxx', 2, 4, 6, 8]

# a = [1, 2, 3, 4, 'aaaa', 'bbbb', ["hello", "world", "!!!!",]]
# print("all:", a)
# a.remove('bbbb')
# print("after remove 'bbbb'", a)
# del a[1]
# print("after del a[1]", a)
# a.pop()
# print("after pop() ", a)
# a.pop(2)
# print("after pop(2)", a)
# del a

# # 输出结果:
# # all: [1, 2, 3, 4, 'aaaa', 'bbbb', ['hello', 'world', '!!!!']]
# # after remove 'bbbb' [1, 2, 3, 4, 'aaaa', ['hello', 'world', '!!!!']]
# # after del a[1] [1, 3, 4, 'aaaa', ['hello', 'world', '!!!!']]
# # after pop()  [1, 3, 4, 'aaaa']
# # after pop(2) [1, 3, 'aaaa']

# a = list(range(5))
# print("all:", a)
# a[1] = 20
# print("all:", a)

# 输出结果:
# all: [0, 1, 2, 3, 4]
# all: [0, 20, 2, 3, 4]
# print("a[0] = ", a[0])
# print("index of value 3 is ", a.index(3, 0, 4))
# print("a[:] = ", a[:])
# print("a[1:3]", a[1:3])
# print("a[:2]", a[:2])
# print("a[1:]", a[1:])
# # 结果输出:
# # all: [0, 1, 2, 3, 4]
# # a[0] =  0
# # index of value 3 is  3
# # a[:] =  [0, 1, 2, 3, 4]
# # a[1:3] [1, 2]
# # a[:2] [0, 1]
# # a[1:] [1, 2, 3, 4]

# a = list(range(0, 10, 2))
# b = list(range(1, 11, 2))
# print("a = ", a)
# a[0], a[1] = a[3], a[4]
# print("after a[0],a[1] = a[3], a[4], a = ", a)

# print("b = ", b)
# print("b[::-1] = ", b[::-1])
# print("b[::-2] = ", b[::-2])
# print("b[::1] = ", b[::1])
# print("b[::2] = ", b[::2])
# print("b[2:5:2] = ", b[2:5:2])
# print("b[5:2:-1] = ", b[5:2:-1])

# if a == b:
#     print("a == b")
# elif a > b:
#     print("a > b")
# else:
#     print("a < b")
# print("a + b = ", a + b)
# print("a * 3 = ", a * 3)
# print("3 * a = ", 3 * a)

# if 3 in a:
#     print(" 3 in a")
# if 3 not in a:
#     print("3 not in a")
# c = [1, 2, [1, 3, 4]]
# print("c[2][0] = ", c[2][0])

# # 输出结果:
# # a =  [0, 2, 4, 6, 8]
# # after a[0],a[1] = a[3], a[4], a =  [6, 8, 4, 6, 8]
# # b =  [1, 3, 5, 7, 9]
# # b[::-1] =  [9, 7, 5, 3, 1]
# # b[::-2] =  [9, 5, 1]
# # b[::1] =  [1, 3, 5, 7, 9]
# # b[::2] =  [1, 5, 9]
# # b[2:5:2] =  [5, 9]
# # b[5:2:-1] =  [9, 7]
# # a > b
# # a + b =  [6, 8, 4, 6, 8, 1, 3, 5, 7, 9]
# # a * 3 =  [6, 8, 4, 6, 8, 6, 8, 4, 6, 8, 6, 8, 4, 6, 8]
# # 3 * a =  [6, 8, 4, 6, 8, 6, 8, 4, 6, 8, 6, 8, 4, 6, 8]
# # 3 not in a
# # c[2][0] =  1

# a = 1,2,3,4
# b = ()
# c = tuple(range(3))
# d = (1,2,3,4)

# print("a's type = ", type(a))
# print("b's type = ", type(b))
# print("c's type = ", type(c))
# print("d's type = ", type(d))
# # 输出结果:
# # a's type =  <class 'tuple'>
# # b's type =  <class 'tuple'>
# # c's type =  <class 'tuple'>
# # d's type =  <class 'tuple'>
# print(dir(tuple))
# a = (1,)
# a.__add__((2,3,4,5))
# print(a)

# str1 = "hello world"

# #将字符串的第一个字符变为大写
# print(str1.capitalize())

# str1 = "HELLO WORLD!!!!!!"
# #把整个字符串的所有字符变为小写
# print(str1.casefold())

# #计算某个子串在字符串中出现的次数
# print(str1.count("L",0))
# print(str1.count("HELLO",0,8))

# #查找某个子串在字符串中的起始index,有则放回第一个字符的index,没有返回-1
# print(str1.find('L',0,20))
# print(str1.find('HELLO',0,20))

# #使用index(sub, [start[, end]])方法来查找某个子串的起始位置，有返回index,没有就抛出异常(ValueError: substring not found)
# print(str1.index("H"))
# print(str1.index("H",0))
# print(str1.index("H", 0, 100)) #结束位置不填写的话就是字符串结尾，超了也没关系
# #print(str1.index("XXXXX"))

# #以字符串作为分隔符号，插入到子串的所有字符之间。（所有字符哟）
# print('x - x'.join(str1))
# print(' '.join("hello world"))
# #也可以这么理解将字符串作为分隔符插入到每个元素之间。
# print('XXXX'.join(["hello", "world", "!!!!"]))
# print('_'.join(('hello', 'world')))

# #替换指定的字符串
# print('hello'.replace('hello', 'world'))
# print('xxxxxx'.replace('x', 'a', 3)) #也可以指定替换的次数

# #以指定字符串拆分字符串split(sep=None, maxsplit=-1) : -1应该是指所有，可以指定拆分次数
# print('h_h_h h h'.split()) #不指定分隔符话，默认是使用空格作为分隔符（可能还有其它的默认，先不查了）
# print('h h h h h'.split(' '))
# print('h h h h h'.split(' ',1))


# # format的用法
# # 类似"{0}"的是位置参数，其数目决定了format()中实参的数量
# print("{0}ello {1}orld{2}".format("H", "W", " !!!"))

# # 位置参数数量与实参数量不匹配，以位置参数的数量为准
# print("{0}ello {1}orld".format("H", "W", " !!!"))
# print("{0}ello {1}orld{2}".format("H", "W", " !!!", "asdasd"))

# #可以在{}用上自己喜欢的参数名（关键字参数）
# print("{a}ello {b}orld{c}".format(a = "H", b = "W", c = " !!!"))

# #关键字参数和位置参数可以混用，但是位置参数要在前面
# print("{0}ello {b}orld{c}".format("H", b = "W", c = " !!!"))

# #如果字符串中正好有个“{0}”要输出时
# #用常规思路使用\会出现KeyError: '0 \\'
# #print('\{0\}sadfas{a1}'.format(a1 = 'asdas'))
# #换一种实现方法用{}
# print('{{0}}sadfas{a1}'.format(a1 = 'asdas'))

# #被{}包起来的叫替换域？
# #{1:.2f} 1标识位置参数1，:标识格式化符号的开始，.2标识小数点后两位，f标识定点数
# print('{0}:{1:.2f}'.format('身高', 183.551))

# #格式化操作符号:%
# #基本格式：包含格式化操作符的字符串 % (与格式化操作符数量相等的实参)
# str1 = "%c_%c_%c"
# print(str1)
# print('%c_%c_%c' % (97,98,99))
# print(str1 % (100,101,102))

# 函数的注释放在def上面一行的化，只有看源码的时候才能看到
# """放这里行不行啊？？？？？不行，这个你自己看？？？"""
# def myFunc(name1, name2, name3):
#     """ 放在这里大家都看得到"""
#     print("Hello world!!")
# #help(名字)可以查看一些帮助内容，函数可以看到其注解
# print(help(myFunc))


# def FunctionName(arg):
#     print(arg)
# FunctionName('xxxxxxxxx')

# #arg1 给了默认值，那么后面的所有参数都必须给默认值
# def FunctionName1(arg1 = 0, arg2 = 'sadfas'):
#     print(arg2, arg1)

# #有默认值的参数，调用时可以不给值
# FunctionName1()

# #有默认值的参数，调用时可以给一部分值
# FunctionName1(2)

# #有默认值的参数，调用时可以给全部值
# FunctionName1(2,'xxxx')

# #函数调用的时候，可以将值赋给指定的形参
# FunctionName1(arg1=4,arg2="AAAAA")

# #函数调用的时候，若指定形参的名字，那么参数的顺序可以和定义时不一致。
# FunctionName1(arg2="BBBB", arg1=333)

# #收集参数有两种：*和**
# #第一种参数名字前加了一个*
# def FunctionName2(*param, extra):
#     print("extra = ", extra, "params size = ", len(param))

# #带有收集参数和额外参数的情况，在调用时要指定额外的那个参数的名字赋值（关键字参数）
# FunctionName2(1,3,4,5, extra='name')

# #带一个收集参数的可以通过序列（列表，元组和字符串）赋值，但是需要解压（在调用时，在实参前加一个*）
# #不解压的话，被看成一个整体赋值给params
# #换个说法：不解压，那么list/tuple/str 被看作一个整体赋值给params,params中的值的个数为1
# #解压后，list/tuple/str中的每个元素都塞给了params,params中值的个数是元素的个数
# FunctionName2(*[1234,313,"xxxxx", 3.1415], extra= 'name')
# FunctionName2(*(1,2,34,4,5,5,5,5,1234),extra='name')
# FunctionName2(*"asjkdljfasjdlkf", extra='XXXX')

# def FunctionName3(extra, *params):
#      print("extra = ", extra, "params size = ", len(params))

# #若收集参数和非收集参数混用，将非收集参数放在前面，在调用时可以使用关键字参数的方式给非收集参数赋值
# FunctionName3('XXXXX', 1,3,4,5,5,6,2,3,3,3)

# #第二种两个**的收集参数
# #表示将收集参数打包成字典
# def FunctionName4(extra, **params):
#     print("extra = ", extra, "len(params) = ", len(params))

# FunctionName4("dict", **{"2222":2222, "3333":3333})

# #总结一下：*/**
# #在函数定义的时候参数名前加表示打包*-打包成序列，**-打包成字典
# #在函数调用的时候使用表示解压，将*将序列中的元素展开，**-将字典中的键值对展开

# global_name = "hello"
# def myFunction(name = "aaaa"):
# #在函数内部想要修改全局变量，使用前先用global声明一下
#     global global_name
#     global_name = "myFunction add world"
#     name1 = name
#     print("var name = ", name)
#     def sunFunction():
# #内部函数想要修改外部函数的变量，使用前用nonlocal声明一下
#         nonlocal name1
# #同样的，内部函数想要修改局部变量的值，也要在使用前用global声明一下
#         global global_name
#         print("local name1 = ", name1)
#         name1 = name1 + " sunFunction add"
#         global_name = global_name + "sunFunction add"
#     sunFunction()
#     print("local name1 = ", name1)


# #
# def nonModify(extra, *params):
#     """ 只是用一下全局变量，并不修改"""
#     print("nonmodify print :", global_name)
#     print("nonmodity params print: extra = ", extra, ", params num = ", len(params))
#     def nonModifySon(*params):
#         param_index = 0
#         for i in params:
#             print("index = ", param_index, ", value = ", i)
#             param_index += 1
#         print('%s  %s   %s' %(str(global_name), str(extra), str(len(params))))
#     nonModifySon(*params)

# nonModify("test", *(1,2,3,4,5,1,3,2,4))

# print("Before global global_name",global_name)
# myFunction("xxxxx")
# print("After global global_name",global_name)

# def noReturn():
#     pass
#     pass

# def hasReturn():
#     pass
#     pass
#     return 1,2,3,4,5

# #使用{}直接定义
# myset1 = {1, 3, 4, 5, 6, 6, 6}

# #通过关键字set()定义
# myset2 = set([1, 2, 34, 5, 6])
# myset3 = set((1, 2, 4, 5, 6))
# myset4 = set("sajdlfkjas")
# myset5 = set(x for x in range(2, 10))
# print("myset1", myset1)
# print("myset2", myset2)
# print("myset3", myset3)
# print("myset4", myset4)
# print("myset5", myset5)
# # 输出结果：
# # myset1 {1, 3, 4, 5, 6}
# # myset2 {1, 2, 34, 5, 6}
# # myset3 {1, 2, 4, 5, 6}
# # myset4 {'s', 'f', 'a', 'd', 'k', 'l', 'j'}
# # myset5 {2, 3, 4, 5, 6, 7, 8, 9}

# # add()
# # 若元素存在于集合中，无影响
# # 若元素不存在于集合中，往集合里面添加
# myset5 = set(x for x in range(2, 10))
# print("myset5", myset5)
# myset5.add(2)
# myset5.add(1100)
# print("myset5", myset5)
# # 输出结果：
# # myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# # myset5 {2, 3, 4, 5, 6, 7, 8, 9, 1100}

# # remove()
# # 参数必须是集合的成员
# myset5 = set(x for x in range(2, 10))
# print("myset5", myset5)
# myset5.remove(2)

# # myset5.remove(1100) #这句会报错
# print("myset5", myset5)

# #如果不想修改集合元素，那么使用frozenset()创建集合
# myset6 = frozenset(x for x in range(1,3))
# #AttributeError: 'frozenset' object has no attribute 'add'
# #myset6.add()
# print(myset6)
# # 输出结果：
# # myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# # myset5 {3, 4, 5, 6, 7, 8, 9}
# # frozenset({1, 2})


# #update()

# myset5 = set(x for x in range(2, 10))
# print("myset5", myset5)
# myset5.update([2, 4, 5, 100, 200])
# myset5.update((2, 4, 5, 100, 200, 300))
# myset5.update(x for x in range(1000, 1010))
# myset5.update('abcdefg')
# print("myset5", myset5)
# # 输出结果 ：
# # myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# # myset5 {2, 3, 4, 5, 6, 7, 8, 9, 'g', 'f', 300, 'a', 'd', 'c', 'b', 200, 'e', 100, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009}

# 查询
# 不能使用下标访问，无序
# 可以使用迭代器
# 可以使用in/not in判断元素是否在集合中

# myset5 = set(x for x in range(2, 10))
# print("myset5", myset5)
# myindex = 0
# for x in myset5:
# 	print("member %d value is %d" % (myindex, x))
# 	myindex += 1
# 	if 2 in myset5:
# 	    print("2 is in set.")
# 	if 100 not in myset5:
# 	    print("100 is not in set.")

# # 输出结果：
# # myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# # member 0 value is 2
# # member 1 value is 3
# # member 2 value is 4
# # member 3 value is 5
# # member 4 value is 6
# # member 5 value is 7
# # member 6 value is 8
# # member 7 value is 9
# # 2 is in set.
# # 100 is not in set.

# # remove()
# # 参数必须是集合的成员
# myset5 = set(x for x in range(2, 10))
# print("myset5", myset5)
# myset5.remove(2)
# # myset5.remove(1100) #这句会报错
# print("myset5", myset5)

# #如果不想修改集合元素，那么使用frozenset()创建集合
# myset6 = frozenset(x for x in range(1,3))
# #AttributeError: 'frozenset' object has no attribute 'add'
# #myset6.add()
# print(myset6)
# del myset6
# # 输出结果：
# # myset5 {2, 3, 4, 5, 6, 7, 8, 9}
# # myset5 {3, 4, 5, 6, 7, 8, 9}
# # frozenset({1, 2})

# #访问字典的方法
# dict1 = dict.fromkeys(range(3), "AaBbCc")
# print("keys:", dict1.keys())
# print("values:", dict1.values())
# print("items", dict1.items())

# #若指定的key在字典中没有，给这个key关联一个value的时候就会往字典里添加一个键值对
# dict1[100] = "aaaaaaa"
# print("keys:", dict1.keys())
# print("values:", dict1.values())
# print("items", dict1.items())

# # 结果输出
# # keys: dict_keys([0, 1, 2])
# # values: dict_values(['AaBbCc', 'AaBbCc', 'AaBbCc'])
# # items dict_items([(0, 'AaBbCc'), (1, 'AaBbCc'), (2, 'AaBbCc')])
# # keys: dict_keys([0, 1, 2, 100])
# # values: dict_values(['AaBbCc', 'AaBbCc', 'AaBbCc', 'aaaaaaa'])
# # items dict_items([(0, 'AaBbCc'), (1, 'AaBbCc'), (2, 'AaBbCc'), (100, 'aaaaaaa')])

# #文件使用完毕一定要关闭
# #'r',文件默认以r模式打开
# f = open('test.txt')
# print(f.read())
# f.close()

# #用模式w打开的文件，以替换原有内容的方式写入。单纯使用w打开的文件无法读取，想要读取可以w+模式打开
# f = open('test.txt', 'w')
# #r和w模式不能混用，直接报错
# #f = open('test.txt', 'rw')

# #w模式的时候，不能读取文件内容，只能往里写
# #print(f.read())
# f.close()

# #用模式x打开已经存在的文件会报错，打开不存在的文件会直接创建一个文件
# f = open('test1.txt','x')
# #单纯用x模式打开的文件不能读和写
# # f.read()
# # f.write("xxxxxxxxxxxxxx")
# f.close()

# #用模式a打开的文件，在写入的时候在文件末尾写入.只以a模式打开的文件，是无法读取的，可以使用a+模式打开
# f = open('test.txt','a')
# f.close()

# #b/t这两个模式不能单独使用，需要指明文件读写模式后才能加上. t以文本的方式打开，b以二进制文件的方式打开
# # t：
# #     1、读写都是以字符串（Unicode）为单位
# #     2、只能针对文本文件
# #     3、必须制定字符编码
# # b: binary模式
# #     1、读写都是以bytes为单位
# #     2、可以针对所有文件
# #     3、一定不能指定字符串编码
# # 总结：
# # 1、在操作纯文本文件方面t模式帮我们省去了编码和解码的环节，b模式则需要手动编码和解码
# # 2、针对非文本文件（如视频，图片、音频等），只能使用b模式
# f = open('test.txt', 'at+')
# f.close()

# #+模式不能单独使用，需要和别的模式一起使用
# f = open('test.txt','r+')
# f.close()
# f = open('test.txt', 'w+')
# f.close()
# f = open('test.txt', 'a+')
# f.close()

# #模式U,不用了。使用的话会提示'U' mode is deprecated

# import os

# print(os.getcwd())
# print(os.chdir(r"D:\coding\py_learning"))
# print(os.getcwd())
# print(os.chdir(r"D:\coding\py_learning\code"))
# print(os.getcwd())
# print(os.listdir())
# print(os.listdir(r"D:\coding\py_learning"))
# os.mkdir("TEST")
# os.rmdir("TEST")
# os.makedirs(r'a\b\c')
# os.removedirs(r'a\b\c')
# open(r"test1.txt", 'x')
# os.remove(r'test1.txt')
# os.rename(r'test.txt', r'test1.txt')
# os.rename(r'test1.txt', r'test.txt')
# os.system(r'ls -alh')
# print("os.listdir(os.curdir) = ",os.listdir(os.curdir))
# print("os.listdir(os.pardir) = ", os.listdir(os.pardir))
# print("os.sep = ", os.sep)

# #这个输出看不见明显的字符，能看到换行了
# print("os.linesep = ", os.linesep)
# print("os.name = ", os.name)

# #walk(top) 遍历top下的所有字母，并将结果返回一个三元组(路径,[包含目录],[包含文件])
# for each in os.walk(r'D:\coding\py_learning'):
#     print(each)

# import os
# import time
# print(os.path.basename(r'D:\coding\py_learning\code\test.txt'))
# print(os.path.dirname(r'D:\coding\py_learning\code\test.txt'))

# #这个join有点好玩
# print(os.path.join(r'D:\coding\py_learning', r'code\test.txt'))
# print(os.path.join(r'D:\coding\py_learning\text.txt', r'code\test.txt'))
# print(os.path.join(r'D:\coding\py_learning', r'D:\code\test.txt'))
# print(os.path.join(r'\coding\py_learning', r'd:\code\test.txt'))

# print(os.path.split(r'D:\coding\py_learning\code\test.txt'))
# print(os.path.splitext(r'D:\coding\py_learning\code\test.txt'))
# print(os.path.splitext(r'D:\coding\py_learning\code\test.txt.exe'))
# print(os.path.getsize(r'D:\coding\py_learning\code\test.py'))

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getatime(r'D:\coding\py_learning\code\test.py'))))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(r'D:\coding\py_learning\code\test.py'))))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(r'D:\coding\py_learning\code\test.py'))))

# my_dir = r"D:\coding\py_learning\code"
# my_file = r"test.py"

# if os.path.exists(my_file):
#     print("file exists:", my_file)
# if os.path.isabs(my_dir):
#     print("path is abs:", my_dir)
# if os.path.isdir(my_dir):
#     print("path is dir:", my_dir)
# if os.path.isfile(my_file):
#     print(my_file, "is file")
# if not os.path.islink(my_file):
#     print(my_file, "is not a link.")
# if not os.path.ismount(my_dir):
#     print(my_dir, "is not a mount.")
# if os.path.samefile(os.path.join(my_dir, my_file), my_file):
#     print(os.path.join(my_dir, my_file), " and ", my_file, "is same.")

# import pickle
# my_list = list(range(5))
# my_tuple = tuple(range(5, 10))
# my_dict = dict.fromkeys(range(5), 'xxxxxx')
# my_set = set(x for x in range(7, 11))

# with open('my_list.pick', "wb") as list_file:
#     pickle.dump(my_list, list_file)

# with open('my_tuple.pick', "wb") as tuple_file:
#     pickle.dump(my_tuple, tuple_file)

# with open('my_dict.pick', "wb") as dict_file:
#     pickle.dump(my_dict, dict_file)

# with open('my_set.pick', "wb") as set_file:
#     pickle.dump(my_set, set_file)

# with open('my_list.pick', "rb") as my_list_file:
#     print(pickle.load(my_list_file))

# with open('my_tuple.pick', "rb") as my_tuple_file:
#     print(pickle.load(my_tuple_file))

# with open('my_dict.pick', "rb") as my_dict_file:
#     print(pickle.load(my_dict_file))

# with open('my_set.pick', "rb") as my_set_file:
#     print(pickle.load(my_set_file))

# a = int(input("Please in put a number:\n"))

# try:
#     f = open("这个文件不存在.txt",'rt')
# except OSError as reason:
#     print(reason)
    
# try:
#     f = open("这个文件不存在.txt",'rt')
# except TypeError as reason:
#     print(reason)
# except OSError as reason:
#     print(reason)
    
# try:
#     f = open("这个文件不存在.txt",'rt')
# except (TypeError, OSError,SyntaxError) as reason:
#     print(reason)
    


# try:
#     f = open("这个文件不存在.txt",'rt')
# except OSError as reason:
#     print(reason)
# finally:
#     #这里是没有办法访问try中的f，如果f在外面定义的话可能可以
#     #f.close() #NameError: name 'f' is not defined
#     print("不管怎样，这个都要执行")
    
# #with...[as var]
# #并不是所有的对象都支持with语句这一新的特性。只有支持上下文管理协议的对象才能使用with语句。

# try:
#     with open("这个文件不存在.txt",'rt') as f:
#         pass
# except OSError as reason:
#     print(reason)

# #可以主动抛出异常
# try:
#     x = 2
#     y = 3
#     if x < y:
#         raise OSError("这是主动抛出的")
# except OSError as reason:
#     print(reason)
    
# try:
#     pass
# finally:
#     print("try-finally 是可以省略异常处理过程的")


# x = 3
# y = 4

# if x > y:
#     print("x > y")
# else:
#     print("x <= y, 这个if....else...结构")

# for x in range(5):
#     my_index = 5
#     while x > 3 and my_index > 3:
#         print("while 循环条件满足 x = ", x,", my_index = ", my_index)
#         my_index -= 1
#     else:
#         print("while 循环的条件不满足 x = ", x, ", my_index = ", my_index)
# else:
#     print("for 循环的循环列表遍历完毕，才执行")


# for x in range(5):
#     if x > 2:
#         print("for 循环break以后是不会再执行for搭配的else")
#         break
# else:
#     print("for 循环的循环列表遍历完毕，才执行")

# for x in range(4):
#     if x < 5:
#         continue
# else:
#     print("for循环continue以后，会遍历完所有元素，所以这个会执行")

# try:
#     with open("这个文件不存在.txt", 'rb'):
#         pass
# except OSError as reason:
#     print("有异常发生，与try配对的else不会执行了")
# else:
#     pass

# try:
#     pass
#     pass
# except:
#     pass
# else:
#     print("没有异常发生, 与try配对的else执行")

# class Person:
#     __name_ = "xxxxxx"
#     __high  = "asdas"
#     def __init__(self, name, high):
#         self.__high = high
#         self.__name_= name
#     def getName(self):
#         return self.__name_
#     def __getHigh(self):
#         return self.__high
    
# me = Person("xxx", "183")
# #这样会报错'Person' object has no attribute '__name_'
# # print(me.__name_)
# # print(me.__high)
# #这样就对了
# print(me._Person__name_)
# print(me._Person__high)

# #AttributeError: 'Person' object has no attribute '__getHigh'
# #me.__getHigh()

# me._Person__getHigh()

# class BaseA:
#     name = "xxxx"

#     def __init__(self, name):
#         self.name = name
#         print("BaseA __init__")


# class BaseB:
#     school = "xxxx"

#     def __init__(self, school):
#         self.school = school
#         print("BaseB __init__")


# class BaseC:
#     phone = "xxxx"

#     def __init__(self, phone):
#         self.phone = phone
#         print("BaseC __init__")


# class Student:
#     address = "xxx"

#     def __init__(self, name, school, phone, address):
#         self.name = BaseA(name)
#         self.school = BaseB(school)
#         self.phone = BaseC(phone)
#         self.address = address

#     def printStudentInfo(self):
#         print("\nname: %s\nschool: %s\nphone: %s\naddress: %s"
#               % (self.name.name, self.school.school, self.phone.phone, self.address))


# stu = Student("sam", "mid", "123131", "asdfas")
# stu.printStudentInfo()

# class BB:
#     # def printBB()
#     def printBB(self):
#         print("This is BB")


# bb = BB()
# bb.printBB()
# #报错的原因是:使用实例对象调.方法的时候，python会把当前实例化的对象的地址当作第一个参数给方法
# #我们定义printBB的时候没有定义参数,

# #当printBB()加上self以后，BB.printBB() missing 1 required positional argument: 'self'
# #BB.printBB()
# #当printBB有参数self的时候，直接用类名.方法()的方式不行了，要求有一个self，而调用的时候没有
# BB.printBB(bb)  #这样就可以了

# 定制一个定时器类
# start和stop方法代表启动和停止计时
# 假设对象t1，print(t1)和直接调用t1均显示结果
# 当计时器未启动或已经停止计时时，调用stop方法会给予温馨的提示
# 两个计时器对象可以进行相加
# 只能使用提供的有限资源完成

# class Rectangle:
#     def __init__(self, width = 0, height = 0):
#         self.width = width
#         self.height = height
#         print("__init__")
#     def __setattr__(self, name, value):
#         if name == 'square':
#             self.__dict__["width"] = value
#             self.__dict__["height"] = value
#             print("__setattr__ if")
#         else:
#             self.__dict__[name] = value
#             print("__setattr__  var = ", name, ", value = ", value)
#     def getArea(self):
#         return self.width * self.height
    
# r1 = Rectangle(4,5)
# print(r1.__dict__)

# class MyProperty:
#     def __init__(self, fget=None, fset=None, fdel=None):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel

#     def __get__(self, instance, owner):
#         return self.fget(instance)

#     def __set__(self, instance, value):
#         self.fset(instance, value)

#     def __delete__(self, instance):
#         self.fdel(instance)


# class C:
#     def __init__(self):
#         self._x = None

#     def getX(self):
#         return self._x

#     def setX(self, value):
#         self._x = value

#     def delX(self):
#         del self._x
#     x = MyProperty(getX, setX, delX)


# c = C()
# c.x = 'X-man'
# print(c.x)
# print(c._x)
# del c.x
# print(c._x)

# ​如果说你希望定制的容器不可变的话，你只需要定义__len__()和__getitem__()方法

# ​如果希望定制的容器是可变的话，除了定义__len__()和__getitem__()以外，还需要定义__setitem__()和__delitem()__两个方法

# 可变的
# import 模块名字 as 新名字
import this 

#