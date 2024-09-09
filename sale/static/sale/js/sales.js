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

const add_cart = () => {
    const id_cliente = document.getElementById("client_select").value;
    const id_produto = document.getElementById("product_id").value;
    const name_product = document.getElementById("product_name").value;
    const quantidade = document.getElementById("quantity").value;
    const valor_uni = document.getElementById("unit_price").value;
    const valor_total = document.getElementById("total_price").value;
    const dadosDoCarrinho = document.getElementById("dados");

    // Create a new table row element
    const newRow = document.createElement("tr");

    // Create table cells for each product attribute
    const nameCell = document.createElement("td");
    nameCell.textContent = name_product;
    const quantityCell = document.createElement("td");
    quantityCell.textContent = quantidade;
    const valorUniCell = document.createElement("td");
    valorUniCell.textContent = valor_uni;
    const valorTotalCell = document.createElement("td");
    valorTotalCell.textContent = valor_total;

    // Append cells to the row
    newRow.appendChild(nameCell);
    newRow.appendChild(quantityCell);
    newRow.appendChild(valorUniCell);
    newRow.appendChild(valorTotalCell);

    // Append the new row to the table
    dadosDoCarrinho.appendChild(newRow);
};