from django.shortcuts import render, redirect
from random import randint
from django.http import HttpResponseBadRequest,JsonResponse
from datetime import datetime
from budget.controller.filter_budget import obter_budget_filtradas
from django.views.decorators.csrf import csrf_exempt
from client.models import Client
from employee.models import Employee
from budget.models import Budget, CartTempBudget, BudgetInfo
from stock.models import Stock
from sale.controler.clients import get_clients
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib import messages
from sale.models import Sale, SaleInfo




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


@csrf_exempt
def new_budget(request):
    clients = Client.objects.all()
    carts = CartTempBudget.objects.all()
    button_enviar = False
    response = ''
    vendedor = Employee.objects.all()
    produtos = Stock.objects.all()
    return render(request, 'budget/pages/new_budget.html', context={
        'clientes': clients,
        'vendedores': vendedor,
        'cart': carts,
        'button_enviar': button_enviar,
        'response': response,
        'produtos_estoque': produtos
    })

@csrf_exempt
def enviar_orcamento(request):
    try:
        if request.method == 'POST':
            carrinho = CartTempBudget.objects.all()
            numero_saida = randint(1, 100)
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
            CartTempBudget.objects.all().delete()
            clients = Client.objects.all()
            carts = CartTempBudget.objects.all()
            button_enviar = False
            response = ''
            vendedor = Employee.objects.all()
            return render(request, 'budget/pages/new_budget.html', context={
                'clientes': clients,
                'vendedores': vendedor,
                'cart': carts,
                'button_enviar': button_enviar,
                'response': response
            })      
    except Exception as e:
        # Handle exceptions appropriately, e.g., return an error response
        return HttpResponseBadRequest(f"An error occurred: {e}")
    

@csrf_exempt
def cart(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        vendedor_id = request.POST.get('vendedor')
        id_produto = request.POST.get('id_produto')
        product_name = request.POST.get('name')
        quantidade = float(request.POST.get('Qntde'))
        valor_uni_str = request.POST.get('valor').replace(',', '.')
        valor_uni = float(valor_uni_str)
        valor_total = float(request.POST.get('valor_total'))

        # Salva o ID do cliente e vendedor na sessão
        request.session['cliente_id'] = cliente_id
        request.session['vendedor_id'] = vendedor_id

        try:
            # Busca cliente e vendedor
            cliente = Client.objects.get(id=cliente_id)
            vendedor = Employee.objects.get(id=vendedor_id)
        except Client.DoesNotExist:
            messages.error(request, 'Cliente não encontrado')  # Mensagem de erro
            return render_cart_page(request)

        except Employee.DoesNotExist:
            messages.error(request, 'Vendedor não encontrado')  # Mensagem de erro
            return render_cart_page(request)

        # Verifica estoque do produto
        try:
            dados_carrinho = Stock.objects.get(id=id_produto)
        except Stock.DoesNotExist:
            messages.error(request, 'Produto não encontrado')  # Mensagem de erro
            return render_cart_page(request)

        # Cria e salva o item no carrinho
        cart_item = CartTempBudget(
            id_cliente=cliente_id,
            id_produto=id_produto,
            name_product=product_name,
            quantidade=quantidade,
            valor_uni=valor_uni,
            valor_total=valor_total
        )

        cart_item.save()
        messages.success(request, 'Produto Adicionado com sucesso!')  # Mensagem de sucesso

        # Busca todos os itens do carrinho
        return render_cart_page(request, cliente, vendedor)

    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)


def render_cart_page(request, cliente=None, vendedor=None):
    # Renderiza o template com o contexto correto
    return render(
        request,
        'budget/pages/new_budget.html',
        context={
            'clientes': Client.objects.all(),
            'vendedores': Employee.objects.all(),
            'selected_cliente': cliente,
            'selected_vendedor': vendedor,
            'cart': CartTempBudget.objects.all(),
            'button_enviar': True  # Habilita o botão enviar na renderização normal
        }
    )
    



@csrf_exempt
def excluir_produto(request, id):
    try:
        produto = CartTempBudget.objects.get(id=id)
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
                carts = CartTempBudget.objects.all()
                produtos = Stock.objects.all()
                return render(
                    request,
                    'budget/pages/new_budget.html',
                    context={
                        'clientes': clientes,  # A lista completa de clientes
                        'vendedores': vendedores,  # A lista completa de vendedores
                        'cart': carts,
                        'response': 'Produto excluído com sucesso',
                        'button_enviar': True,
                        'selected_cliente': cliente,  # O cliente selecionado
                        'selected_vendedor': vendedor,  # O vendedor selecionado
                        'produtos_estoque': produtos,
                    }
                )
            except Client.DoesNotExist:
                return render(request, 'sales/pages/sales.html', {'response': 'Cliente não encontrado'})
            except Employee.DoesNotExist:
                return render(request, 'sales/pages/sales.html', {'response': 'Vendedor não encontrado'})
        else:
            return redirect('sale/salvar-carrinho/')

    except CartTempBudget.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Produto não encontrado'})

@csrf_exempt 
def clear_cart(request):
    # Remove todos os itens do carrinho para o cliente especificado
    CartTempBudget.objects.all().delete()

    # Retorna uma resposta de sucesso
    return redirect('inicio')



@csrf_exempt
def gerar_relatorio(request):
    # Carrega os dados necessários para o relatório
    context = {
        'dados_orcamento': 'Dados do orçamento aqui'  # Atualize com os dados reais do orçamento
    }
    html_string = render_to_string('budget/relatorio.html', context)
    html = HTML(string=html_string)
    
    # Gera o PDF e retorna uma resposta
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as output:
        html.write_pdf(output)
        pdf_file_path = output.name

    # Renderiza o template do relatório com o botão de envio para WhatsApp
    return render(request, 'budget/relatorio.html', {'pdf_file_path': pdf_file_path})




@csrf_exempt
def enviar_whatsapp(request):
    pdf_file_path = request.POST.get('pdf_file_path')
    recipient_number = 'whatsapp:+55SEUNÚMERO'  # Substitua com o número de destino

    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Número do Twilio para WhatsApp
        body='Segue o relatório em PDF.',
        media_url=[pdf_file_path],
        to=recipient_number
    )
    
    return HttpResponse(f"PDF enviado via WhatsApp com sucesso. ID da mensagem: {message.sid}")


def efetuar_venda(request, num_orcamento):
    try:
        dados_orcamento = BudgetInfo.objects.get(number_budget=int(num_orcamento))
        client = Client.objects.get(id=dados_orcamento.cliente.id)
        seller = Employee.objects.get(id=dados_orcamento.vendedor.id)
        budget_items = Budget.objects.filter(number_budget=num_orcamento)
        print(budget_items)
         # Obter o carrinho temporário e informações do orçamento
        numero_venda = randint(1, 1000)
        budget_items = Budget.objects.filter(number_budget=num_orcamento)

        valor = []
        sales = []  # List to collect Sale instances for bulk creation
        for produto in budget_items:
            data = datetime.now()
            item = Stock.objects.get(id=produto.produto.id)

            # Create new sale
            new_sale = Sale(
                num_sale=numero_venda,
                cliente=client,
                data_venda=data,
                vendedor=seller,
                cpf_cnpj_cliente=client.cpf_cnpj,
                produto=item,
                valor_unitario=produto.valor_unitario,
                quantidade=produto.quantidade,
                valor_total=produto.valor_total
            )
            valor.append(produto.valor_total)
            sales.append(new_sale)

        # Bulk create sales for efficiency
        print(sales)
        Sale.objects.bulk_create(sales)

        # Calculate total sale value
        valor_venda = sum(valor)

        # Create sale information
        sale_info = SaleInfo(
            num_sale=numero_venda,
            cliente=client,
            cpf_cnpj=client.cpf_cnpj,
            valor=valor_venda,
            vendedor=seller
        )
        sale_info.save()

        # Clear temporary cart
        dados_orcamento.delete()  # This also deletes related budget items
        Budget.objects.filter(number_budget=num_orcamento).delete() 

        return redirect('receive_page', num_venda = numero_venda)  

    except BudgetInfo.DoesNotExist:
        return HttpResponseBadRequest("Budget information not found.")
    except Client.DoesNotExist:
        return HttpResponseBadRequest("Client not found.")
    except Employee.DoesNotExist:
        return HttpResponseBadRequest("Seller not found.")
    except Stock.DoesNotExist:
        return HttpResponseBadRequest("Stock item not found.")
    except Exception as e:
        return HttpResponseBadRequest(f"An unexpected error occurred: {e}")
