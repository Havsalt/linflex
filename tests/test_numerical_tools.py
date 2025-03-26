from linflex import clamp, sign, lerp


def test_clamp():
    assert clamp(7, 5, 10) == 7
    assert clamp(7, 2, 5) == 5
    assert clamp(7, 4, 6) == 6
    assert clamp(7, 9, 10) == 9
    # NOTE: This one should *also* give a lint error if `float` and `int` are mixed
    assert isinstance(clamp(7, 9.0, 10), float)


def test_sign():
    assert sign(0) == 0
    assert sign(-1) == -1
    assert sign(1) == 1
    assert sign(5) == 1
    assert sign(-5) == -1
    assert sign(3.5) == 1
    assert sign(-3.5) == -1


def test_lerp():
    assert lerp(0, 10, 0.50) == 5
    assert lerp(0, -10, 0.50) == -5
    assert lerp(0, 1, 0.50) == 0.5
    assert lerp(-10, -20, 0.50) == -15
    assert lerp(20, -20, 0.50) == 0
