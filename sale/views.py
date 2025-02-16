from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.db.models.functions import ExtractMonth, ExtractYear
from sale.controler.clients import get_clients
from sale.controler.filter_vendas import obter_vendas_filtradas
from sale.controler.cart import cart_products
from sale.models import CartTemp, Sale, SaleInfo
from stock.models import Stock
from client.models import Client
from employee.models import Employee
from sale.models import Sale
from receive.models import Receive
from receive.models import PaymentHistory
from django.views.decorators.csrf import csrf_exempt
from budget.models import Budget, BudgetInfo
import random
from random import randint
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required

# Create your views here.

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

@login_required
def home (request):
    data = datetime.now()
    mes = data.month
    ano = data.year
    vendas_mes_ano = SaleInfo.objects.annotate(mes=ExtractMonth('data_venda'), ano=ExtractYear('data_venda')).filter(mes=mes, ano=ano)
    valor_a_receber = Receive.objects.annotate(mes=ExtractMonth('data_venda'), ano=ExtractYear('data_venda')).filter(mes=mes, ano=ano, status='Pendente')
    valor_recebido = Receive.objects.annotate(mes=ExtractMonth('data_venda'), ano=ExtractYear('data_venda')).filter(mes=mes, ano=ano, status='Pago')
    #loop sobre os valores para pegar os valores e armazenar em um array 
    valor_vendido = [venda.valor for venda in vendas_mes_ano]
    valores_a_receber = [venda.valor for venda in valor_a_receber]
    valores_recebidos = [venda.valor for venda in valor_recebido]
    # soma os valores qeu estão dentro do array para definir os valores
    soma_vendas = sum(valor_vendido)
    soma_pendentes = sum(valores_a_receber)
    soma_recebidos = sum(valores_recebidos)
    #Formata os valores para melhor experiencia do usuario, formatando em formato de R$
    venda_mes = formatar_moeda(soma_vendas)
    a_receber = formatar_moeda(soma_pendentes)
    recebidos = formatar_moeda(soma_recebidos)
    # pega a quantidade de cada venda
    quantidade_vendas = len(valor_vendido)

    #pagamentos por tipo
    pagamentos = Receive.objects.annotate(mes=ExtractMonth('data_venda'), ano=ExtractYear('data_venda')).filter(mes=mes, ano=ano)
    a_prazo = []
    debito = []
    credito = []
    pix = []
    dinheiro =[]
    for iten in pagamentos:
        if iten.tipo_pagamento.nome == 'A Prazo':
            a_prazo.append(iten.valor)
        if iten.tipo_pagamento.nome == 'Crédito':
            credito.append(iten.valor)
        if iten.tipo_pagamento.nome == 'Débito':
            debito.append(iten.valor)
        if iten.tipo_pagamento.nome == 'PIX':
            pix.append(iten.valor)
        if iten.tipo_pagamento.nome == 'dinheiro':
            dinheiro.append(iten.valor)

    soma_prazo = sum(a_prazo)
    soma_debito = sum(debito)
    soma_credito = sum(credito)
    soma_pix = sum(pix)
    soma_dinheiro = sum(dinheiro)

    valor_prazo = formatar_moeda(soma_prazo)
    quantidade_prazo = len(a_prazo)

    valor_debito = formatar_moeda(soma_debito)
    quantidade_debito = len(debito)

    valor_credito = formatar_moeda(soma_credito)
    quantidade_credito = len(credito)

    valor_pix = formatar_moeda(soma_pix)
    quantidade_pix = len(pix)

    valor_dinheiro = formatar_moeda(soma_dinheiro)
    quantidade_dinheiro = len(dinheiro)

    return render(request, 'sales/pages/home.html', context={
        'Vendas_do_mes': venda_mes,
        'quantidade_vendas': quantidade_vendas,
        'a_receber': a_receber,
        'caixa': recebidos,
        'valor_prazo': valor_prazo,
        'quantidade_prazo': quantidade_prazo,
        'valor_credito': valor_credito,
        'qunatidade_credito': quantidade_credito,
        'valor_debito': valor_debito,
        'quantidade_debito': quantidade_debito,
        'valor_pix': valor_pix,
        'quantidade_pix': quantidade_pix,
        'valor_dinheiro': valor_dinheiro,
        'quantidade_dinheiro': quantidade_dinheiro
    })


@login_required
def new_sale(request):
    clients = Client.objects.all()
    carts = CartTemp.objects.all()
    button_enviar = False
    response = ''
    vendedor = Employee.objects.all()
    produtos = Stock.objects.all()
    return render(request, 'sales/pages/sales.html', context={
        'clientes': clients,
        'vendedores': vendedor,
        'cart': carts,
        'button_enviar': button_enviar,
        'response': response,
        'produtos_estoque': produtos
    })

@login_required
def get_product(request, product_id):
    try:
        # Busque o produto no banco de dados
        product = Stock.objects.get(id=product_id)
        # Retorne os dados do produto como JSON
        product_data = {
            'id': product.id,
            'name': product.nome,  # Nome do produto no banco
            'price': product.valor_venda  # Preço unitário do produto
        }
        print(product_data)
        return JsonResponse(product_data)
    except Stock.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    
@login_required
def cart(request):
    response = ''
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        vendedor_id = request.POST.get('vendedor')
        id_produto = request.POST.get('id_produto')
        product_name = request.POST.get('name')
        quantidade = float(request.POST.get('Qntde'))
        valor_uni = float(request.POST.get('valor'))
        valor_total = float(request.POST.get('valor_total'))

        # Salva o ID do cliente e vendedor na sessão
        request.session['cliente_id'] = cliente_id
        request.session['vendedor_id'] = vendedor_id
        

        try:
            # Busca cliente e vendedor
            cliente = Client.objects.get(id=cliente_id)
            vendedor = Employee.objects.get(id=vendedor_id)
        except Client.DoesNotExist:
            response = 'Cliente não encontrado'
            return JsonResponse({'error': response}, status=404)
        except Employee.DoesNotExist:
            response = 'Vendedor não encontrado'
            return JsonResponse({'error': response}, status=404)

        # Verifica estoque do produto
        try:
            dados_carrinho = Stock.objects.get(id=id_produto)
        except Stock.DoesNotExist:
            response = 'Produto não encontrado'
            return JsonResponse({'error': response}, status=404)

        if dados_carrinho.estoque <= 0:
            response = 'Produto indisponível'
        elif quantidade > dados_carrinho.estoque:
            response = f'Quantidade Indisponível: tem {dados_carrinho.estoque}'
        else:
            # Cria e salva o item no carrinho
            cart_item = CartTemp(
                id_cliente=cliente_id,
                id_produto=id_produto,
                name_product=product_name,
                quantidade=quantidade,
                valor_uni=valor_uni,
                valor_total=valor_total
            )
            cart_item.save()
            response = 'Produto Adicionado'

        # Busca todos os itens do carrinho
        carts = CartTemp.objects.all()
        button_enviar = True
        produtos = Stock.objects.all()
        # Renderiza o template com o contexto correto
        return render(
            request,
            'sales/pages/sales.html',
            context={
                'clientes': Client.objects.all(),  # Passa todos os clientes
                'vendedores': Employee.objects.all(),  # Passa todos os vendedores
                'selected_cliente': cliente,  # Passa o cliente selecionado
                'selected_vendedor': vendedor,  # Passa o vendedor selecionado
                'cart': carts,
                'response': response,
                'button_enviar': button_enviar,
                'produtos_estoque': produtos
            }
        )
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    

@login_required
def excluir_produto(request, id):
    try:
        produto = CartTemp.objects.get(id=id)
        produto.delete()

        # Obtenha os dados necessários para renderizar a página do carrinho
        cliente_id = request.session.get('cliente_id')
        vendedor_id = request.session.get('vendedor_id')

        if cliente_id and vendedor_id:
            try:
                cliente = Client.objects.get(id=cliente_id)
                vendedor = Employee.objects.get(id=vendedor_id)
                clientes = Client.objects.all()
                vendedores = Employee.objects.all()
                carts = CartTemp.objects.all()
                return render(
                    request,
                    'sales/pages/sales.html',
                    context={
                        'clientes': clientes,  # A lista completa de clientes
                        'vendedores': vendedores,  # A lista completa de vendedores
                        'cart': carts,
                        'response': 'Produto excluído com sucesso',
                        'button_enviar': True,
                        'selected_cliente': cliente,  # O cliente selecionado
                        'selected_vendedor': vendedor,  # O vendedor selecionado
                    }
                )
            except Client.DoesNotExist:
                return render(request, 'sales/pages/sales.html', {'response': 'Cliente não encontrado'})
            except Employee.DoesNotExist:
                return render(request, 'sales/pages/sales.html', {'response': 'Vendedor não encontrado'})
        else:
            return redirect('sale/salvar-carrinho/')

    except CartTemp.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Produto não encontrado'})


@login_required
def efetuar_venda(request):
    try:
        carrinho = CartTemp.objects.all()
        numero_venda  = randint(1, 1000)
        cliente_venda = Client.objects.get(id = request.session.get('cliente_id') )
        vendedor_venda = Employee.objects.get(id = request.session.get('vendedor_id'))
        valor = []
        for produto in carrinho:
            data = datetime.now()
            item = Stock.objects.get(id = produto.id_produto)
            new = Sale(
                num_sale = numero_venda,
                cliente = cliente_venda,
                data_venda = data,
                vendedor = vendedor_venda,
                cpf_cnpj_cliente = cliente_venda.cpf_cnpj,
                produto = item,
                valor_unitario = produto.valor_uni,
                quantidade = produto.quantidade,
                valor_total = produto.valor_total
            )
            item.estoque = item.estoque - produto.quantidade
            valor.append(produto.valor_total)
            new.save()
        valor_venda = sum(valor)
        info = SaleInfo(
            num_sale = numero_venda,
            cliente = cliente_venda,
            cpf_cnpj = cliente_venda.cpf_cnpj,
            valor = valor_venda,
            vendedor = vendedor_venda
        )
        info.save()
        CartTemp.objects.all().delete()       
        return redirect('receive_page', num_venda = numero_venda)     
    except Exception as e:
        # Handle exceptions appropriately, e.g., return an error response
        return HttpResponseBadRequest(f"An error occurred: {e}")
    
    #CRIAR TEMPLATE PARA ESSE CODIGO
    def sale_info(request, num_os):
     try:
        venda = Sale.objects.get(num_sale=num_os)
        return render(request, 'sales/pages/sale_info.html', {'venda': venda})
     except Sale.DoesNotExist:
        return HttpResponseNotFound("Venda não encontrada")

@login_required
def enviar_orcamento(request):
    try:
        if request.method == 'POST':
            carrinho = CartTemp.objects.all()
            numero_saida = random.randint(1, 100)
            valor_T = []
            cliente_venda = Client.objects.get(id = request.session.get('cliente_id') )
            vendedor_venda = Employee.objects.get(id = request.session.get('vendedor_id') )
            for item in carrinho:
                agora = datetime.today()
                
                
                produto = Stock.objects.get(id = item.id_produto)

                budget = Budget(
                    number_budget = numero_saida,
                    cliente = cliente_venda,
                    data_orcamento = agora,
                    total = item.valor_total,
                    cpf_cnpj_cliente = cliente_venda.cpf_cnpj,
                    vendedor = vendedor_venda,
                    produto = produto,
                    valor_unitario = item.valor_uni,
                    quantidade = item.quantidade,
                    valor_total = item.valor_total

                    )   
                
                
                budget.save()
                valor_T.append(item.valor_total)

            response = f'Orcamento {numero_saida} criado'
            soma_valores = sum(valor_T)

            info = BudgetInfo(
                number_budget = numero_saida,
                data_orcamento = agora,
                cpf_cnpj_cliente = cliente_venda.cpf_cnpj,
                cliente = cliente_venda,
                total = soma_valores,
                vendedor = vendedor_venda,
            )
            info.save()
            CartTemp.objects.all().delete()
            clients = get_clients()
            carts = CartTemp.objects.all()
            button_enviar = False
            response = ''
            vendedor = Employee.objects.all()
            return redirect('new_sale')      
    except Exception as e:
        # Handle exceptions appropriately, e.g., return an error response
        return HttpResponseBadRequest(f"An error occurred: {e}")
 
@login_required
def searchsales(request):
    try:
        vendas_list = SaleInfo.objects.select_related('cliente', 'vendedor').all().order_by('-data_venda')
        clientes = Client.objects.all()
        vendedores = Employee.objects.all()

        # Filtragem
        cliente_id = request.GET.get('cliente')
        vendedor_id = request.GET.get('vendedor')

        if cliente_id:
            vendas_list = vendas_list.filter(cliente__id=cliente_id)
        if vendedor_id:
            vendas_list = vendas_list.filter(vendedor__id=vendedor_id)

        # Paginação
        page_number = request.GET.get('page', 1)
        paginator = Paginator(vendas_list, 10)

        try:
            vendas = paginator.get_page(page_number)
        except PageNotAnInteger:
            vendas = paginator.get_page(1)
        except EmptyPage:
            vendas = paginator.get_page(paginator.num_pages)

        return render(request, 'sales/pages/searchsales.html', {
            'vendas': vendas,
            'clientes': clientes,
            'vendedores': vendedores
        })
    except Exception as e:
        # Log do erro para depuração
        print(f"Erro ao processar a solicitação: {e}")
        
        # Renderizar uma página de erro
        return render(request, 'sales/pages/error.html', {
            'mensagem': f'Ocorreu um erro inesperado ao processar sua solicitação. Tente novamente mais tarde. {e}'
        })

@login_required
def search_sale_by_number(request, num_venda):
    try:
        products = Sale.objects.filter(num_sale = num_venda)
        paymentes =  PaymentHistory.objects.filter(num_sale = num_venda)
        for produto in products:
            nome = produto.cliente
        return render(
            request,
            'sales/pages/info_sale.html',
            context={
                'products': products,
                'nome': nome,
                'num_venda': num_venda,
                'pagamentos': paymentes
            }
        )
    except Exception as e:
        ...

@login_required
def search_sales_filter(request):
    data_inicial = request.POST.get('date_inicial')
    data_final = request.POST.get('date_final')
    nome = request.POST.get('cliente')
    cpf = request.POST.get('cpf')
    number_sale = request.POST.get('number_sale')
    vendedor = request.POST.get('vendedor')
    clientes = Client.objects.all()
    vendedor_db = Employee.objects.all()
    vendas = obter_vendas_filtradas(data_inicial, data_final, nome,cpf,vendedor,number_sale)
    return render(request, 'sales/pages/searchsales.html', context={
            'vendas':vendas,
            'clientes': clientes, 
            'vendedores': vendedor_db
        })

@login_required
def gerar_pdf(request, num_sale):
    # Dados para o template
    sale = SaleInfo.objects.get(num_sale= num_sale)
    sale_info = Sale.objects.filter(num_sale=num_sale)
     
    context = {'sale': sale, 'sale_info': sale_info}
    
    # Carregar o template HTML
    template = get_template('sales/pages/comprovante_venda.html')
    html = template.render(context) 
    name_arquivo = f'V - {sale.num_sale} - {sale.cliente.nome}'
    # Criar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name_arquivo}.pdf"'

    # Converter HTML para PDFS
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    # Verificar erros
    if pisa_status.err:
        return HttpResponse('Erro ao gerar o PDF', status=500)

    return response


@login_required
def exportar(request):
    # Dados para o template
    sale = SaleInfo.objects.all().order_by('-data_venda')
    data = datetime.now()
    context = {'sale': sale}
    
    # Carregar o template HTML
    template = get_template('sales/pages/relatorio.html')
    html = template.render(context)
    name_arquivo = f'{data}'
    # Criar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name_arquivo}.pdf"'

    # Converter HTML para PDFS
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    # Verificar erros
    if pisa_status.err:
        return HttpResponse('Erro ao gerar o PDF', status=500)

    return response  