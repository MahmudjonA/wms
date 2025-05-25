from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import PurchaseOrder
from .forms import PurchaseOrderForm
from main.views import get_logged_employee

def purchaseorder_list(request):
    employee = get_logged_employee(request)
    if not employee:
        return redirect('login') 

    # CREATE via modal
    if request.method == 'POST' and 'create' in request.POST:
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            po = form.save(commit=False)
            po.created_by = employee 
            po.save()
            return redirect('purchaseorder_list')
    else:
        form = PurchaseOrderForm()

    orders = PurchaseOrder.objects.select_related('supplier', 'created_by').all()
    return render(request, 'purchaseorder_list.html', {
        'orders': orders,
        'create_form': form,
    })

def purchaseorder_update(request, pk):
    po = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST, instance=po)
        if form.is_valid():
            form.save()
            return redirect('purchaseorder_list')
    else:
        form = PurchaseOrderForm(instance=po)
    return render(request, 'purchaseorder_form.html', {'form': form})

def purchaseorder_delete(request, pk):
    po = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        po.delete()
        return redirect('purchaseorder_list')
    # (modal delete so we won't render this)
    return redirect('purchaseorder_list')
