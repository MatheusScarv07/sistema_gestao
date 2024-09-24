from sale.models import SaleInfo


def obter_vendas_filtradas(data_inicio=None, data_fim=None, nome_cliente=None, cpf_cnpj=None, vendedor=None, numero_venda=None):
    print(f'DATA INICIO {data_inicio}')
    print(f'DATA INICIO {data_fim}')
    vendas = SaleInfo.objects.all()  # Acesso ao modelo correto

    # Aplicando filtros de forma dinâmica
    if data_inicio:
        vendas = vendas.filter(data_venda__gte=data_inicio)
    if data_fim:
        vendas = vendas.filter(data_venda__lte=data_fim)
    if nome_cliente:
        vendas = vendas.filter(cliente__id__exact=nome_cliente)  # Busca por nome parcial
    if cpf_cnpj:
        vendas = vendas.filter(cpf_cnpj=cpf_cnpj)  # Busca por CPF ou CNPJ exato
    if vendedor:
        vendas = vendas.filter(vendedor__id__exact=vendedor)  # Busca por nome do vendedor
    if numero_venda:
        vendas = vendas.filter(num_sale=numero_venda)

    # Ordenar por data de venda de forma ascendente
    vendas = vendas.order_by('data_venda')

    return vendas