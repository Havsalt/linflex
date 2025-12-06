# Documentation for `linflex`

## Table of Contents

* [linflex](#linflex)
  * [sign](#linflex.sign)
  * [clamp](#linflex.clamp)
  * [move\_toward](#linflex.move_toward)
  * [Vec2i](#linflex.Vec2i)
    * [from\_angle](#linflex.Vec2i.from_angle)
    * [\_\_init\_\_](#linflex.Vec2i.__init__)
    * [\_\_add\_\_](#linflex.Vec2i.__add__)
    * [\_\_iadd\_\_](#linflex.Vec2i.__iadd__)
    * [\_\_sub\_\_](#linflex.Vec2i.__sub__)
    * [\_\_isub\_\_](#linflex.Vec2i.__isub__)
    * [\_\_mul\_\_](#linflex.Vec2i.__mul__)
    * [\_\_imul\_\_](#linflex.Vec2i.__imul__)
    * [\_\_floordiv\_\_](#linflex.Vec2i.__floordiv__)
    * [\_\_ifloordiv\_\_](#linflex.Vec2i.__ifloordiv__)
    * [\_\_truediv\_\_](#linflex.Vec2i.__truediv__)
    * [\_\_itruediv\_\_](#linflex.Vec2i.__itruediv__)
    * [\_\_mod\_\_](#linflex.Vec2i.__mod__)
    * [\_\_imod\_\_](#linflex.Vec2i.__imod__)
  * [Vec3](#linflex.Vec3)
    * [ZERO](#linflex.Vec3.ZERO)
    * [ONE](#linflex.Vec3.ONE)
    * [INF](#linflex.Vec3.INF)
    * [LEFT](#linflex.Vec3.LEFT)
    * [RIGHT](#linflex.Vec3.RIGHT)
    * [UP](#linflex.Vec3.UP)
    * [DOWN](#linflex.Vec3.DOWN)
    * [FORWARD](#linflex.Vec3.FORWARD)
    * [BACK](#linflex.Vec3.BACK)
    * [from\_angles](#linflex.Vec3.from_angles)
    * [\_\_init\_\_](#linflex.Vec3.__init__)
    * [\_\_reduce\_\_](#linflex.Vec3.__reduce__)
    * [\_\_len\_\_](#linflex.Vec3.__len__)
    * [\_\_iter\_\_](#linflex.Vec3.__iter__)
    * [\_\_getitem\_\_](#linflex.Vec3.__getitem__)
    * [\_\_setitem\_\_](#linflex.Vec3.__setitem__)
    * [\_\_repr\_\_](#linflex.Vec3.__repr__)
    * [\_\_str\_\_](#linflex.Vec3.__str__)
    * [\_\_bool\_\_](#linflex.Vec3.__bool__)
    * [\_\_abs\_\_](#linflex.Vec3.__abs__)
    * [\_\_round\_\_](#linflex.Vec3.__round__)
    * [\_\_floor\_\_](#linflex.Vec3.__floor__)
    * [\_\_ceil\_\_](#linflex.Vec3.__ceil__)
    * [\_\_add\_\_](#linflex.Vec3.__add__)
    * [\_\_radd\_\_](#linflex.Vec3.__radd__)
    * [\_\_iadd\_\_](#linflex.Vec3.__iadd__)
    * [\_\_sub\_\_](#linflex.Vec3.__sub__)
    * [\_\_rsub\_\_](#linflex.Vec3.__rsub__)
    * [\_\_isub\_\_](#linflex.Vec3.__isub__)
    * [\_\_mul\_\_](#linflex.Vec3.__mul__)
    * [\_\_rmul\_\_](#linflex.Vec3.__rmul__)
    * [\_\_imul\_\_](#linflex.Vec3.__imul__)
    * [\_\_floordiv\_\_](#linflex.Vec3.__floordiv__)
    * [\_\_rfloordiv\_\_](#linflex.Vec3.__rfloordiv__)
    * [\_\_ifloordiv\_\_](#linflex.Vec3.__ifloordiv__)
    * [\_\_truediv\_\_](#linflex.Vec3.__truediv__)
    * [\_\_rtruediv\_\_](#linflex.Vec3.__rtruediv__)
    * [\_\_itruediv\_\_](#linflex.Vec3.__itruediv__)
    * [\_\_mod\_\_](#linflex.Vec3.__mod__)
    * [\_\_rmod\_\_](#linflex.Vec3.__rmod__)
    * [\_\_imod\_\_](#linflex.Vec3.__imod__)
    * [\_\_eq\_\_](#linflex.Vec3.__eq__)
    * [\_\_ne\_\_](#linflex.Vec3.__ne__)
    * [\_\_gt\_\_](#linflex.Vec3.__gt__)
    * [\_\_lt\_\_](#linflex.Vec3.__lt__)
    * [\_\_ge\_\_](#linflex.Vec3.__ge__)
    * [\_\_le\_\_](#linflex.Vec3.__le__)
    * [\_\_copy\_\_](#linflex.Vec3.__copy__)
    * [\_\_deepcopy\_\_](#linflex.Vec3.__deepcopy__)
    * [copy](#linflex.Vec3.copy)
    * [length](#linflex.Vec3.length)
    * [length\_squared](#linflex.Vec3.length_squared)
    * [normalized](#linflex.Vec3.normalized)
    * [lerp](#linflex.Vec3.lerp)
    * [sign](#linflex.Vec3.sign)
    * [clamp](#linflex.Vec3.clamp)
    * [move\_toward](#linflex.Vec3.move_toward)
    * [distance\_to](#linflex.Vec3.distance_to)
    * [distance\_squared\_to](#linflex.Vec3.distance_squared_to)
    * [direction\_to](#linflex.Vec3.direction_to)
    * [dot](#linflex.Vec3.dot)
    * [cross](#linflex.Vec3.cross)
    * [angles](#linflex.Vec3.angles)
    * [angles\_to](#linflex.Vec3.angles_to)
    * [rotated\_around\_x](#linflex.Vec3.rotated_around_x)
    * [rotated\_around\_y](#linflex.Vec3.rotated_around_y)
    * [rotated\_around\_z](#linflex.Vec3.rotated_around_z)
    * [rotated](#linflex.Vec3.rotated)
    * [rotated\_around](#linflex.Vec3.rotated_around)

<a id="linflex"></a>

# Module `linflex`

Linflex
=======

A linear algebra package written in Python

Includes
--------

- Functions:
- `lerp`
- `sign`
- `clamp`
- `move_toward`
- Classes:
- `Vec2`
- `Vec2i`
- `Vec3`
- Modules
- `typing`

<a id="linflex.sign"></a>

## `sign`

```python
def sign(number: int | float) -> Literal[-1, 0, 1]
```

Return the sign of the number.

The number `0` will return `0`.

**Arguments**:

- `number` _int | float_ - Number to get the sign of.
  

**Returns**:

  Literal[-1, 0, 1]: Sign.

<a id="linflex.clamp"></a>

## `clamp`

```python
def clamp(
    number: Number,
    smallest: Number,
    largest: Number,
) -> Number
```

Return the number clamped between `smallest` and `largest` (inclusive).

**Arguments**:

- `number` _Number_ - Number to clamp.
- `smallest` _Number_ - Lower bound.
- `largest` _Number_ - Upper bound.
  

**Returns**:

- `Number` - Clamped number.

<a id="linflex.move_toward"></a>

## `move_toward`

```python
def move_toward(
    start: Number,
    stop: Number,
    change: Number,
) -> Number
```

Move toward target number.

**Arguments**:

- `start` _Number_ - Starting number.
- `stop` _Number_ - Target number.
- `change` _Number_ - Step length when moving toward `stop`.
  

**Returns**:

- `float` - Point after move.

<a id="linflex.Vec2i"></a>

## Class `Vec2i`

```python
class Vec2i(Vec2)
```

`Vector2 integer` data structure.

Components: `x`, `y`, only type `int`.

Useful for storing whole numbers in 2D space.

<a id="linflex.Vec2i.from_angle"></a>

### `Vec2i.from_angle`

```python
@classmethod
def from_angle(angle: Radians) -> Self
```

Create a snapped direction vector of length `1` from given angle.

Snapping is done by taking the `sign` of each component.
Formulas used: `x = sign(cos(angle))` and `y = sign(sin(angle))`.

**Arguments**:

- `angle` _Radians_ - Angle in radians.
  

**Returns**:

- `Self` - Snapped direction vector of length `1`.

<a id="linflex.Vec2i.__init__"></a>

### `Vec2i.__init__`

```python
def __init__(
    x: int,
    y: int,
) -> None
```

Initialize integer vector.

**Arguments**:

- `x` _int_ - X component.
- `y` _int_ - Y component.

<a id="linflex.Vec2i.__add__"></a>

### `Vec2i.__add__`

```python
def __add__(other: Vec2i | Vec2) -> Vec2i | Vec2
```

Add two vectors.

**Arguments**:

- `other` _Vec2i | Vec2_ - Vector to add.
  

**Returns**:

  Vec2i | Vec2: Result of addition.

<a id="linflex.Vec2i.__iadd__"></a>

### `Vec2i.__iadd__`

```python
def __iadd__(other: Vec2i) -> Vec2i
```

In-place add two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to add.
  

**Returns**:

- `Vec2i` - Result of addition.

<a id="linflex.Vec2i.__sub__"></a>

### `Vec2i.__sub__`

```python
def __sub__(other: Vec2i | Vec2) -> Vec2i | Vec2
```

Subtract two vectors.

**Arguments**:

- `other` _Vec2i | Vec2_ - Vector to subtract.
  

**Returns**:

  Vec2i | Vec2: Result of subtraction.

<a id="linflex.Vec2i.__isub__"></a>

### `Vec2i.__isub__`

```python
def __isub__(other: Vec2i) -> Vec2i
```

In-place subtract two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to subtract.
  

**Returns**:

- `Vec2i` - Result of subtraction.

<a id="linflex.Vec2i.__mul__"></a>

### `Vec2i.__mul__`

```python
def __mul__(other: Vec2i | Vec2 | int | float) -> Vec2i | Vec2
```

Multiply vector by another vector or scalar.

**Arguments**:

- `other` _Vec2i | Vec2 | int | float_ - Value to multiply.
  

**Returns**:

  Vec2i | Vec2: Result of multiplication.

<a id="linflex.Vec2i.__imul__"></a>

### `Vec2i.__imul__`

```python
def __imul__(other: Vec2i) -> Vec2i
```

In-place multiply two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to multiply.
  

**Returns**:

- `Vec2i` - Result of multiplication.

<a id="linflex.Vec2i.__floordiv__"></a>

### `Vec2i.__floordiv__`

```python
def __floordiv__(other: Vec2i | Vec2 | int | float) -> Vec2i | Vec2
```

Floor divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec2i | Vec2 | int | float_ - Value to divide.
  

**Returns**:

  Vec2i | Vec2: Result of floor division.

<a id="linflex.Vec2i.__ifloordiv__"></a>

### `Vec2i.__ifloordiv__`

```python
def __ifloordiv__(other: Vec2i) -> Vec2i
```

In-place floor divide two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to divide.
  

**Returns**:

- `Vec2i` - Result of floor division.

<a id="linflex.Vec2i.__truediv__"></a>

### `Vec2i.__truediv__`

```python
def __truediv__(other: Vec2i | Vec2 | int | float) -> Vec2i | Vec2
```

Divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec2i | Vec2 | int | float_ - Value to divide.
  

**Returns**:

  Vec2i | Vec2: Result of division.

<a id="linflex.Vec2i.__itruediv__"></a>

### `Vec2i.__itruediv__`

```python
def __itruediv__(other: Vec2i) -> Vec2i
```

In-place divide two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to divide.
  

**Returns**:

- `Vec2i` - Result of division.

<a id="linflex.Vec2i.__mod__"></a>

### `Vec2i.__mod__`

```python
def __mod__(other: Vec2i | Vec2 | int | float) -> Vec2i | Vec2
```

Modulo vector by another vector or scalar.

**Arguments**:

- `other` _Vec2i | Vec2 | int | float_ - Value to modulo.
  

**Returns**:

  Vec2i | Vec2: Result of modulo.

<a id="linflex.Vec2i.__imod__"></a>

### `Vec2i.__imod__`

```python
def __imod__(other: Vec2i) -> Vec2i
```

In-place modulo two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to modulo.
  

**Returns**:

- `Vec2i` - Result of modulo.

<a id="linflex.Vec3"></a>

## Class `Vec3`

```python
class Vec3()
```

`Vector3` data structure.

Components: `x`, `y`, `z`.

Useful for storing position or direction in 3D space.

<a id="linflex.Vec3.ZERO"></a>

### `Vec3.ZERO`

```python
@class_constant
def ZERO(cls: type[Self]) -> Self
```

Vector with all components set to `0`.

<a id="linflex.Vec3.ONE"></a>

### `Vec3.ONE`

```python
@class_constant
def ONE(cls: type[Self]) -> Self
```

Vector with all components set to `1`.

<a id="linflex.Vec3.INF"></a>

### `Vec3.INF`

```python
@class_constant
def INF(cls: type[Self]) -> Self
```

Vector with all components set to `math.inf`.

<a id="linflex.Vec3.LEFT"></a>

### `Vec3.LEFT`

```python
@class_constant
def LEFT(cls: type[Self]) -> Self
```

Left unit vector.

Represents both local direction left, and the global direction west.

<a id="linflex.Vec3.RIGHT"></a>

### `Vec3.RIGHT`

```python
@class_constant
def RIGHT(cls: type[Self]) -> Self
```

Right unit vector.

Represents both local direction right, and global direction east.

<a id="linflex.Vec3.UP"></a>

### `Vec3.UP`

```python
@class_constant
def UP(cls: type[Self]) -> Self
```

Up unit vector.

Represents up direction.

<a id="linflex.Vec3.DOWN"></a>

### `Vec3.DOWN`

```python
@class_constant
def DOWN(cls: type[Self]) -> Self
```

Down unit vector.

Represents down direction.

<a id="linflex.Vec3.FORWARD"></a>

### `Vec3.FORWARD`

```python
@class_constant
def FORWARD(cls: type[Self]) -> Self
```

Forward unit vector.

Represents both local direction forward, and global direction north.

<a id="linflex.Vec3.BACK"></a>

### `Vec3.BACK`

```python
@class_constant
def BACK(cls: type[Self]) -> Self
```

Back/backward unit vector.

Represents local direction back/backwards, and global direction south.

<a id="linflex.Vec3.from_angles"></a>

### `Vec3.from_angles`

```python
@classmethod
def from_angles(angles: Vec3) -> Self
```

Create a direction vector of length `1` from given angles.

**Arguments**:

- `angles` _Vec3_ - Vector representing rotation around each axis (`x`, `y`, `z`).
  

**Returns**:

- `Self` - Direction vector of length `1`.

<a id="linflex.Vec3.__init__"></a>

### `Vec3.__init__`

```python
def __init__(
    x: float,
    y: float,
    z: float,
) -> None
```

Initialize vector.

**Arguments**:

- `x` _float_ - X component.
- `y` _float_ - Y component.
- `z` _float_ - Z component.

<a id="linflex.Vec3.__reduce__"></a>

### `Vec3.__reduce__`

```python
def __reduce__() -> tuple[type[Self], tuple[float, float]]
```

Helper for pickling support.

<a id="linflex.Vec3.__len__"></a>

### `Vec3.__len__`

```python
def __len__() -> Literal[3]
```

Return the number of components in the vector.

**Returns**:

- `int` - Number of components (always `3`).

<a id="linflex.Vec3.__iter__"></a>

### `Vec3.__iter__`

```python
def __iter__() -> Iterator[float]
```

Iterate over the components of the vector.

**Returns**:

- `Iterator[float]` - Iterator over `x`, `y`, and `z`.

<a id="linflex.Vec3.__getitem__"></a>

### `Vec3.__getitem__`

```python
def __getitem__(axis_index: Literal[0, 1, 2]) -> float
```

Get a component by axis index.

**Arguments**:

- `axis_index` _int_ - Axis index, `0` for `x`, `1` for `y` and `2` for `z`.
  

**Returns**:

- `float` - Value of the component.
  

**Raises**:

- `ValueError` - Invalid axis index.

<a id="linflex.Vec3.__setitem__"></a>

### `Vec3.__setitem__`

```python
def __setitem__(
    axis_index: Literal[0, 1],
    value: float,
) -> None
```

Set a component by axis index.

**Arguments**:

- `axis_index` _int_ - Axis index, `0` for `x`, `1` for `y` and `2` for `z`.
- `value` _float_ - New axis value.
  

**Raises**:

- `ValueError` - Invalid axis index.

<a id="linflex.Vec3.__repr__"></a>

### `Vec3.__repr__`

```python
def __repr__() -> str
```

Create representation.

**Returns**:

- `str` - Representation containing the `x`, `y`, and `z` components.

<a id="linflex.Vec3.__str__"></a>

### `Vec3.__str__`

```python
def __str__() -> str
```

Create string representation.

**Returns**:

- `str` - Representation containing the `x`, `y`, and `z` components.

<a id="linflex.Vec3.__bool__"></a>

### `Vec3.__bool__`

```python
def __bool__() -> bool
```

Return whether `x`, `y`, or `z` is not zero.

**Returns**:

- `bool` - Truthiness.

<a id="linflex.Vec3.__abs__"></a>

### `Vec3.__abs__`

```python
def __abs__() -> Self
```

Return a vector with absolute values of each component.

**Returns**:

- `Self` - Vector with absolute values.

<a id="linflex.Vec3.__round__"></a>

### `Vec3.__round__`

```python
def __round__(ndigits: int = 0) -> Self
```

Return a vector with each component rounded.

**Arguments**:

- `ndigits` _int_ - Number of digits to round to.
  

**Returns**:

- `Self` - Rounded vector.

<a id="linflex.Vec3.__floor__"></a>

### `Vec3.__floor__`

```python
def __floor__() -> Self
```

Return a vector with each component floored.

**Returns**:

- `Self` - Floored vector.

<a id="linflex.Vec3.__ceil__"></a>

### `Vec3.__ceil__`

```python
def __ceil__() -> Self
```

Return a vector with each component ceiled.

**Returns**:

- `Self` - Ceiled vector.

<a id="linflex.Vec3.__add__"></a>

### `Vec3.__add__`

```python
def __add__(other: Vec3) -> Vec3
```

Add two vectors.

**Arguments**:

- `other` _Vec3_ - Vector to add.
  

**Returns**:

- `Vec3` - Result of addition.

<a id="linflex.Vec3.__radd__"></a>

### `Vec3.__radd__`

```python
def __radd__(other: Vec3 | int | float) -> Vec3
```

Right-hand addition.

Adds this vector to another vector or scalar, when this vector is on the right side of the `+` operator.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to add.
  

**Returns**:

- `Vec3` - Result of addition.

<a id="linflex.Vec3.__iadd__"></a>

### `Vec3.__iadd__`

```python
def __iadd__(other: Vec3) -> Vec3
```

In-place add two vectors.

**Arguments**:

- `other` _Vec3_ - Vector to add.
  

**Returns**:

- `Vec3` - Result of addition.

<a id="linflex.Vec3.__sub__"></a>

### `Vec3.__sub__`

```python
def __sub__(other: Vec3) -> Vec3
```

Subtract two vectors.

**Arguments**:

- `other` _Vec3_ - Vector to subtract.
  

**Returns**:

- `Vec3` - Result of subtraction.

<a id="linflex.Vec3.__rsub__"></a>

### `Vec3.__rsub__`

```python
def __rsub__(other: Vec3 | int | float) -> Vec3
```

Right-hand subtraction.

Subtracts this vector from another vector or scalar, when this vector is on the right side of the `-` operator.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to subtract from.
  

**Returns**:

- `Vec3` - Result of subtraction.

<a id="linflex.Vec3.__isub__"></a>

### `Vec3.__isub__`

```python
def __isub__(other: Vec3) -> Vec3
```

In-place subtract two vectors.

**Arguments**:

- `other` _Vec3_ - Vector to subtract.
  

**Returns**:

- `Vec3` - Result of subtraction.

<a id="linflex.Vec3.__mul__"></a>

### `Vec3.__mul__`

```python
def __mul__(other: Vec3 | int | float) -> Vec3
```

Multiply vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to multiply.
  

**Returns**:

- `Vec3` - Result of multiplication.

<a id="linflex.Vec3.__rmul__"></a>

### `Vec3.__rmul__`

```python
def __rmul__(other: Vec3 | int | float) -> Vec3
```

Right-hand multiplication.

Multiplies another vector or scalar by this vector, when this vector is on the right side of the `*` operator.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to multiply.
  

**Returns**:

- `Vec3` - Result of multiplication.

<a id="linflex.Vec3.__imul__"></a>

### `Vec3.__imul__`

```python
def __imul__(other: Vec3 | int | float) -> Vec3
```

In-place multiply vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to multiply.
  

**Returns**:

- `Vec3` - Result of multiplication.

<a id="linflex.Vec3.__floordiv__"></a>

### `Vec3.__floordiv__`

```python
def __floordiv__(other: Vec3 | int | float) -> Vec3
```

Floor divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of floor division.

<a id="linflex.Vec3.__rfloordiv__"></a>

### `Vec3.__rfloordiv__`

```python
def __rfloordiv__(other: Vec3 | int | float) -> Vec3
```

Right-hand floor division.

Floor divides another vector or scalar by this vector, when this vector is on the right side of the `//` operator.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of floor division.

<a id="linflex.Vec3.__ifloordiv__"></a>

### `Vec3.__ifloordiv__`

```python
def __ifloordiv__(other: Vec3 | int | float) -> Vec3
```

In-place floor divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of floor division.

<a id="linflex.Vec3.__truediv__"></a>

### `Vec3.__truediv__`

```python
def __truediv__(other: Vec3 | int | float) -> Vec3
```

Divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of division.

<a id="linflex.Vec3.__rtruediv__"></a>

### `Vec3.__rtruediv__`

```python
def __rtruediv__(other: Vec3 | int | float) -> Vec3
```

Right-hand true division.

Divides another vector or scalar by this vector, when this vector is on the right side of the `/` operator.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of division.

<a id="linflex.Vec3.__itruediv__"></a>

### `Vec3.__itruediv__`

```python
def __itruediv__(other: Vec3 | int | float) -> Vec3
```

In-place divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of division.

<a id="linflex.Vec3.__mod__"></a>

### `Vec3.__mod__`

```python
def __mod__(other: Vec3 | int | float) -> Vec3
```

Modulo vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to modulo.
  

**Returns**:

- `Vec3` - Result of modulo.

<a id="linflex.Vec3.__rmod__"></a>

### `Vec3.__rmod__`

```python
def __rmod__(other: Vec3 | int | float) -> Vec3
```

Right-hand modulo.

Computes the modulo of another vector or scalar by this vector, when this vector is on the right side of the `%` operator.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to modulo.
  

**Returns**:

- `Vec3` - Result of modulo.

<a id="linflex.Vec3.__imod__"></a>

### `Vec3.__imod__`

```python
def __imod__(other: Vec3 | int | float) -> Vec3
```

In-place modulo vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to modulo.
  

**Returns**:

- `Vec3` - Result of modulo.

<a id="linflex.Vec3.__eq__"></a>

### `Vec3.__eq__`

```python
def __eq__(other: Vec3) -> bool
```

Check if two vectors are equal.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if equal, False otherwise.

<a id="linflex.Vec3.__ne__"></a>

### `Vec3.__ne__`

```python
def __ne__(other: Vec3) -> bool
```

Check if two vectors are not equal.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if not equal, False otherwise.

<a id="linflex.Vec3.__gt__"></a>

### `Vec3.__gt__`

```python
def __gt__(other: Vec3) -> bool
```

Check if this vector is greater than another.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if greater, False otherwise.

<a id="linflex.Vec3.__lt__"></a>

### `Vec3.__lt__`

```python
def __lt__(other: Vec3) -> bool
```

Check if this vector is less than another.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if less, False otherwise.

<a id="linflex.Vec3.__ge__"></a>

### `Vec3.__ge__`

```python
def __ge__(other: Vec3) -> bool
```

Check if this vector is greater than or equal to another.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if greater or equal, False otherwise.

<a id="linflex.Vec3.__le__"></a>

### `Vec3.__le__`

```python
def __le__(other: Vec3) -> bool
```

Check if this vector is less than or equal to another.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if less or equal, False otherwise.

<a id="linflex.Vec3.__copy__"></a>

### `Vec3.__copy__`

```python
def __copy__() -> Self
```

Return a copy of the vector.

**Returns**:

- `Self` - A new copy.

<a id="linflex.Vec3.__deepcopy__"></a>

### `Vec3.__deepcopy__`

```python
def __deepcopy__(_memo: dict[int, Any]) -> Self
```

Return a deep copy of the vector.

**Arguments**:

- `_memo` _dict_ - Memoization dictionary.
  

**Returns**:

- `Self` - A new deep copy.

<a id="linflex.Vec3.copy"></a>

### `Vec3.copy`

```python
def copy() -> Self
```

Return a vector copy.

**Returns**:

- `Self` - A new copy.

<a id="linflex.Vec3.length"></a>

### `Vec3.length`

```python
def length() -> float
```

Return the length of the vector.

**Returns**:

- `float` - Length.

<a id="linflex.Vec3.length_squared"></a>

### `Vec3.length_squared`

```python
def length_squared() -> float
```

Return the length of the vector squared.

**Returns**:

- `float` - Length squared.

<a id="linflex.Vec3.normalized"></a>

### `Vec3.normalized`

```python
def normalized() -> Vec3
```

Return a vector with length of `1`, still with same direction.

**Returns**:

- `Vec3` - Normalized vector.

<a id="linflex.Vec3.lerp"></a>

### `Vec3.lerp`

```python
def lerp(
    target: Vec3,
    weight: float,
) -> Vec3
```

Lerp towards vector `target` with `weight` ranging from `0` to `1`.

**Arguments**:

- `target` _Vec3_ - Target to lerp towards.
- `weight` _float_ - Percentage to lerp.
  

**Returns**:

- `Vec3` - Vector after performing interpolation.

<a id="linflex.Vec3.sign"></a>

### `Vec3.sign`

```python
def sign() -> Vec3
```

Return a Vec3 with each component being the sign of the vector.

**Returns**:

- `Vec3` - Vector with signed components.

<a id="linflex.Vec3.clamp"></a>

### `Vec3.clamp`

```python
def clamp(
    smallest: Vec3,
    largest: Vec3,
) -> Vec3
```

Return a new clamped vector.

**Arguments**:

- `smallest` _Vec3_ - Lower bound for `x`, `y`, and `z`.
- `largest` _Vec3_ - Upper bound for `x`, `y`, and `z`.
  

**Returns**:

- `Vec3` - Vector clamped.

<a id="linflex.Vec3.move_toward"></a>

### `Vec3.move_toward`

```python
def move_toward(
    stop: Vec3,
    change: int | float,
) -> Vec3
```

Move toward a vector, from a vector, with given change.

**Arguments**:

- `stop` _Vec3_ - Target vector.
- `change` _int | float_ - Max distance to move.
  

**Returns**:

- `Vec3` - New vector moved.

<a id="linflex.Vec3.distance_to"></a>

### `Vec3.distance_to`

```python
def distance_to(target: Vec3) -> float
```

Return the relative distance to the target point.

**Arguments**:

- `target` _Vec3_ - Target point.
  

**Returns**:

- `float` - Distance.

<a id="linflex.Vec3.distance_squared_to"></a>

### `Vec3.distance_squared_to`

```python
def distance_squared_to(target: Vec3) -> float
```

Return the relative distance to the target point, squared.

**Arguments**:

- `target` _Vec3_ - Target point.
  

**Returns**:

- `float` - Distance squared.

<a id="linflex.Vec3.direction_to"></a>

### `Vec3.direction_to`

```python
def direction_to(target: Vec3) -> Vec3
```

Return the direction to the target point.

**Arguments**:

- `target` _Vec3_ - Target point.
  

**Returns**:

- `Vec3` - Direction.

<a id="linflex.Vec3.dot"></a>

### `Vec3.dot`

```python
def dot(other: Vec3) -> float
```

Return the dot product between two 3D vectors.

**Arguments**:

- `other` _Vec3_ - Other vector.
  

**Returns**:

- `float` - Dot product.

<a id="linflex.Vec3.cross"></a>

### `Vec3.cross`

```python
def cross(other: Vec3) -> Vec3
```

Return the cross product between two 3D vectors.

**Arguments**:

- `other` _Vec3_ - Other vector.
  

**Returns**:

- `Vec3` - Cross product.

<a id="linflex.Vec3.angles"></a>

### `Vec3.angles`

```python
def angles() -> Vec3
```

Return the angles (pitch, yaw, roll) of the vector.

**Returns**:

- `Vec3` - Angles in radians.

<a id="linflex.Vec3.angles_to"></a>

### `Vec3.angles_to`

```python
def angles_to(target: Vec3) -> Vec3
```

Return the angles to the target point.

**Arguments**:

- `target` _Vec3_ - Target point.
  

**Returns**:

- `Vec3` - Angles in radians.

<a id="linflex.Vec3.rotated_around_x"></a>

### `Vec3.rotated_around_x`

```python
def rotated_around_x(angle: float) -> Vec3
```

Return a vector rotated around the `X` axis by `angle` radians.

**Arguments**:

- `angle` _float_ - Radians to rotate with.
  

**Returns**:

- `Vec3` - Rotated vector.

<a id="linflex.Vec3.rotated_around_y"></a>

### `Vec3.rotated_around_y`

```python
def rotated_around_y(angle: float) -> Vec3
```

Return a vector rotated around the `Y` axis by `angle` radians.

**Arguments**:

- `angle` _float_ - Radians to rotate with.
  

**Returns**:

- `Vec3` - Rotated vector.

<a id="linflex.Vec3.rotated_around_z"></a>

### `Vec3.rotated_around_z`

```python
def rotated_around_z(angle: float) -> Vec3
```

Return a vector rotated around the `Z` axis by `angle` radians.

**Arguments**:

- `angle` _float_ - Radians to rotate with.
  

**Returns**:

- `Vec3` - Rotated vector.

<a id="linflex.Vec3.rotated"></a>

### `Vec3.rotated`

```python
def rotated(angles: Vec3) -> Vec3
```

Return a vector rotated by the given angles around each axis.

**Arguments**:

- `angles` _Vec3_ - Angles to rotate around each axis.
  

**Returns**:

- `Vec3` - Rotated vector.

<a id="linflex.Vec3.rotated_around"></a>

### `Vec3.rotated_around`

```python
def rotated_around(
    target: Vec3,
    angles: Vec3,
) -> Vec3
```

Return a vector rotated by the given angles around each axis, around a target point.

**Arguments**:

- `target` _Vec3_ - Point to rotate around.
- `angles` _Vec3_ - Angles to rotate around each axis.
  

**Returns**:

- `Vec3` - Rotated vector around the target point.

