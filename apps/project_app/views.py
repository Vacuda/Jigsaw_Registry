from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_reg_app.models import User

def index(request):
    return render(request, 'project_app/index.html')