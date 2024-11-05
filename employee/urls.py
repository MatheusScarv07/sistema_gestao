# employee/urls.py

from django.urls import path
from employee.views import home, new_employee, search_employee, edit_employee,delete_employee

urlpatterns = [
    path('employee/', home, name='employee_home'),
    path('employee/new/', new_employee, name='new_employee'),
    path('employee/search/', search_employee, name='search_employee'),
    path('employee/<int:id>/edit/', edit_employee, name='employee_edit'),
    path('employee/<int:id>/delete/', delete_employee, name='delete_employee'),
]
