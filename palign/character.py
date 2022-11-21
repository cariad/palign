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

    x: int  # pylint: disable=invalid-name
    """
    X pixel coordinate.
    """

    y: int  # pylint: disable=invalid-name
    """
    Y pixel coordinate.
    """
