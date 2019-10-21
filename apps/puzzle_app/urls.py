from django.conf.urls import url
from . import views

urlpatterns=[
    #/puzzles/
    url(r'^$', views.index),
    ]