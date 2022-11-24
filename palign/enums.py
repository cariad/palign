from enum import IntEnum, unique


@unique
class Horizontal(IntEnum):
    Left = -1
    Center = 0
    Right = +1


@unique
class Vertical(IntEnum):
    Top = -1
    Center = 0
    Bottom = +1
