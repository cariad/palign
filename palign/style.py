from dataclasses import dataclass
from typing import Optional

from PIL.ImageFont import FreeTypeFont

from palign.enums import Horizontal, Vertical
from palign.types import Color


@dataclass
class Style:
    """
    Text style.

    `background_color` prescribes the optional background colour. A background
    will not be painted if this is omitted.
    """

    background: Optional[Color] = None
    """
    Background colour.
    """

    color: Optional[Color] = None
    """
    Text colour.
    """

    font: Optional[FreeTypeFont] = None
    """
    Font.
    """

    horizontal: Horizontal = Horizontal.Left

    tracking: float = 0
    """
    Character tracking.
    """

    vertical: Vertical = Vertical.Top
