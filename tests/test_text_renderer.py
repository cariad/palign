from bounden import ResolvedVolume2

from palign import Region, TextRenderer


def test_resolve__point() -> None:
    actual = TextRenderer.resolve((1, 2), ResolvedVolume2.new(3, 4))
    assert actual == Region.new(1, 2, 3, 4).resolve()


def test_resolve__region() -> None:
    region = Region.new(1, 2, 3, 4)
    actual = TextRenderer.resolve(region, ResolvedVolume2.new(0, 0))
    assert actual == Region.new(1, 2, 3, 4).resolve()


def test_resolve__resolved_region() -> None:
    region = Region.new(1, 2, 3, 4).resolve()
    actual = TextRenderer.resolve(region, ResolvedVolume2.new(0, 0))
    assert actual == Region.new(1, 2, 3, 4).resolve()
