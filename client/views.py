from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.db import IntegrityError
from .controler.client_control import ControlClient
from .forms import ClientForm
from client.models import Client
from datetime import datetime
from brasilapy import BrasilAPI
import re
from django.views.decorators.csrf import csrf_exempt


control_client = ControlClient()

def home(request):
      # Crie uma instância da classe ControlClient
    clients = Client.objects.all() # Chame o método get_all da instância
    print(clients)
    return render(request, 'client/pages/home.html', context={
        'clientes':clients
    } )

def details_client(request, id):
    data = control_client.get_by_id(id)
    print(data)
    return render(request, 'client/pages/details_client.html', context={
        'client': data
    })

def register(request):
    estados = control_client.get_estados()
    print(estados)
    return render(request, 'client/pages/register.html', context={
        'estados': estados
    })

def get_endereco(request, cep):
    try:
        # Valida o formato do CEP (BR: 8 dígitos numéricos)
        if not re.match(r'^\d{8}$', cep):
            return JsonResponse({'error': 'Formato de CEP inválido'}, status=400)

        # Faz a requisição para a API BrasilAPI
        api = BrasilAPI()
        endereco = api.get_cep(cep)

        # Verifica se a resposta da API contém o endereço
        if not endereco:
            return JsonResponse({'error': 'Endereço não encontrado'}, status=404)

        # Retorna os dados do endereço como JSON
        endereco_data = {
            'rua': endereco.street,
            'cep': endereco.cep,
            'bairro': endereco.neighborhood,
            'cidade': endereco.city,
            'estado': endereco.state
        }

        return JsonResponse(endereco_data)

    except request.exceptions.RequestException as e:
        # Captura exceções relacionadas à requisição
        return JsonResponse({'error': 'Erro ao buscar o endereço na API'}, status=500)

    except Exception as e:
        # Captura qualquer outra exceção inesperada
        return JsonResponse({'error': 'Ocorreu um erro inesperado'}, status=500)

@csrf_exempt
def cadastrar(request):
    try:
        clients = Client.objects.all()

        if request.method == 'POST':
            name_form = request.POST.get('name')
            email_form = request.POST.get('email')
            telefone_form = request.POST.get('telefone')
            cpf_cnpj_form = request.POST.get('cpf_cnpj')
            rg_form = request.POST.get('rg')
            rua_form = request.POST.get('endereco')
            numero_form = request.POST.get('numero')
            complemento_form = request.POST.get('complemento')
            cep_form = request.POST.get('cep')
            bairro_form = request.POST.get('bairro')
            cidade_form = request.POST.get('cidade')
            estado_form = request.POST.get('estado')
            data_criacao = datetime.now()

            # Verificação de duplicidade de CPF/CNPJ ou email
            if Client.objects.filter(cpf_cnpj=cpf_cnpj_form).exists():
                messages.error(request, 'Este CPF/CNPJ já está cadastrado.')
            elif Client.objects.filter(email=email_form).exists():
                messages.error(request, 'Este email já está cadastrado.')
            else:
                try:
                    # Criação e salvamento do cliente
                    cliente = Client(
                        nome=name_form,
                        email=email_form,
                        telefone=telefone_form,
                        cpf_cnpj=cpf_cnpj_form,
                        rg=rg_form,
                        rua=rua_form,
                        numero_casa=numero_form,
                        complemento=complemento_form,
                        cep=cep_form,
                        bairro=bairro_form,
                        cidade=cidade_form,
                        estado=estado_form,
                        created=data_criacao,
                    )
                    cliente.save()
                    messages.success(request, 'Cliente cadastrado com sucesso!')
                    return redirect('cadastrar')

                except IntegrityError:
                    messages.error(request, 'Erro de integridade ao salvar o cliente.')

        return render(request, 'client/pages/register.html', context={'clientes': clients})

    except Exception as e:
        messages.error(request, f'Erro ao processar sua solicitação. Detalhes: {e}')
        return render(request, 'client/pages/register.html', context={'clientes': clients})
    

def delete_client(request, id):
    # Verifica se a requisição é do tipo POST
    if request.method == "POST":
        cliente = get_object_or_404(Client, id=id)  # Obtém o cliente pelo ID
        cliente.delete()  # Deleta o cliente
        return redirect('consultar_cliente')  # Redireciona para a página inicial ou a lista de clientes

    return redirect('consultar_cliente')  # Redireciona caso a requisição não seja POST

def edit_client(request, id):
    cliente = get_object_or_404(Client, id=id)  # Obtém o cliente pelo ID

    if request.method == "POST":
        form = ClientForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('home')  # Redireciona para a página inicial ou onde desejar
    else:
        form = ClientForm(instance=cliente)  # Cria o formulário com os dados do cliente

    return render(request, 'client/pages/edit_client.html', {'form': form, 'cliente': cliente})