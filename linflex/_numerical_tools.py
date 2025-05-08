from __future__ import annotations

from typing import Literal

from ._annotations import Number


def lerp(
    start: int | float,
    stop: int | float,
    weight: float,
    /,
) -> float:
    """Lerps between `start` and `stop` with `weight` ranging from 0 to 1

    Args:
        start (int | float): starting number
        stop (int | float): target number
        weight (float): percentage to lerp

    Returns:
        float: result of the interpolation
    """
    return (1.0 - weight) * start + (weight * stop)


def sign(number: int | float, /) -> Literal[-1, 0, 1]:
    """Returns the sign of the number. The number 0 will return 0

    Args:
        number (int | float): number to get the sign of

    Returns:
        Literal[-1, 0, 1]: sign
    """
    if number > 0:
        return 1
    if number < 0:
        return -1
    return 0


def clamp(
    number: Number,
    smallest: Number,
    largest: Number,
    /,
) -> Number:
    """Returns the number clamped between smallest and largest (inclusive)

    Args:
        number (Number): number to clamp
        smallest (Number): lower bound
        largest (Number): upper bound

    Returns:
        Number: clamped number
    """
    return max(smallest, min(largest, number))


def move_toward(
    start: Number,
    stop: Number,
    /,
    change: Number,
) -> Number:
    """Moves toward target number

    Args:
        start (Number): starting number
        stop (Number): target number
        change (Number): step length when moving toward `stop`

    Returns:
        float: point after move
    """
    if abs(stop - start) <= change:
        return stop
    elif start < stop:
        return start + change
    else:
        return start - change
