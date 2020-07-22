from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password = password1)
                user.save();
                print('user created')
                return redirect('/')
        else:
            messages.info(request,'password does not match')
            return redirect('register')

            
         
    else:
        return render(request,'register.html')
    
def login(request):
    return render(request,'login.html')

