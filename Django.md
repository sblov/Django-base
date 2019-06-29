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

>**1、python3.x 安装 PyMySQL**
>
>**2、\_init_.py写入**
>
>```python
>import pymysql
>
>pymysql.install_as_MySQLdb()
>```
>
>**3、settings.py配置数据库**
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

```shell
admin.py：站点配置

models.py：模型

views.py：试图
```

### 激活应用

​	在`setting.py`文件中，将创建的应用名加入到`INSTALLED_APPS`中

### 定义模型

​	一个数据表，就对应一个模型

>- 在models.py文件中定义模型
>
>- 引入`from django.db import models`
>
>- 模型类要继承models.Model类
>- 不需要定义主键，会自动生成，为自增

### 在数据库生成数据表

**`python manage.py makemigrations`** ：生成迁移文件在，migrations目录下生成一个迁移文件，此时数据库还没有生成表

![1561643510677](img/1561643510677.png)

**`python manage.py migrate`** ：执行迁移，相当于执行sql语句创建数据表

![1561643930173](img/1561643930173.png)

### 测试数据操作

**`python manage.py shell`** ： 进入python shell

引入包：

```pytho
from myApp.models import Grades,Students
from django.utils import timezone
from datetime import * 
```

![1561645360960](D:\git-rep\django\img\1561645360960.png)

![1561646391127](img/1561646391127.png)

### 启动服务

​	**`python manage.py runserver ip:port`**

​	ip可以不写（默认是本机IP），端口号默认为8000

​	该方式是存python写的轻量级web服务器，仅在开发测试中使用

![1561646807758](img/1561646807758.png)

![1561646780817](img/1561646780817.png)

### Admin站点管理

​	负责添加、修改、删除内容（数据库），公告访问

#### **配置Admin应用(setting.py)**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
```

#### **创建管理员用户**

​	**`python manage.py createsuperuser`**

![1561647256269](img/1561647256269.png)

![1561647279847](img/1561647279847.png)

#### **国际化**

​	修改setting.py，重启服务

```python
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/ShangHai'
```

#### **管理数据表**

​	**修改admin.py**

![1561708424458](img/1561708424458.png)

![1561708455818](img/1561708455818.png)

​	**自定义管理页面**

```python
class GradesAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_filter = ['gname']
    search_fields = ['gname', 'gboynum']
    list_per_page = 10

    # 添加、修改页属性
    # fields与fieldsets属性不能同时使用
    # fields = ['gname', 'isDelete']
    fieldsets = [
        ('num',{'fields':['ggirlnum','gboynum']}),
        ('base',{'fields':['gname','gdate','isDelete']})
    ]

admin.site.register(Grades, GradesAdmin)
```

![1561709749784](img/1561709749784.png)

![1561709771585](img/1561709771585.png)

​	**关联属性**

```python
class StudentsInfo(admin.TabularInline): #StackedInline
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
```

![1561711024682](img/1561711024682.png)

​	**其他属性**

```python
# 使用装饰器注册
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 设置列值
    def gender(self):
        if self.sgender:
            return 'man'
        else:
            return 'woman'
    # 设置页面列的名称
    gender.short_description = '性別'

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False
```

### 试图基本使用

​	在django中，试图对web请求进行回应

​	试图是一个python函数，在views.py中定义

**定义试图——修改views.py**

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('myApp view is working!')
```

**配置url**

```python
# 修改项目目录下的urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls'))
]
------------------------------------------------
# 指定应用下新建urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^(\d+)/$', views.detail)
]
```

### 模板基本使用

​	模板是html页面，可以根据试图中传递过来的数据进行填充

#### 1、创建模板

​	创建templates目录，在目录下创建对应项目的模板模板

![1561780979222](img/1561780979222.png)

#### 2、配置模板路径

​	修改setting.py文件的templates，`os.path.join(BASE_DIR, 'templates')`

![1561781075898](img/1561781075898.png)

#### 3、定义模板内容

![1561781157459](img/1561781157459.png)

#### 4、定义视图 

​	(myApp/views.py)

```python
from .models import Grades, Students
def grades(request):
    # models中取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板渲染到页面
    return render(request, 'myApp/grades.html', {'grades': gradesList})
```

#### 5、配置url

![1561781304646](img/1561781304646.png)

### 模型-表修改

​	将数据库与迁移文件直接删除，重新生成迁移文件，迁移进数据库

## 基本流程

> - 创建工程（`django-admin startproject project`）
> - 创建项目（`python manage.py startapp myApp`）
> - 激活项目（`修改settings.py中的INSTALLED_APPS`）
> - 配置数据库（`修改__init__.py文件`，`修改settings.py中的DATABASES`）
> - 创建模型类（`在项目目录下的 models.py文件中`）
> - 生成迁移文件（`python manage.py makemigrations`）
> - 执行迁移（`python manage.py migrate`）
> - 配置站点（）
> - 创建项目模板/项目模板目录
> - 在settings.py文件中`TEMPLATES`配置模板路径
> - 在project下修改urls.py
> - 在项目目录下创建urls.py

## 模型

​	Django对各种数据库提供了很好的支持，Django为这些数据库提供了统一的调用API，可以根据不同的业务需求选择不同的数据库

**开发流程**

- 配置数据库
- 定义模型类
- 生成迁移文件
- 执行迁移生成数据表
- 使用模型类进行CRUD操作

**ORM**

- 根据对象的类生成表结构
- 将对象、列表的操作转换为sql语句
- 将sql语句查询的结果转换为对象、列表

### 模型定义

#### 定义属性

> ​	Django根据属性的类型确定：
>
> - 当前选择的数据库支持字段的类型
> - 渲染管理表单时使用的默认html控件
> - 在管理站点最低限度的验证

==django会为表增加自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后，django不会再生成默认的主键列==

> ​	定义属性时，需要字段类型，字段类型被定义在`django.db.models.fields`目录下，为方便使用，被导入到`django.db.models`中
>
> ![1561794509839](img/1561794509839.png)

##### **字段Fields**

```python
AutoField\CharField\TextField\IntegerField\DecimalField\FloatField\BooleanField\NullNooleanField\DateField\TimeField\DateTimeField\FileField\ImageField
```

##### **字段选项**

​	通过字段选项，实现字段的约束，在字段对象中通过关键字参数指定

| 选项        | 含义                                                      |
| ----------- | --------------------------------------------------------- |
| null        | 如果为True，Django将空值以NULL存储到数据库，默认值为False |
| blank       | 如果为True，则该字段允许为空白，默认值为False             |
| db_column   | 字段的名称，如果未指定，则使用属性的名称                  |
| db_index    | 如果为True，则在表中会为此字段创建索引                    |
| default     | 默认值                                                    |
| primary_key | 如果为True，则该字段会成为模型的主键字段                  |
| unique      | 如果为True，该字段在表中必须有唯一值                      |

##### **模型关系**

| 字段类          | 含义                         |
| --------------- | ---------------------------- |
| ForeignKey      | 一对多，将字段定义在多的端   |
| ManyToManyField | 多对多，将字段定义在两端     |
| OneToOneField   | 一对一，将字段定义在任意一端 |

**访问方式**

> 一对多：`一方对象.模型类小写_set` ：`grade.students_set`
>
> 一对一：`对象.模型类小写` ：`grade.students`
>
> 访问id：`对象.属性_id` ：`student.sgrade_id`

#### 元选项

​	在模型类中定义Meta类，用于设置元信息

```python
class Students(models.Model):
    ..........

    class Meta:
        # 数据表名
        db_table = 't_student'
        # 查询时以id排序， '-id'为降序
        ordering = ['id'] 

```



# 报错

**Django2.2报错 AttributeError: 'str' object has no attribute 'decode'**

> 1、d:\Python\lib\site-packages\django\db\backends\mysql\operations.py
>
> 2、
>
> ```python
> def last_executed_query(self, cursor, sql, params):
>         # With MySQLdb, cursor objects have an (undocumented) "_executed"
>         # attribute where the exact query sent to the database is saved.
>         # See MySQLdb/cursors.py in the source distribution.
>         query = getattr(cursor, '_executed', None)
>        
>     #注释该段代码
>         # if query is not None:
>         #     query = query.decode(errors='replace')
>         return query
> ```
>
>  query 是 str 类型，而 `decode()` 是用来将 bytes 转换成 string 类型用的，[（关于Python编码点这里）](https://www.cnblogs.com/dbf-/p/10572765.html)，由于 query 不需要解码，所以直接将 if 语句注释掉