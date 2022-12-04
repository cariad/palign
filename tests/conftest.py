from typing import Optional

from PIL.ImageFont import FreeTypeFont, truetype
from pytest import fixture

from palign.log import log
from palign.types import GetTextLength

log.setLevel("DEBUG")


@fixture
def font(font_path: str) -> FreeTypeFont:
    return truetype("tests/font/ChelseaMarket-Regular.ttf", 42)


@fixture
def get_length() -> GetTextLength:
    def wrapped(s: str, _: Optional[FreeTypeFont]) -> int:
        return 10 * len(s)

    return wrapped
