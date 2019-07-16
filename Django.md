# Django

## 一、简介

​	一个开放源代码的Web应用框架，由Python写出

​	初次发布于2005年7月，并于2008年9月发布 第一个正式版本1.0

### MTV

​	本质上于MVC模式没有区别，只是定义上有些不同

- Model  负责业务对象于数据库的对象
- Template   负责如何把页面展示给用户
- View   负责业务逻辑，并在适当的时候调用Model于Template

​	Django有一个url分发器，将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template

## 二、创建

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

## 三、基本流程

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

## 四、模型

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

### 模型成员

#### 类属性

- **objects**

​	是Manager类型的一个对象，作用是与数据库进行交互；当定义模型类没有指定管理器，则Django为模型创建一个名为objects的管理器

- **自定义管理器**

```python
class Students(models.Model):
    # 自定义模型管理器
    # 当自定义模型管理器,objects就不存在了
    stuObj = models.Manager()
    
    ...........
```

当为模型指定模型管理器后，Django就不会为模型生成objects模型管理器

![1561862174879](img/1561862174879.png)

- **自定义管理器Manager类**

​    模型管理器是Django的模型与数据库进行交互的接口，一个模型可以有多个模型管理器

​	**作用：1）向管理类中添加额外的方法；2）修改管理器返回的原始查询集（如：重写get_queryset()方法）**

```python
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete='False')

class Students(models.Model):
    # 自定义模型管理器
    # 当自定义模型管理器,objects就不存在了
    stuObj0 = models.Manager()
    stuObj1 = StudentsManager()
    ............
```

#### 创建对象

​	向数据库中添加数据

​	当创建对象时，django不会对数据库进行读写操作，当调用save()方法时才与数据库交互，将对象保存到数据表中

\__init__方法已经在父类models.Model中使用，在自定义的模型中无法使用

在模型类中增加一个类方法

```python
class Students(models.Model):
    ...........
	
    @classmethod
    def createStudent(cls, name, age, gender, contend, grade, isDel=False):
        stu = cls(sname=name, sage=age, sgender=gender, scontend=contend,sgrade=grade, isDelete=isDel)
        return stu
------------------------------------------------
使用：
    grade = Grades.objects.get(pk=1)

    stu = Students.createStudent('Tony', 20, True, 'this is demo,Tony',grade)
    stu.save()
```

在定义管理器中添加一个方法

```python
class StudentsManager(models.Manager):
    ..........
    def createStudent(self, name, age, gender, contend, grade, isDel=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        
        return stu
-----------------------------------------------
使用：
	stu = Students.stuObj1.createStudent('Tony', 20, True, 'this is demo,Tony',grade)
```

### 模型查询

​	查询集可以有多个过滤器，过滤器就是一个函数，基于所给的参数限制查询集结果；相当于where

查询集

- 在管理器上调用过滤器方法返回查询集

- 查询集经过过滤器筛选后返回新的查询集，所以可以写成链式调用

- 惰性执行：创建查询集不会带来任何数据的访问，直到调用数据时，才会访问数据

- 直接访问数据：迭代；序列化；与if合用

- 返回查询集的方法称为过滤器：all()，filter()，exclude()，order_by()，values()

- 返回单个数据：
  - get()：返回单个满足条件的对象；如果没找到符合对象，或找到多个对象都会引发异常
  - count()：返回当前查询集中的对象个数
  - first()：返回查询集中的第一个对象
  - last()：最后一个对象
  - exists()：判断查询集是否有数据，返回boolean值
  
- 限制查询集：查询集返回列表，可以使用下标的方法进行限制，等同于limit（`studentsList = Students.stuObj1.all()[0:4]`）

- 查询集的缓存：每个查询集都包含一个缓存，来最小化对数据库的访问；在新建的查询集中，缓存首次为空，第一次查询集求值，django会将查询出来的数据做一个缓存，并返回查询结构，以后的查询直接使用查询集的缓存

- 字段查询：实现了sql中的where语句，作为方法filter()，exclude()，get()的参数；语法：`属性名称__比较运算符=值`
  - 比较运算符
  
    |                                                |                                                              |
    | ---------------------------------------------- | ------------------------------------------------------------ |
    | exact                                          | 判断，大小写敏感<br>`filter(isDelete=False)`                 |
    | contains                                       | 是否包含，大小写敏感<br>`studentsList = Students.stuObj1.all().filter(sname__contains='J')` |
    | startswith/endswith                            | 以value开头/结尾，区分大小写<br>`studentsList = Students.stuObj1.all().filter(sname__startswith='J')` |
    | iexact/icontains.......                        | 以上运算符前加上`i`，即不区分大小写                          |
    | in                                             | 是否包含在范围内<br>`studentsList = Students.stuObj1.all().filter(pk__in=[1,3,5])` |
    | gt/gte/lt/lte                                  | 大于/大于等于/小于/小于等于                                  |
    | year/month/day/week_day/<br>hour/minute/second | `Students.stuObj1.all().filter(lastTime__year=2019)`         |
    | 跨关联查询                                     |                                                              |
    | 查询快捷                                       | pk：代表主键                                                 |
  
  - 聚合函数
  
    使用aggregate()函数返回聚合函数的值
  
  |       |                                                              |
  | ----- | ------------------------------------------------------------ |
  | Avg   | `from django.db.models import Max, Min`<br>`maxAge  = Students.stuObj1.aggregate(Max('sage'))` |
  | Count |                                                              |
  | Max   |                                                              |
  | Min   |                                                              |
  | Sum   |                                                              |
  
  - F对象
  
    可以使用模型的A属性与B属性进行比较
  
    `from django.db.models import F, Q`
  
    `gradesList = Grades.objects.filter(ggirlnum__lt=F('gboynum')+1)`
  
    **支持F对象的算术运算，时间也可运算**
  
  - Q对象
  
    过滤器的方法中的关键字参数，条件为and模式
  
    `studentsList = Students.stuObj1.filter(Q(pk__lt=2) | Q(sage__gt=21))`
  
    `~Q(pk=1)` ：取反

## 五、视图

​	视图接受web请求，并响应；视图就是一个python中的函数

### 配置流程

**设置根级url配置文件**

> setting.py文件中：
>
> `ROOT_URLCONF = 'djangoDemo.urls'`

**urlpatterns**

​	url实例的列表

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myApp/', include('myApp.urls'))
]
```

> ​	在应用中创建urls.py文件，定义本应用的url配置，在工程urls.py文件中使用include()方法
>
> 1、` path('myApp/', include('myApp.urls'))`
>
> 2、myApp/urls.py
>
> ```python
> from django.urls import path, re_path
> from . import views
> 
> urlpatterns = [
>     path('', views.index),
>     re_path(r'^(\d+)/$', views.detail),
>     re_path(r'^grades/$', views.grades),
>     re_path(r'^students/$', views.students)
> ]
> ```
>
> 

**URL反向解析**

​	在视图、模板中使用硬编码链接，在url配置改变时，动态生成链接的地址

​	==**在使用链接时，通过url配置的名称，动态 生成url地址**==

### 视图函数

​	视图参数为一个HttpRequest实例，以及获取的路径参数

```python
def index(request):
    return HttpResponse('myApp view is working!')
```

#### 错误视图

**404视图**

​	1、在templates下定义404.html

```html
	<div class="container">
        <header>
            <h1>Page no found!</h1>
        </header>
        <h3>{{request_path}}</h3>
    </div>
```

​	2、配置setting.py

```python
DEBUG = False

ALLOWED_HOSTS = ['*', ]
```

### HttpRequest对象

​	服务器接收http请求后，会根据报文创建HttpRequest对象；视图的第一个参数就是HttpRequest对象；django创建后调用视图传递给视图

#### 属性

- path ：请求的完整路径（不包括域名和端口）
- method ： 表示请求的方式，常有的有GET、POST
- encoding ： 表示浏览器提交的数据的编码方式，一般为utf-8
- GET ：类似字典的对象，包含了get请求的所有参数
- POST ：类似字典的对象，包含了POST请求的所有对象
- FILES ：类似字典的对象，包含了所有上传的文件
- COOKIES ：字典，包含所有cookie
- session ： 类似字典的对象，表示当前会话

#### 方法

​	is_ajax() ：如果通过XMLHttpRequest发起的请求，返回True

#### QueryDict对象

​	request对象中的GET、POST都属于QueryDict对象

​	方法：

- get() ： 根据键获取值，返回单值
- getlist() ：将键的值以列表的形式返回，返回多个值

#### GET属性

```python
# get/?a=0&a=1&b=2&c=3
def getMethod(request):

    a = request.GET.getlist('a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    return HttpResponse(a[0]+' '+a[1]+' '+b+' '+c)
```

#### POST属性

```python
# form / POST
def regist(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')

    return HttpResponse(name+' '+gender+' '+age+' '+hobby[0]+' ')
```

### HttpResponse对象

​	给浏览器返回数据；HttpRequest对象由django创建的，HttpResponse对象手动创建

**用法：**

- 不调用模板，直接返回数据 : `return HttpResponse('.........')`

- 调用模板，使用render方法

  ```python
  '''
      原型 ： render(request, templateName[, context])
      作用 ： 结合数据和模板，返回完整的HTML页面
      参数 : request【请求体对象】， templateName【模板路径】， context【传递给需要渲染在模板上的数据】
  '''
  
  return render(request, 'myApp/attributes.html', {'request': request})
  ```

#### 属性

- content ： 表示返回的内容类型
- charset ： 编码格式
- status_code ：响应状态码
- content-type ： 指定输出的MIME类型

#### 方法

- init ： 使用页面内容实例化HttpResponse对象
- write(content) ： 以文件形式写入
- flush() ： 以文件形式输出到缓冲区
- set_cookie(key, value='', max_age=None, exprise=None)
- delete_cookie(key) ： 删除cookie；删除不存在cookie不会报错

#### HttpResponseRedirect

​	重定向，服务器端跳转

```python
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirectView(request):
    # return HttpResponseRedirect('/myApp/showRegister')
       
    return redirect('/myApp/showRegister')
```

#### JsonResponse

​	返回json数据，一般用于异步请求，Content-type类型为application/json

### 状态保持

​	http协议是无状态的，每次请求都是一次新的请求；客户端与服务器的一次通信就是一次会话；实现状态保持，在客户端或服务端存储有关会话的数据（session/cookie）

​	目的：在一段时间内跟踪请求者的状态，可以实现跨页面访问当前的请求者的数据

#### 启用session

​	settings.py 文件中

```python
INSTALLED_APPS = [
    ....
    'django.contrib.sessions',
]

MIDDLEWARE = [
    ....
    'django.contrib.sessions.middleware.SessionMiddleware',
]
```

#### 使用session

- 启用session后，每个HttpRequest对象中都有一个session属性，类似字典的对象
- get(key, default=None) ：根据键获取session值
- clear()：清空所有会话
- flush()：删除当前的会话并删除会话的cookie

# 报错

**1、Django2.2报错 AttributeError: 'str' object has no attribute 'decode'**

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

**2、跨域问题**

![1563260063934](img/1563260063934.png)

​	暂时将`'django.middleware.csrf.CsrfViewMiddleware'`中间件注释

![1563260173278](img/1563260173278.png)