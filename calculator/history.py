"""Calculation history management module"""
from datetime import datetime
import os

calculation_history = []

def add_entry(operation, result):
    """Add a calculation to history"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    calculation_history.append({
        'timestamp': timestamp,
        'operation': operation,
        'result': result
    })
    # Keep only last 50 entries
    if len(calculation_history) > 50:
        calculation_history.pop(0)

def display_history():
    """Display calculation history"""
    if not calculation_history:
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*18 + "📜 HISTORY" + " "*27 + "│")
        print("├" + "─"*58 + "┤")
        print("│" + " "*15 + "No calculations yet!" + " "*20 + "│")
        print("└" + "─"*58 + "┘")
        input("\n⏎ Press Enter to continue...")
        return
    
    print("\n┌" + "─"*78 + "┐")
    print("│" + " "*30 + "📜 CALCULATION HISTORY" + " "*25 + "│")
    print("├" + "─"*78 + "┤")
    print("│ #  │ Timestamp           │ Operation              │ Result           │")
    print("├" + "─"*78 + "┤")
    
    # Display last 20 entries
    display_count = min(20, len(calculation_history))
    start_index = len(calculation_history) - display_count
    
    for i, entry in enumerate(calculation_history[start_index:], 1):
        timestamp = entry['timestamp']
        operation = entry['operation'][:22]
        result = str(entry['result'])[:16]
        
        print(f"│ {i:<2} │ {timestamp} │ {operation:<22} │ {result:<16} │")
    
    print("└" + "─"*78 + "┘")
    print(f"\nShowing last {display_count} of {len(calculation_history)} calculations")
    input("\n⏎ Press Enter to continue...")

def clear_history():
    """Clear all calculation history"""
    global calculation_history
    calculation_history = []

def get_history():
    """Return the calculation history"""
    return calculation_history

def export_history(filename="calculator_history.txt"):
    """Export history to a text file"""
    if not calculation_history:
        raise ValueError("No history to export")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("Scientific Calculator - Calculation History\n")
            f.write(f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            for i, entry in enumerate(calculation_history, 1):
                f.write(f"{i}. [{entry['timestamp']}]\n")
                f.write(f"   Operation: {entry['operation']}\n")
                f.write(f"   Result: {entry['result']}\n\n")
        
        return filename
    except Exception as e:
        raise ValueError(f"Failed to export history: {str(e)}")
