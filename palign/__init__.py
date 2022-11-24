"""
Palign provides functions for aligning text to be rendered via Pillow.
"""

from importlib.resources import files

from palign.draw_text import draw_text
from palign.grid import Grid
from palign.style import Style

with files(__package__).joinpath("VERSION").open("r") as t:
    version = t.readline().strip()

__all__ = [
    "Style",
    "Grid",
    "draw_text",
    "version",
]
