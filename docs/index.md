# Palign

**Palign** is a Python package that helps to render and align text in [Pillow](https://python-pillow.org/).

## Examples

`draw_text` draws text of a given `Style` at a set of coordinates:

```python
from pathlib import Path

from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from palign import Style, draw_text

image = Image.new("RGB", (150, 28))
draw = ImageDraw.Draw(image)

style = Style(font=truetype("tests/font/ChelseaMarket-Regular.ttf", 21))

draw_text("Hello world!", draw, style, (0, 0))

image.save(Path() / "docs" / "images" / "example-0.png", "png")
```

<figure markdown>
  ![Image title](images/example-0.png)
</figure>

`Style` can also describe colour and tracking:

```python
from pathlib import Path

from PIL import Image, ImageDraw
from PIL.ImageFont import truetype
from palign import Style, draw_text

image = Image.new("RGB", (260, 120), (255, 255, 255))
draw = ImageDraw.Draw(image)

style = Style(
    color=(0, 0, 0),
    font=truetype("tests/font/ChelseaMarket-Regular.ttf", 21),
)

draw_text("Red!", draw, style + Style(color=(255, 0, 0)), (0, 0))
draw_text("Increased tracking!", draw, style + Style(tracking=2), (0, 40))
draw_text("Decreased tracking!", draw, style + Style(tracking=-2), (0, 80))

image.save(Path() / "docs" / "images" / "example-1.png", "png")
```

<figure markdown>
  ![Image title](images/example-1.png)
</figure>

If you specify a region to render within (rather than just a point to render _at_) then text can aligned and the background can be coloured:

```python
from pathlib import Path

from PIL import Image, ImageDraw
from PIL.ImageFont import truetype

from bounden import Percent
from palign import Horizontal, Region, Style, Vertical, draw_text

image_region = Region.image(300, 720)
image = Image.new("RGB", image_region.size, (255, 255, 255))
draw = ImageDraw.Draw(image)

# Build a region to render the first block of text into.
#
# Start by contracting the image boundary to create a margin, then create a
# subregion that starts in the top corner, takes all available width (using
# Percent from the Bounden package) and is 70 pixels tall.
text_region = image_region.expand(-10).pregion(0, 0, Percent(100), 70)

style = Style(
    border_color=(200, 200, 200),
    border_radius=3,
    border_width=1,
    color=(0, 0, 0),
    font=truetype("tests/font/ChelseaMarket-Regular.ttf", 21),
)

for vertical in Vertical:
    for horizontal in Horizontal:
        alignment = Style(horizontal=horizontal, vertical=vertical)
        text = f"{vertical.name} {horizontal.name}"
        draw_text(text, draw, style + alignment, text_region)

        # Translate the region down by (text_region.height + 10) pixels for
        # the next block.
        text_region += (0, text_region.height + 10)

image.save(Path() / "docs" / "images" / "example-2.png", "png")
```

<figure markdown>
  ![Image title](images/example-2.png)
</figure>

For detailed usage information, see the [`Style` class](./style.md).

## Installation

**Palign** requires Python 3.9 or later.

```console
pip install palign
```

## Support

Please raise bugs, request new features and ask questions at [github.com/cariad/palign/issues](https://github.com/cariad/palign/issues).

## Contributions

See [CONTRIBUTING.md](https://github.com/cariad/palign/blob/main/CONTRIBUTING.md) for contribution guidelines.

## The Project

**Palign** is &copy; 2022 Cariad Eccleston and released under the [MIT License](https://github.com/cariad/palign/blob/main/LICENSE) at [github.com/cariad/palign](https://github.com/cariad/palign).

## The Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance backend and infrastructure engineer in the United Kingdom. You can find me at [cariad.earth](https://cariad.earth), [github.com/cariad](https://github.com/cariad), [linkedin.com/in/cariad](https://linkedin.com/in/cariad) and on Mastodon at [@cariad@tech.lgbt](https://tech.lgbt/@cariad).
