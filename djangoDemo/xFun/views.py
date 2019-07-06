from django.shortcuts import render
from django.http import HttpResponse
from .models import faceJav

# Create your views here.

def index(request):
    fjList  = faceJav.fjObject.get_queryset()

    # print(fjList)

    return render(request, 'xFun/index.html',{'fjList':fjList})

def allView(request, htmlName):
    return render(request, 'xFun/'+htmlName+'.html')
