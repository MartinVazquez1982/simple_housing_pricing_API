document.getElementById('predict-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData.entries());

  // Convert numeric fields from strings to numbers
  for (let key in data) {
    data[key] = parseFloat(data[key]);
  }

  try {
    const response = await fetch('https://tu-api.com/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById('result').textContent =
      `Predicted Price: $${result.predicted_price.toLocaleString()}`;
  } catch (error) {
    console.error(error);
    document.getElementById('result').textContent =
      'Error fetching prediction. Please try again.';
  }
});
