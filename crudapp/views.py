from django.shortcuts import render,redirect
from crudapp.forms import EmployeeForm
from crudapp.models import Employee

# Create your views here.

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index.html')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "index.html", {'form': form})