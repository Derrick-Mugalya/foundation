from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Views
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # If user exists on our system
            auth.login(request, user)
            return redirect('entryform')
        else:
            print('Invalid credentials')
            messages.info(request, 'Invalid Cedentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    # Validate that a POST is being used
    if request.method == 'POST':
        username = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        # phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwod and password2 are similar
        if password == password2:
            # check if email exists in db
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,email=email, password=password)
                user.save()
                return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def entryform(request):
    return render(request, 'entryform.html')
