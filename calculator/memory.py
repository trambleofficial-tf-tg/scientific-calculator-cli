"""Memory management module for calculator"""

memory_value = 0

def memory_add(value):
    """Add value to memory"""
    global memory_value
    memory_value += value
    return memory_value

def memory_subtract(value):
    """Subtract value from memory"""
    global memory_value
    memory_value -= value
    return memory_value

def memory_recall():
    """Recall memory value"""
    return memory_value

def memory_clear():
    """Clear memory"""
    global memory_value
    memory_value = 0
    return memory_value

def memory_store(value):
    """Store value in memory"""
    global memory_value
    memory_value = value
    return memory_value
