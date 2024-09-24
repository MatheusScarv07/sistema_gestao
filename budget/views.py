from django.shortcuts import render
from datetime import datetime
from budget.models import BudgetInfo
from budget.controller.filter_budget import obter_budget_filtradas
from django.views.decorators.csrf import csrf_exempt
from client.models import Client
from employee.models import Employee

# Create your views here.
def home (request):
  return render (request, 'budget/pages/home.html')





def budget_search(request):
  data = datetime.today()
  budget = BudgetInfo.objects.filter(data_orcamento=data)

  clientes = Client.objects.all()
  vendedor_db = Employee.objects.all()
  print(budget)
  return render(request, "budget/pages/search_budget.html",{
     "budget":budget,
     'clientes':clientes,
    'vendedores': vendedor_db
                                                            })


@csrf_exempt
def search_budget_filter(request):
    data_inicial = request.POST.get('date_inicial')
    data_final = request.POST.get('date_final')
    nome = request.POST.get('cliente')
    cpf = request.POST.get('cpf')
    number_sale = request.POST.get('number_budget')
    vendedor = request.POST.get('vendedor')
    clientes = Client.objects.all()
    vendedor_db = Employee.objects.all()
    budgets = obter_budget_filtradas(data_inicial, data_final, nome,cpf,vendedor,number_sale)
    return render(request, "budget/pages/search_budget.html",{
       "budget":budgets,
       'clientes':clientes,
       'vendedores': vendedor_db
       })
