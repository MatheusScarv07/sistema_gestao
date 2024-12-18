from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    print("Entrou na view 'home'")
    print(f"Usuário autenticado: {request.user.username}")
    return render(request, 'main/pages/home.html')
