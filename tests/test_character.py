from palign import Character


def test_pillow_coords() -> None:
    assert Character(character="", x=7, y=9).pillow_coords(3, 3) == (10, 12)
