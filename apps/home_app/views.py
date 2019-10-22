from django.shortcuts import render, redirect, HttpResponse
# from .models import (CLASSNAME)
from apps.log_and_reg_app.models import User

def index(request):
    if not 'user_id' in request.session:
        return redirect('/login')

    return render(request, 'home_app/index.html')