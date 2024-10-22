from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Receive, PaymentHistory, PaymentType
from sale.models import SaleInfo
from client.models import Client
from datetime import datetime
# Create your views here.


def home (request):
  return render (request, 'receive/pages/home.html')

def receive_page(request, num_venda):
    num_venda = num_venda
    # Supondo que `num_venda` já tenha sido passado para a função
    venda = SaleInfo.objects.filter(num_sale=num_venda).first()  # Use .first() para pegar o primeiro resultado

    if venda:  # Verifique se a venda existe
        valor = venda.valor  # Acesse o valor da venda
    else:
        valor = None  # Se a venda não for encontrada, atribua None

    # Obtenha todos os tipos de pagamento
    types_payment = PaymentType.objects.all()
    return render (request, 'receive/pages/receive.html', context={
        'num_venda': num_venda,
        'valor': valor,
        'tipos_pagamento': types_payment
    })

def makePayment(request):
    if request.method == 'POST':
        # Coletando os dados do formulário
        num_venda = request.POST.get('num_venda')
        
        # Verificando se 'num_venda' foi fornecido e se é um número válido
        if num_venda is None or not num_venda.isdigit():
            return HttpResponseBadRequest("Número da venda inválido ou ausente.")
        
        numInt = int(num_venda)
        venda = SaleInfo.objects.filter(num_sale=numInt).first()
        
        if venda is None:
            return HttpResponseBadRequest("Venda não encontrada.")
        
        # Para depuração
        
        # Pegando os valores do formulário
        type_payment_1 = request.POST.get('type_payment_1')
        valor_1 = request.POST.get('valor_1')
        type_payment_2 = request.POST.get('type_payment_2', None)  # Opcional
        valor_2 = request.POST.get('valor_2', None)  # Opcional

        # Verificando se o valor 1 foi fornecido
        if valor_1 is None or not valor_1.replace('.', '', 1).isdigit():
            return HttpResponseBadRequest("Valor 1 inválido ou ausente.")

        # Pegando os tipos de pagamento
        id_pagamento1 = int(type_payment_1)
        if type_payment_2:
            id_pagamento2 = int(type_payment_2)
        tipo_pagamento_1 = PaymentType.objects.filter(id=id_pagamento1).first()
        tipo_pagamento_2 = PaymentType.objects.filter(id=id_pagamento2).first() if type_payment_2 else None
        if tipo_pagamento_1.nome == 'A Prazo' or tipo_pagamento_2 == 'A Prazo':
            status = 'Pendente'
        else:
            status ='Pago'
        if not tipo_pagamento_1:
            return HttpResponseBadRequest("Tipo de pagamento 1 inválido ou não encontrado.")

        # Criando a nova venda
        payment = Receive(
            data=datetime.now(),
            num_sale=venda,
            data_venda=venda.data_venda,
            cliente=venda.cliente,
            cpf_cnpj=venda.cpf_cnpj,
            tipo_pagamento=tipo_pagamento_1,
            status= status,
            valor=float(valor_1)
        )
        payment.save()

        # Verificando o pagamento secundário opcional
        if type_payment_2 and valor_2:
            if not valor_2.replace('.', '', 1).isdigit():
                return HttpResponseBadRequest("Valor 2 inválido.")
            
            payment_2 = Receive(
                data=datetime.now(),
                num_sale=venda,
                data_venda=venda.data_venda,
                cliente=venda.cliente,
                cpf_cnpj=venda.cpf_cnpj,
                tipo_pagamento=tipo_pagamento_2,
                status="Pendente" if tipo_pagamento_2.id == 1 else "Pago",
                valor=float(valor_2)
            )
            payment_2.save()

        # Salvando histórico de pagamentos
        if tipo_pagamento_1 and tipo_pagamento_1.id != 1:
            historico = PaymentHistory(
                data=datetime.now(),
                num_sale=venda,
                data_venda=venda.data_venda,
                cliente=venda.cliente,
                cpf_cnpj=venda.cpf_cnpj,
                type=tipo_pagamento_1,
                valor=float(valor_1),
            )
            historico.save()

        if tipo_pagamento_2 and tipo_pagamento_2.id != 1:
            historico_2 = PaymentHistory(
                data=datetime.now(),
                num_sale=venda,
                data_venda=venda.data_venda,
                cliente=venda.cliente,
                cpf_cnpj=venda.cpf_cnpj,
                type=tipo_pagamento_2,
                valor=float(valor_2),
            )
            historico_2.save()

    return redirect('new_sale')

def info_receive(request):
  return render(request, 'receive/pages/info_receive.html')

def search_receive(request):
  try: 
        receives = Receive.objects.filter(status="Pendente")
        clientes = Client.objects.all()
        return render(request, 'receive/pages/searchreceive.html', context={
            'receives': receives,
            'clientes': clientes,
        })
  except Exception as e:
        ...
  