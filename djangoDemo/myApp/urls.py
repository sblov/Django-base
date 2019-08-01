from django.urls import path, re_path
from . import views

app_name = '[myApp]'

urlpatterns = [
    path('', views.index),
    re_path(r'^(\d+)/$', views.detail),
    re_path(r'^grades/$', views.grades),
    re_path(r'^students/$', views.students),
    re_path(r'^grades/(\d+)$', views.gradesStudents, name='grades'),
    re_path(r'^addstudent/$', views.addStudent),
    re_path(r'^editstudent/$', views.editStudent),
    re_path(r'^studentssearch/$', views.studentsSearch),
    re_path(r'^gradessearch/$', views.gradesSearch),
    re_path(r'^attributes/$', views.attributes),
    re_path(r'^exciting/$', views.exciting),
    re_path(r'^get/$', views.getMethod),
    re_path(r'^showRegister/$', views.showRegister),
    re_path(r'^showRegister/regist/$', views.regist),
    re_path(r'^redirectView/$', views.redirectView),
    re_path(r'^login/$', views.login),
    re_path(r'^main/$', views.main),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^logout/$', views.quit),
    re_path(r'^test/$', views.test),
    re_path(r'^verifyCode/$', views.verifyCode, name='vc'),
    re_path(r'^vclogin/$', views.verifyCodeLogin),
    re_path(r'^vccheck/$', views.verifyCodeCheck, name='vccheck'),
    re_path(r'^savefile/$', views.saveFile, name='savefile'),
    re_path(r'^spage/(\d+)$', views.studentPage, name='spage'),
]