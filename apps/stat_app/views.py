from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_reg_app.models import User
from apps.puzzle_app.models import Puzzle

def stats(request):
    puzzles = Puzzle.objects.filter(belongs_to=request.session['user_id'])

    completed_pieces = 0
    uncompleted_pieces = 0
    completed_puzzles = 0
    uncompleted_puzzles = 0
    total_pieces = 0
    total_puzzles = 0
    
    for puzzle in puzzles:
        total_pieces = total_pieces + puzzle.pieces_actual
        total_puzzles = total_puzzles + 1
        if puzzle.completed == True:  
            completed_puzzles = completed_puzzles + 1 
            completed_pieces = completed_pieces + puzzle.pieces_actual
        else:
            uncompleted_puzzles = uncompleted_puzzles + 1
            uncompleted_pieces = uncompleted_pieces + puzzle.pieces_actual
    context = {
        "completed_pieces": completed_pieces,
        "completed_puzzles": completed_puzzles,
        "uncompleted_pieces": uncompleted_pieces,
        "uncompleted_puzzles": uncompleted_puzzles,
        "total_pieces": total_pieces,
        "total_puzzles": total_puzzles,
        
    }
    return render(request, 'stat_app/stats.html', context)