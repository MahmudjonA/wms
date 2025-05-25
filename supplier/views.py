from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

def supplier_list(request, pk=None):
    suppliers = Supplier.objects.all()
    create_form = SupplierForm()

    supplier_forms = {
        f'supplier_{supplier.id}': SupplierForm(instance=supplier)
        for supplier in suppliers
    }

    if request.method == 'POST':
        if not Supplier.objects.filter(pk=pk).exists():
            create_form = SupplierForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('supplier_list')

    return render(request, 'supplier_list.html', {
        'suppliers': suppliers,
        'create_form': create_form,
    })
    
class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier_form.html'
    success_url = reverse_lazy('supplier_list')

def supplier_delete(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
