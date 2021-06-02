from django.shortcuts import render
from django.http import HttpResponse
from fetchApp.models import Employee

# Create your views here.

def display(request):
    Employee_Details = Employee.objects.all()
    return render(request , 'index.html' , {'employee' : Employee_Details})
