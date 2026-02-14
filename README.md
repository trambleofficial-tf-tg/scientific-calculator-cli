# Scientific Calculator - Enhanced Edition v2.0

A production-ready, feature-rich, menu-driven command-line scientific calculator built with Python. Features an enhanced UI/UX with Unicode box-drawing characters, comprehensive error handling, calculation history, and extensive mathematical operations.

## ✨ Features

### 🔢 Basic Operations
- Addition
- Subtraction
- Multiplication
- Division (with zero-division protection)
- Modulo

### 🔬 Scientific Operations
- Power (x^y)
- Square Root (with negative number validation)
- Cube Root (supports negative numbers)
- Logarithm (customizable base with error handling)
- Natural Logarithm (ln)
- Exponential (e^x)
- Absolute Value

### 📐 Trigonometric Operations
- Sine, Cosine, Tangent (degrees)
- Arcsine, Arccosine, Arctangent (inverse functions)
- Degrees ↔ Radians conversion

### 🧮 Advanced Operations
- Factorial
- Percentage Calculator
- nth Root
- GCD (Greatest Common Divisor)
- LCM (Least Common Multiple)

### 📊 Statistics
- Mean (Average)
- Median
- Maximum
- Minimum
- Range

### 🔢 Number System Conversions
- Decimal ↔ Binary
- Decimal ↔ Octal
- Decimal ↔ Hexadecimal

### 📜 Additional Features
- **Calculation History**: Tracks last 50 calculations with timestamps
- **Enhanced UI**: Beautiful Unicode box-drawing characters and emojis
- **Error Handling**: Comprehensive validation for all operations
- **User-Friendly**: Clear prompts and formatted output

## Project Structure

```
scientific-calculator-cli/
├── main.py                 # Main controller and CLI interface
├── calculator/             # Calculator package
│   ├── __init__.py        # Package initializer
│   ├── basic.py           # Basic arithmetic operations
│   ├── scientific.py      # Scientific and trigonometric functions
│   ├── advanced.py        # Advanced math and number conversions
│   ├── history.py         # Calculation history management
│   └── utils.py           # Input validation and display utilities
└── README.md              # Project documentation
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/trambleofficial-tf-tg/scientific-calculator-cli.git
   ```

2. Navigate to the project directory:
   ```bash
   cd scientific-calculator-cli
   ```

## Usage

Run the calculator:
```bash
python main.py
```

### Navigation

1. **Main Menu**: Select from 9 different operation categories
2. **Sub-menus**: Choose specific operations within each category
3. **Input**: Enter numbers when prompted with clear validation
4. **Results**: View beautifully formatted calculation results
5. **History**: Track and review your calculation history
6. **Exit**: Return to previous menu or exit the application

### Example Session

```
════════════════════════════════════════════════════════════
  Welcome to Scientific Calculator - Enhanced Edition! 🎉
════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════╗
║               🔬 SCIENTIFIC CALCULATOR 🔬               ║
║                  Enhanced Edition v2.0                   ║
╚══════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────┐
│                    MAIN MENU                             │
├──────────────────────────────────────────────────────────┤
│  1. ➕ Basic Operations        │  5. 📊 Statistics          │
│  2. 🔬 Scientific Operations   │  6. 🔢 Number Systems      │
│  3. 📐 Trigonometric Ops       │  7. 📜 View History        │
│  4. 🧮 Advanced Operations     │  8. 🗑️  Clear History      │
│                                │  9. ❌ Exit                │
└──────────────────────────────────────────────────────────┘

👉 Select an option (1-9): 1

┌──────────────────────────────────────────────────────────┐
│                  ➕ BASIC OPERATIONS                     │
├──────────────────────────────────────────────────────────┤
│  1. ➕ Addition          │  4. ➗ Division              │
│  2. ➖ Subtraction       │  5. 📊 Modulo               │
│  3. ✖️  Multiplication   │  6. ⬅️  Back to Main Menu   │
└──────────────────────────────────────────────────────────┘

👉 Select operation (1-6): 1
✏️  Enter first number: 15
✏️  Enter second number: 25

┌──────────────────────────────────────────────────────────┐
│                        ✨ RESULT ✨                       │
├──────────────────────────────────────────────────────────┤
│  Operation: 15.0 + 25.0                                  │
│  Result: 40                                              │
└──────────────────────────────────────────────────────────┘
```

## 🛡️ Error Handling

The calculator includes robust error handling for:
- Invalid numeric input (non-numeric values)
- Division by zero and modulo by zero
- Square root of negative numbers
- Even roots of negative numbers
- Logarithm of non-positive numbers
- Invalid logarithm bases
- Factorial of negative numbers
- Inverse trig functions out of range
- Invalid menu selections
- Keyboard interrupts (Ctrl+C)
- Number system conversion errors

## 🏗️ Code Architecture

### Modular Design
- **main.py**: Central controller managing the CLI and menu system
- **basic.py**: Encapsulates basic arithmetic operations
- **scientific.py**: Contains advanced mathematical and trigonometric functions
- **advanced.py**: Factorial, statistics, and number system conversions
- **history.py**: Calculation history tracking and display
- **utils.py**: Input validation, output formatting, and UI helpers

### Key Design Principles
- Separation of concerns
- Single responsibility per module
- Comprehensive error handling
- Enhanced user interface with Unicode characters
- Clean, maintainable, well-documented code
- History tracking for user convenience

## 🚀 Development

### Adding New Operations

1. Add the function to the appropriate module (basic.py, scientific.py, or advanced.py)
2. Create or update the corresponding menu in main.py
3. Include proper error handling
4. Update the README documentation

### Testing

Test the calculator by running various operations:
- Valid inputs across all operation types
- Invalid inputs (letters, symbols, special characters)
- Edge cases (zero, negative numbers, very large numbers)
- Boundary conditions for each function
- History tracking functionality
- Number system conversions

## 🎨 UI/UX Features

- **Unicode Box Drawing**: Beautiful borders and separators
- **Emoji Icons**: Visual indicators for different operation types
- **Color-Coded Messages**: Success (✅), Error (❌), Info (ℹ️)
- **Formatted Output**: Clean, aligned results display
- **Interactive Prompts**: Clear input indicators (👉, ✏️)
- **Pause for Review**: Press Enter to continue after results
- **Calculation History**: Track and review past calculations

## 📝 License

This project is open source and available for educational and commercial use.

## 👨‍💻 Author

Created as a demonstration of clean Python architecture, enhanced CLI application design, and modern UI/UX principles.

## 🔄 Version History

### v2.0 - Enhanced Edition
- Added 40+ new mathematical operations
- Implemented calculation history tracking
- Enhanced UI with Unicode box-drawing characters
- Added emoji icons for better visual experience
- Implemented statistics module
- Added number system conversions
- Improved error handling and user feedback
- Added inverse trigonometric functions
- Implemented advanced operations (factorial, GCD, LCM)

### v1.0 - Initial Release
- Basic arithmetic operations
- Scientific functions (power, sqrt, log)
- Trigonometric functions (sin, cos, tan)
- Menu-driven interface
