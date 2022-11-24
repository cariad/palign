from typing import Optional

from nvalues import Volume
from PIL.ImageDraw import ImageDraw

from palign.cell_style import CellStyle
from palign.types import Bounds


class Grid:
    """
    Text grid.
    """

    def __init__(
        self,
        columns: int,
        rows: int,
        cell_style: Optional[CellStyle] = None,
    ) -> None:
        self._columns = columns
        self._rows = rows

        cell_style = cell_style or CellStyle()
        self._styles = Volume[tuple[int, int], CellStyle](cell_style)

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

    def delete_style(self, column: int, row: int) -> None:
        """
        Deletes a cell's style.
        """

        del self._styles[column, row]

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

        for x in range(self._columns):
            for y in range(self._rows):
                bounds = self._cell_bounds(
                    x,
                    y,
                    left,
                    top,
                    width,
                    height,
                )
                cell_style = self._styles[x, y]
                cell_style.render(draw, bounds)

    def set_style(self, column: int, row: int, style: CellStyle) -> None:
        """
        Sets a cell's style.
        """

        self._styles[column, row] = style
