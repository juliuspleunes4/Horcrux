# GitHub Copilot Instructions for Horcrux

## Project Overview

This is **Horcrux** - a professional, open-source file encryption and splitting tool using Shamir's Secret Sharing Scheme. The PyPI package is published as `hrcx`. This project is inspired by [jesseduffield/horcrux](https://github.com/jesseduffield/horcrux) but implemented in Python.

## Core Principles

### 1. Professional Open Source Standards
- Treat this as a production-grade, enterprise-quality project
- All code must be maintainable, readable, and well-documented
- Follow established Python best practices (PEP 8, PEP 257, type hints)
- Maintain high code quality standards at all times

### 2. No Mock Data or Placeholders
- **NEVER** use mock data, placeholder values, or dummy implementations
- All implementations must be complete and functional
- Use real cryptographic libraries and proper security practices
- If you need test data, use proper test fixtures in the test directory

### 3. Documentation Requirements
- **All functions, classes, and methods MUST have Google-style docstrings**
- Include parameter descriptions, return types, exceptions raised, and usage examples
- Document complex algorithms and cryptographic operations thoroughly
- Use type hints for all function signatures
- Keep inline comments clear and purposeful

### 4. Change Logging (CRITICAL)
- **NEVER create separate documentation files for changes, installation guides, or summaries**
- **ALL changes MUST be logged in `docs/CHANGELOG.md`** following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format
- Use semantic versioning categories: Added, Changed, Deprecated, Removed, Fixed, Security
- Update the CHANGELOG immediately after making significant changes
- Do NOT create files like: CHANGES.md, UPDATES.md, MIGRATION.md, INSTALL.md, etc.

## Code Style & Standards

### Python
- Follow PEP 8 style guide (enforced by `black` and `ruff`)
- Use type hints for all function signatures (PEP 484)
- Maximum line length: 100 characters (configured in `pyproject.toml`)
- Use `black` for code formatting, `ruff` for linting, `mypy` for type checking
- Never use `Any` type without strong justification - prefer specific types

### Documentation Format (Google-style Docstrings)
```python
def split(
    file_path: str,
    total: int,
    threshold: int,
    output_dir: Optional[str] = None
) -> None:
    """
    Split a file into encrypted horcruxes using Shamir's Secret Sharing.
    
    This function encrypts the input file with AES-256-GCM and splits the encryption
    key into N fragments using Shamir's Secret Sharing, where any K fragments can
    reconstruct the original key and decrypt the file.
    
    Args:
        file_path: Path to the file to split
        total: Total number of horcruxes to create (must be >= threshold)
        threshold: Minimum number of horcruxes needed to reconstruct (must be >= 2)
        output_dir: Optional output directory for horcruxes (default: same as input file)
    
    Raises:
        FileNotFoundError: If the input file doesn't exist
        ValueError: If total < threshold or threshold < 2
        PermissionError: If unable to write to output directory
        
    Example:
        >>> split("secret.txt", total=5, threshold=3, output_dir="./vault")
        # Creates: secret_1_of_5.horcrux, secret_2_of_5.horcrux, ...
    """
    # Implementation
```

### Naming Conventions
- Use snake_case for variables and functions: `split_file`, `key_fragment`
- Use PascalCase for classes: `HorcruxHeader`, `ShamirSplitter`
- Use UPPER_SNAKE_CASE for constants: `AES_KEY_SIZE`, `MAX_THRESHOLD`
- Use descriptive names - avoid abbreviations unless widely understood
- Private methods/attributes use leading underscore: `_internal_method`

### Error Handling
- Use custom error classes for specific error types
- Always include helpful error messages
- Handle edge cases explicitly
- Never swallow errors silently

### Security & Cryptography
- Use only well-established cryptographic libraries (`cryptography` package)
- Never implement custom cryptographic algorithms
- Use secure random number generation (`secrets` module or `os.urandom`)
- Properly handle sensitive data (keys, plaintext)
- Clear sensitive data from memory when no longer needed

## Project Structure

```
horcrux/
├── src/hrcx/
│   ├── cli.py            # Command-line interface
│   ├── api.py            # Public API (split, bind functions)
│   ├── crypto/           # Encryption and key management
│   ├── shamir/           # Shamir's Secret Sharing implementation
│   ├── horcrux/          # Horcrux file format and handling
│   └── utils/            # Utility functions
├── tests/                # Test files (mirror src/ structure)
├── docs/
│   └── CHANGELOG.md      # ALL changes logged here
└── pyproject.toml        # Package configuration
```

## Testing Requirements

- Write tests for all new functionality
- Aim for >80% code coverage (configured in `pyproject.toml`)
- Use descriptive test names that read like sentences
- Test edge cases, error conditions, and happy paths
- Use proper test fixtures for files and data

## Git Commit Messages

Follow conventional commits:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `test:` - Test additions/changes
- `refactor:` - Code refactoring
- `chore:` - Build/tooling changes
- `security:` - Security fixes

## Workflow

1. **Before coding**: Understand the requirements fully
2. **While coding**: 
   - Write docstrings as you write functions
   - Consider edge cases and error handling
   - Write tests alongside implementation
3. **After coding**:
   - Update `docs/CHANGELOG.md` with changes
   - Run `ruff check src/` and fix any issues
   - Run `black src/ tests/` to format code
   - Run `pytest` and ensure all tests pass
   - Update README.md if adding new features

## What NOT to Do

❌ Create files like: CHANGES.md, UPDATES.md, INSTALLATION.md, MIGRATION_GUIDE.md  
❌ Use mock data or placeholder implementations  
❌ Leave functions undocumented  
❌ Use `Any` type without strong justification  
❌ Implement custom cryptography  
❌ Use `# type: ignore` without explanation  
❌ Skip tests for new functionality  
❌ Forget to update CHANGELOG.md  

## External References

- **Original Inspiration**: [jesseduffield/horcrux](https://github.com/jesseduffield/horcrux) (Go implementation)
- **Shamir's Secret Sharing**: [Wikipedia](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing)
- **AES-GCM**: Use `cryptography` package with `AESGCM` class

## Questions or Clarifications

If requirements are unclear:
1. Check the original Go implementation in `example/horcrux/` for reference
2. Review the README.md for intended behavior
3. Ask the user for clarification rather than making assumptions

---

Remember: This is a professional open-source project. Quality, security, and maintainability are paramount. Every contribution should meet these high standards.
