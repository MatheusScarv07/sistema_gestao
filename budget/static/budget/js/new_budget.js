
function price_finally() {
    // Pegando os valores de quantidade e preço unitário
    const quantity = document.getElementById('quantity').value;
    const unitPrice = document.getElementById('unit_price').value;
    
    // Convertendo os valores para números e calculando o total
    const totalPrice = parseFloat(quantity) * parseFloat(unitPrice);
    
    // Exibindo o preço total, formatando para duas casas decimais
    if (!isNaN(totalPrice)) {
        document.getElementById('total_price').value = totalPrice.toFixed(2);
    } else {
        document.getElementById('total_price').value = '';
    }
}


function fetchProductData(productId) {
    // Faz uma requisição fetch para obter os dados do produto
    fetch(`/sales/get_product/${productId}`)
        .then(response => response.json()) // Converte a resposta para JSON
        .then(data => {
            console.log(data); // Exibe os dados no console
            if (data.error) {
                // Mostra um alerta se houver um erro nos dados recebidos
                alert(data.error);
            } else {
                // Preenche os campos do formulário com os dados do produto
                document.getElementById(`product_name`).value = data.name;
                document.getElementById(`unit_price`).value = data.price;
            }
        })
        .catch(error => console.error('Error:', error)); // Tratamento de erros
  }

  function formatarMoeda(valor) {
    return `R$ ${valor.toFixed(2).replace(",", "X").replace(".", ",").replace("X", ".")}`;
}

// Seleciona todos os elementos <td> com o atributo data-valor
const tdsValoresTotais = document.querySelectorAll('td[data-valor]');

tdsValoresTotais.forEach(td => {
    // Obtém o valor do data-valor e o converte em número
    const valorTotal = parseFloat(td.getAttribute("data-valor"));
    
    // Formata o valor e substitui o conteúdo do <td>
    td.textContent = formatarMoeda(valorTotal);
});