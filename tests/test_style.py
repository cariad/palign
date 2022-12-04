from PIL.ImageFont import truetype
from pytest import mark, raises

from palign import Alignment, Style

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
                horizontal=Alignment.Center,
                tracking=3,
                vertical=Alignment.Far,
            ),
            Style(
                background=(0, 0, 0),
                color=(1, 0, 0),
                font=font_0,
                horizontal=Alignment.Center,
                tracking=3,
                vertical=Alignment.Far,
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
            Style(horizontal=Alignment.Center),
            Style(horizontal=Alignment.Far),
            Style(horizontal=Alignment.Far),
        ),
        (
            Style(tracking=1),
            Style(tracking=0),
            Style(tracking=0),
        ),
        (
            Style(vertical=Alignment.Far),
            Style(vertical=Alignment.Center),
            Style(vertical=Alignment.Center),
        ),
    ],
)
def test_add(a: Style, b: Style, expect: Style) -> None:
    assert a + b == expect


def test_add__not_style() -> None:
    with raises(TypeError) as ex:
        _ = Style() + "foo"

    assert str(ex.value) == "Can merge only Style to Style"
