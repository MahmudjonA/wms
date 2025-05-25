from django.shortcuts import render, redirect, get_object_or_404
from .models import Warehouse
from .forms import WarehouseForm

def warehouse_list(request):
    # CREATE via modal
    if request.method == 'POST' and 'create' in request.POST:
        create_form = WarehouseForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('warehouse_list')
    else:
        create_form = WarehouseForm()

    warehouses = Warehouse.objects.select_related('manager').all()
    return render(request, 'warehouse_list.html', {
        'warehouses': warehouses,
        'create_form': create_form,
    })

def warehouse_update(request, pk):
    wh = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=wh)
        if form.is_valid():
            form.save()
            return redirect('warehouse_list')
    else:
        form = WarehouseForm(instance=wh)
    return render(request, 'warehouse_form.html', {'form': form})

def warehouse_delete(request, pk):
    wh = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        wh.delete()
        return redirect('warehouse_list')
    return render(request, 'warehouse_confirm_delete.html', {'object': wh})
