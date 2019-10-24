from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    #/puzzles/
    url(r'^$', views.index),
    url(r'^view/(?P<puzzle_id>[0-9]+)$', views.view_puzzle),
    url(r'^view/all$', views.view_all),

    ## Add puzzle
    url(r'^add$', views.add_puzzle_page),
    url(r'^create$', views.create_puzzle),
    url(r'^create/(?P<puzzle_id>[0-9]+)/success$', views.success_create_puzzle),
    
    ## Guided -pages-
    url(r'^guided/(?P<puzzle_id>[0-9]+)/title$', views.guided_title),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/picture$', views.guided_picture),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/brand$', views.guided_brand),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/desc_notes$', views.guided_desc_notes),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/categories$', views.guided_categories),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/measures$', views.guided_measures),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/pieces$', views.guided_pieces),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/owned$', views.guided_owned),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/completion$', views.guided_completion),

    ## Guided -posts-
    url(r'^guided/(?P<puzzle_id>[0-9]+)/title_post$', views.guided_title_post),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/picture_post$', views.guided_picture_post),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/brand_post$', views.guided_brand_post),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/desc_notes_post$', views.guided_desc_notes_post),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/categories_post$', views.guided_categories_post),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/measures_post$', views.guided_measures_post),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/pieces_post$', views.guided_pieces_post),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/completion_post$', views.guided_completion_post),
    
    ## Guided -gets- (OWNED)
    url(r'^guided/(?P<puzzle_id>[0-9]+)/owned_get$', views.guided_owned_get),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/not_owned_get$', views.guided_not_owned_get),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/completed_get$', views.guided_completed_get),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/not_completed_get$', views.guided_not_completed_get),

    ## Guided -creates- / -removes- / -deletes
    url(r'^guided/(?P<puzzle_id>[0-9]+)/brand_create$', views.brand_create),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/brand_delete$', views.brand_delete),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/category_create$', views.category_create),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/category_remove$', views.category_remove),
    url(r'^guided/(?P<puzzle_id>[0-9]+)/category_delete$', views.category_delete),
    
    ]
