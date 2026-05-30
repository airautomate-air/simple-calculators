// Volume converter logic
const volumeValue = document.getElementById('volume-value');
const volumeUnit = document.getElementById('volume-unit');
const resultElements = {
  ml: document.getElementById('result-ml').querySelector('span'),
  l: document.getElementById('result-l').querySelector('span'),
  tsp: document.getElementById('result-tsp').querySelector('span'),
  tbsp: document.getElementById('result-tbsp').querySelector('span'),
  'fl-oz': document.getElementById('result-fl-oz').querySelector('span'),
  cup: document.getElementById('result-cup').querySelector('span'),
  pt: document.getElementById('result-pt').querySelector('span'),
  qt: document.getElementById('result-qt').querySelector('span'),
  gal: document.getElementById('result-gal').querySelector('span')
};

// Conversion factors to milliliters
const toMl = {
  ml: 1,
  l: 1000,
  tsp: 4.92892, // US teaspoon
  tbsp: 14.7868, // US tablespoon
  'fl-oz': 29.5735, // US fluid ounce
  cup: 236.588, // US cup
  pt: 473.176, // US pint
  qt: 946.353, // US quart
  gal: 3785.41 // US gallon
};

function convertVolume() {
  const value = parseFloat(volumeValue.value);
  const unit = volumeUnit.value;

  if (isNaN(value) || value === '') {
    // Clear all results
    Object.values(resultElements).forEach(el => el.textContent = '-');
    return;
  }

  // Convert input value to milliliters
  const valueInMl = value * toMl[unit];

  // Convert milliliters to each unit and display
  for (const [unitKey, factor] of Object.entries(toMl)) {
    const converted = valueInMl / factor;
    resultElements[unitKey].textContent = converted.toFixed(4).replace(/\.0+$/, '');
  }
}

// Event listeners
volumeValue.addEventListener('input', convertVolume);
volumeUnit.addEventListener('change', convertVolume);

// Also convert on Enter key
volumeValue.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    convertVolume();
  }
});