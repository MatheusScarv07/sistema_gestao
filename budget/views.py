from django.shortcuts import render 
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
    return render(request, 'budget/pages/new_budget.html', context={
        'clientes': clients,
        'vendedores': vendedor,
        'cart': carts,
        'button_enviar': button_enviar,
        'response': response
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
        print(cliente_id)
        

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
        response = 'Produto Adicionado'

        # Busca todos os itens do carrinho
        carts = CartTempBudget.objects.all()
        button_enviar = True

        # Renderiza o template com o contexto correto
        return render(
            request,
            'budget/pages/new_budget.html',
            context={
                'clientes': Client.objects.all(),  # Passa todos os clientes
                'vendedores': Employee.objects.all(),  # Passa todos os vendedores
                'selected_cliente': cliente,  # Passa o cliente selecionado
                'selected_vendedor': vendedor,  # Passa o vendedor selecionado
                'cart': carts,
                'response': response,
                'button_enviar': button_enviar
            }
        )
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    



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
