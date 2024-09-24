from budget.models import BudgetInfo


def obter_budget_filtradas(data_inicio=None, data_fim=None, nome_cliente=None, cpf_cnpj=None, vendedor=None, numero_venda=None):
    print(f'def: {vendedor}')
    budget = BudgetInfo.objects.all()  # Acesso ao modelo correto

    # Aplicando filtros de forma dinâmica
    if data_inicio:
        budget = budget.filter(data_orcamento__gte=data_inicio)
    if data_fim:
        budget = budget.filter(data_orcamento__lte=data_fim)
    if nome_cliente:
        budget = budget.filter(cliente__id__exact=nome_cliente)  # Busca por nome parcial
    if cpf_cnpj:
        budget = budget.filter(cpf_cnpj_cliente=cpf_cnpj)  # Busca por CPF ou CNPJ exato
    if vendedor:
        budget = budget.filter(vendedor__id__exact=vendedor)  # Busca por nome do vendedor
    if numero_venda:
        budget = budget.filter(number_budget=numero_venda)

    # Ordenar por data de venda de forma ascendente
    budget = budget.order_by('data_orcamento')

    return budget