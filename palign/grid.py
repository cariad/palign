from nvalues import Volume
from PIL.ImageDraw import ImageDraw

from palign.types import Bounds, Color


class Grid:
    """
    Text grid.
    """

    def __init__(self, columns: int, rows: int) -> None:
        self._backgrounds = Volume[tuple[int, int], Color]()
        self._columns = columns
        self._rows = rows

    def _cell_bounds(
        self,
        column: int,
        row: int,
        grid_left: float,
        grid_top: float,
        grid_width: float,
        grid_height: float,
    ) -> Bounds:
        column_width = grid_width / self._columns
        row_height = grid_height / self._rows
        left = grid_left + (column * column_width)
        top = grid_top + (row * row_height)
        return (left, top, left + column_width, top + row_height)

    def _render_backgrounds(
        self,
        draw: ImageDraw,
        grid_left: float,
        grid_top: float,
        grid_width: float,
        grid_height: float,
    ) -> None:
        for bg in self._backgrounds:
            bounds = self._cell_bounds(
                bg.key[0],
                bg.key[1],
                grid_left,
                grid_top,
                grid_width,
                grid_height,
            )
            draw.rectangle(bounds, fill=bg.value)

    def background(self, column: int, row: int, color: Color) -> None:
        """
        Sets a cell's background colour.
        """

        self._backgrounds[column, row] = color

    def render(
        self,
        draw: ImageDraw,
        left: float,
        top: float,
        width: float,
        height: float,
    ) -> None:
        """
        Renders the grid.
        """

        self._render_backgrounds(draw, left, top, width, height)
