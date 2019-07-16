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
def login(request):
    username = request.POST.get('username')
    request.session['username'] = username
    
    return redirect('/myApp/home')

def home(request):
    username = request.session.get('username', 'anonymous')

    return render(request, 'myApp/home.html', {'username': username})


