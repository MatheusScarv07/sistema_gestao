from django.shortcuts import render
from .models import pay
# Create your views here.


def home (request):
  return render (request, 'payment/pages/home.html')






def search_payment(request):
    pagamentos = pay.objects.all()  # Busca todos os pagamentos no banco de dados
    return render(request, 'payment/pages/search_payment.html', {'pagamentos': pagamentos})







