from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Verificando o parâmetro 'next' para redirecionar para a página correta
            next_url = request.GET.get('next', 'inicio')  # Se não houver 'next', usa 'inicio' como padrão
            print(f"Redirecionando para: {next_url}")  # Imprime o valor de next_url para depuração
            return redirect(next_url)
        else:
            print(form.errors)  # Adiciona um log de erro para ajudar a depurar
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'login/pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirecionar para a página de login após o logout
    return redirect('login')