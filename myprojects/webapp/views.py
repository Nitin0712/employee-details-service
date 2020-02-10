from django.shortcuts import render, redirect
from webapp.forms import EmployeeForm
from webapp.models import Employee
from django.http import HttpResponse


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(show)
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "emp_list.html", {"form":form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "emp_list.html", {'employees': employees})


def edit(request, id):
    employees = Employee.objects.get(id=id)
    return render(request, "emp_list.html", {'employee': employees, 'edit':"1"})


def update(request, id):
    employees = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employees)
    if form.is_valid():
        form.save()
        return redirect(show)
    return render(request, "emp_list.html", {'employee': employees})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect(show)
