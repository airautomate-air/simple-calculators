#!/usr/bin/env python3
"""
Simple API for Simple Calculators site
Provides RESTful endpoints for all calculators
"""

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Temperature conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Length conversion functions (meters as base)
LENGTH_UNITS = {
    'nm': 1e-9,      # nanometer
    'µm': 1e-6,      # micrometer
    'mm': 0.001,     # millimeter
    'cm': 0.01,      # centimeter
    'm': 1.0,        # meter
    'km': 1000.0,    # kilometer
    'in': 0.0254,    # inch
    'ft': 0.3048,    # foot
    'yd': 0.9144,    # yard
    'mi': 1609.34    # mile
}

def convert_length(value, from_unit, to_unit):
    # Convert to meters first
    meters = value * LENGTH_UNITS[from_unit]
    # Convert from meters to target unit
    return meters / LENGTH_UNITS[to_unit]

# Weight conversion functions (kilograms as base)
WEIGHT_UNITS = {
    'mg': 1e-6,      # milligram
    'g': 0.001,      # gram
    'kg': 1.0,       # kilogram
    't': 1000.0,     # metric ton
    'oz': 0.0283495, # ounce
    'lb': 0.453592,  # pound
    'st': 6.35029    # stone
}

def convert_weight(value, from_unit, to_unit):
    # Convert to kilograms first
    kg = value * WEIGHT_UNITS[from_unit]
    # Convert from kilograms to target unit
    return kg / WEIGHT_UNITS[to_unit]

# Volume conversion functions (liters as base)
VOLUME_UNITS = {
    'ml': 0.001,     # milliliter
    'l': 1.0,        # liter
    'kl': 1000.0,    # kiloliter
    'tsp': 0.00492892, # teaspoon
    'tbsp': 0.0147868, # tablespoon
    'fl oz': 0.0295735, # fluid ounce
    'cup': 0.236588,  # cup
    'pt': 0.473176,   # pint
    'qt': 0.946353,   # quart
    'gal': 3.78541    # gallon
}

def convert_volume(value, from_unit, to_unit):
    # Convert to liters first
    liters = value * VOLUME_UNITS[from_unit]
    # Convert from liters to target unit
    return liters / VOLUME_UNITS[to_unit]

# Area conversion functions (square meters as base)
AREA_UNITS = {
    'mm²': 1e-6,     # square millimeter
    'cm²': 0.0001,   # square centimeter
    'm²': 1.0,       # square meter
    'ha': 10000.0,   # hectare
    'km²': 1e6,      # square kilometer
    'in²': 0.00064516, # square inch
    'ft²': 0.092903, # square foot
    'yd²': 0.836127, # square yard
    'ac': 4046.86,   # acre
    'mi²': 2.58999e6 # square mile
}

def convert_area(value, from_unit, to_unit):
    # Convert to square meters first
    sqm = value * AREA_UNITS[from_unit]
    # Convert from square meters to target unit
    return sqm / AREA_UNITS[to_unit]

# Volume (3D) conversion functions (cubic meters as base)
VOLUME3D_UNITS = {
    'mm³': 1e-9,     # cubic millimeter
    'cm³': 1e-6,     # cubic centimeter
    'm³': 1.0,       # cubic meter
    'km³': 1e9,      # cubic kilometer
    'in³': 1.63871e-5, # cubic inch
    'ft³': 0.0283168, # cubic foot
    'yd³': 0.764555  # cubic yard
}

def convert_volume3d(value, from_unit, to_unit):
    # Convert to cubic meters first
    m3 = value * VOLUME3D_UNITS[from_unit]
    # Convert from cubic meters to target unit
    return m3 / VOLUME3D_UNITS[to_unit]

# Time conversion functions (seconds as base)
TIME_UNITS = {
    'ns': 1e-9,      # nanosecond
    'µs': 1e-6,      # microsecond
    'ms': 0.001,     # millisecond
    's': 1.0,        # second
    'min': 60.0,     # minute
    'hr': 3600.0,    # hour
    'day': 86400.0,  # day
    'week': 604800.0, # week
    'month': 2629746, # month (average)
    'year': 31556952 # year (average)
}

def convert_time(value, from_unit, to_unit):
    # Convert to seconds first
    seconds = value * TIME_UNITS[from_unit]
    # Convert from seconds to target unit
    return seconds / TIME_UNITS[to_unit]

@app.route('/')
def api_info():
    return jsonify({
        'name': 'Simple Calculators API',
        'version': '1.0.0',
        'description': 'RESTful API for unit conversions',
        'endpoints': {
            'temperature': {
                'endpoint': '/api/temperature',
                'methods': ['GET'],
                'parameters': {
                    'value': 'float (required)',
                    'from': 'string (celsius, fahrenheit, kelvin)',
                    'to': 'string (celsius, fahrenheit, kelvin)'
                },
                'example': '/api/temperature?value=25&from=celsius&to=fahrenheit'
            },
            'length': {
                'endpoint': '/api/length',
                'methods': ['GET'],
                'parameters': {
                    'value': 'float (required)',
                    'from': 'string (nm, µm, mm, cm, m, km, in, ft, yd, mi)',
                    'to': 'string (nm, µm, mm, cm, m, km, in, ft, yd, mi)'
                },
                'example': '/api/length?value=1&from=m&to=ft'
            },
            'weight': {
                'endpoint': '/api/weight',
                'methods': ['GET'],
                'parameters': {
                    'value': 'float (required)',
                    'from': 'string (mg, g, kg, t, oz, lb, st)',
                    'to': 'string (mg, g, kg, t, oz, lb, st)'
                },
                'example': '/api/weight?value=1&from=kg&to=lb'
            },
            'volume': {
                'endpoint': '/api/volume',
                'methods': ['GET'],
                'parameters': {
                    'value': 'float (required)',
                    'from': 'string (ml, l, kl, tsp, tbsp, fl oz, cup, pt, qt, gal)',
                    'to': 'string (ml, l, kl, tsp, tbsp, fl oz, cup, pt, qt, gal)'
                },
                'example': '/api/volume?value=1&from=l&to=gal'
            },
            'area': {
                'endpoint': '/api/area',
                'methods': ['GET'],
                'parameters': {
                    'value': 'float (required)',
                    'from': 'string (mm², cm², m², ha, km², in², ft², yd², ac, mi²)',
                    'to': 'string (mm², cm², m², ha, km², in², ft², yd², ac, mi²)'
                },
                'example': '/api/area?value=1&from=m²&to=ft²'
            },
            'volume3d': {
                'endpoint': '/api/volume3d',
                'methods': ['GET'],
                'parameters': {
                    'value': 'float (required)',
                    'from': 'string (mm³, cm³, m³, km³, in³, ft³, yd³)',
                    'to': 'string (mm³, cm³, m³, km³, in³, ft³, yd³)'
                },
                'example': '/api/volume3d?value=1&from=m³&to=ft³'
            },
            'time': {
                'endpoint': '/api/time',
                'methods': ['GET'],
                'parameters': {
                    'value': 'float (required)',
                    'from': 'string (ns, µs, ms, s, min, hr, day, week, month, year)',
                    'to': 'string (ns, µs, ms, s, min, hr, day, week, month, year)'
                },
                'example': '/api/time?value=1&from=hr&to=min'
            }
        }
    })

@app.route('/api/temperature')
def convert_temperature():
    try:
        value = float(request.args.get('value'))
        from_unit = request.args.get('from', '').lower()
        to_unit = request.args.get('to', '').lower()
        
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            result = celsius_to_fahrenheit(value)
        elif from_unit == 'celsius' and to_unit == 'kelvin':
            result = celsius_to_kelvin(value)
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            result = fahrenheit_to_celsius(value)
        elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
            result = fahrenheit_to_kelvin(value)
        elif from_unit == 'kelvin' and to_unit == 'celsius':
            result = kelvin_to_celsius(value)
        elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
            result = kelvin_to_fahrenheit(value)
        elif from_unit == to_unit:
            result = value
        else:
            return jsonify({'error': 'Invalid unit combination'}), 400
            
        return jsonify({
            'value': value,
            'from': from_unit,
            'to': to_unit,
            'result': round(result, 6)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/length')
def convert_length_api():
    try:
        value = float(request.args.get('value'))
        from_unit = request.args.get('from', '').lower()
        to_unit = request.args.get('to', '').lower()
        
        if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
            return jsonify({'error': 'Invalid unit'}), 400
            
        result = convert_length(value, from_unit, to_unit)
        return jsonify({
            'value': value,
            'from': from_unit,
            'to': to_unit,
            'result': round(result, 6)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/weight')
def convert_weight_api():
    try:
        value = float(request.args.get('value'))
        from_unit = request.args.get('from', '').lower()
        to_unit = request.args.get('to', '').lower()
        
        if from_unit not in WEIGHT_UNITS or to_unit not in WEIGHT_UNITS:
            return jsonify({'error': 'Invalid unit'}), 400
            
        result = convert_weight(value, from_unit, to_unit)
        return jsonify({
            'value': value,
            'from': from_unit,
            'to': to_unit,
            'result': round(result, 6)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/volume')
def convert_volume_api():
    try:
        value = float(request.args.get('value'))
        from_unit = request.args.get('from', '').lower()
        to_unit = request.args.get('to', '').lower()
        
        if from_unit not in VOLUME_UNITS or to_unit not in VOLUME_UNITS:
            return jsonify({'error': 'Invalid unit'}), 400
            
        result = convert_volume(value, from_unit, to_unit)
        return jsonify({
            'value': value,
            'from': from_unit,
            'to': to_unit,
            'result': round(result, 6)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/area')
def convert_area_api():
    try:
        value = float(request.args.get('value'))
        from_unit = request.args.get('from', '').lower()
        to_unit = request.args.get('to', '').lower()
        
        if from_unit not in AREA_UNITS or to_unit not in AREA_UNITS:
            return jsonify({'error': 'Invalid unit'}), 400
            
        result = convert_area(value, from_unit, to_unit)
        return jsonify({
            'value': value,
            'from': from_unit,
            'to': to_unit,
            'result': round(result, 6)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/volume3d')
def convert_volume3d_api():
    try:
        value = float(request.args.get('value'))
        from_unit = request.args.get('from', '').lower()
        to_unit = request.args.get('to', '').lower()
        
        if from_unit not in VOLUME3D_UNITS or to_unit not in VOLUME3D_UNITS:
            return jsonify({'error': 'Invalid unit'}), 400
            
        result = convert_volume3d(value, from_unit, to_unit)
        return jsonify({
            'value': value,
            'from': from_unit,
            'to': to_unit,
            'result': round(result, 6)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/time')
def convert_time_api():
    try:
        value = float(request.args.get('value'))
        from_unit = request.args.get('from', '').lower()
        to_unit = request.args.get('to', '').lower()
        
        if from_unit not in TIME_UNITS or to_unit not in TIME_UNITS:
            return jsonify({'error': 'Invalid unit'}), 400
            
        result = convert_time(value, from_unit, to_unit)
        return jsonify({
            'value': value,
            'from': from_unit,
            'to': to_unit,
            'result': round(result, 6)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)