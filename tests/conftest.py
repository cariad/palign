# pylint: disable=missing-function-docstring

from PIL.ImageFont import FreeTypeFont, truetype
from pytest import fixture


@fixture
def font() -> FreeTypeFont:
    return truetype("tests/font/ChelseaMarket-Regular.ttf", 42)
