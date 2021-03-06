from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
     if request.method == 'POST':
          if request.POST['password1'] == request.POST['password2']:
               try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'home/signup.html',{'error':'Username has already been taken'})
               except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    auth.login(request,user)
                    return render(request,'home/signup.html',{'flag':'true'})
     else:
          return render(request, 'home/signup.html')