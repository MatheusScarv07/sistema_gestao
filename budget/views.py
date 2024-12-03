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
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def home (request):
  return render (request, 'budget/pages/home.html')




@login_required
def budget_search(request):
    budget_list = BudgetInfo.objects.all().order_by('-data_orcamento')
    clientes = Client.objects.all()
    vendedor_db = Employee.objects.all()
    
    # Paginação
    page_number = request.GET.get('page', 1)  # Página atual, padrão é 1
    paginator = Paginator(budget_list, 10)  # 10 itens por página
    budgets = paginator.get_page(page_number)
    
    return render(request, "budget/pages/search_budget.html", {
        "budget": budgets,  # Passando o objeto paginado
        'clientes': clientes,
        'vendedores': vendedor_db
    })

@login_required
def search_budget_filter(request):
    data_inicial = request.POST.get('date_inicial')
    data_final = request.POST.get('date_final')
    nome = request.POST.get('cliente')
    cpf = request.POST.get('cpf')
    number_sale = request.POST.get('number_budget')
    vendedor = request.POST.get('vendedor')
    clientes = Client.objects.all()
    vendedor_db = Employee.objects.all()
    
    # Aplicar filtros personalizados
    budgets_list = obter_budget_filtradas(data_inicial, data_final, nome, cpf, vendedor, number_sale)
    
    # Paginação
    page_number = request.GET.get('page', 1)
    paginator = Paginator(budgets_list, 10)  # Mostra 10 resultados por página
    budgets = paginator.get_page(page_number)
    
    return render(request, "budget/pages/search_budget.html", {
        "budget": budgets,  # Passando o objeto paginado
        'clientes': clientes,
        'vendedores': vendedor_db
    })

@login_required
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

@login_required
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
    

@login_required
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

@login_required
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
    



@login_required
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

@login_required
def clear_cart(request):
    # Remove todos os itens do carrinho para o cliente especificado
    CartTempBudget.objects.all().delete()

    # Retorna uma resposta de sucesso
    return redirect('inicio')



@login_required
def gerar_pdf(request, number_budget):
    # Dados para o template
    budget = BudgetInfo.objects.get(number_budget= number_budget)
    budget_info = Budget.objects.filter(number_budget=number_budget)
     
    context = {'budget': budget, 'budget_info': budget_info}
    
    # Carregar o template HTML
    template = get_template('budget/pages/orcamento_pdf.html')
    html = template.render(context)
    name_arquivo = f'{budget.number_budget} - {budget.cliente.nome}'
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
    budget = BudgetInfo.objects.all().order_by('-data_orcamento')
    data = datetime.now()
    context = {'budget': budget}
    
    # Carregar o template HTML
    template = get_template('budget/pages/relatorio.html')
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

@login_required
def efetuar_venda(request, num_orcamento):
    try:
        # Tente obter as informações do orçamento
        dados_orcamento = BudgetInfo.objects.get(number_budget=int(num_orcamento))
        
        # Verifique se cliente e vendedor existem
        if dados_orcamento.cliente is None:
            return HttpResponseBadRequest("Cliente não especificado no orçamento.")
        if dados_orcamento.vendedor is None:
            return HttpResponseBadRequest("Vendedor não especificado no orçamento.")
        
        client = Client.objects.get(id=dados_orcamento.cliente.id)
        seller = Employee.objects.get(id=dados_orcamento.vendedor.id)
        
        # Obtenha os itens do orçamento
        budget_items = Budget.objects.filter(number_budget=num_orcamento)
        
        # Obtenha o número da venda e inicialize listas para valores e vendas
        numero_venda = randint(1, 1000)
        valor = []
        sales = []

        for produto in budget_items:
            data = datetime.now()
            item = Stock.objects.get(id=produto.produto.id)

            # Crie uma nova venda
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

        # Criação em massa das vendas
        Sale.objects.bulk_create(sales)

        # Calcula o valor total da venda
        valor_venda = sum(valor)

        # Crie as informações da venda
        sale_info = SaleInfo(
            num_sale=numero_venda,
            cliente=client,
            cpf_cnpj=client.cpf_cnpj,
            valor=valor_venda,
            vendedor=seller
        )
        sale_info.save()

        # Limpe o carrinho temporário
        dados_orcamento.delete()
        Budget.objects.filter(number_budget=num_orcamento).delete()

        return redirect('receive_page', num_venda=numero_venda)

    except BudgetInfo.DoesNotExist:
        return HttpResponseBadRequest("Informações do orçamento não encontradas.")
    except Client.DoesNotExist:
        return HttpResponseBadRequest("Cliente não encontrado.")
    except Employee.DoesNotExist:
        return HttpResponseBadRequest("Vendedor não encontrado.")
    except Stock.DoesNotExist:
        return HttpResponseBadRequest("Item de estoque não encontrado.")
    except Exception as e:
        return HttpResponseBadRequest(f"Ocorreu um erro inesperado: {e}")
    
@login_required
def page_details(request, number_budget):
    budget = BudgetInfo.objects.get(number_budget= number_budget)
    budget_info = Budget.objects.filter(number_budget=number_budget)
    print(budget_info)
    return render(request, 'budget/pages/info_budget.html', context={
        'budget': budget,
        'budget_info': budget_info
    })

@login_required
def delete_budget(request, number_budget):
    try:
        # Tenta obter o orçamento e os itens do orçamento
        budget = BudgetInfo.objects.get(number_budget=number_budget)
        budget_info = Budget.objects.filter(number_budget=number_budget)

        # Exclui o orçamento e os itens relacionados
        budget.delete()
        budget_info.delete()

        return redirect('ver_orcamentos')

    except BudgetInfo.DoesNotExist:
        return HttpResponseBadRequest("Orçamento não encontrado.")
    except Exception as e:
        return HttpResponseBadRequest(f"Ocorreu um erro inesperado: {e}")
    
@login_required
def editar_orcamento(request, number_budget):
    try:
        # Tenta obter o orçamento principal
        budget = BudgetInfo.objects.get(number_budget=number_budget)
        
        # Obter os itens do orçamento relacionados
        budget_items = Budget.objects.filter(number_budget=number_budget)

        # Renderiza a página de edição com os dados do orçamento e itens
        return render(request, 'budget/pages/editar_orcamento.html', {
            'budget': budget,
            'budget_items': budget_items
        })

    except BudgetInfo.DoesNotExist:
        return HttpResponseBadRequest("Orçamento não encontrado.")
    except Exception as e:
        return HttpResponseBadRequest(f"Ocorreu um erro inesperado: {e}")

@login_required   
def salvar_orcamento(request, number_budget):
    if request.method == 'POST':
        try:
            # Obtém o orçamento principal
            budget = BudgetInfo.objects.get(number_budget=number_budget)
            
            # Atualiza dados do orçamento principal, se necessário
            total = request.POST.get('total', str(budget.total))
            total = total.replace(',', '.')  # Substitui vírgula por ponto, se houver
            budget.total = float(total)  # Converte para float após a substituição
            budget.save()

            # Itera sobre os itens do orçamento e atualiza cada um
            budget_items = Budget.objects.filter(number_budget=number_budget)
            for item in budget_items:
                item_id = str(item.id)
                
                # Obtém e converte quantidade
                quantidade = int(request.POST.get(f'quantidade_{item_id}', item.quantidade))
                
                # Obtém e converte valor unitário, substituindo ',' por '.'
                valor_unitario = request.POST.get(f'valor_unitario_{item_id}', str(item.valor_unitario))
                valor_unitario = valor_unitario.replace(',', '.')  # Substitui vírgula por ponto
                valor_unitario = float(valor_unitario)
                
                # Calcula o valor total
                valor_total = quantidade * valor_unitario
                
                # Atualiza o item do orçamento
                item.quantidade = quantidade
                item.valor_unitario = valor_unitario
                item.valor_total = valor_total
                item.save()

            return redirect('ver_orcamentos')

        except BudgetInfo.DoesNotExist:
            return HttpResponseBadRequest("Orçamento não encontrado.")
        except Budget.DoesNotExist:
            return HttpResponseBadRequest("Item do orçamento não encontrado.")
        except Exception as e:
            return HttpResponseBadRequest(f"Ocorreu um erro inesperado: {e}")

    else:
        return HttpResponseBadRequest("Método inválido para esta requisição.")