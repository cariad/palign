from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from palign import (
    Bounds,
    Grid,
    Horizontal,
    Position,
    Style,
    Vertical,
    draw_text,
)


def test_demo(font_path: str) -> None:
    image_margin = 10
    grid_bounds = Bounds(350, image_margin, 400, 280)

    image_width = int(grid_bounds.right + image_margin)
    image_height = int(grid_bounds.bottom + image_margin)

    image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    large_font_size = 36
    large_font = truetype(font_path, large_font_size)
    small_font = truetype(font_path, 26)

    tracking_style = Style(color=(0, 0, 0), font=large_font)

    for index, tracking in enumerate([-5, -2, 0, 2, 5]):
        draw_text(
            f"tracking = {tracking}",
            draw,
            tracking_style + Style(tracking=tracking),
            Position(
                image_margin,
                (index * (large_font_size + 10)) + image_margin,
            ),
        )

    column_count = 3
    row_count = 3

    default_style = Style(
        color=(0, 0, 0),
        font=small_font,
    )

    grid = Grid(column_count, row_count, default_style=default_style)

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

    grid.render(draw, grid_bounds)

    image.save("demo.png", "png")
