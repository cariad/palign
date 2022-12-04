from nvalues.exceptions import InvalidKey
from PIL import Image, ImageDraw
from PIL.ImageFont import truetype
from pytest import mark, raises

from palign import Alignment, Grid, Percent, Region, Style, make_image_region


def test_delete() -> None:
    grid = Grid(3, 3, Region.new(100, 100, 100, 100))
    assert grid[0, 0].text is None

    grid[0, 0].text = "foo"
    assert grid[0, 0].text == "foo"

    del grid[0, 0]
    assert grid[0, 0].text is None


def test_demo_0() -> None:
    image_region = make_image_region(500, 500)

    image = Image.new("RGB", image_region.size)
    draw = ImageDraw.Draw(image)

    grid_region = image_region.region2(
        Alignment.Center,
        Alignment.Center,
        Percent(90),
        Percent(90),
    )

    style = Style(
        border_color=(100, 100, 100),
        border_width=1,
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 34),
    )

    grid = Grid(3, 4, grid_region, style=style)

    grid.draw(draw)

    image.save("./docs/images/grid-example-0.png", "png")


def test_demo_1() -> None:
    image_region = make_image_region(500, 500)

    image = Image.new("RGB", image_region.size)
    draw = ImageDraw.Draw(image)

    style = Style(
        border_color=(100, 100, 100),
        border_width=1,
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 34),
    )

    grid_region = image_region.region2(
        Alignment.Center,
        Alignment.Center,
        Percent(90),
        Percent(90),
    )

    grid = Grid(3, 4, grid_region, style=style)

    grid[0, 0].text = "Hello!"
    grid[2, 1].text = "Hola!"
    grid[1, 3].text = "Hej!"
    grid[0, 2].text = "Bonjour!"

    grid.draw(draw)

    image.save("./docs/images/grid-example-1.png", "png")


def test_demo_2() -> None:
    image_region = make_image_region(500, 500)

    image = Image.new("RGB", image_region.size)
    draw = ImageDraw.Draw(image)

    style = Style(
        border_color=(100, 100, 100),
        border_width=1,
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 34),
    )

    grid_region = image_region.region2(
        Alignment.Center,
        Alignment.Center,
        Percent(90),
        Percent(90),
    )

    grid = Grid(3, 4, grid_region, style=style)

    grid[0, 0].style.color = (255, 255, 0)
    grid[0, 0].text = "Hello!"

    grid[2, 1].style.tracking = 10
    grid[2, 1].text = "Hola!"

    grid[1, 3].style.background = (0, 50, 0)
    grid[1, 3].text = "Hej!"

    grid[0, 2].style.vertical = Alignment.Center
    grid[0, 2].text = "Bonjour!"

    grid.draw(draw)

    image.save("./docs/images/grid-example-2.png", "png")


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
