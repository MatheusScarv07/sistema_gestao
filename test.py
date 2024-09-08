from django.db import models


class Client(models.Model):
    nome = models.TextField()
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.TextField(null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    nome_fantasia = models.TextField(null=True, blank=True)
    cpf_cliente = models.TextField(null=True, blank=True)
    cnpj_cliente = models.TextField(null=True, blank=True)
    rg_cliente = models.TextField(null=True, blank=True)
    inscricao_estadual_cliente = models.TextField(null=True, blank=True)
    telefone_contato = models.TextField(null=True, blank=True)
    telefone_celular = models.TextField(null=True, blank=True)
    numero_casa = models.TextField(null=True, blank=True)
    complemento = models.TextField(null=True, blank=True)
    bairro = models.TextField(null=True, blank=True)
    cidade = models.TextField(null=True, blank=True)
    estado = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Stock(models.Model):
    nome = models.TextField()
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.TextField(null=True, blank=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade_minima_estoque = models.IntegerField(null=True, blank=True)
    unidade_medida = models.TextField(null=True, blank=True)
    fornecedor = models.TextField(null=True, blank=True)
    fornecedor_id = models.ForeignKey('Fornecedor', on_delete=models.SET_NULL, null=True, blank=True)
    localizacao_estoque = models.TextField(null=True, blank=True)
    status_produto = models.TextField(null=True, blank=True)
    garantia = models.TextField(null=True, blank=True)
    observacao_adicional = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.TextField()
    contato = models.TextField(null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    cnpj = models.TextField(null=True, blank=True)
    telefone = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.TextField()
    cargo = models.TextField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_venda = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cpf_cnpj_cliente = models.TextField(null=True, blank=True)
    nome_cliente = models.TextField(null=True, blank=True)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Venda {self.id}"


class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_orcamento = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cpf_cnpj_cliente = models.TextField(null=True, blank=True)
    nome_cliente = models.TextField(null=True, blank=True)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Orçamento {self.id}"


class NFE(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    data_entrada = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    nome_fornecedor = models.TextField(null=True, blank=True)
    cnpj = models.TextField(null=True, blank=True)
    data_emissao = models.DateTimeField(null=True, blank=True)
    numero_nota = models.TextField(null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    nome_produto = models.TextField(null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Entrada Nota Fiscal {self.id}"