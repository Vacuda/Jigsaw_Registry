from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_reg_app.models import User
from apps.puzzle_app.models import Puzzle
from apps.project_app.models import Project, ProjectImage, Helper

# def index(request):
#     return render(request, 'project_app/index.html')

def edit_project(request, project_id):
    context = {
        "project": Project.objects.filter(id=project_id)[0],
    }
    return render(request, 'project_app/project_edit_page.html', context)

def view_project(request, project_id):
    context = {
        "project": Project.objects.filter(id=project_id)[0],
    }
    return render(request, 'project_app/project_view_page.html', context)

def view_all_projects(request):
    context = {
        "projects": Project.objects.filter(belongs_to=request.session['user_id']),
    }
    return render(request, 'project_app/project_view_all_page.html', context)

#######Adding a project

def add_project_page(request):

    return render(request, 'project_app/project_add_page.html')

def create_project(request):
    user=User.objects.filter(id=request.session['user_id'])[0]
    Project.objects.create(
        name = request.POST['name'],
        belongs_to = user
    )
    pid=Project.objects.last().id
    return redirect(f'/projects/create/{pid}/success')

def success_create_project(request, project_id):
    context = {
        "project": Project.objects.filter(id=project_id)[0]
    }
    return render(request, 'project_app/project_create_success_page.html',context)

######## Guided project pages

def guided_puzzles(request, project_id):
    try:
        selected_puzzle = Project.puzzles.all()[0]
    except:
        selected_puzzle = "None Selected"

    context = {
        "project": Project.objects.filter(id=project_id)[0],
        "puzzles": Puzzle.objects.filter(belongs_to=request.session['user_id']),
        #only select the first puzzle.  Dual puzzle not implemented yet
        "selected_puzzle": selected_puzzle.title,
    }
    return render(request, 'project_app/project_guided_puzzle_page.html',context)

######## Guided project pages   POST POST POST POST

def guided_puzzles_get(request, project_id, puzzle_id):
    puzz = Puzzle.objects.filter(id=puzzle_id)[0]
    proj = Project.objects.filter(id=project_id)[0]
    
    while len(proj.puzzles.all()) >= 1:
        proj.puzzles.remove(proj.puzzles.last())
    proj.puzzles.add(puzz)
    return redirect(f'/projects/guided/{project_id}/puzzles')