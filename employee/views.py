from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

from employee.models import Employee  # kerakli import
from .forms import EmployeeForm

def employee_list(request):
    if request.method == 'POST' and 'create' in request.POST:
        create_form = EmployeeForm(request.POST)
        if create_form.is_valid():
            employee = create_form.save(commit=False)  # vaqtincha saqlamaymiz
            raw_password = create_form.cleaned_data['password']
            employee.set_password(raw_password)  # parolni hashlab olamiz
            employee.save()
            return redirect('employee_list')
    else:
        create_form = EmployeeForm()

    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {
        'employees': employees,
        'create_form': create_form,
    })


def employee_update(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'object': emp})
