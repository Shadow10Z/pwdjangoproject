const expressionInput = document.getElementById('expression');
const calculateBtn = document.getElementById('calculate-btn');
const clearBtn = document.getElementById('clear-btn');
const resultText = document.getElementById('result');

calculateBtn.addEventListener('click', () => {
  const expression = expressionInput.value;
  const result = eval(expression);
  
  resultText.textContent = result;
});

clearBtn.addEventListener('click', () => {
  resultText.textContent = '';
  expressionInput.value = '';
});