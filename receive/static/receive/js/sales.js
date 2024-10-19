 // Função para buscar os dados de um produto específico usando o ID do produto
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

// Função para calcular o preço total com base no preço unitário e na quantidade
const price_finally = () => {
  let price = parseFloat(document.getElementById('unit_price').value);
  let quantity = parseInt(document.getElementById('quantity').value, 10);

  // Calcula o valor final multiplicando preço pela quantidade
  let valor_finally = price * quantity;

  // Atualiza o campo de preço total no formulário
  document.getElementById(`total_price`).value = valor_finally;
} 

//FUNCAO ACIMA E A ANTIGA QUE ESTAVA FUNCIONANDO



//ABAIXO FUNCAO NOVA PARA TESTE, REVISAR CASO TENHA VISIBILIDADE PARA FUNCIONAR



/* function searchSales() {
  const params = new URLSearchParams();

  const name = document.getElementById('name').value;
  const cpfCnpj = document.getElementById('cpfCnpj').value;
  const vendedor = document.getElementById('vendedor').value;

  // Adiciona somente parâmetros que não estejam vazios
  if (name) params.append('name', name);
  if (cpfCnpj) params.append('cpf_cnpj', cpfCnpj);
  if (vendedor) params.append('vendedor', vendedor);

  // Redireciona para a URL com os parâmetros adequados
  const queryString = params.toString();
  window.location.href = `/sales/searchsales?${queryString}`;
}
 */




/* // Função para enviar os dados do carrinho para o backend
const enviarCarrinhoParaBanco = () => {
  // Coleta os dados do carrinho do formulário
  const id_cliente = document.getElementById("client_select").value;
  const id_produto = document.getElementById("product_id").value;
  const name_product = document.getElementById("product_name").value;
  const quantidade = document.getElementById("quantity").value;
  const valor_uni = document.getElementById("unit_price").value;
  const valor_total = document.getElementById("total_price").value;

  // Organiza os dados do carrinho em um objeto
  const dadosCarrinho = {
      'id_cliente': id_cliente,
      'id_produto': id_produto,
      'name': name_product,
      'Qntde': quantidade,
      'valor': valor_uni,
      'valor_total': valor_total
  };

  // Envia os dados para o backend via fetch
  fetch('/sale/salvar-carrinho', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken') // Inclui o token CSRF
      },
      body: JSON.stringify(dadosCarrinho) // Envia o objeto como JSON
  })
  .then(renderizarTabelaCarrinho()) // Re-renderiza a tabela com os produtos do carrinho
  .catch(error => console.error('Erro:', error)); // Tratamento de erros
};

// Função para renderizar a tabela com os produtos do carrinho
const renderizarTabelaCarrinho = () => {
  // Faz uma requisição para buscar os produtos no carrinho
  fetch('/sales/cart_products')
    .then(response => response.json()) // Converte a resposta para JSON
    .then(data => {
      if (data.error) {
        console.error('Erro ao buscar produtos do carrinho:', data.error);
        return;
      }

      const tableBody = document.getElementById('dados'); // Tabela onde os produtos serão exibidos

      if (!tableBody) {
        console.error('Elemento tbody não encontrado. Verifique se o ID do table está correto.');
        return;
      }

      tableBody.innerHTML = ''; // Limpa as linhas anteriores

      if (!Array.isArray(data.cart_products) || data.cart_products.length === 0) {
        const emptyRow = document.createElement('tr');
        emptyRow.innerHTML = '<td colspan="4">Nenhum produto no carrinho</td>'; // Exibe mensagem se o carrinho estiver vazio
        tableBody.appendChild(emptyRow);
        return;
      }

      // Itera sobre os produtos do carrinho e cria as linhas na tabela
      data.cart_products.forEach(item => {
        const linha = document.createElement("tr");

        // Cria um link para excluir o produto
        const deleteLink = document.createElement("a");
        deleteLink.href = `/sale/excluir/${item.id}`;
        deleteLink.textContent = "Excluir";
        deleteLink.classList.add('delete-product-link'); // Adiciona uma classe para estilização

        linha.innerHTML = `
          <td>${item.name_product || ''}</td>
          <td>${item.quantidade || ''}</td>
          <td>${item.valor_uni || ''}</td>
          <td>${item.valor_total || ''}</td>
          <td>${deleteLink.outerHTML}</td>
        `;

        tableBody.appendChild(linha); // Adiciona a linha na tabela
      });
    })
    .catch(error => console.error('Erro:', error)); // Tratamento de erros
};

// Chama a função para renderizar a tabela do carrinho ao carregar a página
renderizarTabelaCarrinho();

// Adiciona um event listener para manipular a exclusão de produtos
document.addEventListener('click', event => {
  const clickedElement = event.target;
  if (clickedElement.classList.contains('delete-product-link')) {
    event.preventDefault(); // Previne o comportamento padrão de recarregar a página

    const productId = clickedElement.href.split('/').pop(); // Extrai o ID do produto do link
    const csrftoken = getCookie('csrftoken'); // Obtém o token CSRF

    // Envia uma requisição para excluir o produto
    fetch(`sale/excluir_produto/${productId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken // Inclui o token CSRF
      }
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          console.log('Produto excluído com sucesso!');
          window.location.reload(); // Recarrega a página para atualizar a tabela
        } else {
          console.error('Erro ao excluir produto:', data.message);
        }
      })
      .catch(error => console.error('Erro na requisição AJAX:', error)); // Tratamento de erros
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
  return cookieValue; // Retorna o valor do cookie
};

// Função para excluir um item específico do carrinho
function excluirItem(itemId) {
  fetch(`/sale/excluir/${itemId}`, {
    method: 'DELETE' // Método HTTP para exclusão
  })
  .then(response => {
    if (response.ok) {
      // Encontra e remove a linha do item excluído da tabela
      const linha = document.querySelector(`tr[data-item-id="${itemId}"]`);
      linha.remove();
    } else {
      console.error('Erro ao excluir item');
    }
  })
  .catch(error => console.error('Erro:', error)); // Tratamento de erros
}
 */