from bounden import ResolvedVolume2
from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from palign import Alignment, Percent, Region, Style, Text, make_image_region


def test_demo_0() -> None:
    image = Image.new("RGB", (300, 300))
    draw = ImageDraw.Draw(image)

    style = Style(
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 42),
    )

    renderer = Text(draw, style)

    renderer.draw("Hello!", (0, 0))

    image.save("./docs/images/text-example-0.png", "png")


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

    renderer = Text(draw, style)

    renderer.draw("Hello!", region)

    image.save("./docs/images/text-example-1.png", "png")


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

    renderer = Text(draw, style)

    renderer.draw("Hello!", region)

    image.save("./docs/images/text-example-2.png", "png")


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

    renderer = Text(draw, style)

    renderer.draw("Hello!", region)

    image.save("./docs/images/text-example-3.png", "png")


def test_demo_4() -> None:
    image_region = make_image_region(300, 300)

    image = Image.new("RGB", image_region.size)
    draw = ImageDraw.Draw(image)

    style = Style(
        font=truetype("tests/font/ChelseaMarket-Regular.ttf", 42),
        horizontal=Alignment.Center,
        vertical=Alignment.Center,
    )

    renderer = Text(draw, style)

    world = Style(color=(255, 255, 0)).text("world")

    renderer.draw(
        ("Hello ", world, "!"),
        image_region,
    )

    image.save("./docs/images/text-example-4.png", "png")


def test_resolve__point() -> None:
    actual = Text.resolve((1, 2), ResolvedVolume2.new(3, 4))
    assert actual == Region.new(1, 2, 3, 4).resolve()


def test_resolve__region() -> None:
    region = Region.new(1, 2, 3, 4)
    actual = Text.resolve(region, ResolvedVolume2.new(0, 0))
    assert actual == Region.new(1, 2, 3, 4).resolve()


def test_resolve__resolved_region() -> None:
    region = Region.new(1, 2, 3, 4).resolve()
    actual = Text.resolve(region, ResolvedVolume2.new(0, 0))
    assert actual == Region.new(1, 2, 3, 4).resolve()
