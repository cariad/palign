from typing import Iterator

from palign.config import DEFAULT_FONT_SIZE
from palign.style import Style
from palign.text_line import TextLine
from palign.types import GetTextLength


class TextLines:
    """
    An ordered set of text lines.
    """

    def __init__(
        self,
        text: str,
        style: Style,
        get_length: GetTextLength,
    ) -> None:
        curr_line = TextLine(style, get_length)
        self._lines = [curr_line]

        for char in text:
            if char == "\n":
                curr_line = TextLine(style, get_length)
                self._lines.append(curr_line)
            else:
                curr_line.append(char)

        self._line_height = (
            int(style.font.size) if style.font else DEFAULT_FONT_SIZE
        )

    def __iter__(self) -> Iterator[TextLine]:
        return iter(self._lines)

    def __str__(self) -> str:
        return str(self._lines)

    @property
    def height(self) -> int:
        """
        Height of all lines.
        """

        return self._line_height * len(self._lines)

    @property
    def line_height(self) -> int:
        """
        Height of each line.
        """

        return self._line_height

    @property
    def width(self) -> float:
        """
        Width of the the longest line.
        """

        return max(line.width for line in self._lines)
