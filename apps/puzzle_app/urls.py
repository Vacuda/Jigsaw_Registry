from django.conf.urls import url
from . import views

urlpatterns=[
    #/puzzles/
    url(r'^$', views.index),
    url(r'^view/(?P<puzzle_id>[0-9]+)$', views.view_puzzle),

    url(r'^add$', views.add_puzzle_page),
    url(r'^create$', views.create_puzzle),
    url(r'^create/(?P<puzzle_id>[0-9]+)/success$', views.success_create_puzzle),
   
    url(r'^guided/(?P<puzzle_id>[0-9]+)/picture$', views.guided_picture),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/brand$', views.guided_brand),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/desc_notes$', views.guided_desc_notes),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/categories$', views.guided_categories),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/measures$', views.guided_measures),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/pieces$', views.guided_pieces),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/owned$', views.guided_owned),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/completion$', views.guided_completion),
    ]