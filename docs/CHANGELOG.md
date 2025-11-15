# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2025-11-15

**🎉 Initial Release - Published to PyPI**

### Added
- **Shamir's Secret Sharing**: Complete implementation over GF(256) with polynomial interpolation
  - `split()` function: Split secrets into N shares with K threshold
  - `combine()` function: Reconstruct secrets from K or more shares
  - Supports up to 255 shares
  - Comprehensive validation and error handling
- **AES-256-GCM Encryption**: Secure file encryption with authenticated encryption
  - `generate_key()`: Cryptographically secure key generation
  - `encrypt()`: AES-256-GCM encryption with random nonces
  - `decrypt()`: Authenticated decryption with tampering detection
- **Horcrux File Format**: Custom `.hrcx` file format with JSON headers
  - Human-readable headers with metadata (filename, timestamp, index, total, threshold)
  - Base64-encoded key fragments and nonces
  - Binary encrypted content storage
  - `write_horcrux()` and `read_horcrux()` functions
  - `find_horcrux_files()`: Auto-discovery of horcrux files in directories
- **Public API**: Complete split and bind functionality
  - `split()`: Encrypt file and create N horcruxes with K threshold
  - `bind()`: Reconstruct original file from K or more horcruxes
  - Comprehensive validation (file existence, parameter bounds, horcrux compatibility)
  - Overwrite protection with optional force flag
- **CLI Application**: Full-featured command-line interface
  - `hrcx split`: Split files with interactive prompts or command-line options
  - `hrcx bind`: Reconstruct files with auto-discovery of horcruxes
  - User-friendly output with emoji indicators (🔒, 🔓, ✅, ❌)
  - Interactive mode for total/threshold when not specified
  - Support for custom output directories and filenames
- **Testing**: Comprehensive test suite with 77 tests
  - 88% code coverage across core modules
  - Integration tests for end-to-end workflows
  - Edge case testing (empty files, binary data, large files)
  - Error condition testing (missing files, invalid parameters, corrupted data)
- **Documentation**: 
  - Professional README with installation, usage examples, and API reference
  - Google-style docstrings for all functions and classes
  - GitHub Copilot contributor guidelines
  - PyPI publishing guide
  - Type hints throughout codebase
- **Development Tools**:
  - pytest for testing with coverage reports
  - black for code formatting
  - ruff for linting
  - mypy for type checking
  - requirements.txt and requirements-dev.txt
  - Pre-configured pyproject.toml with all settings

### Security
- AES-256-GCM provides authenticated encryption (confidentiality + authenticity)
- Shamir's Secret Sharing ensures no single horcrux reveals information
- Cryptographically secure random number generation for keys and nonces
- Tampering detection through GCM authentication tags
