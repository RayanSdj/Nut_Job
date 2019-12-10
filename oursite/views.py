from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def all_squirrels(request):
    squirells = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'mapster/all.html', context)

def edit_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(id=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'mapster/{Unique_Squirrel_ID}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }

    return render(request, 'mapster/edit.html', context)


def index(request):
    return HttpResponse("Average latitude = 40.78, Average longitude = -73.9672, Proportion of squirrels running = 0.2415, Proportion of squirrels chasing = 0.0923, Proportion of squirrels 0.2177")

def coordinates_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrel.object.get(id=Unique_Squirrel_ID)
    return HttpResponse(squirrel.X, squirrel.Y)
