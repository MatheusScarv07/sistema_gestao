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
  
        const tableBody = document.getElementById('dados');
  
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
  
          // Create a link for product deletion
          const deleteLink = document.createElement("a");
          deleteLink.href = `/sale/excluir/${item.id}`; // Replace with your deletion URL pattern
          deleteLink.textContent = "Excluir";
          deleteLink.classList.add('delete-product-link'); // Add a class for styling/behavior
  
          linha.innerHTML = `
            <td>${item.name_product || ''}</td>
            <td>${item.quantidade || ''}</td>
            <td>${item.valor_uni || ''}</td>
            <td>${item.valor_total || ''}</td>
            <td>${deleteLink.outerHTML}</td>
          `;
  
          tableBody.appendChild(linha);
        });
      })
      .catch(error => console.error('Erro:', error));
  };
  
  // Call the function initially to render the cart table
  renderizarTabelaCarrinho();
  
  // Add event listener for product deletion links
  document.addEventListener('click', event => {
    const clickedElement = event.target;
    if (clickedElement.classList.contains('delete-product-link')) {
      event.preventDefault(); // Prevent default link behavior (full page reload)
  
      const productId = clickedElement.href.split('/').pop(); // Extract product ID from URL
      const csrftoken = getCookie('csrftoken');

      fetch(`sale/excluir_produto/${productId}`, {
        method: 'POST', // Ensure the view handles POST requests
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken // Include CSRF token for security
        }
      })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            console.log('Produto excluído com sucesso!');
            window.location.reload()
            // Update the DOM with the new data (optional)
            // You can call renderizarTabelaCarrinho() again to refresh the entire table
            // Or, selectively update specific elements based on data.cart_html (if provided)
  
            // Show a success message (optional)
            // ...
          } else {
            console.error('Erro ao excluir produto:', data.message);
            // Show an error message (optional)
            // ...
          }
        })
        .catch(error => console.error('Erro na requisição AJAX:', error));
    }
  });
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

function excluirItem(itemId) {
    fetch(`/sale/excluir/${itemId}`, {
      method: 'DELETE' // Método HTTP para exclusão
    })
    .then(response => {
      if (response.ok) {
        // Encontrar a linha a ser removida (ajuste o seletor conforme sua estrutura HTML)
        const linha = document.querySelector(`tr[data-item-id="${itemId}"]`);
        linha.remove();
  
        // Atualizar a contagem de itens ou o total (opcional)
        // ...
      } else {
        console.error('Erro ao excluir item');
      }
    })
    .catch(error => {
      console.error('Erro:', error);
    });
  }