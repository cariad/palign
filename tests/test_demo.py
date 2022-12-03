from pathlib import Path

from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from palign import Alignment, Grid, Percent, Region, Style, Text

image_dir = Path() / "docs" / "images"


def test_demo(font_path: str) -> None:
    image_size = (600, 400)
    image_region = Region.new(0, 0, *image_size).resolve()

    image = Image.new("RGB", image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    small_font = truetype(font_path, 26)

    column_count = 3
    row_count = 3

    default_style = Style(
        color=(0, 0, 0),
        font=small_font,
    )

    grid = Grid(
        column_count,
        row_count,
        image_region.expand(-40),
        default_style=default_style,
    )

    grid[0, 0].text = "Top\nLeft"
    grid[0, 0].style.horizontal = Alignment.Near
    grid[0, 0].style.vertical = Alignment.Near

    grid[1, 0].text = "Top\nCenter"
    grid[1, 0].style.horizontal = Alignment.Center
    grid[1, 0].style.vertical = Alignment.Near

    grid[2, 0].text = "Top\nRight"
    grid[2, 0].style.horizontal = Alignment.Far
    grid[2, 0].style.vertical = Alignment.Near

    grid[0, 1].text = "Center\nLeft"
    grid[0, 1].style.horizontal = Alignment.Near
    grid[0, 1].style.vertical = Alignment.Center

    grid[1, 1].text = "Center\nCenter"
    grid[1, 1].style.horizontal = Alignment.Center
    grid[1, 1].style.vertical = Alignment.Center

    grid[2, 1].text = "Center\nRight"
    grid[2, 1].style.horizontal = Alignment.Far
    grid[2, 1].style.vertical = Alignment.Center

    grid[0, 2].text = "Bottom\nLeft"
    grid[0, 2].style.horizontal = Alignment.Near
    grid[0, 2].style.vertical = Alignment.Far

    grid[1, 2].text = "Bottom\nCenter"
    grid[1, 2].style.horizontal = Alignment.Center
    grid[1, 2].style.vertical = Alignment.Far

    grid[2, 2].text = "Bottom\nRight"
    grid[2, 2].style.horizontal = Alignment.Far
    grid[2, 2].style.vertical = Alignment.Far

    def color_bit(column: int) -> int:
        return 155 + int((100 / column_count) * column)

    for x in range(column_count):
        for y in range(row_count):
            red = color_bit(x) if y == 0 else 255
            green = color_bit(x) if y == 1 else 255
            blue = color_bit(x) if y == 2 else 255
            grid[x, y].style.background = (red, green, blue)

    grid.render(draw)

    image.save(image_dir / "grid.png", "png")


def test_example_0() -> None:
    image = Image.new("RGB", (150, 28))
    draw = ImageDraw.Draw(image)

    style = Style(font=truetype("tests/font/ChelseaMarket-Regular.ttf", 21))

    Text(draw).draw_text("Hello world!", style, (0, 0))

    image.save(image_dir / "example-0.png", "png")


def test_example_1() -> None:
    image = Image.new("RGB", (260, 120), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    style = Style(
        color=(0, 0, 0),
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 21),
    )

    renderer = Text(draw, style)

    renderer.draw_text("Red!", Style(color=(255, 0, 0)), (0, 0))
    renderer.draw_text("Increased tracking!", Style(tracking=2), (0, 40))
    renderer.draw_text("Decreased tracking!", Style(tracking=-2), (0, 80))

    image.save(Path() / "docs" / "images" / "example-1.png", "png")


def test_example_2() -> None:
    image_size = (300, 720)
    image_region = Region.new(0, 0, *image_size).resolve()

    image = Image.new("RGB", image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Build a region to render the first block of text into.
    #
    # Start by contracting the image boundary to create a margin, then create a
    # subregion that starts in the top corner, takes all available width and is
    # 70 pixels tall.
    text_region = (
        image_region.expand(-10).region2(0, 0, Percent(100), 70).resolve()
    )

    style = Style(
        border_color=(200, 200, 200),
        border_radius=3,
        border_width=1,
        color=(0, 0, 0),
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 21),
    )

    renderer = Text(draw, style)

    for vertical in Alignment:
        for horizontal in Alignment:
            alignment = Style(horizontal=horizontal, vertical=vertical)

            match horizontal:
                case Alignment.Near:
                    horizontal_name = "Left"
                case Alignment.Center:
                    horizontal_name = "Center"
                case Alignment.Far:
                    horizontal_name = "Right"

            match vertical:
                case Alignment.Near:
                    vertical_name = "Top"
                case Alignment.Center:
                    vertical_name = "Center"
                case Alignment.Far:
                    vertical_name = "Bottom"

            text = f"{vertical_name} {horizontal_name}"
            renderer.draw_text(text, alignment, text_region)

            # Translate the region down by (text_region.height + 10) pixels for
            # the next block.
            text_region += (0, text_region.height + 10)

    image.save(image_dir / "example-2.png", "png")
