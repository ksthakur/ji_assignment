from django.shortcuts import render
from api.models import Employee
from .serializer import EmployeeSerializer
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
# Create your views here.

def home(request):
    context1 = {'employee' : Employee.objects.all()}
    return render(request, 'home_page.html', context1)

@api_view(['GET', 'POST', 'DELETE'])
def employee_list(request):
    if request.method == 'GET':
        employee_list = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee_list, many=True)
        response_data = {
        	"message": "all employees list",
            "employee": employee_serializer.data
        }
        return JsonResponse(response_data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
        response_data = {
        	"message": "employee added successfully"
        }
        return JsonResponse(response_data, safe=False)

    elif request.method == 'DELETE':
        response_data = {
            "message": "this method is not allowed as it delete all employees"
        }
        return JsonResponse(response_data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        response_data = {
        	"message": "this employee id is not valid"
        }
        return JsonResponse(response_data, safe=False)

    if request.method == 'GET':
        employee_serializer = EmployeeSerializer(employee)
        response_data = {
        	"message": "employee detail",
            "employee": employee_serializer.data
        }
        return JsonResponse(response_data, safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
        response_data = {
        	"message": "employee updated successfully"
        }
        return JsonResponse(response_data, safe=False)

    elif request.method == 'DELETE':
        employee.delete()
        response_data = {
        	"message": "employee deleted successfully"
        }
        return JsonResponse(response_data, safe=False)

@api_view(['GET'])
def employee_filter(request):
    employee_list = Employee.objects.filter(gender='Male')

    if request.method == 'GET':
        employee_serializer = EmployeeSerializer(employee_list, many=True)
        response_data = {
        	"message": "all employees list with filter gender=male",
            "employee": employee_serializer.data
        }
        return JsonResponse(response_data, safe=False)