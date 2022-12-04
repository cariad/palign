from typing import Sequence

from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont
from pytest import mark

from palign.style import Style
from palign.text_line import TextLine


@mark.parametrize(
    "text, tracking, expect",
    [
        (
            "foo bar",
            0,
            [
                ("f", 0),
                ("o", 16.0),
                ("o", 43.0),
                (" ", 70.0),
                ("b", 87.0),
                ("a", 115.0),
                ("r", 143.0),
            ],
        ),
        (
            "foo bar",
            -2,
            [
                ("f", 0),
                ("o", 14.0),
                ("o", 39.0),
                (" ", 64.0),
                ("b", 79.0),
                ("a", 105.0),
                ("r", 131.0),
            ],
        ),
        (
            "foo bar",
            +2,
            [
                ("f", 0),
                ("o", 18.0),
                ("o", 47.0),
                (" ", 76.0),
                ("b", 95.0),
                ("a", 125.0),
                ("r", 155.0),
            ],
        ),
    ],
)
def test_characters(
    font: FreeTypeFont,
    text: str,
    tracking: float,
    expect: Sequence[tuple[str, int]],
) -> None:
    image = Image.new("RGB", (1600, 900))
    draw = ImageDraw.Draw(image)
    style = Style(font=font, tracking=tracking)

    text_line = TextLine(draw.textlength)

    for f in style.text(text).lines:
        text_line.append(f)

    for index, actual_char in enumerate(text_line):
        assert actual_char.character == expect[index][0]
        assert actual_char.x == expect[index][1]
