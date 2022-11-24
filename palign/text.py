from typing import Iterator, List

from palign.character import Character
from palign.style import Style
from palign.types import GetTextSize


class Text:
    def __init__(self, text: str, style: Style, get_size: GetTextSize) -> None:
        self._width: float = 0
        self._height: float = 0

        if style.font:
            self._height = style.font.size

        y: float = 0

        self._characters: List[Character] = []

        for index, char in enumerate(text):
            if index > 0:
                self._width += style.tracking

            self._characters.append(Character(char, self._width, y))
            (width, height) = get_size(char, style.font)
            self._width += width
            if not style.font:
                self._height = max(self._height, height)

    def __iter__(self) -> Iterator[Character]:
        for character in self._characters:
            yield character

    @property
    def height(self) -> float:
        return self._height

    @property
    def width(self) -> float:
        return self._width
