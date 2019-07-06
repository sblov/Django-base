from django.shortcuts import render
from django.http import HttpResponse
from .models import faceJav

# Create your views here.

def index(request):
    ck = request.session.get("username")
    if not ck:
        return render(request, 'xFun/login.html')

    fjList  = faceJav.fjObject.get_queryset()[0:24]

    return render(request, 'xFun/index.html',{'fjList':fjList, 'prePage':0, 'nexPage':2})

def indexPage(request, page):
    ck = request.session.get("username")
    if not ck:
        return render(request, 'xFun/login.html')

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

def loginView(request):
    
    return render(request, 'xFun/login.html')


from django.http import HttpResponseRedirect
from .models import User
from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def loginSubmit(request):

    user = request.POST['xfun_user']
    psw = request.POST['xfun_password']
    print(user, psw)

    user = User.objects.all().filter(Q(username__contains=user) , Q(password__contains=psw))
    
    if len(user) != 0:
        request.session['username'] = 1
        request.session.set_expiry(0) 
        return HttpResponseRedirect('/xfun/')

    return render(request, 'xFun/login.html')

    
