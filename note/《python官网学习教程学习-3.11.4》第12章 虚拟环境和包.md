# 12. 虚拟环境和包

## 12.1. 概述

Python应用程序通常会使用不在标准库内的软件包和模块。应用程序有时需要特定版本的库，因为应用程序可能需要修复特定的错误，或者可以使用库的过时版本的接口编写应用程序。

这意味着一个Python安装可能无法满足每个应用程序的要求。如果应用程序A需要特定模块的1.0版本但应用程序B需要2.0版本，则需求存在冲突，安装版本1.0或2.0将导致某一个应用程序无法运行。

这个问题的解决方案是创建一个 virtual environment，一个目录树，其中安装有特定Python版本，以及许多其他包。

然后，不同的应用将可以使用不同的虚拟环境。 要解决先前需求相冲突的例子，应用程序 A 可以拥有自己的 安装了 1.0 版本的虚拟环境，而应用程序 B 则拥有安装了 2.0 版本的另一个虚拟环境。 如果应用程序 B 要求将某个库升级到 3.0 版本，也不会影响应用程序 A 的环境。

## 12.2. 创建虚拟环境

venv 模块用于创建和管理虚拟环境。

```python
# 创建 tutorial-env 目录，如果它不存在的话，并在其中创建包含 Python 解释器副本和各种支持文件的目录。
# 虚拟环境的常用目录位置是 .venv。 这个名称通常会令该目录在你的终端中保持隐藏，从而避免需要对所在目录进行额外解释的一般名称。 
# 它还能防止与某些工具所支持的 .env 环境变量定义文件发生冲突。
python -m venv tutorial-env
```

激活虚拟环境

```python
# 在Windows上，运行:
tutorial-env\Scripts\activate.bat
# 在Unix或MacOS上，运行:
source tutorial-env/bin/activate
```

去激活虚拟环境

```python
deactivate
```

## 12.3. 使用pip管理包

使用pip安装包：

```python
# python -m pip install 包名
python -m pip install novas
```

使用pip安装指定版本的包

```python
# 可以通过提供包名称后跟 == 和版本号来安装特定版本的包
python -m pip install requests==2.6.0
```

更新包

```python
# python -m pip install --upgrade 包名字
python -m pip install --upgrade requests
```

查看某个包的信息

```python
# python -m pip show 包名
python -m pip show requests
```

查看当前已经安装的包

```python
# 展示当前虚拟环境中安装的所有包的
python -m pip list
# novas (3.1.1.3)
# numpy (1.9.2)
# pip (7.0.3)
# requests (2.7.0)
# setuptools (16.0)
```

```python
# 按照 “python -m pip install”的格式展示当前已经安装的包。
python -m pip freeze
# novas==3.1.1.3
# numpy==1.9.2
# requests==2.7.0
```

卸载包

```python
# python -m pip uninstall 包1[ 包2 ...]
python -m pip uninstall novas
```

