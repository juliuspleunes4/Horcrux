# Contributing to Horcrux

Thank you for your interest in contributing to Horcrux! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow:

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Respect differing viewpoints and experiences
- Accept responsibility and apologize for mistakes

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Horcrux.git
   cd Horcrux
   ```
3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/juliuspleunes4/Horcrux.git
   ```

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Setting Up Your Environment

1. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:
   - Windows: `.venv\Scripts\Activate.ps1`
   - macOS/Linux: `source .venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks** (optional but recommended):
   ```bash
   pip install pre-commit
   pre-commit install
   ```

5. **Verify the setup**:
   ```bash
   pytest
   hrcx --version
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix issues reported in the issue tracker
- **Features**: Implement new functionality
- **Documentation**: Improve or add documentation
- **Tests**: Add or improve test coverage
- **Code quality**: Refactor code, improve performance
- **Examples**: Add usage examples or tutorials

### Before You Start

1. **Check existing issues** to see if someone is already working on it
2. **Create an issue** if one doesn't exist for your proposed change
3. **Discuss your approach** in the issue before starting major work
4. **Keep changes focused** - one pull request per feature/bug fix

## Coding Standards

### Python Style Guide

This project follows strict coding standards:

- **PEP 8**: Python style guide (enforced by `black` and `ruff`)
- **PEP 257**: Docstring conventions (Google-style docstrings)
- **PEP 484**: Type hints for all function signatures
- **Maximum line length**: 100 characters

### Code Formatting

Before committing, format your code:

```bash
# Format with black
black src/ tests/

# Lint with ruff
ruff check src/ tests/

# Type check with mypy
mypy src/
```

### Docstring Requirements

All functions, classes, and methods **must** have Google-style docstrings:

```python
def split_file(file_path: str, total: int, threshold: int) -> None:
    """
    Split a file into encrypted horcruxes.
    
    This function encrypts the input file and splits the encryption key
    using Shamir's Secret Sharing Scheme.
    
    Args:
        file_path: Path to the file to split
        total: Total number of horcruxes to create (2-255)
        threshold: Minimum number needed to reconstruct (2-total)
    
    Raises:
        FileNotFoundError: If the input file doesn't exist
        ValueError: If total < threshold or values out of range
        
    Example:
        >>> split_file("secret.txt", total=5, threshold=3)
    """
    # Implementation
```

### Type Hints

All function signatures must include type hints:

```python
from typing import Optional, List, Tuple

def example(name: str, count: int, tags: Optional[List[str]] = None) -> Tuple[bool, str]:
    """Example function with proper type hints."""
    pass
```

### Naming Conventions

- **Functions/variables**: `snake_case` (e.g., `split_file`, `key_fragment`)
- **Classes**: `PascalCase` (e.g., `HorcruxHeader`, `ShamirSplitter`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `AES_KEY_SIZE`, `MAX_THRESHOLD`)
- **Private methods**: `_leading_underscore` (e.g., `_internal_helper`)

### Security Guidelines

- **Never** use mock data or placeholders for cryptographic operations
- Use only well-established libraries (`cryptography` package)
- Use `secrets` module or `os.urandom` for random number generation
- Never implement custom cryptographic algorithms
- Handle sensitive data securely (clear from memory when done)

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=hrcx --cov-report=html

# Run specific test file
pytest tests/test_shamir.py

# Run specific test
pytest tests/test_shamir.py::test_split_and_combine
```

### Writing Tests

- Write tests for all new functionality
- Aim for >80% code coverage
- Use descriptive test names that read like sentences
- Test edge cases, error conditions, and happy paths
- Use proper fixtures for file operations

Example test structure:

```python
def test_split_creates_correct_number_of_horcruxes(tmp_path):
    """Test that split creates the expected number of horcrux files."""
    # Setup
    test_file = tmp_path / "test.txt"
    test_file.write_text("secret content")
    
    # Execute
    split(str(test_file), total=5, threshold=3)
    
    # Assert
    horcruxes = list(tmp_path.glob("*.horcrux"))
    assert len(horcruxes) == 5
```

### Test Coverage

Current coverage: 78% overall, 88% on core modules (crypto, shamir, horcrux).

We aim to maintain or improve coverage with each contribution.

## Submitting Changes

### Commit Message Format

Follow conventional commits:

```
type: brief description

Longer explanation if needed.

Fixes #123
```

Types:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `test:` - Test additions/changes
- `refactor:` - Code refactoring
- `chore:` - Build/tooling changes
- `security:` - Security fixes

Examples:
```
feat: add support for compression before encryption

fix: correct threshold calculation in horcrux header

docs: update installation instructions for Windows
```

### Pull Request Process

1. **Update your fork**:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch**:
   ```bash
   git checkout -b feat/my-new-feature
   ```

3. **Make your changes**:
   - Write code following the coding standards
   - Add tests for new functionality
   - Update documentation if needed
   - Format code with `black`
   - Run linters and type checkers

4. **Update CHANGELOG.md**:
   - Add your changes under `[Unreleased]` section
   - Follow [Keep a Changelog](https://keepachangelog.com/) format
   - Use categories: Added, Changed, Deprecated, Removed, Fixed, Security

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feat/my-new-feature
   ```

7. **Open a Pull Request**:
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template with details
   - Link related issues

### Pull Request Checklist

Before submitting, ensure:

- [ ] Code follows the project's coding standards
- [ ] All tests pass (`pytest`)
- [ ] Code is formatted (`black src/ tests/`)
- [ ] No linting errors (`ruff check src/`)
- [ ] Type checking passes (`mypy src/`)
- [ ] New tests added for new functionality
- [ ] Documentation updated (README, docstrings, CHANGELOG)
- [ ] Commit messages follow conventional commits format
- [ ] PR description clearly explains the changes

## Reporting Bugs

### Before Submitting a Bug Report

- Check the [FAQ](FAQ.md) for common issues
- Search existing issues to avoid duplicates
- Try the latest version of hrcx
- Gather relevant information about your environment

### Bug Report Template

When creating a bug report, include:

**Description**: Clear description of the bug

**Steps to Reproduce**:
1. Step one
2. Step two
3. Expected vs actual behavior

**Environment**:
- OS: [e.g., Windows 11, macOS 14, Ubuntu 22.04]
- Python version: [e.g., 3.11.9]
- hrcx version: [e.g., 1.2.2]

**Additional Context**:
- Error messages or stack traces
- Screenshots if applicable
- Sample files (if safe to share)

## Suggesting Enhancements

### Enhancement Proposal Template

**Feature Description**: What feature would you like to see?

**Use Case**: How would this feature be used?

**Proposed Implementation**: (Optional) How might this be implemented?

**Alternatives Considered**: What other approaches did you consider?

**Additional Context**: Screenshots, examples, references

## Questions?

If you have questions about contributing:

- Open a [GitHub Discussion](https://github.com/juliuspleunes4/Horcrux/discussions)
- Check the [FAQ](FAQ.md)
- Review existing [issues](https://github.com/juliuspleunes4/Horcrux/issues)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Horcrux! 🔮
