from django.shortcuts import render, redirect
from .models import Supplier
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
from brasilapy import BrasilAPI

# Create your views here.
def home(request):
    fornecedores = Supplier.objects.all()
    return render(request, 'supplier/pages/home.html', context={
        'fornecedores': fornecedores
    })

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

        # Verificar se o CNPJ já existe
        if Supplier.objects.filter(cnpj=cnpj_form).exists():
            messages.error(request, 'Este CNPJ já está cadastrado.')
            return redirect('/supplier/register_new')

        # Criar o fornecedor se o CNPJ for único
        fornecedor = Supplier(
            nome=nome_form,
            cnpj=cnpj_form,
            email=email_form,
            contato=contato_form,
            rua=rua_form,
            numero=numero_form,
            bairro=bairro_form,
            cidade=cidade_form,
            estado=estado_form,
            cep=cep_form,
            created=created_at
        )
        fornecedor.save()
        
        messages.success(request, 'Fornecedor registrado com sucesso!')
        return redirect('/supplier')  # Ou para a página de listagem de fornecedores

    return render(request, 'supplier/pages/home.html')

""" def get_dados(request, cnpj):
    try:
        api = BrasilAPI()
        empresa = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
        print(empresa)
        
        if not empresa:
            return JsonResponse({'error': 'Dados não encontrados'}, status=404)

        # Retorna os dados da empresa como JSON
        empresa_data = {
            'razao_social': empresa[0]['razao_social'],
            'nome_fantasia': empresa["nome_fantasia"],
            'logradouro': empresa["logradouro"],
            'numero': empresa["numero"],
            'complemento': empresa['complemento'],
            'bairro': empresa['bairro'],
            'cep': empresa['cep'],
            'uf': empresa['uf'],
            'municipio': empresa['municipio'],
            'ddd_telefone_1': empresa['ddd_telefone_1']
        }
        print(empresa_data)
        return JsonResponse(empresa_data)

    except Exception as e:
        print(f"Erro: {e.__class__.__name__} - {e}")  # Tipo de erro e mensagem
        return JsonResponse({'error': 'Ocorreu um erro inesperado'}, status=500) """

def details_client(request, id):
    data = Supplier.objects.get(id=id)
    return render(request, 'supplier/pages/details_supplier.html', context={
        'supplier': data
    })








def listar_fornecedores(request):
    # Variáveis para armazenar os dados de filtro
    nome = request.POST.get('nome', '')
    cpf_cnpj = request.POST.get('cpf_cnpj', '')

    # Filtrando os fornecedores com base nos dados de filtro
    fornecedores = Supplier.objects.all()  # Começa com todos os fornecedores

    if nome:
        fornecedores = fornecedores.filter(nome__icontains=nome)  # Filtra pelo nome
    if cpf_cnpj:
        fornecedores = fornecedores.filter(cnpj__icontains=cpf_cnpj)  # Filtra pelo CPF/CNPJ

    # Renderiza a página com os fornecedores filtrados
    return render(request, 'supplier/pages/home.html', {'fornecedores': fornecedores})



def detalhes_fornecedor(request, id):
    fornecedor = get_object_or_404(Supplier, id=id)  # Buscar fornecedor pelo ID
    return render(request, 'supplier/details_supplier.html', {'fornecedor': fornecedor})