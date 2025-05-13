fetch('http://localhost:8000/products')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('products');
    data.forEach(product => {
      const div = document.createElement('div');
      div.innerHTML = `
        <img src="assets/sample-product.jpg" alt="${product.name}" style="width: 100%; border-radius: 8px;" />
        <h3>${product.name}</h3>
        <p>${product.description}</p>
        <strong>${product.price} ₸</strong>
      `;
      div.style.border = '1px solid #ccc';
      div.style.padding = '1rem';
      div.style.borderRadius = '8px';
      container.appendChild(div);
    });
  });
