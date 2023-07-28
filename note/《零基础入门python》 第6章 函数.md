

@[TOC](文章目录)

---

# 前言
学习这部分内容之前，先说明我存在的疑问
1.如何创建python的函数？
2.函数的参数如何定义？
3.函数体如何书写？
4.函数的返回值怎么书写？
5.如何调用函数？

---
# 1.创建函数
## 1.1 函数的定义
	使用关键字def 函数名(参数列表): 封装起来的代码块。
## 1.2 创建函数时的注意事项
	1.使用def 函数名(参数列表):的格式定义
```python
def myFunc(name1, name2, name3):
    print("Hello world!!")
```
2.可以使用lambda表达式创建一个函数（lambda的返回值是一个函数）
格式： lambda 参数列表:返回值

```python
g = lambda x, y,z: x if x > y else z 
print(type(g))
#输出结果
#<class 'function'>
```
3.可以使用“”“说明”“”为函数添加注解
```python
#函数的注释放在def上面一行的化，只有看源码的时候才能看到
"""放这里行不行啊？？？？？不行，这个你自己看？？？"""
def myFunc(name1, name2, name3):
    """ 放在这里大家都看得到"""
    print("Hello world!!")

#help(名字)可以查看一些帮助内容，函数可以看到其注解
print(help(myFunc))
#输出结果
# Help on function myFunc in module __main__:

# myFunc(name1, name2, name3)
#     放在这里大家都看得到

# None
```

# 2.函数的参数
在定义函数的时候写的参数是形参，在调用的时候给的参数是实参
在定义的时候赋了值的参数是默认参数
在调用的时候把参数的名字带上这叫关键字参数
可以在形参前面加上一个或者两个星号
```python
def FunctionName(arg):
    print(arg)
FunctionName('xxxxxxxxx')

#arg1 给了默认值，那么后面的所有参数都必须给默认值
def FunctionName1(arg1 = 0, arg2 = 'sadfas'):
    print(arg2, arg1)

#有默认值的参数，调用时可以不给值
FunctionName1()

#有默认值的参数，调用时可以给一部分值
FunctionName1(2)

#有默认值的参数，调用时可以给全部值
FunctionName1(2,'xxxx')

#函数调用的时候，可以将值赋给指定的形参
FunctionName1(arg1=4,arg2="AAAAA")

#函数调用的时候，若指定形参的名字，那么参数的顺序可以和定义时不一致。
FunctionName1(arg2="BBBB", arg1=333)

#收集参数有两种：*和**
#第一种参数名字前加了一个*
def FunctionName2(*param, extra):
    print("extra = ", extra, "params size = ", len(param))

#带有收集参数和额外参数的情况，在调用时要指定额外的那个参数的名字赋值（关键字参数）
FunctionName2(1,3,4,5, extra='name')

#带一个收集参数的可以通过序列（列表，元组和字符串）赋值，但是需要解压（在调用时，在实参前加一个*）
#不解压的话，被看成一个整体赋值给params
#换个说法：不解压，那么list/tuple/str 被看作一个整体赋值给params,params中的值的个数为1
#解压后，list/tuple/str中的每个元素都塞给了params,params中值的个数是元素的个数
FunctionName2(*[1234,313,"xxxxx", 3.1415], extra= 'name')
FunctionName2(*(1,2,34,4,5,5,5,5,1234),extra='name')
FunctionName2(*"asjkdljfasjdlkf", extra='XXXX')

def FunctionName3(extra, *params):
     print("extra = ", extra, "params size = ", len(params))

#若收集参数和非收集参数混用，将非收集参数放在前面，在调用时可以使用关键字参数的方式给非收集参数赋值
FunctionName3('XXXXX', 1,3,4,5,5,6,2,3,3,3)

#第二种两个**的收集参数
#表示将收集参数打包成字典
def FunctionName4(extra, **params):
    print("extra = ", extra, "len(params) = ", len(params))

FunctionName4("dict", **{"2222":2222, "3333":3333})

#总结一下：*/**
#在函数定义的时候参数名前加表示打包*-打包成序列，**-打包成字典
#在函数调用的时候使用表示解压，将*将序列中的元素展开，**-将字典中的键值对展开

#输出结果
# xxxxxxxxx
# sadfas 0
# sadfas 2
# xxxx 2
# AAAAA 4
# BBBB 333
# extra =  name params size =  4
# extra =  name params size =  4
# extra =  name params size =  9
# extra =  XXXX params size =  15
# extra =  XXXXX params size =  10
# extra =  dict len(params) =  2
#最后的建议手动试试在调用有收集参数的函数时不解包（调用时不加*/**）
```
# 3.函数体
函数体中可以写入任何符合语法的语句，哪怕是再定义一个函数

在函数里边定义的参数以及变量，都称为局部变量

在函数中修改全局变量，在使用前，用"global 全局变量名" 的形式声明一下

内嵌函数的作用域在外部函数之内。

如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为闭包。

（内部函数用了外部函数的变量）

```python
global_name = "hello"
def myFunction(name = "aaaa"):
#在函数内部想要修改全局变量，使用前先用global声明一下
    global global_name 
    global_name = "myFunction add world"
    name1 = name;
    print("var name = ", name)
    def sunFunction():
#内部函数想要修改外部函数的变量，使用前用nonlocal声明一下
        nonlocal name1
#同样的，内部函数想要修改局部变量的值，也要在使用前用global声明一下
        global global_name
        print("local name1 = ", name1)
        name1 = name1 + " sunFunction add"
        global_name = global_name + "sunFunction add"
    sunFunction()
    print("local name1 = ", name1)


#
def nonModify(extra, *params):
    """ 只是用一下全局变量，并不修改"""
    print("nonmodify print :", global_name)
    print("nonmodity params print: extra = ", extra, ", params num = ", len(params))
    def nonModifySon(*params):
        param_index = 0
        for i in params:
            print("index = ", param_index, ", value = ", i)
            param_index += 1
        print('%s  %s   %s' %(str(global_name), str(extra), str(len(params))))
    nonModifySon(*params)

nonModify("test", *(1,2,3,4,5,1,3,2,4))

print("Before global global_name",global_name)
myFunction("xxxxx")
print("After global global_name",global_name)

```



# 4.函数的返回值

python中定义的函数都有返回值

当不写return 时函数默认返回None

```python
def noReturn():
    pass 
    pass

def hasReturn():
    pass
    pass
    return 1,2,3,4,5
```



# 5.如何调用函数

函数名(实参,...)

