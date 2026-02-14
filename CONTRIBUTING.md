# Contributing to Scientific Calculator CLI

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs
- Use GitHub Issues
- Include Python version and OS
- Provide steps to reproduce
- Include error messages

### Suggesting Features
- Open an issue with [Feature Request] tag
- Describe the feature and use case
- Explain expected behavior

### Code Contributions

1. **Fork the repository**
2. **Create a branch**: `git checkout -b feature/your-feature`
3. **Make changes**:
   - Follow existing code style
   - Add tests for new features
   - Update documentation
4. **Test**: Run `python test_calculator.py`
5. **Commit**: Use clear commit messages
6. **Push**: `git push origin feature/your-feature`
7. **Pull Request**: Submit PR with description

## Code Style

- Follow PEP 8
- Use docstrings for functions
- Keep functions focused and small
- Add error handling
- Write clear variable names

## Testing

All new features must include tests:
```python
def test_new_feature():
    result = new_function(input)
    assert result == expected
```

## Documentation

Update relevant files:
- README.md for user-facing changes
- Docstrings for code changes
- CHANGELOG.md for version updates

## Questions?

Open an issue or discussion on GitHub.

Thank you for contributing! 🚀
