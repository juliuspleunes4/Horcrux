# Security Policy

## Supported Versions

We take security seriously. The following versions of Horcrux (hrcx) are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.2.x   | :white_check_mark: |
| 1.1.x   | :white_check_mark: |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Security Features

### Cryptographic Implementation

Horcrux uses industry-standard cryptographic algorithms:

- **AES-256-GCM**: Advanced Encryption Standard with 256-bit keys in Galois/Counter Mode
  - Provides authenticated encryption with associated data (AEAD)
  - Protects against tampering and forgery
  - NIST-approved and widely audited

- **Shamir's Secret Sharing Scheme**: Threshold cryptography over GF(256)
  - Mathematically proven security properties
  - Information-theoretically secure (K-1 shares reveal nothing)
  - No single point of failure

- **Random Number Generation**: Cryptographically secure sources
  - Uses `os.urandom()` on all platforms
  - Suitable for cryptographic key generation
  - Non-deterministic and unpredictable

### Implementation Security

- **Well-audited libraries**: Uses Python's `cryptography` package (maintained by PyCA)
- **No custom crypto**: All algorithms are standard implementations
- **Type safety**: Comprehensive type hints to prevent type-related bugs
- **Input validation**: All user inputs are validated and sanitized
- **Memory handling**: Sensitive data is handled in memory appropriately

## Security Considerations

### What Horcrux Protects

✅ **File content encryption**: AES-256-GCM ensures content confidentiality and integrity

✅ **Threshold security**: Less than K horcruxes reveal zero information about the original file

✅ **Tamper detection**: GCM authentication detects any modifications to ciphertext

✅ **Key distribution**: Shamir's scheme securely splits the encryption key

### What Horcrux Does NOT Protect

❌ **Metadata privacy**: Horcrux headers contain plaintext metadata (filename, timestamp, indices)

❌ **File existence**: The presence of `.horcrux` files reveals that encrypted data exists

❌ **Access control**: Anyone with K horcruxes can reconstruct the file (by design)

❌ **Original file deletion**: You must securely delete the original file yourself

❌ **Horcrux distribution**: You are responsible for distributing horcruxes securely

### Best Practices

#### For Maximum Security

1. **Secure the original file**:
   - Use secure deletion tools (Windows: `cipher /w`, Linux/macOS: `shred -uvz`)
   - Or use full-disk encryption (BitLocker, FileVault, LUKS)

2. **Distribute horcruxes safely**:
   - Never store K or more horcruxes in the same location
   - Use physical separation (different devices, locations)
   - Use different cloud providers if storing online
   - Consider geographic distribution

3. **Choose appropriate thresholds**:
   - Higher threshold (K) = more security, less redundancy
   - Lower threshold (K) = more redundancy, less security
   - Common ratios: K = ⌈N/2⌉ or K = ⌈2N/3⌉

4. **Verify reconstruction**:
   - Test horcrux reconstruction before deleting the original
   - Verify the reconstructed file matches the original (checksum)
   - Keep one set of K horcruxes offline for verification

5. **Regular integrity checks**:
   - Periodically verify horcrux files are not corrupted
   - Check backups and cloud storage integrity
   - Refresh storage media every 5-10 years

#### For Sensitive Data

- **Air-gapped encryption**: Encrypt on a machine not connected to the internet
- **Offline storage**: Store some horcruxes on offline media (USB, external HDD)
- **Trusted parties**: Distribute horcruxes to different trusted individuals
- **Document the scheme**: Keep records of how many horcruxes exist and their locations (but not where they are stored together)

## Reporting a Vulnerability

### How to Report

If you discover a security vulnerability in Horcrux, please report it responsibly:

**DO NOT** open a public GitHub issue for security vulnerabilities.

**Instead**, report privately:

1. **Email**: Send details to [jjgpleunes@gmail.com](mailto:jjgpleunes@gmail.com)
2. **Subject line**: "Horcrux Security Vulnerability"
3. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)
   - Your contact information

### What to Expect

1. **Acknowledgment**: We'll acknowledge receipt within 48 hours
2. **Assessment**: We'll assess the vulnerability and determine severity
3. **Communication**: We'll keep you informed of progress
4. **Fix**: We'll develop and test a fix
5. **Disclosure**: We'll coordinate public disclosure with you
6. **Credit**: We'll credit you in the security advisory (if desired)

### Response Timeline

- **Critical vulnerabilities**: Fix within 7 days, release immediately
- **High severity**: Fix within 14 days, coordinated disclosure
- **Medium severity**: Fix within 30 days, regular release cycle
- **Low severity**: Fix in next scheduled release

### Vulnerability Scope

#### In Scope

Security issues in:
- Core cryptographic operations (encryption, key splitting)
- Authentication and integrity verification
- Input validation and sanitization
- Dependency vulnerabilities (cryptography package)
- Command injection or code execution
- Information disclosure vulnerabilities

#### Out of Scope

Issues that are not security vulnerabilities:
- Bugs that don't affect security
- Missing features
- Performance issues
- Documentation errors
- Issues requiring physical access to an unlocked machine
- Social engineering attacks
- Issues in dependencies we don't control (report to those projects)

## Security Advisories

### Viewing Published Advisories

Security advisories are published at:
- GitHub Security Advisories: https://github.com/juliuspleunes4/Horcrux/security/advisories
- CHANGELOG: docs/CHANGELOG.md (Security section)

### Subscribing to Security Updates

To receive security notifications:
1. Watch the repository on GitHub
2. Enable "Security alerts" in your notification settings
3. Check CHANGELOG.md for security updates when upgrading

## Cryptographic Details

### Encryption Algorithm: AES-256-GCM

- **Key size**: 256 bits (32 bytes)
- **Nonce**: 96 bits (12 bytes), randomly generated per horcrux
- **Tag size**: 128 bits (16 bytes) for authentication
- **Mode**: Galois/Counter Mode (GCM) for authenticated encryption

**Security properties**:
- IND-CPA secure (indistinguishable under chosen-plaintext attack)
- INT-CTXT secure (ciphertext integrity)
- Provides both confidentiality and authenticity

### Key Derivation: Shamir's Secret Sharing

- **Field**: GF(256) (Galois Field with 256 elements)
- **Polynomial degree**: K-1 (threshold minus one)
- **Shares**: N (total number of horcruxes)
- **Secret**: 256-bit AES key

**Security properties**:
- Information-theoretically secure
- Any K shares fully reconstruct the secret
- Any K-1 or fewer shares reveal zero information
- No computational assumptions required

### Random Number Generation

- **Source**: `os.urandom()` (platform-specific secure source)
  - Windows: `CryptGenRandom()`
  - Linux: `/dev/urandom`
  - macOS: `/dev/urandom`
- **Usage**: 
  - AES-256 key generation (32 bytes)
  - GCM nonce generation (12 bytes per horcrux)
  - Polynomial coefficients in Shamir's scheme

## Dependencies

### Core Cryptographic Library

- **cryptography**: Python cryptography library by PyCA
  - Version: >= 41.0.0
  - Maintained by: Python Cryptographic Authority
  - Audit status: Regularly audited, widely used
  - GitHub: https://github.com/pyca/cryptography

### Dependency Management

We actively monitor dependencies for security vulnerabilities:
- GitHub Dependabot alerts enabled
- Regular updates to latest stable versions
- Security patches applied immediately

### Updating Dependencies

If you discover a vulnerability in a dependency:
1. Report to the dependency's maintainers first
2. Open a private security advisory on our repository
3. We'll update the dependency once a fix is available

## Audit History

### Version 1.0.0 - 1.2.2 (Current)

- **Self-review**: Complete code review by author
- **External audit**: None yet (open to volunteer auditors)
- **Penetration testing**: None formal
- **Static analysis**: Ruff, mypy, black (linting and type checking)

### Request for Audits

We welcome security audits from the community:
- Review cryptographic implementation
- Test for vulnerabilities
- Analyze code for security issues
- Report findings responsibly

Contact us at [jjgpleunes@gmail.com](mailto:jjgpleunes@gmail.com) to coordinate an audit.

## Compliance & Standards

### Followed Standards

- **NIST**: Uses NIST-approved algorithms (AES-GCM)
- **IETF**: Follows RFC 5116 (AEAD Cipher Modes)
- **PEP 8**: Python code style for readability
- **OWASP**: Secure coding practices

### Not Certified For

Horcrux is **not certified** for:
- FIPS 140-2/3 compliance (uses compliant algorithms but not certified implementation)
- Common Criteria (no formal certification)
- Government classified data (no accreditation)

If you need certified encryption, use tools specifically certified for your requirements.

## Limitations & Threats

### Known Limitations

1. **No key rotation**: Once encrypted, the key cannot be changed without re-encrypting
2. **No versioning**: Reconstructed file may differ if horcruxes from different splits are mixed
3. **Metadata leakage**: Filenames and timestamps are visible in headers
4. **Side-channel attacks**: No protection against timing attacks or power analysis (low risk for file encryption)

### Threat Model

**Protected against**:
- Attacker with K-1 horcruxes (learns nothing)
- Passive network eavesdropping (if encrypting locally)
- File modification (detected by GCM tag)
- Chosen-plaintext attacks (AES-GCM is IND-CPA secure)

**Not protected against**:
- Attacker with K or more horcruxes (can reconstruct by design)
- Compromised encryption machine (malware, keyloggers)
- Physical access to original file before deletion
- Side-channel attacks on encryption hardware
- Quantum computers (in distant future, though AES-256 has partial quantum resistance)

## Future Security Enhancements

Planned improvements:
- [ ] Optional metadata encryption
- [ ] Key stretching for password-based encryption (optional mode)
- [ ] Hardware security module (HSM) support
- [ ] Compression before encryption (to reduce metadata leakage)
- [ ] Post-quantum cryptography research (when standards mature)

---

## Questions About Security?

- Read the [FAQ](FAQ.md#security--cryptography)
- Open a [GitHub Discussion](https://github.com/juliuspleunes4/Horcrux/discussions)
- For vulnerabilities: Email [jjgpleunes@gmail.com](mailto:jjgpleunes@gmail.com)

**Remember**: Security is a process, not a product. Use Horcrux as part of a comprehensive security strategy.
