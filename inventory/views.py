# inventory/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory
from .forms import InventoryForm
from django.core.cache import cache


def inventory_list(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            cache.delete('inventory_list')
            return redirect('inventory_list')
    else:
        form = InventoryForm()
         
    ctx = cache.get('inventory_list')
    if not ctx:
        inventories = Inventory.objects.select_related('product', 'location').all()
        ctx = {
            'inventory_list': inventories,
            'create_form': form,
        }
        cache.set('inventory_list', ctx, timeout=5)
    
    return render(request, 'inventory_list.html', ctx)



def inventory_update(request, pk):
    inv = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inv)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=inv)
    return render(request, 'inventory_form.html', {'form': form})

def inventory_delete(request, pk):
    inv = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        inv.delete()
        return redirect('inventory_list')
    return render(request, 'inventory_confirm_delete.html', {'object': inv})
