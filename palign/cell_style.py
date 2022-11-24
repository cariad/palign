from typing import Optional

from PIL.ImageDraw import ImageDraw

from palign.types import Bounds, Color


class CellStyle:
    """
    Cell style.

    `background_color` prescribes the optional background colour. A background
    will not be painted if this is omitted.
    """

    def __init__(self, background_color: Optional[Color] = None) -> None:
        self.background_color = background_color
        """
        Background colour.
        """

    def render(self, draw: ImageDraw, bounds: Bounds) -> None:
        """
        Renders the cell via `draw` within `bounds`.
        """

        if self.background_color is not None:
            draw.rectangle(bounds, fill=self.background_color)
