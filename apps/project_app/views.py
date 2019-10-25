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
        # "project_puzzles": Puzzles.objects.filter(belongs_to=request.session['user_id']),
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
    return render(request, 'project_app/project_create_success_page.html', context)

######## Guided project pages

def guided_name(request, project_id):
    context = {
        "project": Project.objects.filter(id=project_id)[0]
    }
    return render(request, 'project_app/project_guided_name_page.html', context)

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
    return render(request, 'project_app/project_guided_puzzles_page.html', context)

def guided_helpers(request, project_id):
    #find unused helpers to pass in context, that belond to user
    user=User.objects.filter(id=request.session['user_id'])
    h=Helper.objects.filter(belongs_to = user)
    proj=Project.objects.filter(id=project_id)[0].helpers.all()
    for helper_h in h:
        for helper_proj in proj:
            if helper_h.id == helper_proj.id:
                h = h.exclude(id=helper_h.id)
    context = {
        "project": Project.objects.filter(id=project_id)[0],
        "used_helpers": Project.objects.filter(id=project_id)[0].helpers.all(),
        "unused_helpers": h
    }
    return render(request, 'project_app/project_guided_helpers_page.html', context)

def guided_time(request, project_id):
    context = {
        "project": Project.objects.filter(id=project_id)[0],
    }
    return render(request, 'project_app/project_guided_time_page.html', context)

######## Guided project pages   POST POST POST POST

def guided_name_post(request, project_id):
    proj = Project.objects.filter(id=project_id)[0]
    proj.name = request.POST['name']
    proj.save()

    return redirect(f'/projects/guided/{project_id}/name')

def guided_puzzles_get(request, project_id, puzzle_id):
    puzz = Puzzle.objects.filter(id=puzzle_id)[0]
    proj = Project.objects.filter(id=project_id)[0]
    # removes multiple puzzles, for now
    while len(proj.puzzles.all()) >= 1:
        proj.puzzles.remove(proj.puzzles.last())
    proj.puzzles.add(puzz)
    return redirect(f'/projects/guided/{project_id}/puzzles')

def guided_helpers_post(request, project_id):
    proj = Project.objects.filter(id=project_id)[0]
    proj.helpers.add(Helper.objects.filter(id=request.POST['helper'])[0])
    return redirect(f'/projects/guided/{project_id}/helpers')

def guided_time_post(request, project_id):

    return redirect(f'/projects/guided/{project_id}/time')

######## Helper create

def helper_create(request, project_id):
    Helper.objects.create(
        name        = request.POST['added_helper'],
        belongs_to  = User.objects.filter(id=request.session['user_id'])[0],
        )
    return redirect(f'/projects/guided/{project_id}/helpers')

def helper_remove(request, project_id):
    proj = Project.objects.filter(id=project_id)[0]
    h = Helper.objects.filter(name=request.POST['removed_helper'])[0]
    proj.helpers.remove(h)
    return redirect(f'/projects/guided/{project_id}/helpers')

def helper_delete(request, project_id):
    # p = Puzzle.objects.filter(id=puzzle_id)[0]
    # c = Category.objects.filter(name=request.POST['remove_category'])
    # p.categories.remove(c)
    return redirect(f'/projects/guided/{project_id}/helpers')