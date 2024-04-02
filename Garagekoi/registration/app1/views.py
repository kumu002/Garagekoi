from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        fname=request.POST.get('fullname')
        uname=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')

    return render(request,'RegistrationForm.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        pass1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password Incorrect!!")
    return render(request,'index.html')