from django.shortcuts import render
from sale.controler.clients import get_clients
from sale.controler.cart import cart
from stock.models import Stock
# Create your views here.
def home (request):
    return render(request, 'sales/pages/home.html')

def new_sale(request):
    clients = get_clients()
    cart_temp = cart()
    return render(request, 'sales/pages/sales.html', context={
        'clients': clients
    })
def get_product(request, product_id):
    try:
        # Busque o produto no banco de dados
        product = Stock.objects.get(id=product_id)
        print(product)
        # Retorne os dados do produto como JSON
        product_data = {
            'id': product.id,
            'name': product.nome,  # Nome do produto no banco
            'price': product.valor_venda  # Preço unitário do produto
        }
        return JsonResponse(product_data)
    except Stock.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    
def searchsales(request):
    return render(request, 'sales/pages/searchsales.html')
