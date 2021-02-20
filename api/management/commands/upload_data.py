import json
from django.core.management.base import BaseCommand
from api.models import Employee

json_data = open('TestJSON.json')   
data1 = json.load(json_data)

class Command(BaseCommand):

    def handle(self, *args, **options):
    	for item1 in data1['employee']:
	        user = Employee(name=item1['name'], phone=item1['phone'], email=item1['email'], gender=item1['gender'], address=item1['address'])
	        user.save()