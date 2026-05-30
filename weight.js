// Weight converter logic
const weightValue = document.getElementById('weight-value');
const weightUnit = document.getElementById('weight-unit');
const resultElements = {
  mg: document.getElementById('result-mg').querySelector('span'),
  g: document.getElementById('result-g').querySelector('span'),
  kg: document.getElementById('result-kg').querySelector('span'),
  oz: document.getElementById('result-oz').querySelector('span'),
  lb: document.getElementById('result-lb').querySelector('span'),
  stone: document.getElementById('result-stone').querySelector('span'),
  ton: document.getElementById('result-ton').querySelector('span'),
  'short-ton': document.getElementById('result-short-ton').querySelector('span'),
  'long-ton': document.getElementById('result-long-ton').querySelector('span')
};

// Conversion factors to grams
const toGram = {
  mg: 0.001,
  g: 1,
  kg: 1000,
  oz: 28.3495, // avoirdupois ounce
  lb: 453.592, // avoirdupois pound
  stone: 6350.29, // 1 stone = 14 lb
  ton: 1000000, // metric ton = 1000 kg
  'short-ton': 907185, // US short ton = 2000 lb
  'long-ton': 1016050 // UK long ton = 2240 lb
};

function convertWeight() {
  const value = parseFloat(weightValue.value);
  const unit = weightUnit.value;

  if (isNaN(value) || value === '') {
    // Clear all results
    Object.values(resultElements).forEach(el => el.textContent = '-');
    return;
  }

  // Convert input value to grams
  const valueInGrams = value * toGram[unit];

  // Convert grams to each unit and display
  for (const [unitKey, factor] of Object.entries(toGram)) {
    const converted = valueInGrams / factor;
    resultElements[unitKey].textContent = converted.toFixed(4).replace(/\.0+$/, '');
  }
}

// Event listeners
weightValue.addEventListener('input', convertWeight);
weightUnit.addEventListener('change', convertWeight);

// Also convert on Enter key
weightValue.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    convertWeight();
  }
});