from django import forms
from crudapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        Model = Employee
        fields = "_all__"