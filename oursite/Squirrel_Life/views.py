from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'Squirrel_Life/all.html', context)

def edit_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(id=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        form.save()
        return redirect(f'Squirrel_Life/{Unique_Squirrel_ID}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
         'form': form,
    }

    return render(request, 'Squirrel_Life/all.html', context)

def index(request):
    return HttpResponse("avg lat = 40.78, avg lon = -73.967, proportion of squirrels running = 0.2418, propof squirrels chasing = 0.0923, prop of squirrels eating = 0.218")

def coordinates_squirrel(request):
    sightings = Squirrel.objects.order_by('date')[:50]
    context = {
            'sightings': sightings
    }
    return render(request, 'Squirrel_Life/map.html', context)


def add_squirrel(request, new_sighting):
    context = {
            'new_sighting': new_sighting
    }
    return render(request, 'Squirrel_Life/add_sighting.html', context)
# Create your views here.
