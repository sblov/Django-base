# Django

## 简介

​	一个开放源代码的Web应用框架，由Python写出

​	初次发布于2005年7月，并于2008年9月发布 第一个正式版本1.0

### MTV

​	本质上于MVC模式没有区别，只是定义上有些不同

- Model  负责业务对象于数据库的对象
- Template   负责如何把页面展示给用户
- View   负责业务逻辑，并在适当的时候调用Model于Template

​	Django有一个url分发器，将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template

## 创建

### 新建项目结构

​		`django-admin startproject projectname` 命令创建django基本项目结构

​	**目录结构**

```shell
djangoDemo			
    │  manage.py	#命令工具，对django项目进行交互
    │
    └─djangoDemo
          settings.py	#项目配置文件
          urls.py		#项目的url声明
          wsgi.py		#项目与WSGI兼容的Web服务入口
          __init__.py 	#空文件，表示该目录为python包
        
```

### 配置数据库

​	**Django默认使用SQLite数据库**

​	**在settings.py文件中，通过DATABASES选项进行数据库配置**

![1558357603575](img/1558357603575.png)

>**python3.x 安装 PyMySQL**
>
>**\_init_.py写入**
>
>```python
>import pymysql
>
>pymysql.install_as_MySQLdb()
>```
>
>**settings.py配置数据库**
>
>```python
>DATABASES = {
>    'default': {
>        'ENGINE': 'django.db.backends.mysql',
>        'NAME':'djangoDemo',
>        'USER':'root',
>        'PASSWORD':'root',
>        'HOST':'localhost',
>        'PORT':3306,
>    }
>}
>```

### 创建应用

​	**一个项目中可以创建多个应用，每个应用进行一种业务处理**

​	**在项目根目录下执行`python manage.py startapp appName`**

​	**应用目录**