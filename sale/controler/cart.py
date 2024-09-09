from sale.models import CartTemp
from stock.models import Stock
from django.http import JsonResponse

def cart():
    # Acessando o manager diretamente pela classe CartTemp
    products = CartTemp.objects.all()  # Se você quer obter o primeiro item
    if products:  # Verifica se existe algum produto
        cart_dict = _model_to_dict(products)
        return cart_dict
    return {}  # Retorna um dicionário vazio se nenhum produto for encontrado



def _model_to_dict(obj):
    """
    Converte um objeto de modelo Django para um dicionário.
    """
    return {field.name: getattr(obj, field.name) for field in obj._meta.fields}