from django.shortcuts import render, redirect
from payment.models import Payment

def home(request):
    return render(request, 'payment/pages/home.html')

def new_payment(request):
    if request.method == 'POST':
        # Recuperar dados do formulário
        num_nota = request.POST.get('num_nota')
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        vencimento = request.POST.get('vencimento')
        data_venda = request.POST.get('data_venda')
        valor = request.POST.get('valor')

        # Criar novo objeto Pagamento
        Payment.objects.create(
            num_nota=num_nota,
            nome=nome,
            cnpj=cnpj,
            vencimento=vencimento,
            data_venda=data_venda,
            valor=valor
        )

        # Redirecionar para a página de sucesso ou outra página
        return redirect('payment:home')  # Use o namespace aqui

    # Renderizar o template com o formulário para GET request
    return render(request, 'payment/pages/new_payment.html')

def search_payment(request):
    num_nota = request.GET.get('num_nota')
    nome = request.GET.get('nome')
    cnpj = request.GET.get('cnpj')
    data_venda = request.GET.get('data_venda')

    pagamentos = Payment.objects.all()

    if num_nota:
        pagamentos = pagamentos.filter(num_nota__icontains=num_nota)
    
    if nome:
        pagamentos = pagamentos.filter(nome__icontains=nome)
    
    if cnpj:
        pagamentos = pagamentos.filter(cnpj__icontains=cnpj)

    if data_venda:
        pagamentos = pagamentos.filter(data_venda=data_venda)

    return render(request, 'payment/pages/search_payment.html', {'pagamentos': pagamentos})
