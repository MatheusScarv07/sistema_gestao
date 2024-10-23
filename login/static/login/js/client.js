function fetchEnderecoData(cep) {
    // Mostra uma mensagem de carregamento

    
    fetch(`/client/get_endereco/${cep}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro na requisição: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            
            console.log(data); // Exibe os dados no console
            
            if (data.error) {
                alert(data.error); // Mostra um alerta se houver erro nos dados
            } else {
                // Preenche os campos do formulário com os dados do endereço
                document.getElementById('rua').value = data.rua;
                document.getElementById('bairro').value = data.bairro;
                document.getElementById('cidade').value = data.cidade;
                document.getElementById('estado').value = data.estado;
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Ocorreu um erro ao buscar o endereço. Tente novamente.');
        });
}