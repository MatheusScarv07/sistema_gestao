function fetchProductData(productId) {
    fetch(`/sales/get_product/${productId}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.error) {
                alert(data.error);
            } else {
                console.log(data)
                // Preenche os campos com os dados do produto
                document.getElementById(`product_name`).value = data.name
                document.getElementById(`unit_price`).value = data.price
            }
        })
        .catch(error => console.error('Error:', error));
}

const price_finally = () =>{
    let price = document.getElementById(`unit_price`).value
    let quantity = document.getElementById(`quantity`).value

    let valor_finally = price * quantity

    document.getElementById(`total_price`).value = valor_finally

}

const enviarCarrinhoParaBanco = () => {
    // Coletar dados do carrinho temporário
    
    
    const id_cliente = document.getElementById("client_select").value;
    const id_produto = document.getElementById("product_id").value;
    const name_product = document.getElementById("product_name").value;
    const quantidade = document.getElementById("quantity").value;
    const valor_uni = document.getElementById("unit_price").value;
    const valor_total = document.getElementById("total_price").value;
    const dadosDoCarrinho = document.getElementById("dados");
    const dadosCarrinho = {
        'id_cliente': id_cliente,
        'id_produto': id_produto,
        'name': name_product,
        'Qntde': quantidade,
        'valor': valor_uni,
        'valor_total': valor_total
    }
    
    // Enviar dados para o backend via fetch
    fetch('/sale/salvar-carrinho', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(dadosCarrinho)
    })
    renderizarTabelaCarrinho()
    .catch(error => console.error('Erro:', error));
};

const renderizarTabelaCarrinho = () => {
    fetch('/sales/cart_products')
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Erro ao buscar produtos do carrinho:', data.error);
            return;
        }
        
        console.log(data);
        const tableBody = document.querySelector('#cart-table tbody');
        
        if (!tableBody) {
            console.error('Elemento tbody não encontrado. Verifique se o ID do table está correto.');
            return;
        }
        
        tableBody.innerHTML = ''; // Clear existing rows
        
        if (!Array.isArray(data.cart_products) || data.cart_products.length === 0) {
            const emptyRow = document.createElement('tr');
            emptyRow.innerHTML = '<td colspan="4">Nenhum produto no carrinho</td>';
            tableBody.appendChild(emptyRow);
            return;
        }
        
        data.cart_products.forEach(item => {
            const linha = document.createElement("tr");
            linha.innerHTML = `
                <td>${item.name_produto || ''}</td>
                <td>${item.quantidade || ''}</td>
                <td>${item.valor_uni || ''}</td>
                <td>${item.valor_total || ''}</td>
            `;
            tableBody.appendChild(linha);
        });
    })
    .catch(error => console.error('Erro:', error));
};

// Função auxiliar para obter o token CSRF
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};