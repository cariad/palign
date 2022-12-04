from pathlib import Path

from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from palign import Alignment, Grid, Percent, Style, Text, make_image_region

image_dir = Path() / "docs" / "images"


def test_demo(font_path: str) -> None:
    image_region = make_image_region(600, 400)

    image = Image.new("RGB", image_region.size, (255, 255, 255))
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
    # Create a Pillow Image and Draw as usual:
    image = Image.new("RGB", (270, 60))
    draw = ImageDraw.Draw(image)

    # Create a Style to describe the font:
    style = Style(
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 42),
    )

    # Create a text renderer:
    renderer = Text(draw, style)

    # Draw "Hello world!" at (0, 0):
    renderer.draw_text("Hello world!", (0, 0))

    # Same the image via Pillow:
    image.save("./docs/images/example-0.png", "png")


def test_example_1() -> None:
    image = Image.new("RGB", (410, 410), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    style = Style(
        color=(0, 0, 0),
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 42),
    )

    renderer = Text(draw, style)

    # Pass in a style to merge into the renderer's base style:
    renderer.draw_text(
        "Red!",
        (0, 0),
        style=Style(color=(255, 0, 0)),
    )

    renderer.draw_text(
        "More tracking!",
        (0, 60),
        style=Style(tracking=2),
    )

    renderer.draw_text(
        "Less tracking!",
        (0, 120),
        style=Style(tracking=-5),
    )

    renderer.draw_text(
        "Highlight!",
        (0, 180),
        style=Style(background=(100, 255, 255)),
    )

    renderer.draw_text(
        "Rounded highlight!",
        (0, 240),
        style=Style(background=(100, 255, 255), border_radius=20),
    )

    renderer.draw_text(
        "Border!",
        (0, 300),
        style=Style(border_color=(255, 0, 0), border_width=3),
    )

    renderer.draw_text(
        "Rounded border!",
        (0, 360),
        style=Style(
            border_color=(255, 0, 0), border_radius=20, border_width=3
        ),
    )

    image.save("./docs/images/example-1.png", "png")


def test_example_2() -> None:
    # Create an image region:
    image_region = make_image_region(300, 720)

    # Pass the image region's size into Image.new:
    image = Image.new("RGB", image_region.size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # We're going to build a region to render the first block of text into.
    #
    # We want this region to fill the entire width of the image, with a little
    # margin on every edge for comfort.
    #
    # So, let's start by creating a subregion with that margin by contracting:
    margin_region = image_region.expand(-10)

    # Now we'll create a subregion that starts in the top-left corner, fills
    # 100% of the available width and is 70 pixels tall:
    text_region = margin_region.region2(0, 0, Percent(100), 70).resolve()
    # Note that we need to .resolve() the region to resolve the relative values
    # to absolutes.

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
            renderer.draw_text(text, text_region, style=alignment)

            # Translate the region down by (text_region.height + 10) pixels for
            # the next block.
            text_region += (0, text_region.height + 10)

    image.save("./docs/images/example-2.png", "png")
