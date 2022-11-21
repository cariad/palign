# pylint: disable=missing-function-docstring

from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont

from palign import Render


def test_demo(font: FreeTypeFont) -> None:
    image = Image.new("RGB", (400, 300), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    render = Render(draw, color=(0, 0, 0), font=font)

    for index, tracking in enumerate([-5, -2, 0, 2, 5]):
        render.tracking = tracking
        render.text(f"tracking = {tracking}", 10, index * 50)

    image.save("demo.png", "png")
