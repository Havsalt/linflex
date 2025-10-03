from math import isclose, pi as PI

from linflex import Vec2i


DIAGONAL_LENGTH = Vec2i(1, 1).length()  # ~1.414


def test_constants():
    assert Vec2i.ZERO == Vec2i(0, 0)
    assert Vec2i.ONE == Vec2i(1, 1)
    # TODO: Implement `INF` subtype for `int`
    # assert Vec2i.INF == Vec2i(INF, INF)
    assert Vec2i.LEFT == Vec2i(-1, 0)
    assert Vec2i.RIGHT == Vec2i(1, 0)
    assert Vec2i.UP == Vec2i(0, -1)
    assert Vec2i.DOWN == Vec2i(0, 1)
    # Constants should generate a new unique instance each time to avoid mutation
    assert Vec2i.ZERO is not Vec2i.ZERO
    assert Vec2i.ONE is not Vec2i.ONE
    assert Vec2i.INF is not Vec2i.INF
    assert Vec2i.LEFT is not Vec2i.LEFT
    assert Vec2i.RIGHT is not Vec2i.RIGHT
    assert Vec2i.UP is not Vec2i.UP
    assert Vec2i.DOWN is not Vec2i.DOWN


def test_from_angle():
    v1 = Vec2i.from_angle(PI)
    assert isclose(v1.length(), 1)
    assert v1.x == -1 and v1.y == 0
    v2 = Vec2i.from_angle(PI / 2)
    assert isclose(v2.length(), 1)
    assert v2.x == 0 and v2.y == 1
    # Angles that lays *in* a quadrant
    v3 = Vec2i.from_angle(PI / 8)
    assert isclose(v3.length(), DIAGONAL_LENGTH)
    assert v3.x == 1 and v3.y == 1
    v4 = Vec2i.from_angle(-PI / 8)
    assert isclose(v4.length(), DIAGONAL_LENGTH)
    assert v4.x == 1 and v4.y == -1
