function fetchSupplierData(cnpj) {
    // Faz uma requisição para obter os dados do CNPJ
    fetch(`/supplier/get_dados/${cnpj}/`)
        .then(response => response.json())
        .then(data => {
            console.log(data); // Exibe os dados no console
            if (data.error) {
                // Mostra um alerta se houver um erro nos dados recebidos
                alert(data.error);
            } else {
                // Preenche os campos do formulário com os dados do fornecedor
                document.getElementById('razao_social').value = data.razao_social;
                document.getElementById('nome_fantasia').value = data.nome_fantasia;
                document.getElementById('endereco').value = data.logradouro;
                document.getElementById('numero').value = data.numero;
                document.getElementById('complemento').value = data.complemento;
                document.getElementById('bairro').value = data.bairro;
                document.getElementById('cep').value = data.cep;
                document.getElementById('cidade').value = data.municipio;
                document.getElementById('estado').value = data.uf;
                document.getElementById('telefone').value = data.ddd_telefone_1;
            }
        })
        .catch(error => console.error('Erro:', error)); // Tratamento de erros
}

// Adiciona evento de busca quando o campo de CNPJ perde o foco
document.getElementById('cnpj').addEventListener('blur', function() {
    const cnpj = this.value;
    if (cnpj) {
        fetchSupplierData(cnpj);
    }
});