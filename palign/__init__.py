"""
Palign provides functions for aligning text to be rendered via Pillow.
"""

from importlib.resources import files

from palign.cell_style import CellStyle
from palign.character import Character
from palign.grid import Grid
from palign.render import Render

with files(__package__).joinpath("VERSION").open("r") as t:
    version = t.readline().strip()

__all__ = [
    "CellStyle",
    "Character",
    "Grid",
    "Render",
    "version",
]
