from typing import Iterable

from PIL.ImageDraw import ImageDraw
from PIL.ImageFont import FreeTypeFont

from palign.character import Character


class Render:
    """
    Pillow text renderer.

    Args:
        draw: Editable image.
        font: Font.
        tracking: Character tracking.
    """

    def __init__(
        self,
        draw: ImageDraw,
        font: FreeTypeFont,
        tracking: float = 0,
    ) -> None:
        self.draw = draw
        self.font = font
        self.tracking = tracking

    def characters(self, text: str) -> Iterable[Character]:
        """
        Yields the render coordinates of each character.

        Args:
            text: Text to render.

        Returns:
            Render coordinates of each character.
        """

        x: float = 0  # pylint: disable=invalid-name
        y: float = 0  # pylint: disable=invalid-name

        for index, char in enumerate(text):
            if index > 0:
                x += self.tracking  # pylint: disable=invalid-name

            yield Character(char, int(x), int(y))

            # pylint: disable=invalid-name
            x += self.draw.textlength(char, self.font)
