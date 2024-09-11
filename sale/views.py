from django.shortcuts import render
from django.http import JsonResponse
from sale.controler.clients import get_clients
from sale.controler.cart import cart
from sale.models import CartTemp
from stock.models import Stock
import json
# Create your views here.
def home (request):
    return render(request, 'sales/pages/home.html')

def new_sale(request):
    clients = get_clients()
    
    return render(request, 'sales/pages/sales.html', context={
        'clients': clients
    })
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
    
def searchsales(request):
    return render(request, 'sales/pages/searchsales.html')

def cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Cria uma nova instância de CartTemp com os dados recebidos
        cart_item = CartTemp(
            id_cliente=data.get('id_cliente'),
            id_produto=data.get('id_produto'),
            name_product=data.get('name'),
            quantidade=data.get('Qntde'),
            valor_uni=data.get('valor'),
            valor_total=data.get('valor_total')
        )
        
        # Salva o item no banco de dados
        cart_item.save()
          # Imprime os dados no console
        # Faça algo com os dados, como salvar no banco de dados
        return JsonResponse({'message': 'Dados salvos com sucesso'})
    else:
        return JsonResponse({'error': 'Método não permitido'})
    
def cart_products(request):
    cart_products = CartTemp.objects.all()
    products_data = list(cart_products.values()) 
    print(products_data) # Convert queryset to list of dictionaries
    return JsonResponse({'cart_products': products_data}, safe=False)
    