from typing import Optional

from PIL.ImageFont import FreeTypeFont, truetype
from pytest import fixture

from palign.log import log
from palign.types import GetTextLength

log.setLevel("DEBUG")


@fixture
def font(font_path: str) -> FreeTypeFont:
    return truetype(font_path, 42)


@fixture
def font_path() -> str:
    return "tests/font/ChelseaMarket-Regular.ttf"


@fixture
def get_length() -> GetTextLength:
    def wrapped(s: str, _: Optional[FreeTypeFont]) -> int:
        return 10 * len(s)

    return wrapped
