from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'authenticate/home.html')

def user_reg(request):
    page ='reg'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = name
            myuser.save()
            messages.success(request, "Account has been successfully created.")
            return redirect('home')
        else:
            return HttpResponse('Diffrent Password')
    context = {'page':page}
    return render(request, 'authenticate/login.html', context)