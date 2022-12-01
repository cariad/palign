from pathlib import Path

from bounden import Percent, Vector2
from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from palign import Grid, Horizontal, Region, Style, Vertical, draw_text

image_dir = Path() / "docs" / "images"


def test_demo(font_path: str) -> None:
    image_bounds = Region.image(600, 400)

    image = Image.new("RGB", image_bounds.size, (255, 255, 255))
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
        image_bounds.expand(-40),
        default_style=default_style,
    )

    grid[0, 0].text = "Top\nLeft"
    grid[0, 0].style.horizontal = Horizontal.Left
    grid[0, 0].style.vertical = Vertical.Top

    grid[1, 0].text = "Top\nCenter"
    grid[1, 0].style.horizontal = Horizontal.Center
    grid[1, 0].style.vertical = Vertical.Top

    grid[2, 0].text = "Top\nRight"
    grid[2, 0].style.horizontal = Horizontal.Right
    grid[2, 0].style.vertical = Vertical.Top

    grid[0, 1].text = "Center\nLeft"
    grid[0, 1].style.horizontal = Horizontal.Left
    grid[0, 1].style.vertical = Vertical.Center

    grid[1, 1].text = "Center\nCenter"
    grid[1, 1].style.horizontal = Horizontal.Center
    grid[1, 1].style.vertical = Vertical.Center

    grid[2, 1].text = "Center\nRight"
    grid[2, 1].style.horizontal = Horizontal.Right
    grid[2, 1].style.vertical = Vertical.Center

    grid[0, 2].text = "Bottom\nLeft"
    grid[0, 2].style.horizontal = Horizontal.Left
    grid[0, 2].style.vertical = Vertical.Bottom

    grid[1, 2].text = "Bottom\nCenter"
    grid[1, 2].style.horizontal = Horizontal.Center
    grid[1, 2].style.vertical = Vertical.Bottom

    grid[2, 2].text = "Bottom\nRight"
    grid[2, 2].style.horizontal = Horizontal.Right
    grid[2, 2].style.vertical = Vertical.Bottom

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


def test_text(font_path: str) -> None:
    font_height = 21
    font = truetype(font_path, font_height)
    line_height = font_height * 3

    margin = 40

    image_region = Region.image(500, (line_height * 8) + margin)
    image = Image.new("RGB", image_region.size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    render_region = image_region.expand(-margin)

    text_region = render_region.pregion(0, 0, Percent(100), line_height)

    style = Style(color=(0, 0, 0), font=font, vertical=Vertical.Center)

    draw_text(
        "Hello! This is left aligned!",
        draw,
        style + Style(horizontal=Horizontal.Left),
        text_region,
    )

    text_region += Vector2(0, line_height)

    draw_text(
        "And this is right-aligned!",
        draw,
        style + Style(horizontal=Horizontal.Right),
        text_region,
    )

    text_region += Vector2(0, text_region.height)

    draw_text(
        "And this is centred!",
        draw,
        style + Style(horizontal=Horizontal.Center),
        text_region,
    )

    text_region += Vector2(0, text_region.height)

    draw_text(
        "We can increase the tracking...",
        draw,
        style + Style(horizontal=Horizontal.Center, tracking=2),
        text_region,
    )

    text_region += Vector2(0, text_region.height)

    draw_text(
        "...and naturally, decrease it too.",
        draw,
        style + Style(horizontal=Horizontal.Center, tracking=-2),
        text_region,
    )

    text_region += Vector2(0, text_region.height)

    draw_text(
        "Text can be coloured...",
        draw,
        style + Style(color=(255, 0, 0), horizontal=Horizontal.Center),
        text_region,
    )

    text_region += Vector2(0, text_region.height)

    draw_text(
        "...as can backgrounds",
        draw,
        style
        + Style(
            background=(0, 0, 0),
            color=(255, 255, 255),
            horizontal=Horizontal.Center,
        ),
        text_region,
    )

    text_region += Vector2(0, text_region.height)

    draw_text(
        "<3",
        draw,
        style + Style(horizontal=Horizontal.Center),
        text_region,
    )

    image.save(image_dir / "text.png", "png")
