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
    # 将数据传递给模板，模板渲染到页面
    return render(request, 'myApp/students.html', {'students': studentsList})

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

    