# ji_assignment
- python3, sqlite3 and django REST Framework is used

A Django application with Employee models
A custom management command to populate the database with some dummy data
An api is created to get the data in json

## to run the application

clone or download the project form github
go to project dirctory in terminal/command prompt
change the setting file accordingly

- run the command "python manage.py makemigrations"
- run the command "python manage.py migrate"

to add dummy data by file provided i.e "TestJSON.json"
- run the command "python manage.py upload_data"

now run the server
- run the command "python manage.py runserver"

to run the api, hit the url in postman or browser with methods get,put,post,delete
- api url "http://127.0.0.1:8000/api/employee_list"
- api url "http://127.0.0.1:8000/api/employee_detail/5"
- api url "http://127.0.0.1:8000/api/employee_filter"

provide body raw data for post/put method as follows
{
    "name": "employee4",
    "phone": "2342345211",
    "email": "emp4@example.com",
    "gender": "Male",
    "address": "Banglore"
}

default superuser credentials to login djngo admin
username - employee@example.com
password - employee
