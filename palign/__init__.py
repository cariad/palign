"""
Palign provides functions for aligning text to be rendered via Pillow.
"""

from importlib.resources import files

from bounden import Alignment, Percent

from palign.grid import Grid
from palign.style import Style
from palign.text import Text
from palign.types import Region, ResolvedRegion

with files(__package__).joinpath("VERSION").open("r") as t:
    version = t.readline().strip()

__all__ = [
    "Alignment",
    "Grid",
    "Percent",
    "Region",
    "ResolvedRegion",
    "Style",
    "Text",
    "version",
]
