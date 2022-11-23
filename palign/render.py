from typing import Iterable, Optional

from PIL.ImageDraw import ImageDraw
from PIL.ImageFont import FreeTypeFont

from palign.character import Character
from palign.types import Color


class Render:
    """
    Pillow text renderer.

    Args:
        draw: Editable image.
        font: Font. Defaults to Pillow's default font.
        color: Colour. Defaults to white.
        tracking: Character tracking. Defaults to 0.
    """

    def __init__(
        self,
        draw: ImageDraw,
        color: Optional[Color] = None,
        font: Optional[FreeTypeFont] = None,
        tracking: Optional[float] = None,
    ) -> None:
        self._draw = draw

        self._color = color or (255, 255, 255)
        self._font = font

        self.tracking = tracking or 0
        """
        Character tracking.
        """

    def characters(self, text: str) -> Iterable[Character]:
        """
        Yields the render coordinates of each character.

        Args:
            text: Text to render.

        Returns:
            Render coordinates of each character.
        """

        x: float = 0
        y: float = 0

        for index, char in enumerate(text):
            if index > 0:
                x += self.tracking

            yield Character(char, int(x), int(y))

            x += self._draw.textlength(char, self._font)

    def text(self, text: str, x: int, y: int) -> None:
        """
        Renders a string of text.

        Args:
            text: Text.
            x: X pixel coordinate.
            y: Y pixel coordinate.
        """

        for char in self.characters(text):
            self._draw.text(
                char.pillow_coords(x, y),
                char.character,
                fill=self._color,
                font=self._font,
            )
