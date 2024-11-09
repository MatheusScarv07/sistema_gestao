from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from supplier.models import Supplier
from stock.models import Stock
from nfe.models import NFE, NFECartTemp, NFEInfo
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, Http404


# Create your views here.

def home (request):
    return render(request, 'nfe/pages/home.html')

@csrf_exempt
def new_NFE(request):
    fornecedores = Supplier.objects.all()
    carts = NFECartTemp.objects.all()
    button_enviar = False
    response = ''
    return render(request, 'nfe/pages/nfes.html', context={
        'fornecedores': fornecedores,
        'cart': carts,
        'button_enviar': button_enviar,
        'response': response
    })

def get_product(request, product_id):
    try:
        # Busque o produto no banco de dados
        product = Stock.objects.get(id=product_id)
        # Retorne os dados do produto como JSON
        product_data = {
            'id': product.id,
            'name': product.nome,
        }
        print(product_data)
        return JsonResponse(product_data)
    except Stock.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    
@csrf_exempt
def cart(request):
    response = ''
    if request.method == 'POST':
        fornecedor_id = request.POST.get('fornecedor')
        data_emissao = request.POST.get('vendedor')
        numero_nota = request.POST.get('numero_nota')
        valor_nota = request.POST.get('valor_total_nfe')
        boleto = request.POST.get('boleto')
        produto = request.POST.get('id_produto')
        data_emissao = request.POST.get('data_emissao')
        valor_unitario = float(request.POST.get('valor'))
        quantidade = float(request.POST.get('Qntde'))
        valor_total = float(request.POST.get('valor_total'))
        data_entrada = datetime.now()
        if boleto == 'Sim':
            info_bol = True
        else:
            info_bol = False
        # Salva o ID do cliente e vendedor na sessão
        request.session['fornecedor_id'] = fornecedor_id
        request.session['numero_nota'] = numero_nota
        request.session['data_emissao'] = data_emissao
        request.session['boleto'] = boleto
        request.session['valor_nota'] = valor_nota

        try:
            # Busca cliente e vendedor
            fornecedor = Supplier.objects.get(id=fornecedor_id)
        except Supplier.DoesNotExist:
            response = 'fornecedor não encontrado'
            return JsonResponse({'error': response}, status=404)

        # Verifica estoque do produto
        try:
            dados_carrinho = Stock.objects.get(id=produto)
        except Stock.DoesNotExist:
            response = 'Cadastre o produto para continuar'
            return JsonResponse({'error': response}, status=404)

        
        
        # Cria e salva o item no carrinho
        cart_item = NFECartTemp(
            fonecedor=fornecedor_id,
            id_produto=dados_carrinho.id,
            name_product=dados_carrinho.nome,
            quantidade=quantidade,
            valor_uni=valor_unitario,
            valor_total=valor_total
        )
        cart_item.save()
        response = 'Produto Adicionado'

        # Busca todos os itens do carrinho
        carts = NFECartTemp.objects.all()
        button_enviar = True
        print(data_emissao)
        data_emi = data_emissao
        # Renderiza o template com o contexto correto
        return render(
            request,
            'nfe/pages/nfes.html',
            context={
                'fornecedores': Supplier.objects.all(),  # Passa todos os clientes
                'selected_fornecedor': fornecedor,
                'cart': carts,
                'response': response,
                'button_enviar': button_enviar,
                'num_nota': numero_nota,
                "data_emi": data_emi,
                'valor_total_nota': valor_nota
            }
        )
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    

@csrf_exempt
def excluir_produto(request, id):
    try:
        produto = NFECartTemp.objects.get(id=id)
        produto.delete()

        # Obtenha os dados necessários para renderizar a página do carrinho
        fornecedor_id = request.session.get('fornecedor_id')
        

        if fornecedor_id:
            try:
                fornecedor = Supplier.objects.get(id=fornecedor_id)
                fornecedores = Supplier.objects.all()
                carts = NFECartTemp.objects.all()
                return render(
                    request,
                    'nfe/pages/nfes.html',
                    context={
                        'fornecedores': fornecedores,  # A lista completa de clientes
                        'cart': carts,
                        'response': 'Produto excluído com sucesso',
                        'button_enviar': True,
                        'selected_fornecedor': fornecedor,
                    }
                )
            except Supplier.DoesNotExist:
                return render(request, 'nfe/pages/nfes.html', {'response': 'Cliente não encontrado'})
        else:
            return redirect('sale/salvar-carrinho/')

    except NFECartTemp.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Produto não encontrado'})

@csrf_exempt
def efetuar_entrada(request):
    try:
        carrinho = NFECartTemp.objects.all()
        fornecedor_ = Supplier.objects.get(id = request.session.get('fornecedor_id') )
        numero_nota_ = request.session.get('numero_nota')
        data_emissao_ = request.session.get('data_emissao')
        boleto = request.session.get('boleto')
        valor_nfe = request.session.get('valor_nota')
        valor = []
       
        for produto in carrinho:
            data = datetime.now()
            item = Stock.objects.get(id = produto.id_produto)
            new = NFE(
                fornecedor = fornecedor_,
                data_emissao = data_emissao_,
                numero_nota = numero_nota_,
                produto = item,
                valor_unitario = produto.valor_uni,
                quantidade = produto.quantidade,
                valor_total = produto.valor_total,
                data_entrada = data,
                
            )
            estoque_atual = item.estoque or 0  # Considera 0 caso o estoque esteja vazio
            novo_estoque = estoque_atual + produto.quantidade
            item.estoque = novo_estoque  # Atualiza o estoque do item
            item.valor_custo = produto.valor_uni
            item.save()  # Salva a atualização no banco de dados

            valor.append(produto.valor_total)
            new.save()
            valor_nota = sum(valor)
        data_entrada = datetime.now()
        info = NFEInfo(
            fornecedor = fornecedor_,
            data_entrada = data_entrada,
            data_emissao = data_emissao_,
            numero_nota = numero_nota_,
            quantidade_itens = len(valor),
            boleto = boleto,
            valor_total = valor_nfe
        )
        info.save()
        NFECartTemp.objects.all().delete()
        request.session.pop('numero_nota')
        request.session.pop('fornecedor_id')
        request.session.pop('data_emissao')
        return redirect('entrada_de_nota')      
    except Exception as e:
        # Handle exceptions appropriately, e.g., return an error response
        return HttpResponseBadRequest(f"An error occurred: {e}")


def search_nfes(request):
    compras = NFEInfo.objects.all()
    fornecedores = Supplier.objects.all()

    return render(request, 'nfe/pages/searchnfe.html', context={
        'fornecedores': fornecedores,
        'notas':compras
    })

def info_nfe(request, num_nota):
    # Tenta recuperar as informações da NFE
    try:
        compra = NFE.objects.filter(numero_nota=num_nota)
        dados = NFEInfo.objects.get(numero_nota=num_nota)
    except NFEInfo.DoesNotExist:
        raise Http404("Informações da NFE não encontradas")
    
    return render(request, 'nfe/pages/info_nfe.html', context={
        'budget': dados,
        'budget_info': compra
    })