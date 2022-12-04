# Style class

The `Style` class describes the style of text to render.

```python
from palign import Style

style = Style(
    background=...,
    border_color=...,
    border_radius=...,
    border_width=...,
    color=...,
    font=...,
    horizontal=...,
    tracking=...,
    vertical=...,
)
```

## Style properties

`background` sets the background [colour](#colour).

`border_color` sets the border [colour](#colour).

!!! warning

    Borders will be painted only if both `border_color` and `border_width` have values.

`border_radius` sets the border radius. Corners will be square by default and rounded if a radius is set.

!!! warning

    Borders will be painted only if both `border_color` and `border_width` have values.

`border_width` sets the border width.

!!! warning

    Borders will be painted only if both `border_color` and `border_width` have values.

`color` sets the text colour.

`font` sets text font.

`horizontal` sets the horizontal alignment. `Alignment.Near` implies _left_, `Alignment.Center` will centre the text and `Alignment.Far` implies _right_.

!!! warning

    Text will be aligned only if the text is rendered within a region and not just a point.

`tracking` sets the spacing between characters.

`vertical` sets the vertical alignment. `Alignment.Near` implies _top_, `Alignment.Center` will centre the text and `Alignment.Far` implies _bottom_.

!!! warning

    Text will be aligned only if the text is rendered within a region and not just a point.

## Merging styles

Styles can be merged via addition. The style on the right always takes precedence.

```python
a = Style(
    border_width=2,
    color=(0, 0, 0),
)

b = Style(
    color=(255, 255, 255),
    tracking=5,
)

c = a + b
```

In the example above, `c` has:

- `border_width` = 2
- `color` = `(255, 255, 255)`
- `tracking` = 5

## Colour

Colours in Palign are described via either:

- `(red, green, blue)`
- `(red, green, blue, alpha)`

Values run from 0 to 255.

For example:

- `(0, 0, 0)` is black
- `(255, 255, 255)` is white
- `(255, 0, 0)` is red
- `(0, 255, 0)` is green
- `(0, 0, 255)` is blue
- `(0, 0, 0, 0)` is transparent
- `(255, 0, 255, 127)` is 50% opaque magenta
