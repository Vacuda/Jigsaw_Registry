from django.conf.urls import url
from . import views

urlpatterns=[
    #/puzzles/
    url(r'^$', views.index),
    url(r'^view/(?P<puzzle_id>[0-9]+)$', views.view_puzzle),

    url(r'^add$', views.add_puzzle_page),
    url(r'^create$', views.create_puzzle),
    url(r'^create/(?P<puzzle_id>[0-9]+)/success$', views.success_create_puzzle),
    ]