from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_reg_app.models import User
from apps.puzzle_app.models import Puzzle

def index(request):
    return render(request, 'puzzle_app/index.html')

def view_puzzle(request, puzzle_id):

    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }
    return render(request, 'puzzle_app/puzzle_view_page.html', context)

#######




def add_puzzle_page(request):


    return render(request, 'puzzle_app/puzzle_add_page.html')

def create_puzzle(request):

    Puzzle.objects.create(
        title           = request.POST['title'],
        pieces_labeled  = request.POST['pieces_labeled'],
        pieces_actual   = request.POST['pieces_labeled'],
        owned_by        = User.objects.filter(id=request.session['user_id'])[0],
        )

    c=Puzzle.objects.last().id
    return redirect(f'/puzzles/create/{c}/success')

def success_create_puzzle(request, puzzle_id):

    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }

    return render(request, 'puzzle_app/puzzle_create_success_page.html',context)
