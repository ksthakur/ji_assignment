from django.urls import path
from .import views

urlpatterns = [
	path('', views.home, name="home"),
    path('api/employee_list', views.employee_list, name='employee_list'),
    path('api/employee_detail/<pk>', views.employee_detail, name='employee_detail'),
    path('api/employee_filter', views.employee_filter, name='employee_filter')
]