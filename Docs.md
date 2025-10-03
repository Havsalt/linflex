# Documentation for `linflex`

## Table of Contents

* [linflex](#linflex)
* [linflex.\_annotations](#linflex._annotations)
* [linflex.\_class\_constant](#linflex._class_constant)
* [linflex.\_numerical\_tools](#linflex._numerical_tools)
  * [lerp](#linflex._numerical_tools.lerp)
  * [sign](#linflex._numerical_tools.sign)
  * [clamp](#linflex._numerical_tools.clamp)
  * [move\_toward](#linflex._numerical_tools.move_toward)
* [linflex.\_vec2](#linflex._vec2)
  * [Vec2](#linflex._vec2.Vec2)
    * [ZERO](#linflex._vec2.Vec2.ZERO)
    * [ONE](#linflex._vec2.Vec2.ONE)
    * [INF](#linflex._vec2.Vec2.INF)
    * [LEFT](#linflex._vec2.Vec2.LEFT)
    * [RIGHT](#linflex._vec2.Vec2.RIGHT)
    * [UP](#linflex._vec2.Vec2.UP)
    * [DOWN](#linflex._vec2.Vec2.DOWN)
    * [from\_angle](#linflex._vec2.Vec2.from_angle)
    * [\_\_init\_\_](#linflex._vec2.Vec2.__init__)
    * [\_\_reduce\_\_](#linflex._vec2.Vec2.__reduce__)
    * [\_\_len\_\_](#linflex._vec2.Vec2.__len__)
    * [\_\_iter\_\_](#linflex._vec2.Vec2.__iter__)
    * [\_\_getitem\_\_](#linflex._vec2.Vec2.__getitem__)
    * [\_\_abs\_\_](#linflex._vec2.Vec2.__abs__)
    * [\_\_round\_\_](#linflex._vec2.Vec2.__round__)
    * [\_\_floor\_\_](#linflex._vec2.Vec2.__floor__)
    * [\_\_ceil\_\_](#linflex._vec2.Vec2.__ceil__)
    * [\_\_neg\_\_](#linflex._vec2.Vec2.__neg__)
    * [\_\_add\_\_](#linflex._vec2.Vec2.__add__)
    * [\_\_radd\_\_](#linflex._vec2.Vec2.__radd__)
    * [\_\_iadd\_\_](#linflex._vec2.Vec2.__iadd__)
    * [\_\_sub\_\_](#linflex._vec2.Vec2.__sub__)
    * [\_\_rsub\_\_](#linflex._vec2.Vec2.__rsub__)
    * [\_\_isub\_\_](#linflex._vec2.Vec2.__isub__)
    * [\_\_mul\_\_](#linflex._vec2.Vec2.__mul__)
    * [\_\_rmul\_\_](#linflex._vec2.Vec2.__rmul__)
    * [\_\_imul\_\_](#linflex._vec2.Vec2.__imul__)
    * [\_\_floordiv\_\_](#linflex._vec2.Vec2.__floordiv__)
    * [\_\_rfloordiv\_\_](#linflex._vec2.Vec2.__rfloordiv__)
    * [\_\_ifloordiv\_\_](#linflex._vec2.Vec2.__ifloordiv__)
    * [\_\_truediv\_\_](#linflex._vec2.Vec2.__truediv__)
    * [\_\_rtruediv\_\_](#linflex._vec2.Vec2.__rtruediv__)
    * [\_\_itruediv\_\_](#linflex._vec2.Vec2.__itruediv__)
    * [\_\_mod\_\_](#linflex._vec2.Vec2.__mod__)
    * [\_\_rmod\_\_](#linflex._vec2.Vec2.__rmod__)
    * [\_\_imod\_\_](#linflex._vec2.Vec2.__imod__)
    * [\_\_eq\_\_](#linflex._vec2.Vec2.__eq__)
    * [\_\_ne\_\_](#linflex._vec2.Vec2.__ne__)
    * [\_\_gt\_\_](#linflex._vec2.Vec2.__gt__)
    * [\_\_lt\_\_](#linflex._vec2.Vec2.__lt__)
    * [\_\_ge\_\_](#linflex._vec2.Vec2.__ge__)
    * [\_\_le\_\_](#linflex._vec2.Vec2.__le__)
    * [\_\_copy\_\_](#linflex._vec2.Vec2.__copy__)
    * [\_\_deepcopy\_\_](#linflex._vec2.Vec2.__deepcopy__)
    * [copy](#linflex._vec2.Vec2.copy)
    * [length](#linflex._vec2.Vec2.length)
    * [length\_squared](#linflex._vec2.Vec2.length_squared)
    * [distance\_to](#linflex._vec2.Vec2.distance_to)
    * [distance\_squared\_to](#linflex._vec2.Vec2.distance_squared_to)
    * [normalized](#linflex._vec2.Vec2.normalized)
    * [dot](#linflex._vec2.Vec2.dot)
    * [cross](#linflex._vec2.Vec2.cross)
    * [direction\_to](#linflex._vec2.Vec2.direction_to)
    * [angle](#linflex._vec2.Vec2.angle)
    * [angle\_to](#linflex._vec2.Vec2.angle_to)
    * [lerp](#linflex._vec2.Vec2.lerp)
    * [sign](#linflex._vec2.Vec2.sign)
    * [clamp](#linflex._vec2.Vec2.clamp)
    * [move\_toward](#linflex._vec2.Vec2.move_toward)
    * [rotated](#linflex._vec2.Vec2.rotated)
    * [rotated\_around](#linflex._vec2.Vec2.rotated_around)
* [linflex.\_vec2i](#linflex._vec2i)
  * [Vec2i](#linflex._vec2i.Vec2i)
    * [from\_angle](#linflex._vec2i.Vec2i.from_angle)
    * [\_\_init\_\_](#linflex._vec2i.Vec2i.__init__)
    * [\_\_add\_\_](#linflex._vec2i.Vec2i.__add__)
    * [\_\_iadd\_\_](#linflex._vec2i.Vec2i.__iadd__)
    * [\_\_sub\_\_](#linflex._vec2i.Vec2i.__sub__)
    * [\_\_isub\_\_](#linflex._vec2i.Vec2i.__isub__)
    * [\_\_mul\_\_](#linflex._vec2i.Vec2i.__mul__)
    * [\_\_imul\_\_](#linflex._vec2i.Vec2i.__imul__)
    * [\_\_floordiv\_\_](#linflex._vec2i.Vec2i.__floordiv__)
    * [\_\_ifloordiv\_\_](#linflex._vec2i.Vec2i.__ifloordiv__)
    * [\_\_truediv\_\_](#linflex._vec2i.Vec2i.__truediv__)
    * [\_\_itruediv\_\_](#linflex._vec2i.Vec2i.__itruediv__)
    * [\_\_mod\_\_](#linflex._vec2i.Vec2i.__mod__)
    * [\_\_imod\_\_](#linflex._vec2i.Vec2i.__imod__)
* [linflex.\_vec3](#linflex._vec3)
  * [Vec3](#linflex._vec3.Vec3)
    * [ZERO](#linflex._vec3.Vec3.ZERO)
    * [ONE](#linflex._vec3.Vec3.ONE)
    * [INF](#linflex._vec3.Vec3.INF)
    * [LEFT](#linflex._vec3.Vec3.LEFT)
    * [RIGHT](#linflex._vec3.Vec3.RIGHT)
    * [UP](#linflex._vec3.Vec3.UP)
    * [DOWN](#linflex._vec3.Vec3.DOWN)
    * [FORWARD](#linflex._vec3.Vec3.FORWARD)
    * [BACK](#linflex._vec3.Vec3.BACK)
    * [from\_angles](#linflex._vec3.Vec3.from_angles)
    * [\_\_init\_\_](#linflex._vec3.Vec3.__init__)
    * [\_\_reduce\_\_](#linflex._vec3.Vec3.__reduce__)
    * [\_\_len\_\_](#linflex._vec3.Vec3.__len__)
    * [\_\_iter\_\_](#linflex._vec3.Vec3.__iter__)
    * [\_\_getitem\_\_](#linflex._vec3.Vec3.__getitem__)
    * [\_\_repr\_\_](#linflex._vec3.Vec3.__repr__)
    * [\_\_str\_\_](#linflex._vec3.Vec3.__str__)
    * [\_\_bool\_\_](#linflex._vec3.Vec3.__bool__)
    * [\_\_abs\_\_](#linflex._vec3.Vec3.__abs__)
    * [\_\_round\_\_](#linflex._vec3.Vec3.__round__)
    * [\_\_floor\_\_](#linflex._vec3.Vec3.__floor__)
    * [\_\_ceil\_\_](#linflex._vec3.Vec3.__ceil__)
    * [\_\_add\_\_](#linflex._vec3.Vec3.__add__)
    * [\_\_radd\_\_](#linflex._vec3.Vec3.__radd__)
    * [\_\_iadd\_\_](#linflex._vec3.Vec3.__iadd__)
    * [\_\_sub\_\_](#linflex._vec3.Vec3.__sub__)
    * [\_\_rsub\_\_](#linflex._vec3.Vec3.__rsub__)
    * [\_\_isub\_\_](#linflex._vec3.Vec3.__isub__)
    * [\_\_mul\_\_](#linflex._vec3.Vec3.__mul__)
    * [\_\_rmul\_\_](#linflex._vec3.Vec3.__rmul__)
    * [\_\_imul\_\_](#linflex._vec3.Vec3.__imul__)
    * [\_\_floordiv\_\_](#linflex._vec3.Vec3.__floordiv__)
    * [\_\_rfloordiv\_\_](#linflex._vec3.Vec3.__rfloordiv__)
    * [\_\_ifloordiv\_\_](#linflex._vec3.Vec3.__ifloordiv__)
    * [\_\_truediv\_\_](#linflex._vec3.Vec3.__truediv__)
    * [\_\_rtruediv\_\_](#linflex._vec3.Vec3.__rtruediv__)
    * [\_\_itruediv\_\_](#linflex._vec3.Vec3.__itruediv__)
    * [\_\_mod\_\_](#linflex._vec3.Vec3.__mod__)
    * [\_\_rmod\_\_](#linflex._vec3.Vec3.__rmod__)
    * [\_\_imod\_\_](#linflex._vec3.Vec3.__imod__)
    * [\_\_eq\_\_](#linflex._vec3.Vec3.__eq__)
    * [\_\_ne\_\_](#linflex._vec3.Vec3.__ne__)
    * [\_\_gt\_\_](#linflex._vec3.Vec3.__gt__)
    * [\_\_lt\_\_](#linflex._vec3.Vec3.__lt__)
    * [\_\_ge\_\_](#linflex._vec3.Vec3.__ge__)
    * [\_\_le\_\_](#linflex._vec3.Vec3.__le__)
    * [\_\_copy\_\_](#linflex._vec3.Vec3.__copy__)
    * [\_\_deepcopy\_\_](#linflex._vec3.Vec3.__deepcopy__)
    * [copy](#linflex._vec3.Vec3.copy)
    * [length](#linflex._vec3.Vec3.length)
    * [length\_squared](#linflex._vec3.Vec3.length_squared)
    * [normalized](#linflex._vec3.Vec3.normalized)
    * [lerp](#linflex._vec3.Vec3.lerp)
    * [sign](#linflex._vec3.Vec3.sign)
    * [clamp](#linflex._vec3.Vec3.clamp)
    * [move\_toward](#linflex._vec3.Vec3.move_toward)
    * [distance\_to](#linflex._vec3.Vec3.distance_to)
    * [distance\_squared\_to](#linflex._vec3.Vec3.distance_squared_to)
    * [direction\_to](#linflex._vec3.Vec3.direction_to)
    * [dot](#linflex._vec3.Vec3.dot)
    * [cross](#linflex._vec3.Vec3.cross)
    * [angles](#linflex._vec3.Vec3.angles)
    * [angles\_to](#linflex._vec3.Vec3.angles_to)
    * [rotated\_around\_x](#linflex._vec3.Vec3.rotated_around_x)
    * [rotated\_around\_y](#linflex._vec3.Vec3.rotated_around_y)
    * [rotated\_around\_z](#linflex._vec3.Vec3.rotated_around_z)
    * [rotated](#linflex._vec3.Vec3.rotated)
    * [rotated\_around](#linflex._vec3.Vec3.rotated_around)

<a id="linflex"></a>

# Module `linflex`

Linflex
=======

A linear algebra package written in Python

Includes
--------

- `lerp`
- `sign`
- `clamp`
- `move_toward`
- `Vec2`
- `Vec2i`
- `Vec3`

<a id="linflex._annotations"></a>

# Module `linflex._annotations`

<a id="linflex._class_constant"></a>

# Module `linflex._class_constant`

<a id="linflex._numerical_tools"></a>

# Module `linflex._numerical_tools`

<a id="linflex._numerical_tools.lerp"></a>

## `lerp`

```python
def lerp(
    start: int | float,
    stop: int | float,
    weight: float,
) -> float
```

Lerp between `start` and `stop` with `weight` ranging from `0` to `1`.

**Arguments**:

- `start` _int | float_ - Starting number.
- `stop` _int | float_ - Target number.
- `weight` _float_ - Percentage to lerp.
  

**Returns**:

- `float` - Result of the interpolation.

<a id="linflex._numerical_tools.sign"></a>

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

<a id="linflex._numerical_tools.clamp"></a>

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

<a id="linflex._numerical_tools.move_toward"></a>

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

<a id="linflex._vec2"></a>

# Module `linflex._vec2`

<a id="linflex._vec2.Vec2"></a>

## Class `Vec2`

```python
class Vec2()
```

`Vector2` data structure.

Components: `x`, `y`.

Useful for storing position or direction in 2D space.

<a id="linflex._vec2.Vec2.ZERO"></a>

### `Vec2.ZERO`

```python
@class_constant
def ZERO(cls: type[Self]) -> Self
```

Vector with all components set to `0`.

<a id="linflex._vec2.Vec2.ONE"></a>

### `Vec2.ONE`

```python
@class_constant
def ONE(cls: type[Self]) -> Self
```

Vector with all components set to `1`.

<a id="linflex._vec2.Vec2.INF"></a>

### `Vec2.INF`

```python
@class_constant
def INF(cls: type[Self]) -> Self
```

Vector with all components set to `math.inf`.

<a id="linflex._vec2.Vec2.LEFT"></a>

### `Vec2.LEFT`

```python
@class_constant
def LEFT(cls: type[Self]) -> Self
```

Left unit vector.

Represents the `left direction`.

<a id="linflex._vec2.Vec2.RIGHT"></a>

### `Vec2.RIGHT`

```python
@class_constant
def RIGHT(cls: type[Self]) -> Self
```

Right unit vector.

Represents the `right direction`.

<a id="linflex._vec2.Vec2.UP"></a>

### `Vec2.UP`

```python
@class_constant
def UP(cls: type[Self]) -> Self
```

Up unit vector.

Represents the `up direction`.

`NOTE`
Since `positive Y` points `downward` in this 2D coordinate system,
the `up direction` is represented by `-Y`.

<a id="linflex._vec2.Vec2.DOWN"></a>

### `Vec2.DOWN`

```python
@class_constant
def DOWN(cls: type[Self]) -> Self
```

Down unit vector.

Represents the `down direction`.

`NOTE`
Since `positive Y` points `downward` in this 2D coordinate system,
the `down direction` is represented by `+Y`.

<a id="linflex._vec2.Vec2.from_angle"></a>

### `Vec2.from_angle`

```python
@classmethod
def from_angle(angle: Radians) -> Self
```

Create a direction vector of length 1 from given angle.

**Arguments**:

- `angle` _Radians_ - Angle in radians.
  

**Returns**:

- `Self` - Direction vector of length 1.

<a id="linflex._vec2.Vec2.__init__"></a>

### `Vec2.__init__`

```python
def __init__(
    x: float,
    y: float,
) -> None
```

Initialize vector.

**Arguments**:

- `x` _float_ - X component.
- `y` _float_ - Y component.

<a id="linflex._vec2.Vec2.__reduce__"></a>

### `Vec2.__reduce__`

```python
def __reduce__() -> tuple[type[Self], tuple[float, float]]
```

Helper for pickling support.

<a id="linflex._vec2.Vec2.__len__"></a>

### `Vec2.__len__`

```python
def __len__() -> Literal[2]
```

Return the number of components in the vector.

**Returns**:

- `int` - Number of components (always ´2´).

<a id="linflex._vec2.Vec2.__iter__"></a>

### `Vec2.__iter__`

```python
def __iter__() -> Iterator[float]
```

Iterate over the components of the vector.

**Returns**:

- `Iterator[float]` - Iterator over ´x´ and ´y´.

<a id="linflex._vec2.Vec2.__getitem__"></a>

### `Vec2.__getitem__`

```python
def __getitem__(item: Literal[0, 1]) -> float
```

Get a component by index.

**Arguments**:

- `item` _int_ - Index (´0´ for ´x´, ´1´ for ´y´).
  

**Returns**:

- `float` - Value of the component.

<a id="linflex._vec2.Vec2.__abs__"></a>

### `Vec2.__abs__`

```python
def __abs__() -> Self
```

Return a vector with absolute values of each component.

**Returns**:

- `Self` - Vector with absolute values.

<a id="linflex._vec2.Vec2.__round__"></a>

### `Vec2.__round__`

```python
def __round__(ndigits: int = 0) -> Self
```

Return a vector with each component rounded.

**Arguments**:

- `ndigits` _int_ - Number of digits to round to.
  

**Returns**:

- `Self` - Rounded vector.

<a id="linflex._vec2.Vec2.__floor__"></a>

### `Vec2.__floor__`

```python
def __floor__() -> Self
```

Return a vector with each component floored.

**Returns**:

- `Self` - Floored vector.

<a id="linflex._vec2.Vec2.__ceil__"></a>

### `Vec2.__ceil__`

```python
def __ceil__() -> Self
```

Return a vector with each component ceiled.

**Returns**:

- `Self` - Ceiled vector.

<a id="linflex._vec2.Vec2.__neg__"></a>

### `Vec2.__neg__`

```python
def __neg__() -> Vec2
```

Return a vector with each component negated.

**Returns**:

- `Vec2` - Negated vector.

<a id="linflex._vec2.Vec2.__add__"></a>

### `Vec2.__add__`

```python
def __add__(other: Vec2) -> Vec2
```

Add two vectors.

**Arguments**:

- `other` _Vec2_ - Vector to add.
  

**Returns**:

- `Vec2` - Result of addition.

<a id="linflex._vec2.Vec2.__radd__"></a>

### `Vec2.__radd__`

```python
def __radd__(other: Vec2 | int | float) -> Vec2
```

Right-hand addition.

Adds this vector to another vector or scalar, when this vector is on the right side of the `+` operator.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to add.
  

**Returns**:

- `Vec2` - Result of addition.

<a id="linflex._vec2.Vec2.__iadd__"></a>

### `Vec2.__iadd__`

```python
def __iadd__(other: Vec2) -> Vec2
```

In-place add two vectors.

**Arguments**:

- `other` _Vec2_ - Vector to add.
  

**Returns**:

- `Vec2` - Result of addition.

<a id="linflex._vec2.Vec2.__sub__"></a>

### `Vec2.__sub__`

```python
def __sub__(other: Vec2) -> Vec2
```

Subtract two vectors.

**Arguments**:

- `other` _Vec2_ - Vector to subtract.
  

**Returns**:

- `Vec2` - Result of subtraction.

<a id="linflex._vec2.Vec2.__rsub__"></a>

### `Vec2.__rsub__`

```python
def __rsub__(other: Vec2 | int | float) -> Vec2
```

Right-hand subtraction.

Subtracts this vector from another vector or scalar, when this vector is on the right side of the `-` operator.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to subtract from.
  

**Returns**:

- `Vec2` - Result of subtraction.

<a id="linflex._vec2.Vec2.__isub__"></a>

### `Vec2.__isub__`

```python
def __isub__(other: Vec2) -> Vec2
```

In-place subtract two vectors.

**Arguments**:

- `other` _Vec2_ - Vector to subtract.
  

**Returns**:

- `Vec2` - Result of subtraction.

<a id="linflex._vec2.Vec2.__mul__"></a>

### `Vec2.__mul__`

```python
def __mul__(other: Vec2 | int | float) -> Vec2
```

Multiply vector by another vector or scalar.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to multiply.
  

**Returns**:

- `Vec2` - Result of multiplication.

<a id="linflex._vec2.Vec2.__rmul__"></a>

### `Vec2.__rmul__`

```python
def __rmul__(other: Vec2 | int | float) -> Vec2
```

Right-hand multiplication.

Multiplies another vector or scalar by this vector, when this vector is on the right side of the `*` operator.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to multiply.
  

**Returns**:

- `Vec2` - Result of multiplication.

<a id="linflex._vec2.Vec2.__imul__"></a>

### `Vec2.__imul__`

```python
def __imul__(other: Vec2 | int | float) -> Vec2
```

In-place multiply vector by another vector or scalar.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to multiply.
  

**Returns**:

- `Vec2` - Result of multiplication.

<a id="linflex._vec2.Vec2.__floordiv__"></a>

### `Vec2.__floordiv__`

```python
def __floordiv__(other: Vec2 | int | float) -> Vec2
```

Floor divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to divide.
  

**Returns**:

- `Vec2` - Result of floor division.

<a id="linflex._vec2.Vec2.__rfloordiv__"></a>

### `Vec2.__rfloordiv__`

```python
def __rfloordiv__(other: Vec2 | int | float) -> Vec2
```

Right-hand floor division.

Floor divides another vector or scalar by this vector, when this vector is on the right side of the `//` operator.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to divide.
  

**Returns**:

- `Vec2` - Result of floor division.

<a id="linflex._vec2.Vec2.__ifloordiv__"></a>

### `Vec2.__ifloordiv__`

```python
def __ifloordiv__(other: Vec2 | int | float) -> Vec2
```

In-place floor divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to divide.
  

**Returns**:

- `Vec2` - Result of floor division.

<a id="linflex._vec2.Vec2.__truediv__"></a>

### `Vec2.__truediv__`

```python
def __truediv__(other: Vec2 | int | float) -> Vec2
```

Divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to divide.
  

**Returns**:

- `Vec2` - Result of division.

<a id="linflex._vec2.Vec2.__rtruediv__"></a>

### `Vec2.__rtruediv__`

```python
def __rtruediv__(other: Vec2 | int | float) -> Vec2
```

Right-hand true division.

Divides another vector or scalar by this vector, when this vector is on the right side of the `/` operator.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to divide.
  

**Returns**:

- `Vec2` - Result of division.

<a id="linflex._vec2.Vec2.__itruediv__"></a>

### `Vec2.__itruediv__`

```python
def __itruediv__(other: Vec2 | int | float) -> Vec2
```

In-place divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to divide.
  

**Returns**:

- `Vec2` - Result of division.

<a id="linflex._vec2.Vec2.__mod__"></a>

### `Vec2.__mod__`

```python
def __mod__(other: Vec2 | int | float) -> Vec2
```

Modulo vector by another vector or scalar.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to modulo.
  

**Returns**:

- `Vec2` - Result of modulo.

<a id="linflex._vec2.Vec2.__rmod__"></a>

### `Vec2.__rmod__`

```python
def __rmod__(other: Vec2 | int | float) -> Vec2
```

Right-hand modulo.

Computes the modulo of another vector or scalar by this vector, when this vector is on the right side of the `%` operator.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to modulo.
  

**Returns**:

- `Vec2` - Result of modulo.

<a id="linflex._vec2.Vec2.__imod__"></a>

### `Vec2.__imod__`

```python
def __imod__(other: Vec2 | int | float) -> Vec2
```

In-place modulo vector by another vector or scalar.

**Arguments**:

- `other` _Vec2 | int | float_ - Value to modulo.
  

**Returns**:

- `Vec2` - Result of modulo.

<a id="linflex._vec2.Vec2.__eq__"></a>

### `Vec2.__eq__`

```python
def __eq__(other: Vec2) -> bool
```

Check if two vectors are equal.

**Arguments**:

- `other` _Vec2_ - Vector to compare.
  

**Returns**:

- `bool` - True if equal, False otherwise.

<a id="linflex._vec2.Vec2.__ne__"></a>

### `Vec2.__ne__`

```python
def __ne__(other: Vec2) -> bool
```

Check if two vectors are not equal.

**Arguments**:

- `other` _Vec2_ - Vector to compare.
  

**Returns**:

- `bool` - True if not equal, False otherwise.

<a id="linflex._vec2.Vec2.__gt__"></a>

### `Vec2.__gt__`

```python
def __gt__(other: Vec2) -> bool
```

Check if this vector is greater than another.

**Arguments**:

- `other` _Vec2_ - Vector to compare.
  

**Returns**:

- `bool` - True if greater, False otherwise.

<a id="linflex._vec2.Vec2.__lt__"></a>

### `Vec2.__lt__`

```python
def __lt__(other: Vec2) -> bool
```

Check if this vector is less than another.

**Arguments**:

- `other` _Vec2_ - Vector to compare.
  

**Returns**:

- `bool` - True if less, False otherwise.

<a id="linflex._vec2.Vec2.__ge__"></a>

### `Vec2.__ge__`

```python
def __ge__(other: Vec2) -> bool
```

Check if this vector is greater than or equal to another.

**Arguments**:

- `other` _Vec2_ - Vector to compare.
  

**Returns**:

- `bool` - True if greater or equal, False otherwise.

<a id="linflex._vec2.Vec2.__le__"></a>

### `Vec2.__le__`

```python
def __le__(other: Vec2) -> bool
```

Check if this vector is less than or equal to another.

**Arguments**:

- `other` _Vec2_ - Vector to compare.
  

**Returns**:

- `bool` - True if less or equal, False otherwise.

<a id="linflex._vec2.Vec2.__copy__"></a>

### `Vec2.__copy__`

```python
def __copy__() -> Self
```

Return a copy of the vector.

**Returns**:

- `Self` - A new copy.

<a id="linflex._vec2.Vec2.__deepcopy__"></a>

### `Vec2.__deepcopy__`

```python
def __deepcopy__(_memo: dict[int, Any]) -> Self
```

Return a deep copy of the vector.

**Arguments**:

- `_memo` _dict_ - Memoization dictionary.
  

**Returns**:

- `Self` - A new deep copy.

<a id="linflex._vec2.Vec2.copy"></a>

### `Vec2.copy`

```python
def copy() -> Self
```

Return a vector copy.

**Returns**:

- `Self` - A new copy.

<a id="linflex._vec2.Vec2.length"></a>

### `Vec2.length`

```python
def length() -> float
```

Return the length of the vector.

**Returns**:

- `float` - Length.

<a id="linflex._vec2.Vec2.length_squared"></a>

### `Vec2.length_squared`

```python
def length_squared() -> float
```

Return the length of the vector squared.

**Returns**:

- `float` - Length squared.

<a id="linflex._vec2.Vec2.distance_to"></a>

### `Vec2.distance_to`

```python
def distance_to(other: Vec2) -> float
```

Return the relative distance to the other point.

**Arguments**:

- `other` _Vec2_ - Other point.
  

**Returns**:

- `float` - Distance.

<a id="linflex._vec2.Vec2.distance_squared_to"></a>

### `Vec2.distance_squared_to`

```python
def distance_squared_to(other: Vec2) -> float
```

Return the relative distance to the other point, squared.

**Arguments**:

- `other` _Vec2_ - Other point.
  

**Returns**:

- `float` - Distance squared.

<a id="linflex._vec2.Vec2.normalized"></a>

### `Vec2.normalized`

```python
def normalized() -> Vec2
```

Return a vector with length of 1, still with same direction.

**Returns**:

- `Vec2` - Normalized vector.

<a id="linflex._vec2.Vec2.dot"></a>

### `Vec2.dot`

```python
def dot(other: Vec2) -> float
```

Return the dot product between two 2D vectors.

**Arguments**:

- `other` _Vec2_ - Other vector.
  

**Returns**:

- `float` - Dot product.

<a id="linflex._vec2.Vec2.cross"></a>

### `Vec2.cross`

```python
def cross(other: Vec2) -> float
```

Cross product interpreted in 2D space, like defined in the `Godot Game Engine`.

**Arguments**:

- `other` _Vec2_ - Other vector.
  

**Returns**:

- `float` - Cross product.

<a id="linflex._vec2.Vec2.direction_to"></a>

### `Vec2.direction_to`

```python
def direction_to(other: Vec2) -> Vec2
```

Return the direction to the other point.

**Arguments**:

- `other` _Vec2_ - Other point.
  

**Returns**:

- `Vec2` - Direction.

<a id="linflex._vec2.Vec2.angle"></a>

### `Vec2.angle`

```python
def angle() -> float
```

Return the angle (measured in radians), using `atan2`.

**Returns**:

- `float` - Angle given in radians.

<a id="linflex._vec2.Vec2.angle_to"></a>

### `Vec2.angle_to`

```python
def angle_to(other: Vec2) -> float
```

Return the angle (measured in radians) to the other point.

**Arguments**:

- `other` _Vec2_ - Other point.
  

**Returns**:

- `float` - Angle given in radians.

<a id="linflex._vec2.Vec2.lerp"></a>

### `Vec2.lerp`

```python
def lerp(
    target: Vec2,
    weight: float,
) -> Vec2
```

Lerp towards vector `target` with `weight` ranging from 0 to 1.

**Arguments**:

- `target` _Vec2_ - Target to lerp towards.
- `weight` _float_ - Percentage to lerp.
  

**Returns**:

- `Vec2` - Vector after performing interpolation.

<a id="linflex._vec2.Vec2.sign"></a>

### `Vec2.sign`

```python
def sign() -> Vec2
```

Return a Vec2 with each component being the sign of the vector.

**Returns**:

- `Vec2` - Vector with signed components.

<a id="linflex._vec2.Vec2.clamp"></a>

### `Vec2.clamp`

```python
def clamp(
    smallest: Vec2,
    largest: Vec2,
) -> Vec2
```

Return a new clamped vector.

**Arguments**:

- `smallest` _Vec2_ - Lower bound for x and y.
- `largest` _Vec2_ - Upper bound for x and y.
  

**Returns**:

- `Vec2` - Vector clamped.

<a id="linflex._vec2.Vec2.move_toward"></a>

### `Vec2.move_toward`

```python
def move_toward(
    stop: Vec2,
    change: int | float,
) -> Vec2
```

Move toward a vector, from a vector, with given change.

**Arguments**:

- `stop` _Vec2_ - Target vector.
- `change` _int | float_ - Max distance to move.
  

**Returns**:

- `Vec2` - New vector moved.

<a id="linflex._vec2.Vec2.rotated"></a>

### `Vec2.rotated`

```python
def rotated(angle: float) -> Vec2
```

Return a vector rotated clockwise by `angle` given in radians.

**Arguments**:

- `angle` _float_ - Radians to rotate with.
  

**Returns**:

- `Vec2` - Rotated vector.

<a id="linflex._vec2.Vec2.rotated_around"></a>

### `Vec2.rotated_around`

```python
def rotated_around(
    angle: float,
    point: Vec2,
) -> Vec2
```

Return a vector rotated by `angle` given in radians, around `point`.

**Arguments**:

- `angle` _float_ - Radians to rotate with.
- `point` _Vec2_ - Point to rotate around.
  

**Returns**:

- `Vec2` - Vector rotated around `point`.

<a id="linflex._vec2i"></a>

# Module `linflex._vec2i`

<a id="linflex._vec2i.Vec2i"></a>

## Class `Vec2i`

```python
class Vec2i(Vec2)
```

`Vector2 integer` data structure.

Components: `x`, `y`, only type `int`.

Useful for storing whole numbers in 2D space.

<a id="linflex._vec2i.Vec2i.from_angle"></a>

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

<a id="linflex._vec2i.Vec2i.__init__"></a>

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

<a id="linflex._vec2i.Vec2i.__add__"></a>

### `Vec2i.__add__`

```python
def __add__(other: Vec2i | Vec2) -> Vec2i | Vec2
```

Add two vectors.

**Arguments**:

- `other` _Vec2i | Vec2_ - Vector to add.
  

**Returns**:

  Vec2i | Vec2: Result of addition.

<a id="linflex._vec2i.Vec2i.__iadd__"></a>

### `Vec2i.__iadd__`

```python
def __iadd__(other: Vec2i) -> Vec2i
```

In-place add two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to add.
  

**Returns**:

- `Vec2i` - Result of addition.

<a id="linflex._vec2i.Vec2i.__sub__"></a>

### `Vec2i.__sub__`

```python
def __sub__(other: Vec2i | Vec2) -> Vec2i | Vec2
```

Subtract two vectors.

**Arguments**:

- `other` _Vec2i | Vec2_ - Vector to subtract.
  

**Returns**:

  Vec2i | Vec2: Result of subtraction.

<a id="linflex._vec2i.Vec2i.__isub__"></a>

### `Vec2i.__isub__`

```python
def __isub__(other: Vec2i) -> Vec2i
```

In-place subtract two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to subtract.
  

**Returns**:

- `Vec2i` - Result of subtraction.

<a id="linflex._vec2i.Vec2i.__mul__"></a>

### `Vec2i.__mul__`

```python
def __mul__(other: Vec2i | Vec2 | int | float) -> Vec2i | Vec2
```

Multiply vector by another vector or scalar.

**Arguments**:

- `other` _Vec2i | Vec2 | int | float_ - Value to multiply.
  

**Returns**:

  Vec2i | Vec2: Result of multiplication.

<a id="linflex._vec2i.Vec2i.__imul__"></a>

### `Vec2i.__imul__`

```python
def __imul__(other: Vec2i) -> Vec2i
```

In-place multiply two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to multiply.
  

**Returns**:

- `Vec2i` - Result of multiplication.

<a id="linflex._vec2i.Vec2i.__floordiv__"></a>

### `Vec2i.__floordiv__`

```python
def __floordiv__(other: Vec2i | Vec2 | int | float) -> Vec2i | Vec2
```

Floor divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec2i | Vec2 | int | float_ - Value to divide.
  

**Returns**:

  Vec2i | Vec2: Result of floor division.

<a id="linflex._vec2i.Vec2i.__ifloordiv__"></a>

### `Vec2i.__ifloordiv__`

```python
def __ifloordiv__(other: Vec2i) -> Vec2i
```

In-place floor divide two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to divide.
  

**Returns**:

- `Vec2i` - Result of floor division.

<a id="linflex._vec2i.Vec2i.__truediv__"></a>

### `Vec2i.__truediv__`

```python
def __truediv__(other: Vec2i | Vec2 | int | float) -> Vec2i | Vec2
```

Divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec2i | Vec2 | int | float_ - Value to divide.
  

**Returns**:

  Vec2i | Vec2: Result of division.

<a id="linflex._vec2i.Vec2i.__itruediv__"></a>

### `Vec2i.__itruediv__`

```python
def __itruediv__(other: Vec2i) -> Vec2i
```

In-place divide two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to divide.
  

**Returns**:

- `Vec2i` - Result of division.

<a id="linflex._vec2i.Vec2i.__mod__"></a>

### `Vec2i.__mod__`

```python
def __mod__(other: Vec2i | Vec2 | int | float) -> Vec2i | Vec2
```

Modulo vector by another vector or scalar.

**Arguments**:

- `other` _Vec2i | Vec2 | int | float_ - Value to modulo.
  

**Returns**:

  Vec2i | Vec2: Result of modulo.

<a id="linflex._vec2i.Vec2i.__imod__"></a>

### `Vec2i.__imod__`

```python
def __imod__(other: Vec2i) -> Vec2i
```

In-place modulo two integer vectors.

**Arguments**:

- `other` _Vec2i_ - Vector to modulo.
  

**Returns**:

- `Vec2i` - Result of modulo.

<a id="linflex._vec3"></a>

# Module `linflex._vec3`

<a id="linflex._vec3.Vec3"></a>

## Class `Vec3`

```python
class Vec3()
```

`Vector3` data structure.

Components: `x`, `y`, `z`.

Useful for storing position or direction in 3D space.

<a id="linflex._vec3.Vec3.ZERO"></a>

### `Vec3.ZERO`

```python
@class_constant
def ZERO(cls: type[Self]) -> Self
```

Vector with all components set to `0`.

<a id="linflex._vec3.Vec3.ONE"></a>

### `Vec3.ONE`

```python
@class_constant
def ONE(cls: type[Self]) -> Self
```

Vector with all components set to `1`.

<a id="linflex._vec3.Vec3.INF"></a>

### `Vec3.INF`

```python
@class_constant
def INF(cls: type[Self]) -> Self
```

Vector with all components set to `math.inf`.

<a id="linflex._vec3.Vec3.LEFT"></a>

### `Vec3.LEFT`

```python
@class_constant
def LEFT(cls: type[Self]) -> Self
```

Left unit vector.

Represents both local direction left, and the global direction west.

<a id="linflex._vec3.Vec3.RIGHT"></a>

### `Vec3.RIGHT`

```python
@class_constant
def RIGHT(cls: type[Self]) -> Self
```

Right unit vector.

Represents both local direction right, and global direction east.

<a id="linflex._vec3.Vec3.UP"></a>

### `Vec3.UP`

```python
@class_constant
def UP(cls: type[Self]) -> Self
```

Up unit vector.

Represents up direction.

<a id="linflex._vec3.Vec3.DOWN"></a>

### `Vec3.DOWN`

```python
@class_constant
def DOWN(cls: type[Self]) -> Self
```

Down unit vector.

Represents down direction.

<a id="linflex._vec3.Vec3.FORWARD"></a>

### `Vec3.FORWARD`

```python
@class_constant
def FORWARD(cls: type[Self]) -> Self
```

Forward unit vector.

Represents both local direction forward, and global direction north.

<a id="linflex._vec3.Vec3.BACK"></a>

### `Vec3.BACK`

```python
@class_constant
def BACK(cls: type[Self]) -> Self
```

Back/backward unit vector.

Represents local direction back/backwards, and global direction south.

<a id="linflex._vec3.Vec3.from_angles"></a>

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

<a id="linflex._vec3.Vec3.__init__"></a>

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

<a id="linflex._vec3.Vec3.__reduce__"></a>

### `Vec3.__reduce__`

```python
def __reduce__() -> tuple[type[Self], tuple[float, float]]
```

Helper for pickling support.

<a id="linflex._vec3.Vec3.__len__"></a>

### `Vec3.__len__`

```python
def __len__() -> Literal[3]
```

Return the number of components in the vector.

**Returns**:

- `int` - Number of components (always `3`).

<a id="linflex._vec3.Vec3.__iter__"></a>

### `Vec3.__iter__`

```python
def __iter__() -> Iterator[float]
```

Iterate over the components of the vector.

**Returns**:

- `Iterator[float]` - Iterator over `x`, `y`, and `z`.

<a id="linflex._vec3.Vec3.__getitem__"></a>

### `Vec3.__getitem__`

```python
def __getitem__(item: Literal[0, 1, 2]) -> float
```

Get a component by index.

**Arguments**:

- `item` _int_ - Index (`0` for `x`, `1` for `y`, `2` for `z`).
  

**Returns**:

- `float` - Value of the component.

<a id="linflex._vec3.Vec3.__repr__"></a>

### `Vec3.__repr__`

```python
def __repr__() -> str
```

Create representation.

**Returns**:

- `str` - Representation containing the `x`, `y`, and `z` components.

<a id="linflex._vec3.Vec3.__str__"></a>

### `Vec3.__str__`

```python
def __str__() -> str
```

Create string representation.

**Returns**:

- `str` - Representation containing the `x`, `y`, and `z` components.

<a id="linflex._vec3.Vec3.__bool__"></a>

### `Vec3.__bool__`

```python
def __bool__() -> bool
```

Return whether `x`, `y`, or `z` is not zero.

**Returns**:

- `bool` - Truthiness.

<a id="linflex._vec3.Vec3.__abs__"></a>

### `Vec3.__abs__`

```python
def __abs__() -> Self
```

Return a vector with absolute values of each component.

**Returns**:

- `Self` - Vector with absolute values.

<a id="linflex._vec3.Vec3.__round__"></a>

### `Vec3.__round__`

```python
def __round__(ndigits: int = 0) -> Self
```

Return a vector with each component rounded.

**Arguments**:

- `ndigits` _int_ - Number of digits to round to.
  

**Returns**:

- `Self` - Rounded vector.

<a id="linflex._vec3.Vec3.__floor__"></a>

### `Vec3.__floor__`

```python
def __floor__() -> Self
```

Return a vector with each component floored.

**Returns**:

- `Self` - Floored vector.

<a id="linflex._vec3.Vec3.__ceil__"></a>

### `Vec3.__ceil__`

```python
def __ceil__() -> Self
```

Return a vector with each component ceiled.

**Returns**:

- `Self` - Ceiled vector.

<a id="linflex._vec3.Vec3.__add__"></a>

### `Vec3.__add__`

```python
def __add__(other: Vec3) -> Vec3
```

Add two vectors.

**Arguments**:

- `other` _Vec3_ - Vector to add.
  

**Returns**:

- `Vec3` - Result of addition.

<a id="linflex._vec3.Vec3.__radd__"></a>

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

<a id="linflex._vec3.Vec3.__iadd__"></a>

### `Vec3.__iadd__`

```python
def __iadd__(other: Vec3) -> Vec3
```

In-place add two vectors.

**Arguments**:

- `other` _Vec3_ - Vector to add.
  

**Returns**:

- `Vec3` - Result of addition.

<a id="linflex._vec3.Vec3.__sub__"></a>

### `Vec3.__sub__`

```python
def __sub__(other: Vec3) -> Vec3
```

Subtract two vectors.

**Arguments**:

- `other` _Vec3_ - Vector to subtract.
  

**Returns**:

- `Vec3` - Result of subtraction.

<a id="linflex._vec3.Vec3.__rsub__"></a>

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

<a id="linflex._vec3.Vec3.__isub__"></a>

### `Vec3.__isub__`

```python
def __isub__(other: Vec3) -> Vec3
```

In-place subtract two vectors.

**Arguments**:

- `other` _Vec3_ - Vector to subtract.
  

**Returns**:

- `Vec3` - Result of subtraction.

<a id="linflex._vec3.Vec3.__mul__"></a>

### `Vec3.__mul__`

```python
def __mul__(other: Vec3 | int | float) -> Vec3
```

Multiply vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to multiply.
  

**Returns**:

- `Vec3` - Result of multiplication.

<a id="linflex._vec3.Vec3.__rmul__"></a>

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

<a id="linflex._vec3.Vec3.__imul__"></a>

### `Vec3.__imul__`

```python
def __imul__(other: Vec3 | int | float) -> Vec3
```

In-place multiply vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to multiply.
  

**Returns**:

- `Vec3` - Result of multiplication.

<a id="linflex._vec3.Vec3.__floordiv__"></a>

### `Vec3.__floordiv__`

```python
def __floordiv__(other: Vec3 | int | float) -> Vec3
```

Floor divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of floor division.

<a id="linflex._vec3.Vec3.__rfloordiv__"></a>

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

<a id="linflex._vec3.Vec3.__ifloordiv__"></a>

### `Vec3.__ifloordiv__`

```python
def __ifloordiv__(other: Vec3 | int | float) -> Vec3
```

In-place floor divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of floor division.

<a id="linflex._vec3.Vec3.__truediv__"></a>

### `Vec3.__truediv__`

```python
def __truediv__(other: Vec3 | int | float) -> Vec3
```

Divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of division.

<a id="linflex._vec3.Vec3.__rtruediv__"></a>

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

<a id="linflex._vec3.Vec3.__itruediv__"></a>

### `Vec3.__itruediv__`

```python
def __itruediv__(other: Vec3 | int | float) -> Vec3
```

In-place divide vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to divide.
  

**Returns**:

- `Vec3` - Result of division.

<a id="linflex._vec3.Vec3.__mod__"></a>

### `Vec3.__mod__`

```python
def __mod__(other: Vec3 | int | float) -> Vec3
```

Modulo vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to modulo.
  

**Returns**:

- `Vec3` - Result of modulo.

<a id="linflex._vec3.Vec3.__rmod__"></a>

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

<a id="linflex._vec3.Vec3.__imod__"></a>

### `Vec3.__imod__`

```python
def __imod__(other: Vec3 | int | float) -> Vec3
```

In-place modulo vector by another vector or scalar.

**Arguments**:

- `other` _Vec3 | int | float_ - Value to modulo.
  

**Returns**:

- `Vec3` - Result of modulo.

<a id="linflex._vec3.Vec3.__eq__"></a>

### `Vec3.__eq__`

```python
def __eq__(other: Vec3) -> bool
```

Check if two vectors are equal.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if equal, False otherwise.

<a id="linflex._vec3.Vec3.__ne__"></a>

### `Vec3.__ne__`

```python
def __ne__(other: Vec3) -> bool
```

Check if two vectors are not equal.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if not equal, False otherwise.

<a id="linflex._vec3.Vec3.__gt__"></a>

### `Vec3.__gt__`

```python
def __gt__(other: Vec3) -> bool
```

Check if this vector is greater than another.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if greater, False otherwise.

<a id="linflex._vec3.Vec3.__lt__"></a>

### `Vec3.__lt__`

```python
def __lt__(other: Vec3) -> bool
```

Check if this vector is less than another.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if less, False otherwise.

<a id="linflex._vec3.Vec3.__ge__"></a>

### `Vec3.__ge__`

```python
def __ge__(other: Vec3) -> bool
```

Check if this vector is greater than or equal to another.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if greater or equal, False otherwise.

<a id="linflex._vec3.Vec3.__le__"></a>

### `Vec3.__le__`

```python
def __le__(other: Vec3) -> bool
```

Check if this vector is less than or equal to another.

**Arguments**:

- `other` _Vec3_ - Vector to compare.
  

**Returns**:

- `bool` - True if less or equal, False otherwise.

<a id="linflex._vec3.Vec3.__copy__"></a>

### `Vec3.__copy__`

```python
def __copy__() -> Self
```

Return a copy of the vector.

**Returns**:

- `Self` - A new copy.

<a id="linflex._vec3.Vec3.__deepcopy__"></a>

### `Vec3.__deepcopy__`

```python
def __deepcopy__(_memo: dict[int, Any]) -> Self
```

Return a deep copy of the vector.

**Arguments**:

- `_memo` _dict_ - Memoization dictionary.
  

**Returns**:

- `Self` - A new deep copy.

<a id="linflex._vec3.Vec3.copy"></a>

### `Vec3.copy`

```python
def copy() -> Self
```

Return a vector copy.

**Returns**:

- `Self` - A new copy.

<a id="linflex._vec3.Vec3.length"></a>

### `Vec3.length`

```python
def length() -> float
```

Return the length of the vector.

**Returns**:

- `float` - Length.

<a id="linflex._vec3.Vec3.length_squared"></a>

### `Vec3.length_squared`

```python
def length_squared() -> float
```

Return the length of the vector squared.

**Returns**:

- `float` - Length squared.

<a id="linflex._vec3.Vec3.normalized"></a>

### `Vec3.normalized`

```python
def normalized() -> Vec3
```

Return a vector with length of `1`, still with same direction.

**Returns**:

- `Vec3` - Normalized vector.

<a id="linflex._vec3.Vec3.lerp"></a>

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

<a id="linflex._vec3.Vec3.sign"></a>

### `Vec3.sign`

```python
def sign() -> Vec3
```

Return a Vec3 with each component being the sign of the vector.

**Returns**:

- `Vec3` - Vector with signed components.

<a id="linflex._vec3.Vec3.clamp"></a>

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

<a id="linflex._vec3.Vec3.move_toward"></a>

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

<a id="linflex._vec3.Vec3.distance_to"></a>

### `Vec3.distance_to`

```python
def distance_to(target: Vec3) -> float
```

Return the relative distance to the target point.

**Arguments**:

- `target` _Vec3_ - Target point.
  

**Returns**:

- `float` - Distance.

<a id="linflex._vec3.Vec3.distance_squared_to"></a>

### `Vec3.distance_squared_to`

```python
def distance_squared_to(target: Vec3) -> float
```

Return the relative distance to the target point, squared.

**Arguments**:

- `target` _Vec3_ - Target point.
  

**Returns**:

- `float` - Distance squared.

<a id="linflex._vec3.Vec3.direction_to"></a>

### `Vec3.direction_to`

```python
def direction_to(target: Vec3) -> Vec3
```

Return the direction to the target point.

**Arguments**:

- `target` _Vec3_ - Target point.
  

**Returns**:

- `Vec3` - Direction.

<a id="linflex._vec3.Vec3.dot"></a>

### `Vec3.dot`

```python
def dot(other: Vec3) -> float
```

Return the dot product between two 3D vectors.

**Arguments**:

- `other` _Vec3_ - Other vector.
  

**Returns**:

- `float` - Dot product.

<a id="linflex._vec3.Vec3.cross"></a>

### `Vec3.cross`

```python
def cross(other: Vec3) -> Vec3
```

Return the cross product between two 3D vectors.

**Arguments**:

- `other` _Vec3_ - Other vector.
  

**Returns**:

- `Vec3` - Cross product.

<a id="linflex._vec3.Vec3.angles"></a>

### `Vec3.angles`

```python
def angles() -> Vec3
```

Return the angles (pitch, yaw, roll) of the vector.

**Returns**:

- `Vec3` - Angles in radians.

<a id="linflex._vec3.Vec3.angles_to"></a>

### `Vec3.angles_to`

```python
def angles_to(target: Vec3) -> Vec3
```

Return the angles to the target point.

**Arguments**:

- `target` _Vec3_ - Target point.
  

**Returns**:

- `Vec3` - Angles in radians.

<a id="linflex._vec3.Vec3.rotated_around_x"></a>

### `Vec3.rotated_around_x`

```python
def rotated_around_x(angle: float) -> Vec3
```

Return a vector rotated around the `X` axis by `angle` radians.

**Arguments**:

- `angle` _float_ - Radians to rotate with.
  

**Returns**:

- `Vec3` - Rotated vector.

<a id="linflex._vec3.Vec3.rotated_around_y"></a>

### `Vec3.rotated_around_y`

```python
def rotated_around_y(angle: float) -> Vec3
```

Return a vector rotated around the `Y` axis by `angle` radians.

**Arguments**:

- `angle` _float_ - Radians to rotate with.
  

**Returns**:

- `Vec3` - Rotated vector.

<a id="linflex._vec3.Vec3.rotated_around_z"></a>

### `Vec3.rotated_around_z`

```python
def rotated_around_z(angle: float) -> Vec3
```

Return a vector rotated around the `Z` axis by `angle` radians.

**Arguments**:

- `angle` _float_ - Radians to rotate with.
  

**Returns**:

- `Vec3` - Rotated vector.

<a id="linflex._vec3.Vec3.rotated"></a>

### `Vec3.rotated`

```python
def rotated(angles: Vec3) -> Vec3
```

Return a vector rotated by the given angles around each axis.

**Arguments**:

- `angles` _Vec3_ - Angles to rotate around each axis.
  

**Returns**:

- `Vec3` - Rotated vector.

<a id="linflex._vec3.Vec3.rotated_around"></a>

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

