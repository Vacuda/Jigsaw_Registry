from django.conf.urls import url
from . import views

urlpatterns=[
    #/projects/
    url(r'^$', views.index),
    url(r'^add$', views.add_project),
]