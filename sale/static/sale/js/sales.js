function fetchProductData(productId) {
    fetch(`/sales/get_product/${productId}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                // Preenche os campos com os dados do produto
                productNameInput.value = data.name;
                unitPriceInput.value = data.price;
            }
        })
        .catch(error => console.error('Error:', error));
}