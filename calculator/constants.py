"""Mathematical and physical constants module"""
import math

# Mathematical constants
PI = math.pi
E = math.e
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
TAU = 2 * math.pi

# Physical constants
SPEED_OF_LIGHT = 299792458  # m/s
GRAVITATIONAL_CONSTANT = 6.67430e-11  # m³/kg/s²
PLANCK_CONSTANT = 6.62607015e-34  # J⋅s
AVOGADRO_NUMBER = 6.02214076e23  # mol⁻¹

CONSTANTS = {
    'π': PI,
    'pi': PI,
    'e': E,
    'φ': PHI,
    'phi': PHI,
    'τ': TAU,
    'tau': TAU,
    'c': SPEED_OF_LIGHT,
    'G': GRAVITATIONAL_CONSTANT,
    'h': PLANCK_CONSTANT,
    'Na': AVOGADRO_NUMBER
}

def get_constant(name):
    """Get constant value by name"""
    return CONSTANTS.get(name.lower())

def list_constants():
    """Return list of available constants"""
    return {
        'Mathematical': {
            'π (pi)': PI,
            'e': E,
            'φ (phi) - Golden Ratio': PHI,
            'τ (tau)': TAU
        },
        'Physical': {
            'c - Speed of Light': SPEED_OF_LIGHT,
            'G - Gravitational Constant': GRAVITATIONAL_CONSTANT,
            'h - Planck Constant': PLANCK_CONSTANT,
            'Na - Avogadro Number': AVOGADRO_NUMBER
        }
    }
