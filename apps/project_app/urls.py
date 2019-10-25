from django.conf.urls import url
from . import views

urlpatterns=[
    #/projects/
    url(r'^$', views.add_project_page),
    url(r'^edit/(?P<project_id>[0-9]+)$', views.edit_project),
    url(r'^view/(?P<project_id>[0-9]+)$', views.view_project),
    url(r'^view/all$', views.view_all_projects),

    ## Add project
    url(r'^add$', views.add_project_page),
    url(r'^create$', views.create_project),
    url(r'^create/(?P<project_id>[0-9]+)/success$', views.success_create_project),

    ## Guided -pages
    url(r'^guided/(?P<project_id>[0-9]+)/puzzles$', views.guided_puzzles),

    ## Guided -posts-
    url(r'^guided/(?P<project_id>[0-9]+)/puzzles_get/(?P<puzzle_id>[0-9]+)$', views.guided_puzzles_get),




]