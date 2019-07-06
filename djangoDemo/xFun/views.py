from django.shortcuts import render
from django.http import HttpResponse
from .models import faceJav

# Create your views here.

def index(request):
    fjList  = faceJav.fjObject.get_queryset()[0:24]

    return render(request, 'xFun/index.html',{'fjList':fjList, 'prePage':0, 'nexPage':2})

def indexPage(request, page):
    print(page)
    sIndex = (int(page)-1)*24
    eIndex = (int(page))*24
    fjList  = faceJav.fjObject.get_queryset()[sIndex:eIndex]

    if len(fjList) < 24:
        nexPage = 0
    else:
        nexPage = int(page)+1


    return render(request, 'xFun/index.html',{'fjList':fjList, 'prePage':int(page)-1, 'nexPage':nexPage})

def allView(request, htmlName):
    return render(request, 'xFun/'+htmlName+'.html')
