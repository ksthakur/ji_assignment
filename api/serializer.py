from api.models import Employee
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = ['name', 'phone', 'email', 'gender', 'address']