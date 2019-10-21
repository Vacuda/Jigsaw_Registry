from django.shortcuts import render, redirect, HttpResponse
# from .models import (CLASSNAME)
from apps.log_and_reg_app.models import User

def index(request):
    return render(request, 'home_app/index.html')