// Length converter logic
const lengthValue = document.getElementById('length-value');
const lengthUnit = document.getElementById('length-unit');
const resultElements = {
  mm: document.getElementById('result-mm').querySelector('span'),
  cm: document.getElementById('result-cm').querySelector('span'),
  m: document.getElementById('result-m').querySelector('span'),
  km: document.getElementById('result-km').querySelector('span'),
  in: document.getElementById('result-in').querySelector('span'),
  ft: document.getElementById('result-ft').querySelector('span'),
  yd: document.getElementById('result-yd').querySelector('span'),
  mi: document.getElementById('result-mi').querySelector('span'),
  nmi: document.getElementById('result-nmi').querySelector('span')
};

// Conversion factors to meters
const toMeter = {
  mm: 0.001,
  cm: 0.01,
  m: 1,
  km: 1000,
  in: 0.0254,
  ft: 0.3048,
  yd: 0.9144,
  mi: 1609.344,
  nmi: 1852
};

function convertLength() {
  const value = parseFloat(lengthValue.value);
  const unit = lengthUnit.value;

  if (isNaN(value) || value === '') {
    // Clear all results
    Object.values(resultElements).forEach(el => el.textContent = '-');
    return;
  }

  // Convert input value to meters
  const valueInMeters = value * toMeter[unit];

  // Convert meters to each unit and display
  for (const [unitKey, factor] of Object.entries(toMeter)) {
    const converted = valueInMeters / factor;
    resultElements[unitKey].textContent = converted.toFixed(4).replace(/\.0+$/, '');
  }
}

// Event listeners
lengthValue.addEventListener('input', convertLength);
lengthUnit.addEventListener('change', convertLength);

// Also convert on Enter key
lengthValue.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    convertLength();
  }
});