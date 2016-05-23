from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu
from .models import Employee
from .models import ShareEmployee
from mongoengine import *
from django.template import loader

connect('pythonLearn')

def index(request):
	employees = Employee.objects.all()
	context = {
		'employees': employees,
	}
	# template = loader.get_template('myPythonWebsite/index.html')
	# return HttpResponse(template.render(context, request))
	return render(request, 'myPythonWebsite/index.html', context)

def employee_detail(request, employee_id):
	employee = Employee.objects.get(employeeId = employee_id)
	return HttpResponse("You're looking at employee %s." % employee.name)

def add(request):
	employeeName = request.POST.get("employeeName")
	employeeId = request.POST.get("employeeId")
	sharedEmployee1Name = request.POST.get("sharedEmployee1Name")
	sharedEmployee1Id = request.POST.get("sharedEmployee1Id")
	sharedEmployee2Name = request.POST.get("sharedEmployee2Name")
	sharedEmployee2Id = request.POST.get("sharedEmployee2Id")
	employee = Employee(employeeId=employeeId, name=employeeName, gender='F')
	employee.shareEmployees = [ShareEmployee(employeeId=sharedEmployee1Id, name=sharedEmployee1Name, gender='F'), ShareEmployee(employeeId=sharedEmployee2Id, name=sharedEmployee2Name, gender='F')]
	employee.save()
	return render(request, 'myPythonWebsite/addComplete.html', {"employeeName" : employeeName})