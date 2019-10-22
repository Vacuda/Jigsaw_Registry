from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_reg_app.models import User

def index(request):
    return render(request, 'project_app/index.html')

def add_project(request):
    return render(request, 'project_app/project_add_page.html')