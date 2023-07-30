from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app.models import *

# Create your views here.
def registration(request):
    d={'umfo':UserModelForm(),'pmfo':ProfileModelForm()}
    if request.method=='POST' and request.FILES :
        unfd=UserModelForm(request.POST)
        pmfd=ProfileModelForm(request.POST,request.FILES)
        if unfd.is_valid() and pmfd.is_valid():
            nsud=unfd.save(commit=False)
            submittedpw=unfd.cleaned_data['password']
            nsud.set_password(submittedpw)
            nsud.save()
            nspd=pmfd.save(commit=False)
            nspd.username=nsud
            nspd.save()
            

            send_mail (
                'regisration',
                'Registration successfull  ....... ! ',
                'tirukurisetty@gmail.com',
                [nsud.email],
                fail_silently=False
            )


            return HttpResponse('data inserted into admin')
    return render(request,'registration.html',d)

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else : 
                return HttpResponse('Not a active reponse')

        else:
            return HttpResponse('User Not Valid')
    return render(request,'user_login.html')
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)

    return render(request,'home.html')


    return render(request,'home.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



@login_required
def display_details(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'display_details.html',d)


@login_required
def change_password(request):
    if request.method=="POST":
        pw=request.POST['password']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('PASSWORD CHANGED SUCCESSFULLY')
    return render(request,'change_password.html')

def reset_password(request):
    if request.method=='POST':
        password=request.POST['password']
        username=request.POST['username']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(password)
            UO.save()
            return HttpResponse('Modify The password successfully')
        else:
            return HttpResponse('Username is not validate')
    return render(request,'reset_password.html')