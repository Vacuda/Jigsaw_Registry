from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages

def index(request):
    return render(request,'log_and_reg_app/index.html')

def register(request):
    if request.method=="POST":
        ##Run Registration Validator
        errors = User.objects.registration_validator(request.POST)
        ##If Errors
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/login')
        ##If No Errors
        else:
            ##Hash Password
            password = request.POST['password']
            pw_hash=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            ##Create User
            User.objects.create(
                username        = request.POST['username'],
                first_name      = request.POST['first_name'],
                last_name       = request.POST['last_name'],
                birth_date      = request.POST['birth_date'],
                email           = request.POST['email'],
                password        = pw_hash,
                )
            #Create Session
            request.session['user_id']=User.objects.last().id
            request.session['first_name']=User.objects.last().first_name
            return redirect('/login/success')
    return redirect('/login')

def login(request):
    if request.method=="POST":
        ##Checks For Email
        user = User.objects.filter(email=request.POST['email'])
        ##If Found
        if user:
            ##Password Match
            if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                request.session['user_id']=user[0].id
                request.session['first_name']=user[0].first_name
                return redirect('/login/success')
        #No User Match, or No Password Match
        messages.error(request, "Email or Password is not correct", extra_tags="login")
        return redirect('/login')
    return redirect('/login')

def success(request):
    if not 'user_id' in request.session:
        messages.error(request, "You are not logged in!", extra_tags="login")
        return redirect('/login')
    return render(request,'home_app/index.html')
    
def reset(request):  
    del request.session['first_name']
    del request.session['user_id']
    return redirect('/login')
