from PIL.ImageFont import FreeTypeFont, truetype
from pytest import fixture

from palign.log import log

log.setLevel("DEBUG")


@fixture
def font(font_path: str) -> FreeTypeFont:
    return truetype(font_path, 42)


@fixture
def font_path() -> str:
    return "tests/font/ChelseaMarket-Regular.ttf"
