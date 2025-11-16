# Frequently Asked Questions (FAQ)

## Table of Contents

- [General Questions](#general-questions)
- [Installation & Setup](#installation--setup)
- [Usage & Features](#usage--features)
- [Security & Cryptography](#security--cryptography)
- [Troubleshooting](#troubleshooting)
- [Advanced Topics](#advanced-topics)

## General Questions

### What is Horcrux?

Horcrux is a file encryption and splitting tool that uses Shamir's Secret Sharing Scheme to divide files into multiple encrypted fragments. It allows you to split a file into N pieces where only K pieces are needed to reconstruct the original file.

### How does Horcrux differ from regular encryption?

Regular encryption requires you to remember a password. With Horcrux:
- No passwords to remember
- Split into multiple fragments for distributed storage
- Threshold scheme provides redundancy (lose some pieces, still recover the file)
- Ideal for long-term storage where passwords might be forgotten

### Is Horcrux a Harry Potter reference?

Yes! In Harry Potter, a Horcrux is an object containing a fragment of someone's soul. Similarly, this tool creates fragments of your file that must be combined to restore the whole.

### Is Horcrux secure?

Yes. Horcrux uses industry-standard encryption:
- **AES-256-GCM**: Military-grade authenticated encryption
- **Shamir's Secret Sharing**: Mathematically proven threshold scheme
- **Well-audited libraries**: Uses Python's `cryptography` package
- **No custom crypto**: All algorithms are established standards

### What's the difference between hrcx and horcrux?

- **hrcx**: The Python package name and CLI command (`pip install hrcx`)
- **Horcrux**: The project name and concept
- **.horcrux**: The file extension for encrypted fragments

## Installation & Setup

### How do I install Horcrux?

```bash
pip install hrcx
```

For detailed installation instructions, see the [README](../README.md#-installation).

### What are the system requirements?

- Python 3.8 or higher
- Windows, macOS, or Linux
- ~10 MB disk space for the package
- No other dependencies (installed automatically)

### Can I install Horcrux without pip?

Yes, you can install from source:

```bash
git clone https://github.com/juliuspleunes4/Horcrux.git
cd Horcrux
pip install -e .
```

### How do I update Horcrux?

```bash
pip install --upgrade hrcx
```

### How do I uninstall Horcrux?

```bash
pip uninstall hrcx
```

## Usage & Features

### How do I split a file?

**Interactive mode** (easiest for beginners):
```bash
hrcx interactive
```

**Command-line mode**:
```bash
hrcx split secret.txt -t 5 -k 3
```

This creates 5 horcruxes where any 3 can reconstruct the file.

### How do I reconstruct a file?

**Interactive mode**:
```bash
hrcx interactive
# Choose "Bind (reconstruct)"
```

**Command-line mode**:
```bash
hrcx bind secret_1_of_5.horcrux secret_2_of_5.horcrux secret_3_of_5.horcrux
```

### What's the difference between total and threshold?

- **Total (-t)**: How many horcrux fragments to create (2-255)
- **Threshold (-k)**: How many fragments needed to reconstruct (2-total)

Example: `-t 5 -k 3` means:
- Creates 5 fragments total
- Need any 3 fragments to reconstruct
- Can lose up to 2 fragments and still recover the file

### Can I use special folder names like "Desktop"?

Yes! In interactive mode, you can type shortcuts:
- `Desktop` → Your Desktop folder
- `Downloads` → Your Downloads folder
- `Documents` → Your Documents folder
- `Pictures`, `Videos`, `Music` → Respective folders

### What file types are supported?

All file types! Horcrux treats files as binary data, so it works with:
- Documents (PDF, DOCX, TXT)
- Images (JPG, PNG, GIF)
- Videos (MP4, AVI, MOV)
- Archives (ZIP, RAR, TAR)
- Databases, executables, anything

### What's the maximum file size?

There's no hard limit, but practical considerations:
- Limited by available RAM (file is loaded into memory)
- For files >1 GB, ensure you have sufficient RAM
- Large files take longer to encrypt/decrypt

### Where are the horcrux files created?

By default, in the same directory as the original file. You can specify a different output directory with `-o`:

```bash
hrcx split secret.txt -t 5 -k 3 -o ./vault
```

### Can I rename horcrux files?

Yes, but be careful:
- The filename doesn't affect reconstruction (metadata is inside the file)
- Descriptive names help you organize multiple sets of horcruxes
- The file extension must remain `.horcrux` for auto-discovery

### What happens to the original file?

The original file is **not** deleted or modified. You should:
1. Verify the horcruxes work (test reconstruction)
2. Securely delete the original file yourself
3. Distribute the horcruxes to different locations

## Security & Cryptography

### How secure is the encryption?

Very secure:
- **AES-256-GCM**: 256-bit keys, authenticated encryption
- **Random nonces**: Each horcrux uses a unique random nonce
- **No password vulnerabilities**: No weak passwords or dictionary attacks
- **Forward secrecy**: Losing one horcrux doesn't compromise others

### What is Shamir's Secret Sharing?

A cryptographic algorithm that splits a secret into N shares where any K shares can reconstruct the secret, but K-1 shares reveal nothing. It's mathematically proven and widely used in:
- Key management systems
- Multi-signature wallets
- Distributed storage
- Threshold cryptography

### Can someone decrypt my file with fewer than K horcruxes?

No. With K-1 horcruxes, an attacker gains **zero information** about:
- The encryption key
- The file contents
- Even the file size or type

This is a mathematical guarantee of Shamir's Secret Sharing.

### What if someone gets exactly K horcruxes?

Then they can reconstruct your file (that's the point). Distribute your horcruxes carefully:
- Store in different physical locations
- Different cloud services
- With different trusted people
- Never keep K horcruxes in the same place

### Is the metadata encrypted?

The metadata header (filename, timestamp, etc.) is stored in **plaintext** in each horcrux file. This allows you to identify which horcruxes belong together without decrypting.

The file **content** is fully encrypted with AES-256-GCM.

### Should I still delete the original file securely?

**Yes!** Horcrux encrypts the fragments, but the original file remains until you delete it. Use secure deletion tools:
- Windows: `cipher /w` or tools like Eraser
- macOS/Linux: `shred -uvz filename`
- Or use disk encryption (BitLocker, FileVault, LUKS)

### Can quantum computers break Horcrux encryption?

Current quantum computers cannot break AES-256 (may require 2^128 operations even with Grover's algorithm). However:
- Quantum-resistant encryption is an active research area
- By the time practical quantum computers exist, we'll have updated algorithms
- Shamir's Secret Sharing is information-theoretically secure (quantum-safe)

## Troubleshooting

### "hrcx: command not found"

This means Python's script directory isn't in your PATH. Solutions:

**Option 1**: Use `python -m hrcx` instead:
```bash
python -m hrcx split file.txt -t 5 -k 3
```

**Option 2**: Add Python's script directory to PATH:
- Windows: `C:\Python3X\Scripts`
- macOS/Linux: `~/.local/bin` or `/usr/local/bin`

### "ModuleNotFoundError: No module named 'hrcx'"

Horcrux isn't installed in the current Python environment. Install it:
```bash
pip install hrcx
```

If using virtual environments, ensure it's activated first.

### "Permission denied" when creating horcruxes

Check that you have write permissions to the output directory:
```bash
# Try a different output directory
hrcx split file.txt -t 5 -k 3 -o ~/Desktop
```

### "Not enough horcruxes provided for reconstruction"

You need at least K horcruxes (the threshold). Check the horcrux header to see the threshold:
```
YOU MUST FIND AT LEAST 2 OTHER HORCRUX(ES) TO RESURRECT THIS FILE
```
This means K=3 (you need 3 total).

### Horcruxes from different files mixed up

Each set of horcruxes has unique metadata (filename, timestamp). Check the header in each `.horcrux` file to identify which set it belongs to.

### "Horcrux files are corrupted or incomplete"

Possible causes:
- File transfer corruption (verify checksums)
- Incomplete download
- Storage media failure
- Wrong encoding during transfer (always use binary mode)

Try using other horcruxes from the set. You only need K out of N.

### Interactive mode not showing colors on Windows

Install colorama (usually bundled with Click):
```bash
pip install colorama
```

Or use Windows Terminal instead of cmd.exe for better color support.

### "Invalid horcrux file format"

The file may not be a valid `.horcrux` file:
- Check the file extension
- Verify it wasn't corrupted during transfer
- Ensure it's from a compatible Horcrux version

## Advanced Topics

### Can I use Horcrux in a Python script?

Yes! Horcrux provides a Python API:

```python
from hrcx import split, bind

# Split a file
split("secret.txt", total=5, threshold=3, output_dir="./vault")

# Bind (reconstruct) from horcruxes
bind(
    ["secret_1_of_5.horcrux", "secret_2_of_5.horcrux", "secret_3_of_5.horcrux"],
    output_path="./reconstructed.txt"
)
```

See the [README](../README.md#-python-api) for full API documentation.

### What's the format of a .horcrux file?

Each `.horcrux` file contains:
1. **ASCII art header** with instructions
2. **JSON metadata**: filename, timestamp, index, total, threshold, key fragment, nonce
3. **Separator line**: `--- SNIP ABOVE HERE ---`
4. **Encrypted content**: AES-256-GCM ciphertext (same in all horcruxes)

### Can I extract the key fragment manually?

Yes, the key fragment is in the JSON header (base64 encoded). However, you'd need to:
1. Extract K fragments from K horcruxes
2. Implement Shamir's Secret Sharing combination in GF(256)
3. Use the reconstructed key with the nonce to decrypt with AES-GCM

It's easier to just use `hrcx bind`.

### Can I compress files before encrypting?

Currently not built-in, but you can:
1. Compress the file first (ZIP, GZIP, etc.)
2. Split the compressed file with Horcrux
3. When reconstructing, decompress afterward

This can significantly reduce horcrux sizes for text files.

### Can I create multiple sets of horcruxes?

Yes! Each time you run `split`, it creates a new set with fresh encryption:
```bash
hrcx split secret.txt -t 5 -k 3 -o ./set1
hrcx split secret.txt -t 7 -k 4 -o ./set2
```

Each set is independent and has different encryption keys.

### How do I securely distribute horcruxes?

Best practices:
- **Physical separation**: Different USB drives, external HDDs
- **Cloud separation**: Different providers (Dropbox, Google Drive, OneDrive)
- **Geographic separation**: Different locations, different countries
- **Trusted parties**: Give to different trusted individuals
- **Never together**: Ensure <K horcruxes are never in one place

### Can I version control horcrux files?

Not recommended because:
- Horcruxes are binary files (Git handles poorly)
- Large files bloat repositories
- History exposes old versions

Instead, version control the original file (if appropriate) or use dedicated backup solutions.

### What's the performance impact?

- **Encryption**: ~10-50 MB/s (depends on CPU)
- **Shamir splitting**: Very fast (microseconds for key splitting)
- **Memory**: ~2x file size during operation
- **Horcrux size**: Identical to original file size (each horcrux contains full ciphertext)

### Why is each horcrux the same size as the original?

Shamir's Secret Sharing splits the **encryption key**, not the file itself. Each horcrux contains:
- A unique key fragment (small)
- The complete encrypted file content (same size as original)

This design ensures any K horcruxes can reconstruct the file without needing all N horcruxes.

### Can I audit the source code?

Absolutely! Horcrux is open source:
- Repository: https://github.com/juliuspleunes4/Horcrux
- License: MIT
- All code is readable Python
- Uses well-known libraries (no hidden dependencies)

We welcome security audits and vulnerability reports.

---

## Still Have Questions?

- Check the [README](../README.md)
- Review [CONTRIBUTING.md](CONTRIBUTING.md)
- Open an [issue](https://github.com/juliuspleunes4/Horcrux/issues)
- Start a [discussion](https://github.com/juliuspleunes4/Horcrux/discussions)
