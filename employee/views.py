from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Employee
from .forms import EmployeeForm


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

def edit_employee(request, id):
    # Obtém o funcionário pelo ID
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        # Popula o formulário com os dados enviados e a instância do funcionário
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('search_employee')  # Redireciona para a página inicial ou a página desejada
    else:
        # Cria o formulário com os dados do funcionário
        form = EmployeeForm(instance=employee)

    return render(request, 'employee/pages/edit_employee.html', {'form': form, 'employee': employee})

def inativar_employee(request, id):
    # Verifica se a requisição é do tipo POST
    if request.method == "POST":
        funcionario = get_object_or_404(Employee, id=id)  # Obtém o funcionário pelo ID
        funcionario.status = False  # Altera o status para 'inativo'
        funcionario.save()  # Salva as alterações no banco de dados
        return redirect('search_employee')  # Redireciona para a página de pesquisa ou lista de funcionários

    return redirect('search_employee')  # Redireciona se a requisição não for POST


def ativar_employee(request, id):
    # Verifica se a requisição é do tipo POST
    if request.method == "POST":
        funcionario = get_object_or_404(Employee, id=id)  # Obtém o funcionário pelo ID
        funcionario.status = True  # Altera o status para 'inativo'
        funcionario.save()  # Salva as alterações no banco de dados
        return redirect('search_employee')  # Redireciona para a página de pesquisa ou lista de funcionários

    return redirect('search_employee')  # Redireciona se a requisição não for POST
ativar_employee