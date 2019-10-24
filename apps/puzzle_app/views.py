from django.shortcuts import render, redirect, HttpResponse
from apps.log_and_reg_app.models import User
from apps.puzzle_app.models import Puzzle, Brand, Category, PuzzleImage

def index(request):
    return render(request, 'puzzle_app/index.html')

def view_puzzle(request, puzzle_id):
    if Puzzle.objects.filter(id=puzzle_id)[0].owned == True:
        ownage = "Owned"
    if Puzzle.objects.filter(id=puzzle_id)[0].owned == False:
        ownage = "On Wishlist"
    if Puzzle.objects.filter(id=puzzle_id)[0].completed == False:
        completed = "Not Completed"
        initial = "Not Completed"
    if Puzzle.objects.filter(id=puzzle_id)[0].completed == True:
        completed = "Completed!"
        p = Puzzle.objects.filter(id=puzzle_id)[0]
        if p.initial_complete == None:
            initial = "Completed prior to entry!"
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0],
        "ownage": ownage,
        "completed": completed,
        "initial": initial,
    }
    return render(request, 'puzzle_app/puzzle_edit_page.html', context)

def view_all(request):

    context = {
        "puzzles": Puzzle.objects.filter(belongs_to=request.session['user_id']),
    }

    return render(request, 'puzzle_app/puzzle_view_all_page.html', context)

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


######## Guided puzzle pages

def guided_title(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0]
    }
    return render(request, 'puzzle_app/guided_title.html', context)

def guided_picture(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0],
        "images": PuzzleImage.objects.all()
    }
    return render(request, 'puzzle_app/guided_picture.html', context)

def guided_brand(request, puzzle_id):
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0],
        "brands": Brand.objects.all()
    }
    return render(request, 'puzzle_app/guided_brand.html', context)

def guided_desc_notes(request, puzzle_id):
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
    if Puzzle.objects.filter(id=puzzle_id)[0].owned == True:
        c = "Owned"
    if Puzzle.objects.filter(id=puzzle_id)[0].owned == False:
        c = "On Wishlist"
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0],
        "ownage": c,
    }
    return render(request, 'puzzle_app/guided_owned.html', context)

def guided_completion(request, puzzle_id):
    if Puzzle.objects.filter(id=puzzle_id)[0].completed == False:
        c = "Not Completed"
    if Puzzle.objects.filter(id=puzzle_id)[0].completed == True:
        c = "Completed!"
    context = {
        "puzzle": Puzzle.objects.filter(id=puzzle_id)[0],
        "completed": c,
    }
    return render(request, 'puzzle_app/guided_completion.html', context)

######## Guided puzzle changes - POST POST POST POST POST POST GET POST

def guided_title_post(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.title = request.POST['title']
    p.save()
    p.pieces_labeled = request.POST['pieces_labeled']
    p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/title')

def guided_picture_post(request, puzzle_id):

    # cropped_picture = 
    # Uploads Picture
    PuzzleImage.objects.create(image = request.FILES['picture'])

    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.picture = PuzzleImage.objects.last()
    p.save()

    return redirect(f'/puzzles/guided/{puzzle_id}/picture')

def guided_brand_post(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.brand = Brand.objects.filter(id=request.POST['brand'])[0]
    p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/brand')

def guided_desc_notes_post(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.desc = request.POST['desc']
    p.save()
    p.notes = request.POST['notes']
    p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/desc_notes')

def guided_categories_post(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.categories.add(Category.objects.filter(id=request.POST['category'])[0])
    return redirect(f'/puzzles/guided/{puzzle_id}/categories')

def guided_measures_post(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.width = float(request.POST['width'])
    p.save()
    p.height = float(request.POST['height'])
    p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/measures')

def guided_pieces_post(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.pieces_actual = int(request.POST['pieces_actual'])
    p.save()
    p.missing_pieces = int(request.POST['missing_pieces'])
    p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/pieces')

def guided_owned_get(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.owned = True
    p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/owned')

def guided_not_owned_get(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.owned = False
    p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/owned')

def guided_completed_get(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.completed = True
    p.save()
    if p.completions == 0:
        p.completions = 1
        p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/completion')

def guided_not_completed_get(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.completed = False
    p.save()
    p.completions = 0
    print(p.completions)
    p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/completion')

def guided_completion_post(request, puzzle_id):
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    p.completions = int(request.POST['completions'])
    p.save()
    if p.completions > 0:
        p.completed = True
        p.save()
    return redirect(f'/puzzles/guided/{puzzle_id}/completion')




######## Full list puzzle info





######## Category and Brand create

def category_create(request, puzzle_id):
    Category.objects.create(name=request.POST['added_category'])
    return redirect(f'/puzzles/guided/{puzzle_id}/categories')

def category_remove(request, puzzle_id):
    print(request.POST['removed_category'])
    p = Puzzle.objects.filter(id=puzzle_id)[0]
    c = Category.objects.filter(name=request.POST['removed_category'])[0]
    print(p)
    print(c)
    p.categories.remove(c)
    return redirect(f'/puzzles/guided/{puzzle_id}/categories')

def category_delete(request, puzzle_id):
    # p = Puzzle.objects.filter(id=puzzle_id)[0]
    # c = Category.objects.filter(name=request.POST['remove_category'])
    # p.categories.remove(c)
    return redirect(f'/puzzles/guided/{puzzle_id}/categories')

def brand_create(request, puzzle_id):
    Brand.objects.create(name=request.POST['added_brand'])
    return redirect(f'/puzzles/guided/{puzzle_id}/brand')

def brand_delete(request, puzzle_id):
    # Brand.objects.create(name=request.POST['added_brand'])
    return redirect(f'/puzzles/guided/{puzzle_id}/brand')
