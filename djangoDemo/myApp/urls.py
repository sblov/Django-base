from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^(\d+)/$', views.detail),
    re_path(r'^grades/$', views.grades),
    re_path(r'^students/$', views.students),
    re_path(r'^grades/(\d+)$', views.gradesStudents),
    re_path(r'^addstudent/$', views.addStudent),
    re_path(r'^editstudent/$', views.editStudent),
    re_path(r'^studentssearch/$', views.studentsSearch),
    re_path(r'^gradessearch/$', views.gradesSearch),
    re_path(r'^attributes/$', views.attributes)
]