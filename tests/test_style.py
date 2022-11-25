from PIL.ImageFont import truetype
from pytest import mark

from palign import Horizontal, Style, Vertical

font_0 = truetype("tests/font/ChelseaMarket-Regular.ttf", 0)
font_1 = truetype("tests/font/ChelseaMarket-Regular.ttf", 1)


@mark.parametrize(
    "a, b, expect",
    [
        (
            Style(),
            Style(
                background=(0, 0, 0),
                color=(1, 0, 0),
                font=font_0,
                horizontal=Horizontal.Center,
                tracking=3,
                vertical=Vertical.Bottom,
            ),
            Style(
                background=(0, 0, 0),
                color=(1, 0, 0),
                font=font_0,
                horizontal=Horizontal.Center,
                tracking=3,
                vertical=Vertical.Bottom,
            ),
        ),
        (
            Style(background=(0, 0, 0)),
            Style(background=(1, 0, 0)),
            Style(background=(1, 0, 0)),
        ),
        (
            Style(color=(0, 0, 0)),
            Style(color=(1, 0, 0)),
            Style(color=(1, 0, 0)),
        ),
        (
            Style(font=font_0),
            Style(font=font_1),
            Style(font=font_1),
        ),
        (
            Style(horizontal=Horizontal.Center),
            Style(horizontal=Horizontal.Right),
            Style(horizontal=Horizontal.Right),
        ),
        (
            Style(tracking=1),
            Style(tracking=0),
            Style(tracking=0),
        ),
        (
            Style(vertical=Vertical.Bottom),
            Style(vertical=Vertical.Center),
            Style(vertical=Vertical.Center),
        ),
    ],
)
def test_add(a: Style, b: Style, expect: Style) -> None:
    assert a + b == expect
