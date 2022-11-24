from typing import List, Optional

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
                Character(character="o", x=17, y=0),
                Character(character="o", x=44, y=0),
                Character(character=" ", x=71, y=0),
                Character(character="b", x=88, y=0),
                Character(character="a", x=116, y=0),
                Character(character="r", x=144, y=0),
            ],
        ),
        (
            "foo bar",
            -2,
            [
                Character(character="f", x=0, y=0),
                Character(character="o", x=15, y=0),
                Character(character="o", x=40, y=0),
                Character(character=" ", x=65, y=0),
                Character(character="b", x=80, y=0),
                Character(character="a", x=106, y=0),
                Character(character="r", x=132, y=0),
            ],
        ),
        (
            "foo bar",
            +2,
            [
                Character(character="f", x=0, y=0),
                Character(character="o", x=19, y=0),
                Character(character="o", x=48, y=0),
                Character(character=" ", x=77, y=0),
                Character(character="b", x=96, y=0),
                Character(character="a", x=126, y=0),
                Character(character="r", x=156, y=0),
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

    def get_text_size(
        measure: str,
        font: Optional[FreeTypeFont],
    ) -> tuple[float, float]:
        b = draw.textbbox((0, 0), measure, font=font)
        return (b[2] - b[0], b[3] - b[1])

    t = Text(text, style, get_text_size)
    assert list(t) == expect
