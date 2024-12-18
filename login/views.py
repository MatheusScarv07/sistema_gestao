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

            # Testando autenticação
            if request.user.is_authenticated:
                print(f"Usuário autenticado: {request.user.username}")
            else:
                print("Usuário não autenticado após login.")
            
            # Redirecionar para a página definida no parâmetro 'next' ou 'inicio'
            next_url = request.POST.get('next', 'inicio')
            print(f"Redirecionando para: {next_url}")
            return redirect(next_url)
        else:
            print(form.errors)
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'login/pages/login.html', {'form': form, 'next': request.GET.get('next', '/')})

def logout_view(request):
    logout(request)
    return redirect('login')
