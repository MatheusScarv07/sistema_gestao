from django.shortcuts import render,redirect
from .models import Employee


def home(request):
    return render(request, 'employee/pages/home.html')  # Página inicial



def new_employee(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        cargo = request.POST.get('cargo')
        status = request.POST.get('status') == 'on'  # Para campo Booleano

        # Criar o novo funcionário com os dados inseridos
        Employee.objects.create(nome=nome, cargo=cargo, status=status)

        # Redirecionar para a página inicial após o cadastro
        return redirect('new_employee')

    return render(request, 'employee/pages/new_employee.html')




def search_employee(request):
    employees = Employee.objects.all()

    # Filtragem por nome e cargo, se fornecidos
    name = request.GET.get('name')
    cargo = request.GET.get('cargo')

    if name:
        employees = employees.filter(nome__icontains=name)

    if cargo:
        employees = employees.filter(cargo__icontains=cargo)

    return render(request, 'employee/pages/search_employee.html', {'employees': employees})
