from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_reg_app.models import User
from apps.puzzle_app.models import Puzzle, Brand, Category

def index(request):
    return render(request, 'puzzle_app/index.html')

def view_puzzle(request, puzzle_id):

    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }
    return render(request, 'puzzle_app/puzzle_view_page.html', context)

#######Adding a puzzle

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


######## Guided puzzle info

def guided_picture(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }
    return render(request, 'puzzle_app/guided_picture.html', context)

def guided_brand(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(name=puzzle_id)[0],
        "brands": Brand.objects.all()
    }
    return render(request, 'puzzle_app/guided_brand.html', context)

def guided_desc_notes(request, puzzle_id):
    print("yellow")
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }
    return render(request, 'puzzle_app/guided_desc_notes.html', context)

def guided_categories(request, puzzle_id):
    #find unused categories to pass in context
    c=Category.objects.all()
    p=Puzzle.objects.filter(id=puzzle_id)[0].categories.all()
    for catc in c:
        for catp in p:
            if catc.id == catp.id:
                c = c.exclude(id=catc.id)
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0],
        "used_categories": Puzzle.objects.filter(id=puzzle_id)[0].categories.all(),
        "unused_categories": c
    }
    return render(request, 'puzzle_app/guided_categories.html', context)

def guided_measures(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }
    return render(request, 'puzzle_app/guided_measures.html', context)

def guided_pieces(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }
    return render(request, 'puzzle_app/guided_pieces.html', context)

def guided_owned(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }
    return render(request, 'puzzle_app/guided_owned.html', context)

def guided_completion(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0],
    }
    return render(request, 'puzzle_app/guided_completion.html', context)

######## Guided puzzle info - POST POST POST POST POST POST POST POST POST POST

def guided_picture_post(request, puzzle_id):

    print(request.POST)

    return redirect(f'/puzzles/guided/{puzzle_id}/brand')

def guided_brand_post(request, puzzle_id):
    c = Puzzle.objects.filter(id=puzzle_id)[0]
    c.brand = Brand.objects.filter(id=request.POST['brand'])[0]
    c.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/desc_notes')

def guided_desc_notes_post(request, puzzle_id):
    c = Puzzle.objects.filter(id=puzzle_id)[0]
    c.desc = request.POST['desc']
    c.save()
    c.notes = request.POST['notes']
    c.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/categories')

def guided_categories_post(request, puzzle_id):
    c = Puzzle.objects.filter(id=puzzle_id)[0]
    c.categories.add(Category.objects.filter(id=request.POST['category'])[0])
    return redirect(f'/puzzles/guided/{puzzle_id}/categories')

def guided_measures_post(request, puzzle_id):
    c = Puzzle.objects.filter(id=puzzle_id)[0]
    c.length = request.POST['length']
    c.save()
    c.height = request.POST['height']
    c.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/pieces')

def guided_pieces_post(request, puzzle_id):
    c = Puzzle.objects.filter(id=puzzle_id)[0]
    c.pieces_actual = request.POST['pieces_actual']
    c.save()
    c.missing_pieces = request.POST['missing_pieces']
    c.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/owned')

def guided_owned_post(request, puzzle_id):
    c = Puzzle.objects.filter(id=puzzle_id)[0]
    c.owned = request.POST['owned']
    c.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/completion')

def guided_completion_post(request, puzzle_id):
    c = Puzzle.objects.filter(id=puzzle_id)[0]
    c.completions = request.POST['completions']
    c.save()
    c.initial_complete = request.POST['initial_complete']
    c.save()
    return redirect(f'/puzzles/view/{puzzle_id}')




######## Full list puzzle info





######## Category and Brand create

def category_create(request, puzzle_id):
    Category.objects.create(name=request.POST['added_category'])
    return redirect(f'/puzzles/guided/{puzzle_id}/categories')

def brand_create(request, puzzle_id):
    Brand.objects.create(name=request.POST['added_brand'])
    return redirect(f'/puzzles/guided/{puzzle_id}/brand')
