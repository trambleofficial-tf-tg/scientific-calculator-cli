"""Terminal-based function graphing module"""
import math

def plot_function(func_str, x_min=-10, x_max=10, width=60, height=20):
    """Plot function in terminal"""
    from calculator.expression import evaluate_expression
    
    points = []
    x_step = (x_max - x_min) / width
    
    # Calculate y values
    for i in range(width + 1):
        x = x_min + i * x_step
        try:
            func_at_x = func_str.replace('x', f'({x})')
            y = evaluate_expression(func_at_x)
            if not math.isnan(y) and not math.isinf(y):
                points.append((x, y))
            else:
                points.append((x, None))
        except:
            points.append((x, None))
    
    # Find y range
    valid_y = [p[1] for p in points if p[1] is not None]
    if not valid_y:
        return "Cannot plot function - no valid points"
    
    y_min = min(valid_y)
    y_max = max(valid_y)
    
    # Add padding
    y_range = y_max - y_min
    if y_range == 0:
        y_range = 1
    y_min -= y_range * 0.1
    y_max += y_range * 0.1
    
    # Create grid
    grid = [[' ' for _ in range(width + 1)] for _ in range(height)]
    
    # Plot points
    for x, y in points:
        if y is not None:
            col = int((x - x_min) / (x_max - x_min) * width)
            row = height - 1 - int((y - y_min) / (y_max - y_min) * (height - 1))
            if 0 <= row < height and 0 <= col <= width:
                grid[row][col] = '*'
    
    # Add axes
    zero_row = height - 1 - int((0 - y_min) / (y_max - y_min) * (height - 1))
    zero_col = int((0 - x_min) / (x_max - x_min) * width)
    
    if 0 <= zero_row < height:
        for col in range(width + 1):
            if grid[zero_row][col] == ' ':
                grid[zero_row][col] = '-'
    
    if 0 <= zero_col <= width:
        for row in range(height):
            if grid[row][zero_col] == ' ':
                grid[row][zero_col] = '|'
    
    # Build output
    result = []
    result.append(f"\nFunction: {func_str}")
    result.append(f"Range: x=[{x_min:.2f}, {x_max:.2f}], y=[{y_min:.2f}, {y_max:.2f}]")
    result.append("")
    result.append(f"  {y_max:8.2f} +")
    
    for i, row in enumerate(grid):
        if i == height // 2:
            result.append(f"           |{''.join(row)}|")
        else:
            result.append(f"           |{''.join(row)}|")
    
    result.append(f"  {y_min:8.2f} +")
    result.append(f"           {x_min:8.2f}{' '*(width-16)}{x_max:8.2f}")
    
    return '\n'.join(result)

def plot_data(x_data, y_data, title="Data Plot", width=60, height=20):
    """Plot data points in terminal"""
    if len(x_data) != len(y_data) or len(x_data) == 0:
        return "Invalid data"
    
    x_min, x_max = min(x_data), max(x_data)
    y_min, y_max = min(y_data), max(y_data)
    
    # Add padding
    x_range = x_max - x_min if x_max != x_min else 1
    y_range = y_max - y_min if y_max != y_min else 1
    x_min -= x_range * 0.1
    x_max += x_range * 0.1
    y_min -= y_range * 0.1
    y_max += y_range * 0.1
    
    # Create grid
    grid = [[' ' for _ in range(width + 1)] for _ in range(height)]
    
    # Plot points
    for x, y in zip(x_data, y_data):
        col = int((x - x_min) / (x_max - x_min) * width)
        row = height - 1 - int((y - y_min) / (y_max - y_min) * (height - 1))
        if 0 <= row < height and 0 <= col <= width:
            grid[row][col] = 'o'
    
    # Build output
    result = []
    result.append(f"\n{title}")
    result.append(f"Points: {len(x_data)}")
    result.append("")
    result.append(f"  {y_max:8.2f} +")
    
    for row in grid:
        result.append(f"           |{''.join(row)}|")
    
    result.append(f"  {y_min:8.2f} +")
    result.append(f"           {x_min:8.2f}{' '*(width-16)}{x_max:8.2f}")
    
    return '\n'.join(result)
