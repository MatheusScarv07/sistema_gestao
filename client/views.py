from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .controler.client_control import ControlClient
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

    except requests.exceptions.RequestException as e:
        # Captura exceções relacionadas à requisição
        return JsonResponse({'error': 'Erro ao buscar o endereço na API'}, status=500)

    except Exception as e:
        # Captura qualquer outra exceção inesperada
        return JsonResponse({'error': 'Ocorreu um erro inesperado'}, status=500)

@csrf_exempt
def cadastrar(request):
    controle = Client
    clients = controle.objects.all()
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

        cliente = Client(
            nome = name_form,
            email = email_form,
            telefone = telefone_form,
            cpf_cnpj = cpf_cnpj_form,
            rg = rg_form,
            rua = rua_form,
            numero_casa = numero_form,
            complemento = complemento_form,
            cep = cep_form,
            bairro = bairro_form,
            cidade = cidade_form,
            estado = estado_form,
            created = data_criacao,
            )
        cliente.save()
    return render(request, 'client/pages/home.html', context={
        'clientes':clients
    } )