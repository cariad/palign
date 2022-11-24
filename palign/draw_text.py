from typing import Optional

from PIL.ImageDraw import ImageDraw

from palign.enums import Horizontal, Vertical
from palign.style import Style
from palign.text import Text
from palign.types import Bounds


def draw_text(
    text: Optional[str],
    draw: ImageDraw,
    style: Style,
    bounds: Bounds,
) -> None:
    if style.background is not None:
        draw.rectangle(bounds, fill=style.background)

    if text:
        t = Text(text, style, draw.textlength)

        bounds_width = bounds[2] - bounds[0]
        bounds_height = bounds[3] - bounds[1]

        match style.horizontal:
            case Horizontal.Center:
                origin_x = bounds[0] + (bounds_width / 2) - (t.width / 2)
            case Horizontal.Right:
                origin_x = bounds[0] + bounds_width - t.width
            case _:
                origin_x = bounds[0]

        match style.vertical:
            case Vertical.Center:
                origin_y = bounds[1] + (bounds_height / 2) - (t.height / 2)
            case Vertical.Bottom:
                origin_y = bounds[1] + bounds_height - t.height
            case _:
                origin_y = bounds[1]

        origin = (origin_x, origin_y)

        for char in t:
            draw.text(
                char.pillow_coords(origin),
                char.character,
                fill=style.color,
                font=style.font,
            )
