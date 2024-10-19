from django.shortcuts import render, redirect
from .models import pay
from datetime import datetime
from supplier.models import Supplier
# Create your views here.


def home (request):
  return render (request, 'payment/pages/home.html')


def new_payment(request):
    fornecedor = Supplier.objects.all()
    if request.method == 'POST':
        # Recuperar dados do formulário
        num_nota = request.POST.get('num_nota')
        nome = request.POST.get('nome')
        fornecedor = Supplier.objects.get(cnpj=nome)
        vencimento = request.POST.get('vencimento')
        data_emissao = request.POST.get('data_emissao')
        valor = request.POST.get('valor')

        # Criar novo objeto Pagamento
        pay.objects.create(
            fornecedor = fornecedor,
            data_emissao = data_emissao,
            numero_nota=num_nota,
            valor_boleto=valor,
            data_vencimento=vencimento,
            data_entrada = datetime.now()
            
            
        )

        # Redirecionar para a página de sucesso ou outra página
        return redirect('payment:home')  # Use o namespace aqui

    # Renderizar o template com o formulário para GET request
    return render (request, 'payment/pages/new_payment.html',context={
        "fornecedores" : fornecedor
    })



def search_payment(request):
    if request.method == "GET": 
        num_nota = request.GET.get('num_nota')
        nome = request.GET.get('nome')
        cnpj = request.GET.get('cnpj')
        data_venda = request.GET.get('data_venda')

    pagamentos = pay.objects.all()
    

    if num_nota:
        pagamentos = pagamentos.filter(num_nota__icontains=num_nota)
    
    if nome:
        pagamentos = pagamentos.filter(nome__icontains=nome)
    
    if cnpj:
        pagamentos = pagamentos.filter(cnpj__icontains=cnpj)

    if data_venda:
        pagamentos = pagamentos.filter(data_venda=data_venda)

    return render(request, 'payment/pages/search_payment.html', context={'pagamentos': pagamentos})







