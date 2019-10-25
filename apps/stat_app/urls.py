from django.conf.urls import url
from . import views

urlpatterns=[
    #/stats/
    url(r'^$', views.stats),
]