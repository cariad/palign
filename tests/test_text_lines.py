from pytest import mark

from palign import Style
from palign.text_lines import TextLines
from palign.types import GetTextLength


@mark.parametrize(
    "source, expect",
    [
        ("foo", "foo"),
    ],
)
def test_str(source: str, expect: str, get_length: GetTextLength) -> None:
    assert str(TextLines(source, Style(), get_length)) == expect
