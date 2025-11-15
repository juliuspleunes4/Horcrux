"""
Tests for the public API (split and bind functions).
"""

import pytest
from pathlib import Path
from hrcx import split, bind


def test_split_not_implemented():
    """Test that split raises NotImplementedError (temporary)."""
    with pytest.raises(NotImplementedError):
        split("test.txt", total=5, threshold=3)


def test_bind_not_implemented():
    """Test that bind raises NotImplementedError (temporary)."""
    with pytest.raises(NotImplementedError):
        bind(["test_1_of_5.horcrux"])
