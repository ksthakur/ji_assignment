from django.shortcuts import render
from api.models import Employee
from .serializer import EmployeeSerializer
from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
# Create your views here.

def home(request):
    context1 = {'employee' : Employee.objects.all()}
    return render(request, 'home_page.html', context1)

@api_view(['GET', 'POST'])
@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        employee_list = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee_list, many=True)
        return Response(employee_serializer.data)

    elif request.method == 'POST':
        employee_serializer = EmployeeSerializer(data=request.data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        employee_serializer = EmployeeSerializer(employee)
        return Response(employee_serializer.data)

    elif request.method == 'PUT':
        employee_serializer = EmployeeSerializer(employee, data=request.data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response(employee_serializer.data)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@csrf_exempt
def employee_filter(request):
    if request.method == 'GET':
        employee_list = Employee.objects.filter(gender='Female')
        employee_serializer = EmployeeSerializer(employee_list, many=True)
        return Response(employee_serializer.data)