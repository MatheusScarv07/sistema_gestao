from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
        else:
            # Exibe os erros do formulário para diagnóstico
            print(form.errors)  # Adicione esta linha para depurar
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'login/pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirecionar para a página de login após o logout
    return redirect('login')