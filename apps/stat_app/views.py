from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_reg_app.models import User

def index(request):
    return render(request, 'stat_app/index.html')