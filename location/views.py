from django.shortcuts import render, redirect, get_object_or_404
from .models import Location
from .forms import LocationForm

def location_list(request):
    # CREATE via modal
    if request.method == 'POST' and 'create' in request.POST:
        create_form = LocationForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('location_list')
    else:
        create_form = LocationForm()

    locations = Location.objects.select_related('warehouse').all()
    return render(request, 'location_list.html', {
        'locations': locations,
        'create_form': create_form,
    })

def location_update(request, pk):
    loc = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=loc)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm(instance=loc)
    return render(request, 'location_form.html', {'form': form})

def location_delete(request, pk):
    loc = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        loc.delete()
        return redirect('location_list')
    return render(request, 'location_confirm_delete.html', {'object': loc})
