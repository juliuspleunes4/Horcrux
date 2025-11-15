"""
Public API for Horcrux file operations.

This module provides the main split() and bind() functions for the library interface.
"""

from pathlib import Path
from typing import List, Optional


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
    # TODO: Implementation
    raise NotImplementedError("split() not yet implemented")


def bind(
    horcrux_paths: List[str],
    output_path: Optional[str] = None,
    overwrite: bool = False
) -> None:
    """
    Reconstruct the original file from horcruxes.
    
    This function takes K or more horcrux files, reconstructs the encryption key
    using Shamir's Secret Sharing, and decrypts the original file using AES-256-GCM.
    
    Args:
        horcrux_paths: List of paths to horcrux files (must have >= threshold files)
        output_path: Optional output file path (default: original filename from horcrux metadata)
        overwrite: If True, overwrite existing file without prompting
    
    Raises:
        FileNotFoundError: If any horcrux file doesn't exist
        ValueError: If insufficient horcruxes provided or files are incompatible
        FileExistsError: If output file exists and overwrite=False
        
    Example:
        >>> bind(["secret_1_of_5.horcrux", "secret_3_of_5.horcrux", "secret_5_of_5.horcrux"])
        # Reconstructs: secret.txt
    """
    # TODO: Implementation
    raise NotImplementedError("bind() not yet implemented")
