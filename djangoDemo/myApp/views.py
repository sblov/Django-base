from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('myApp view is working!')

def detail(request, num):
    return HttpResponse('detail-%s'%num)

from .models import Grades, Students
def grades(request):
    # models中取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板渲染到页面
    return render(request, 'myApp/grades.html', {'grades': gradesList})

def students(request):
    # models中取数据
    studentsList = Students.stuObj1.all()
    # studentsList = Students.stuObj1.all()[0:4]
    # 将数据传递给模板，模板渲染到页面
    return render(request, 'myApp/students.html', {'students': studentsList})

from django.db.models import Max, Min
def studentsSearch(request):
    
    # studentsList = Students.stuObj1.all().filter(sname__contains='J')
    # studentsList = Students.stuObj1.all().filter(sname__startswith='J')
    # studentsList = Students.stuObj1.all().filter(pk__in=[1,3,5])
    studentsList = Students.stuObj1.filter(Q(pk__lt=2) | Q(sage__gt=21))

    maxAge  = Students.stuObj1.aggregate(Max('sage'))
    print(maxAge, '-------------------------')
    return render(request, 'myApp/students.html', {'students': studentsList})

from django.db.models import F, Q
def gradesSearch(request):
   
    # gradesList = Grades.objects.filter(ggirlnum__lt=F('gboynum')+1)
    gradesList = Grades.objects.filter(students__scontend__contains='J')
    
    return render(request, 'myApp/grades.html', {'grades': gradesList})


def gradesStudents(request, num):
    grade = Grades.objects.get(pk=num)
    
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {'students': studentsList})

def editStudent(request):
    
    return render(request, 'myApp/editstu.html')

def addStudent(request):
    grade = Grades.objects.get(pk=1)

    # stu = Students.createStudent('Tony', 20, True, 'this is demo,Tony',grade)
    stu = Students.stuObj1.createStudent('Tony', 20, True, 'this is demo,Tony',grade)
    stu.save()
    return HttpResponse('Save Success!')

def attributes(request):
    
    return render(request, 'myApp/attributes.html', {'request': request})

def exciting(request):
    
    return render(request, 'exciting.html')

# get/?a=0&a=1&b=2&c=3
def getMethod(request):

    a = request.GET.getlist('a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    return HttpResponse(a[0]+' '+a[1]+' '+b+' '+c)

def showRegister(request):

    return render(request, 'myApp/register.html')

# form / POST
def regist(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    return HttpResponse(name+' '+gender+' '+age+' '+hobby[0]+' ')

'''
    原型 ： render(request, templateName[, context])
    作用 ： 结合数据和模板，返回完整的HTML页面
    参数 : request【请求体对象】， templateName【模板路径】， context【传递给需要渲染在模板上的数据】
'''
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirectView(request):
    # return HttpResponseRedirect('/myApp/showRegister')
    return redirect('/myApp/showRegister')

def main(request):
    
    return render(request, 'myApp/login.html')
# 设置session
def login(request):
    username = request.POST.get('username')
    request.session['username'] = username
    request.session.set_expiry(20)
    return redirect('/myApp/home')

def home(request):
    username = request.session.get('username', 'anonymous')

    return render(request, 'myApp/home.html', {'username': username})

from django.contrib.auth import logout
def quit(request):
    # 清除Session
    logout(request)
    # request.session.clear()
    # request.session.flush()

    return redirect('/myApp/home')

def test(request):
    return render(request, 'myApp/test.html',{'num': 10})

# 验证码
def verifyCode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str = '1234567890QWERTUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选择4个值为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\ARLRDBD.TTF', 40)
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 绘制四个字
    draw.text((5,2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25,2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50,2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75,2), rand_str[3], font=font, fill=fontcolor4)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifyCode'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为PNG
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，mime类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def verifyCodeLogin(request):
    return render(request, 'myApp/vclogin.html')

def verifyCodeCheck(request):

    vctext = request.POST.get('vctext').upper()
    vc_s = request.session.get('verifyCode').upper()
    print(vc_s)
    if vctext == vc_s:
        return HttpResponse('Success!')
    return HttpResponse('Failure!')



