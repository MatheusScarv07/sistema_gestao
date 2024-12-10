from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def criar_usuario_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "O nome de usuário já existe.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "O e-mail já está em uso.")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('criar_usuario')

    return render(request, 'criar_usuario.html')

def listar_usuarios_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        user.is_active = not user.is_active  # Alterna o status ativo/inativo
        user.save()
        status = "ativado" if user.is_active else "desativado"
        messages.success(request, f"Usuário '{user.username}' foi {status} com sucesso.")

    usuarios = User.objects.all()  # Busca todos os usuários
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})