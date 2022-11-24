from typing import List

from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont
from pytest import mark

from palign import Character
from palign.style import Style
from palign.text import Text


@mark.parametrize(
    "text, tracking, expect",
    [
        (
            "foo bar",
            0,
            [
                Character(character="f", x=0, y=0),
                Character(character="o", x=16.0, y=0),
                Character(character="o", x=43.0, y=0),
                Character(character=" ", x=70.0, y=0),
                Character(character="b", x=87.0, y=0),
                Character(character="a", x=115.0, y=0),
                Character(character="r", x=143.0, y=0),
            ],
        ),
        (
            "foo bar",
            -2,
            [
                Character(character="f", x=0, y=0),
                Character(character="o", x=14.0, y=0),
                Character(character="o", x=39.0, y=0),
                Character(character=" ", x=64.0, y=0),
                Character(character="b", x=79.0, y=0),
                Character(character="a", x=105.0, y=0),
                Character(character="r", x=131.0, y=0),
            ],
        ),
        (
            "foo bar",
            +2,
            [
                Character(character="f", x=0, y=0),
                Character(character="o", x=18.0, y=0),
                Character(character="o", x=47.0, y=0),
                Character(character=" ", x=76.0, y=0),
                Character(character="b", x=95.0, y=0),
                Character(character="a", x=125.0, y=0),
                Character(character="r", x=155.0, y=0),
            ],
        ),
    ],
)
def test_characters(
    font: FreeTypeFont,
    text: str,
    tracking: float,
    expect: List[Character],
) -> None:
    image = Image.new("RGB", (1600, 900))
    draw = ImageDraw.Draw(image)
    style = Style(font=font, tracking=tracking)
    t = Text(text, style, draw.textlength)
    assert list(t) == expect
