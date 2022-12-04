from nvalues.exceptions import InvalidKey
from pytest import mark, raises

from palign import Grid, Region


@mark.parametrize(
    "coords, expect",
    [
        ((4, 0), "Key (4, 0) failed validation (No column 4; grid has 3)"),
        ((0, 4), "Key (0, 4) failed validation (No row 4; grid has 3)"),
    ],
)
def test_set_out_of_range(coords: tuple[int, int], expect: str) -> None:
    grid = Grid(3, 3, Region.new(100, 100, 100, 100))

    with raises(InvalidKey) as ex:
        grid[coords].text = "foo"

    assert str(ex.value) == expect
