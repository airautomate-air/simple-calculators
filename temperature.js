// Temperature converter logic
const celsiusInput = document.getElementById('celsius');
const fahrenheitInput = document.getElementById('fahrenheit');
const kelvinInput = document.getElementById('kelvin');

let isUpdating = false;

function updateFromCelsius() {
  if (isUpdating) return;
  isUpdating = true;
  const c = parseFloat(celsiusInput.value);
  if (!isNaN(c)) {
    fahrenheitInput.value = (c * 9/5 + 32).toFixed(2);
    kelvinInput.value = (c + 273.15).toFixed(2);
  } else {
    fahrenheitInput.value = '';
    kelvinInput.value = '';
  }
  isUpdating = false;
}

function updateFromFahrenheit() {
  if (isUpdating) return;
  isUpdating = true;
  const f = parseFloat(fahrenheitInput.value);
  if (!isNaN(f)) {
    celsiusInput.value = ((f - 32) * 5/9).toFixed(2);
    kelvinInput.value = ((f - 32) * 5/9 + 273.15).toFixed(2);
  } else {
    celsiusInput.value = '';
    kelvinInput.value = '';
  }
  isUpdating = false;
}

function updateFromKelvin() {
  if (isUpdating) return;
  isUpdating = true;
  const k = parseFloat(kelvinInput.value);
  if (!isNaN(k)) {
    celsiusInput.value = (k - 273.15).toFixed(2);
    fahrenheitInput.value = ((k - 273.15) * 9/5 + 32).toFixed(2);
  } else {
    celsiusInput.value = '';
    fahrenheitInput.value = '';
  }
  isUpdating = false;
}

celsiusInput.addEventListener('input', updateFromCelsius);
fahrenheitInput.addEventListener('input', updateFromFahrenheit);
kelvinInput.addEventListener('input', updateFromKelvin);