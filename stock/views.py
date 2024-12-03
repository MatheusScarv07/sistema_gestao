from django.shortcuts import render, redirect,get_object_or_404
from supplier.models import Supplier
from stock.models import Stock
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home (request):
  return render (request, 'stock/pages/home.html')


response = ''







from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse  # Para gerar URLs dinâmicas

@login_required
def cadastrar_produto(request):
    if request.method == "POST":
        id = request.POST.get('id-product')
        nome = request.POST.get('name-product')
        categoria = request.POST.get('category')
        valor_custo = request.POST.get('cost-price')
        valor_venda = request.POST.get('sale-price')
        estoque = request.POST.get('quantity-in-stock')
        quantidade_minima_estoque = request.POST.get('minimum-stock')
        descricao = request.POST.get('description')
        localizacao_estoque = request.POST.get('location-in-stock')
        status_produto = request.POST.get('status-product')
        unidade_medida = request.POST.get('unit-of-measure')
        garantia = request.POST.get('guarantee')
        observacao_adicional = request.POST.get('additional-observations')
        fornecedor_id = request.POST.get('id-supplier')

        fornecedor = None
        if fornecedor_id:
            fornecedor = Supplier.objects.filter(id=fornecedor_id).first()
        elif nome:
            fornecedor, _ = Supplier.objects.get_or_create(nome=nome)

        # Verifica se já existe um produto com o mesmo ID
        if Stock.objects.filter(id=id).exists():
            messages.error(request, 'Erro: Já existe um produto com o ID informado.')
            return redirect(reverse('new_product'))  # Redireciona para a mesma página após erro

        produto = Stock.objects.create(
            id=id,
            nome=nome,
            categoria=categoria,
            valor_custo=valor_custo,
            valor_venda=valor_venda,
            estoque=estoque,
            quantidade_minima_estoque=quantidade_minima_estoque,
            descricao=descricao,
            localizacao_estoque=localizacao_estoque,
            status_produto=status_produto,
            unidade_medida=unidade_medida,
            garantia=garantia,
            observacao_adicional=observacao_adicional,
            fornecedor=fornecedor,
        )

        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect(reverse('new_product'))  # Redireciona para a página de cadastro

    return render(request, 'stock/pages/new_product.html')



 
@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Stock, id=id)
    if request.method == "POST":
        produto.nome = request.POST.get('name-product')
        produto.descricao = request.POST.get('description')
        produto.estoque = request.POST.get('quantity')
        produto.valor_venda = request.POST.get('sale-price').replace(',', '.')  # Converte o valor
        produto.valor_custo = request.POST.get('cost-price').replace(',', '.')  # Adicionando a mesma conversão aqui
        produto.save()
        messages.success(request, 'Produto editado com sucesso!')
        return redirect('product')
    return render(request, 'stock/pages/edit_product.html', {'produto': produto})





@login_required
def product(request):
    print("Acessando a página de produtos")
    produtos = Stock.objects.all()
    return render(request, 'stock/pages/product.html', {'produtos': produtos})



