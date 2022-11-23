from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont

from palign import Grid, Render


def test_demo(font: FreeTypeFont) -> None:
    image_width = 1450
    image_height = 850

    image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    render = Render(draw, color=(0, 0, 0), font=font)

    for index, tracking in enumerate([-5, -2, 0, 2, 5]):
        render.tracking = tracking
        render.text(f"tracking = {tracking}", 10, index * 50)

    column_count = 3
    row_count = 3

    grid = Grid(column_count, row_count)

    def color_bit(column: int) -> int:
        return 155 + int((100 / column_count) * column)

    for column in range(column_count):
        for row in range(row_count):
            red = color_bit(column) if row == 0 else 255
            green = color_bit(column) if row == 1 else 255
            blue = color_bit(column) if row == 2 else 255
            grid.background(column, row, (red, green, blue))

    grid.render(draw, 400, 10, 1000, 800)

    image.save("demo.png", "png")
