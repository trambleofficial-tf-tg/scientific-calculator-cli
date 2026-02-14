"""Unit conversion module"""

# Length conversions (to meters)
LENGTH_UNITS = {
    'meter': 1, 'm': 1,
    'kilometer': 1000, 'km': 1000,
    'centimeter': 0.01, 'cm': 0.01,
    'millimeter': 0.001, 'mm': 0.001,
    'mile': 1609.34, 'mi': 1609.34,
    'yard': 0.9144, 'yd': 0.9144,
    'foot': 0.3048, 'ft': 0.3048,
    'inch': 0.0254, 'in': 0.0254
}

# Weight conversions (to kilograms)
WEIGHT_UNITS = {
    'kilogram': 1, 'kg': 1,
    'gram': 0.001, 'g': 0.001,
    'milligram': 0.000001, 'mg': 0.000001,
    'pound': 0.453592, 'lb': 0.453592,
    'ounce': 0.0283495, 'oz': 0.0283495,
    'ton': 1000, 't': 1000
}

# Temperature conversions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

# Time conversions (to seconds)
TIME_UNITS = {
    'second': 1, 's': 1, 'sec': 1,
    'minute': 60, 'min': 60,
    'hour': 3600, 'h': 3600, 'hr': 3600,
    'day': 86400, 'd': 86400,
    'week': 604800, 'wk': 604800,
    'month': 2592000, 'mo': 2592000,
    'year': 31536000, 'yr': 31536000
}

# Area conversions (to square meters)
AREA_UNITS = {
    'square_meter': 1, 'sq_m': 1, 'm2': 1,
    'square_kilometer': 1000000, 'sq_km': 1000000, 'km2': 1000000,
    'square_centimeter': 0.0001, 'sq_cm': 0.0001, 'cm2': 0.0001,
    'square_mile': 2589988.11, 'sq_mi': 2589988.11,
    'square_foot': 0.092903, 'sq_ft': 0.092903, 'ft2': 0.092903,
    'acre': 4046.86, 'ac': 4046.86,
    'hectare': 10000, 'ha': 10000
}

# Volume conversions (to liters)
VOLUME_UNITS = {
    'liter': 1, 'l': 1,
    'milliliter': 0.001, 'ml': 0.001,
    'cubic_meter': 1000, 'm3': 1000,
    'gallon': 3.78541, 'gal': 3.78541,
    'quart': 0.946353, 'qt': 0.946353,
    'pint': 0.473176, 'pt': 0.473176,
    'cup': 0.236588, 'c': 0.236588,
    'fluid_ounce': 0.0295735, 'fl_oz': 0.0295735
}

# Speed conversions (to m/s)
SPEED_UNITS = {
    'meter_per_second': 1, 'm/s': 1, 'mps': 1,
    'kilometer_per_hour': 0.277778, 'km/h': 0.277778, 'kph': 0.277778,
    'mile_per_hour': 0.44704, 'mph': 0.44704,
    'foot_per_second': 0.3048, 'ft/s': 0.3048, 'fps': 0.3048,
    'knot': 0.514444, 'kn': 0.514444
}

def convert_length(value, from_unit, to_unit):
    """Convert length units"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
        raise ValueError("Invalid length unit")
    meters = value * LENGTH_UNITS[from_unit]
    return meters / LENGTH_UNITS[to_unit]

def convert_weight(value, from_unit, to_unit):
    """Convert weight units"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in WEIGHT_UNITS or to_unit not in WEIGHT_UNITS:
        raise ValueError("Invalid weight unit")
    kg = value * WEIGHT_UNITS[from_unit]
    return kg / WEIGHT_UNITS[to_unit]

def convert_time(value, from_unit, to_unit):
    """Convert time units"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in TIME_UNITS or to_unit not in TIME_UNITS:
        raise ValueError("Invalid time unit")
    seconds = value * TIME_UNITS[from_unit]
    return seconds / TIME_UNITS[to_unit]

def convert_area(value, from_unit, to_unit):
    """Convert area units"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in AREA_UNITS or to_unit not in AREA_UNITS:
        raise ValueError("Invalid area unit")
    sq_m = value * AREA_UNITS[from_unit]
    return sq_m / AREA_UNITS[to_unit]

def convert_volume(value, from_unit, to_unit):
    """Convert volume units"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in VOLUME_UNITS or to_unit not in VOLUME_UNITS:
        raise ValueError("Invalid volume unit")
    liters = value * VOLUME_UNITS[from_unit]
    return liters / VOLUME_UNITS[to_unit]

def convert_speed(value, from_unit, to_unit):
    """Convert speed units"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in SPEED_UNITS or to_unit not in SPEED_UNITS:
        raise ValueError("Invalid speed unit")
    mps = value * SPEED_UNITS[from_unit]
    return mps / SPEED_UNITS[to_unit]
