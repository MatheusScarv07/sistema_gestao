from django.shortcuts import render
from datetime import datetime
from budget.models import BudgetInfo

# Create your views here.
def home (request):
  return render (request, 'budget/pages/home.html')





def budget_search(request):
  data = datetime.today()

  budget = BudgetInfo.objects.filter(data_orcamento=data)
  print(budget)
  return render(request, "budget/pages/search_budget.html",{"budget":budget})







""" def budget_filter(request):
    # Obtém a data atual
    agora = datetime.now()

    # Filtra os orçamentos do dia atual
    budget = Budget.objects.filter(agora)

    # Formulário de filtro
    form = OrcamentoFilterForm(request.GET or None)
    cliente_venda = Client.objects.get(id = request.session.get('cliente_id') )
    vendedor_venda = Employee.objects.get(id = request.session.get('vendedor_id') )

    if form.is_valid():
        cliente = cliente_venda('cliente'),
        cpf_cnpj = cliente_venda.cpf_cnpj('cpf_cnpj'),
        vendedor = vendedor_venda('vendedor'),
        data_orcamento = agora('data_inicial'),
        data_final = ('data_final')

        # Aplica os filtros
        if cliente:
            budget = orcamentos.filter(cliente_venda=cliente)
        if cpf_cnpj:
            orcamentos = orcamentos.filter(=cpf_cnpj)
        if vendedor:
            orcamentos = orcamentos.filter(vendedor__icontains=vendedor)
        if data_inicial and data_final:
            orcamentos = orcamentos.filter(data_criacao__date__range=[data_inicial, data_final])

    context = {
        'orcamentos': orcamentos,
        'form': form,
    }
    return render(request, 'orcamentos.html', context) """