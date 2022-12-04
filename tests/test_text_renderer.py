from bounden import ResolvedVolume2
from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from palign import (
    Alignment,
    Percent,
    Region,
    Style,
    TextRenderer,
    make_image_region,
)


def test_demo_0() -> None:
    image = Image.new("RGB", (300, 300))
    draw = ImageDraw.Draw(image)

    style = Style(
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 42),
    )

    renderer = TextRenderer(draw, style)

    renderer.draw_text("Hello!", (0, 0))

    image.save("./docs/images/text-renderer-example-0.png", "png")


def test_demo_1() -> None:
    image = Image.new("RGB", (300, 300))
    draw = ImageDraw.Draw(image)

    style = Style(
        border_color=(100, 100, 100),
        border_width=1,
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 42),
        horizontal=Alignment.Center,
        vertical=Alignment.Center,
    )

    region = Region.new(0, 0, 200, 200)

    renderer = TextRenderer(draw, style)

    renderer.draw_text("Hello!", region)

    image.save("./docs/images/text-renderer-example-1.png", "png")


def test_demo_2() -> None:
    image_region = make_image_region(300, 300)

    image = Image.new("RGB", image_region.size)
    draw = ImageDraw.Draw(image)

    style = Style(
        border_color=(100, 100, 100),
        border_width=1,
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 42),
        horizontal=Alignment.Center,
        vertical=Alignment.Center,
    )

    region = image_region.region2(Alignment.Far, Alignment.Far, 200, 200)

    renderer = TextRenderer(draw, style)

    renderer.draw_text("Hello!", region)

    image.save("./docs/images/text-renderer-example-2.png", "png")


def test_demo_3() -> None:
    image_region = make_image_region(300, 300)

    image = Image.new("RGB", image_region.size)
    draw = ImageDraw.Draw(image)

    style = Style(
        border_color=(100, 100, 100),
        border_width=1,
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 42),
        horizontal=Alignment.Center,
        vertical=Alignment.Center,
    )

    region = image_region.region2(
        Alignment.Center,
        Alignment.Center,
        Percent(50),
        Percent(50),
    )

    renderer = TextRenderer(draw, style)

    renderer.draw_text("Hello!", region)

    image.save("./docs/images/text-renderer-example-3.png", "png")


def test_resolve__point() -> None:
    actual = TextRenderer.resolve((1, 2), ResolvedVolume2.new(3, 4))
    assert actual == Region.new(1, 2, 3, 4).resolve()


def test_resolve__region() -> None:
    region = Region.new(1, 2, 3, 4)
    actual = TextRenderer.resolve(region, ResolvedVolume2.new(0, 0))
    assert actual == Region.new(1, 2, 3, 4).resolve()


def test_resolve__resolved_region() -> None:
    region = Region.new(1, 2, 3, 4).resolve()
    actual = TextRenderer.resolve(region, ResolvedVolume2.new(0, 0))
    assert actual == Region.new(1, 2, 3, 4).resolve()
