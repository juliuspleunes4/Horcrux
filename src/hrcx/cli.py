"""
Command-line interface for Horcrux.

This module provides the CLI commands using Click.
"""

import click
from pathlib import Path
from typing import Optional


@click.group()
@click.version_option(version="1.0.0", prog_name="hrcx")
def main() -> None:
    """
    Horcrux - Split your files into encrypted fragments.
    
    Split files using Shamir's Secret Sharing Scheme and AES-256-GCM encryption.
    """
    pass


@main.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("-t", "--total", type=int, help="Total number of horcruxes to create")
@click.option("-k", "--threshold", type=int, help="Minimum horcruxes needed to reconstruct")
@click.option("-o", "--output", type=click.Path(), help="Output directory for horcruxes")
def split(file: str, total: Optional[int], threshold: Optional[int], output: Optional[str]) -> None:
    """
    Split a file into encrypted horcruxes.
    
    Example:
        hrcx split secret.txt -t 5 -k 3
    """
    # TODO: Implement interactive prompts if total/threshold not provided
    # TODO: Call hrcx.api.split()
    click.echo(f"Splitting {file}...")
    click.echo("⚠️  Not yet implemented")


@main.command()
@click.argument("directory", type=click.Path(exists=True), default=".")
@click.option("-o", "--output", type=click.Path(), help="Output file path")
@click.option("-f", "--force", is_flag=True, help="Overwrite existing file without prompting")
def bind(directory: str, output: Optional[str], force: bool) -> None:
    """
    Reconstruct the original file from horcruxes.
    
    Example:
        hrcx bind ./vault
    """
    # TODO: Find all .horcrux files in directory
    # TODO: Call hrcx.api.bind()
    click.echo(f"Binding horcruxes from {directory}...")
    click.echo("⚠️  Not yet implemented")


if __name__ == "__main__":
    main()
