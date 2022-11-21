# pylint: disable=missing-function-docstring

from typing import List

from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont
from pytest import mark

from palign import Character, Render


@mark.parametrize(
    "text, tracking, expect",
    [
        (
            "foo bar",
            0,
            [
                Character(character="f", x=0, y=0),
                Character(character="o", x=16, y=0),
                Character(character="o", x=43, y=0),
                Character(character=" ", x=70, y=0),
                Character(character="b", x=87, y=0),
                Character(character="a", x=115, y=0),
                Character(character="r", x=143, y=0),
            ],
        ),
        (
            "foo bar",
            -2,
            [
                Character(character="f", x=0, y=0),
                Character(character="o", x=14, y=0),
                Character(character="o", x=39, y=0),
                Character(character=" ", x=64, y=0),
                Character(character="b", x=79, y=0),
                Character(character="a", x=105, y=0),
                Character(character="r", x=131, y=0),
            ],
        ),
        (
            "foo bar",
            +2,
            [
                Character(character="f", x=0, y=0),
                Character(character="o", x=18, y=0),
                Character(character="o", x=47, y=0),
                Character(character=" ", x=76, y=0),
                Character(character="b", x=95, y=0),
                Character(character="a", x=125, y=0),
                Character(character="r", x=155, y=0),
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
    render = Render(draw, font, tracking)
    assert list(render.characters(text)) == expect
