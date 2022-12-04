from typing import Optional

from bounden import Region2, ResolvedRegion2
from PIL.ImageDraw import ImageDraw

from palign.config import DEFAULT_FONT_SIZE
from palign.log import log
from palign.style import Style
from palign.text_lines import TextLines
from palign.types import Point, Region, ResolvedRegion


class TextRenderer:
    """
    Text renderer.

    `draw` is the Pillow drawing instance to render to.

    `style` is the optional default style to apply.
    """

    def __init__(self, draw: ImageDraw, style: Optional[Style] = None) -> None:
        self._draw = draw
        self._style = style or Style()

    def _render_text(
        self,
        text_lines: TextLines,
        style: Style,
        target: ResolvedRegion,
    ) -> None:
        line_height = style.font.size if style.font else DEFAULT_FONT_SIZE

        lines_region = target.region2(
            0 if style.horizontal is None else style.horizontal,
            0 if style.vertical is None else style.vertical,
            text_lines.width,
            text_lines.height,
        ).resolve()

        for line_index, line in enumerate(text_lines):
            line_region = lines_region.region2(
                0 if style.horizontal is None else style.horizontal,
                0,
                line.width,
                line_height,
            ).resolve()

            line_resolved = line_region + (0, line_height * line_index)

            for character in line:
                self._draw.text(
                    (line_resolved.left + character.x, line_resolved.top),
                    character.character,
                    fill=style.color,
                    font=style.font,
                )

    def draw_text(
        self,
        text: Optional[str],
        bounds: Region | Region2[float, float] | ResolvedRegion | Point,
        style: Optional[Style] = None,
    ) -> None:
        style = self._style if style is None else self._style + style
        lines = TextLines(text, style, self._draw.textlength) if text else None

        if lines is not None and isinstance(bounds, tuple):
            bounds = Region.new(
                bounds[0],
                bounds[1],
                lines.width,
                lines.height,
            )

        if isinstance(bounds, Region2):
            resolved = bounds.resolve()
        elif isinstance(bounds, ResolvedRegion2):
            resolved = bounds
        else:
            resolved = None

        resolved_bounds = (
            None
            if resolved is None
            else (resolved.left, resolved.top, resolved.right, resolved.bottom)
        )

        if style.background is not None:
            if resolved_bounds is None:
                log.warning(
                    "Will not draw background when bounds is a position"
                )
            else:
                if style.border_radius is None:
                    self._draw.rectangle(
                        resolved_bounds,
                        fill=style.background,
                    )
                else:
                    self._draw.rounded_rectangle(
                        resolved_bounds,
                        fill=style.background,
                        radius=style.border_radius,
                    )

        if style.border_color is not None and style.border_width is not None:
            if resolved_bounds is None:
                log.warning("Will not draw border when bounds is a position")
            else:
                if style.border_radius is None:
                    self._draw.rectangle(
                        resolved_bounds,
                        outline=style.border_color,
                        width=style.border_width,
                    )
                else:
                    self._draw.rounded_rectangle(
                        resolved_bounds,
                        outline=style.border_color,
                        radius=style.border_radius,
                        width=style.border_width,
                    )

        if lines is not None and resolved is not None:
            self._render_text(lines, style, resolved)
