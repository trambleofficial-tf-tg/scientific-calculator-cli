# 🔬 Scientific Calculator CLI - Enhanced Edition

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](test_calculator.py)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

A production-ready, feature-rich, menu-driven command-line scientific calculator built with Python. Features an enhanced UI/UX with Unicode box-drawing characters, comprehensive error handling, calculation history, and 40+ mathematical operations.

![Calculator Demo](https://via.placeholder.com/800x400/1a1a1a/00ff00?text=Scientific+Calculator+CLI)

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔢 Basic Operations
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 📊 Modulo

### 🔬 Scientific Operations
- 🔺 Power (x^y)
- √ Square Root
- ∛ Cube Root
- 📊 Logarithm (any base)
- 📈 Natural Log (ln)
- ⚡ Exponential (e^x)
- 🔢 Absolute Value

</td>
<td width="50%">

### 📐 Trigonometric Operations
- 📊 Sin, Cos, Tan
- 🔄 Arcsin, Arccos, Arctan
- 🔄 Degrees ↔ Radians

### 🧮 Advanced Operations
- 🔢 Factorial
- 📊 Percentage
- 🔺 nth Root
- 🎲 GCD & LCM

### 📊 Statistics
- 📈 Mean, Median
- 📊 Max, Min, Range

### 🔢 Number Systems
- Binary, Octal, Hexadecimal

</td>
</tr>
</table>

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/trambleofficial-tf-tg/scientific-calculator-cli.git

# Navigate to directory
cd scientific-calculator-cli

# Run the calculator
python main.py
```

### Usage

```bash
# Interactive mode
python main.py

# Run demo
python demo.py

# Run tests
python test_calculator.py
```

## 📸 Screenshots

### Main Menu
```
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
```

## 📚 Documentation

- [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- [Complete Guide](GUIDE.md) - Comprehensive usage guide
- [API Documentation](calculator/) - Module documentation
- [Contributing](CONTRIBUTING.md) - How to contribute
- [Changelog](CHANGELOG.md) - Version history

## 🏗️ Project Structure

```
scientific-calculator-cli/
├── main.py                    # Main application
├── demo.py                    # Feature demonstration
├── test_calculator.py         # Test suite
├── setup.py                   # Package setup
├── calculator/                # Core modules
│   ├── __init__.py
│   ├── basic.py              # Basic operations
│   ├── scientific.py         # Scientific functions
│   ├── advanced.py           # Advanced operations
│   ├── history.py            # History tracking
│   └── utils.py              # Utilities
├── docs/                      # Documentation
│   ├── README.md
│   ├── QUICKSTART.md
│   ├── GUIDE.md
│   └── PROJECT_SUMMARY.md
└── .github/
    └── workflows/
        └── tests.yml          # CI/CD pipeline
```

## 🧪 Testing

All modules are fully tested:

```bash
python test_calculator.py
```

```
[PASS] Basic operations
[PASS] Scientific operations
[PASS] Trigonometric operations
[PASS] Advanced operations
[PASS] Statistics
[PASS] Number system conversions
[PASS] History tracking
[PASS] Error handling

✅ ALL TESTS PASSED
```

## 🎨 UI/UX Features

- 🎨 Unicode box-drawing characters
- 😊 Emoji icons for visual appeal
- ✅ Color-coded messages
- 📊 Formatted output
- 🎯 Clear input prompts
- 📜 Calculation history
- ⚡ Fast and responsive

## 🛡️ Error Handling

Comprehensive validation for:
- Invalid inputs
- Division by zero
- Domain errors (sqrt, log)
- Range errors (inverse trig)
- Type errors
- Keyboard interrupts

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (stdlib only)

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## 👨‍💻 Authors

- **Scientific Calculator Team** - [GitHub](https://github.com/trambleofficial-tf-tg)

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐!

## 📞 Support

- 📧 Issues: [GitHub Issues](https://github.com/trambleofficial-tf-tg/scientific-calculator-cli/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/trambleofficial-tf-tg/scientific-calculator-cli/discussions)

## 🔗 Links

- [Repository](https://github.com/trambleofficial-tf-tg/scientific-calculator-cli)
- [Documentation](docs/)
- [Releases](https://github.com/trambleofficial-tf-tg/scientific-calculator-cli/releases)

---

<p align="center">Made with ❤️ and Python</p>
<p align="center">⭐ Star this repository if you find it helpful!</p>
