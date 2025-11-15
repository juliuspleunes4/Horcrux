# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2025-11-15

### Improved
- **Interactive CLI Input Validation**: Rock-solid error handling for all user inputs
  - All input functions now wrapped in comprehensive try-except blocks
  - Invalid inputs no longer crash the application - users are re-prompted instead
  - Added validation for output directory paths (checks parent directory exists, prevents file paths)
  - Added validation for output file paths (checks parent directory exists, prevents directory paths)
  - Empty input validation for number prompts
  - Handles EOF errors gracefully (e.g., piped input scenarios)
  - Keyboard interrupts (Ctrl+C) handled properly throughout
  - Users never lose progress from previous steps due to input errors
  - Clear, color-coded error messages guide users to correct their input
  - Improved user experience: no forced restarts, no crashes from typos or invalid paths

## [1.1.0] - 2025-11-15

### Added
- **Interactive CLI Mode**: Beautiful, user-friendly interface for non-technical users
  - `hrcx interactive` command launches a guided wizard-style interface
  - Large ocean-blue ASCII art header with version and links
  - Color-coded menus and prompts for easy navigation (green for success, red for errors, yellow for warnings, cyan for info)
  - Step-by-step workflows for both splitting and binding operations
  - Automatic file discovery and validation with helpful error messages
  - Smart defaults and confirmations to prevent mistakes
  - Windows batch file (`horcrux.bat`) for one-click launch without technical knowledge
  - Comprehensive input validation and error handling
  - Option to perform multiple operations in one session
  - Graceful handling of user cancellation (Ctrl+C)

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
