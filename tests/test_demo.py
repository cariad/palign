from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from palign import Grid, Style, draw_text
from palign.enums import Horizontal, Vertical


def test_demo(font_path: str) -> None:
    image_width = 1240
    image_height = 350

    image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    large_font = truetype(font_path, 42)
    small_font = truetype(font_path, 26)

    for index, tracking in enumerate([-5, -2, 0, 2, 5]):
        style = Style(color=(0, 0, 0), font=large_font, tracking=tracking)
        draw_text(
            f"tracking = {tracking}",
            draw,
            style,
            (10, index * 50, -1, -1),
        )

    column_count = 3
    row_count = 3

    grid = Grid(column_count, row_count)

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
            grid[x, y].style.color = (0, 0, 0)
            grid[x, y].style.font = small_font

    grid.render(draw, 400, 10, 800, 300)

    image.save("demo.png", "png")
