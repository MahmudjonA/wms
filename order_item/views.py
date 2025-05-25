from django.shortcuts import render, redirect, get_object_or_404
from .models import PurchaseOrderItem
from .forms import PurchaseOrderItemForm

def order_item_list(request):
    # Handle create (modal form)
    if request.method == 'POST' and 'create' in request.POST:
        form = PurchaseOrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_item_list')
    else:
        form = PurchaseOrderItemForm()

    items = PurchaseOrderItem.objects.select_related('purchase_order', 'product').all()
    return render(request, 'order_item_list.html', {
        'items': items,
        'create_form': form,
    })

def order_item_update(request, pk):
    item = get_object_or_404(PurchaseOrderItem, pk=pk)
    if request.method == 'POST':
        form = PurchaseOrderItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('order_item_list')
    else:
        form = PurchaseOrderItemForm(instance=item)
    return render(request, 'order_item_form.html', {
        'form': form,
        'item': item,
    })

def order_item_delete(request, pk):
    item = get_object_or_404(PurchaseOrderItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('order_item_list')
    # Should never GET — deletion happens via POST from modal
    return redirect('order_item_list')
