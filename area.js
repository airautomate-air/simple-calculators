// Area Converter
const areaValue = document.getElementById('area-value');
const areaUnit = document.getElementById('area-unit');
const results = {
    mm2: document.getElementById('result-mm2').querySelector('span'),
    cm2: document.getElementById('result-cm2').querySelector('span'),
    m2: document.getElementById('result-m2').querySelector('span'),
    km2: document.getElementById('result-km2').querySelector('span'),
    in2: document.getElementById('result-in2').querySelector('span'),
    ft2: document.getElementById('result-ft2').querySelector('span'),
    yd2: document.getElementById('result-yd2').querySelector('span'),
    mi2: document.getElementById('result-mi2').querySelector('span'),
    acre: document.getElementById('result-acre').querySelector('span'),
    hectare: document.getElementById('result-hectare').querySelector('span')
};

// Conversion factors to square meters
const toM2 = {
    mm2: 1e-6,
    cm2: 1e-4,
    m2: 1,
    km2: 1e6,
    in2: 0.00064516,
    ft2: 0.092903,
    yd2: 0.836127,
    mi2: 2.58999e6,
    acre: 4046.86,
    hectare: 10000
};

function convert() {
    const value = parseFloat(areaValue.value);
    if (isNaN(value)) {
        clearResults();
        return;
    }

    const valueInM2 = value * toM2[areaUnit.value];
    
    for (const [unit, span] of Object.entries(results)) {
        const converted = valueInM2 / toM2[unit];
        span.textContent = converted.toLocaleString(undefined, { maximumFractionDigits: 4, minimumFractionDigits: 0 });
    }
}

function clearResults() {
    for (const span of Object.values(results)) {
        span.textContent = '-';
    }
}

areaValue.addEventListener('input', convert);
areaUnit.addEventListener('change', convert);