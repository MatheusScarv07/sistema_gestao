from django.shortcuts import render
from .models import Supplier
from datetime import datetime
from django.http import JsonResponse
from brasilapy import BrasilAPI

# Create your views here.
def home(request):
    return render(request, 'supplier/pages/home.html')

def page_register(request):
    return render (request, 'supplier/pages/register.html')

def register(request):
    if request.method == 'POST':
        nome_form = request.POST.get('name')
        cnpj_form = request.POST.get('cpf_cnpj')
        email_form = request.POST.get('email')
        contato_form = request.POST.get('telefone')
        rua_form = request.POST.get('endereco')
        numero_form = request.POST.get('numero')
        bairro_form = request.POST.get('bairro')
        cidade_form = request.POST.get('cidade')
        estado_form = request.POST.get('estado')
        cep_form = request.POST.get('cep')
        created_at = datetime.now()

        fornecedor = Supplier(
            nome = nome_form,
            cnpj = cnpj_form,
            email = email_form,
            contato = contato_form,
            rua = rua_form,
            numero = numero_form,
            bairro = bairro_form,
            cidade = cidade_form,
            estado = estado_form,
            cep = cep_form,
            created = created_at
            )
        fornecedor.save()
    return render(request, 'supplier/pages/home.html')

def get_dados(request, cnpj):
    try:
        api = BrasilAPI()
        empresa = api.get_cnpj(cnpj)
        
        
        if not empresa:
            return JsonResponse({'error': 'Dados não encontrados'}, status=404)

        # Retorna os dados da empresa como JSON
        empresa_data = {
            'razao_social': empresa.razao_social,
            'nome_fantasia': empresa.nome_fantasia,
            'logradouro': empresa.logradouro,
            'numero': empresa.numero,
            'complemento': empresa.complemento,
            'bairro': empresa.bairro,
            'cep': empresa.cep,
            'uf': empresa.uf,
            'municipio': empresa.municipio,
            'ddd_telefone_1': empresa.ddd_telefone_1
        }
        print(empresa_data)
        return JsonResponse(empresa_data)

    except Exception as e:
        print(f"Erro: {e.__class__.__name__} - {e}")  # Tipo de erro e mensagem
        return JsonResponse({'error': 'Ocorreu um erro inesperado'}, status=500)