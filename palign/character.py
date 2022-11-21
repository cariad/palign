from dataclasses import dataclass
from typing import Tuple


@dataclass
class Character:
    """
    Describes the render coordinates of a character.
    """

    character: str
    """
    Character.
    """

    x: int  # pylint: disable=invalid-name
    """
    X pixel coordinate.
    """

    y: int  # pylint: disable=invalid-name
    """
    Y pixel coordinate.
    """

    def pillow_coords(self, x_offset: int, y_offset: int) -> Tuple[int, int]:
        """
        Converts the character's coordinates to Pillow coordinates.

        Args:
            x_offset: X pixel offset.
            y_offset: Y pixel offset.

        Returns:
            (x, y) render coordinates.
        """

        return (self.x + x_offset, self.y + y_offset)
