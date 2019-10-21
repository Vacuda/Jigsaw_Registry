from django.conf.urls import url
from . import views

urlpatterns=[
    #/login/
    url(r'^$', views.index),
    url(r'^success$', views.success),

    url(r'^user/register$', views.register),
    url(r'^user/login$', views.login),

    url(r'^logout$', views.reset),
    ]