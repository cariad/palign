from dataclasses import dataclass


@dataclass
class Character:
    """
    Describes the render coordinates of a character.
    """

    character: str
    """
    Character.
    """

    x: float
    """
    X pixel coordinate.
    """

    y: float
    """
    Y pixel coordinate.
    """

    def pillow_coords(
        self,
        offset: tuple[float, float],
    ) -> tuple[float, float]:
        """
        Converts the character's coordinates to Pillow coordinates.

        Returns:
            (x, y) render coordinates.
        """

        return (self.x + offset[0], self.y + offset[1])
