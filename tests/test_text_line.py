from typing import List

from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont
from pytest import mark

from palign.character import TextLineCharacter
from palign.style import Style
from palign.text_line import TextLine


@mark.parametrize(
    "text, tracking, expect",
    [
        (
            "foo bar",
            0,
            [
                TextLineCharacter(character="f", x=0),
                TextLineCharacter(character="o", x=16.0),
                TextLineCharacter(character="o", x=43.0),
                TextLineCharacter(character=" ", x=70.0),
                TextLineCharacter(character="b", x=87.0),
                TextLineCharacter(character="a", x=115.0),
                TextLineCharacter(character="r", x=143.0),
            ],
        ),
        (
            "foo bar",
            -2,
            [
                TextLineCharacter(character="f", x=0),
                TextLineCharacter(character="o", x=14.0),
                TextLineCharacter(character="o", x=39.0),
                TextLineCharacter(character=" ", x=64.0),
                TextLineCharacter(character="b", x=79.0),
                TextLineCharacter(character="a", x=105.0),
                TextLineCharacter(character="r", x=131.0),
            ],
        ),
        (
            "foo bar",
            +2,
            [
                TextLineCharacter(character="f", x=0),
                TextLineCharacter(character="o", x=18.0),
                TextLineCharacter(character="o", x=47.0),
                TextLineCharacter(character=" ", x=76.0),
                TextLineCharacter(character="b", x=95.0),
                TextLineCharacter(character="a", x=125.0),
                TextLineCharacter(character="r", x=155.0),
            ],
        ),
    ],
)
def test_characters(
    font: FreeTypeFont,
    text: str,
    tracking: float,
    expect: List[TextLineCharacter],
) -> None:
    image = Image.new("RGB", (1600, 900))
    draw = ImageDraw.Draw(image)
    style = Style(font=font, tracking=tracking)

    text_line = TextLine(style, draw.textlength)
    text_line.append(text)
    assert list(text_line) == expect
