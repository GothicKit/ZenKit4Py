from ctypes import Structure, c_uint8
from typing import ClassVar, Any

class Color(Structure):
    """
    A class to represent a color with red, green, blue, and alpha (transparency) components.

    Attributes:
        _r (int): The red component of the color (0 to 255).
        _g (int): The green component of the color (0 to 255).
        _b (int): The blue component of the color (0 to 255).
        _a (int): The alpha (transparency) component of the color (0 to 255).
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("_r", c_uint8),
        ("_g", c_uint8),
        ("_b", c_uint8),
        ("_a", c_uint8),
    ]

    @property
    def r(self) -> int:
        """
        Return the red component of the color.

        Returns:
            int: The red component (0 to 255).
        """
        return self._r

    @property
    def g(self) -> int:
        """
        Return the green component of the color.

        Returns:
            int: The green component (0 to 255).
        """
        return self._g

    @property
    def b(self) -> int:
        """
        Return the blue component of the color.

        Returns:
            int: The blue component (0 to 255).
        """
        return self._b

    @property
    def a(self) -> int:
        """
        Return the alpha (transparency) component of the color.

        Returns:
            int: The alpha component (0 to 255).
        """
        return self._a

    def __repr__(self) -> str:
        """
        Return a string representation of the color.

        Returns:
            str: A string in the format '<Color r=R g=G b=B a=A>'.
        """
        return f"<Color r={self._r} g={self._g} b={self._b} a={self._a}>"

    def __add__(self, other):
        """
        Add this color to another color component-wise.

        Args:
            other (Color): The color to add to this color.

        Returns:
            Color: A new Color instance representing the sum.

        Raises:
            TypeError: If the operand is not a Color object.
        """
        if isinstance(other, Color):
            return Color(
                min(self._r + other._r, 255),
                min(self._g + other._g, 255),
                min(self._b + other._b, 255),
                min(self._a + other._a, 255)
            )
        raise TypeError("Operand must be of type Color")

    def __sub__(self, other):
        """
        Subtract another color from this color component-wise.

        Args:
            other (Color): The color to subtract from this color.

        Returns:
            Color: A new Color instance representing the difference.

        Raises:
            TypeError: If the operand is not a Color object.
        """
        if isinstance(other, Color):
            return Color(
                max(self._r - other._r, 0),
                max(self._g - other._g, 0),
                max(self._b - other._b, 0),
                max(self._a - other._a, 0)
            )
        raise TypeError("Operand must be of type Color")

    def __mul__(self, other):
        """
        Multiply this color by a scalar or another color component-wise.

        Args:
            other (Color or float): The color to multiply with this color or a scalar to multiply each component by.

        Returns:
            Color: A new Color instance representing the product.

        Raises:
            TypeError: If the operand is not a Color object or a number.
        """
        if isinstance(other, Color):
            return Color(
                min(self._r * other._r // 255, 255),
                min(self._g * other._g // 255, 255),
                min(self._b * other._b // 255, 255),
                min(self._a * other._a // 255, 255)
            )
        elif isinstance(other, (int, float)):
            return Color(
                min(int(self._r * other), 255),
                min(int(self._g * other), 255),
                min(int(self._b * other), 255),
                min(int(self._a * other), 255)
            )
        raise TypeError("Operand must be of type Color or Number")

    def __truediv__(self, other):
        """
        Divide this color by a scalar.

        Args:
            other (float): The scalar to divide each component by.

        Returns:
            Color: A new Color instance representing the quotient.

        Raises:
            TypeError: If the operand is not a number.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Color(
                min(int(self._r / other), 255),
                min(int(self._g / other), 255),
                min(int(self._b / other), 255),
                min(int(self._a / other), 255)
            )
        raise TypeError("Operand must be a number")

    def to_hex(self) -> str:
        """
        Convert the color to a hexadecimal string.

        Returns:
            str: The color as a hexadecimal string in the format '#RRGGBB' or '#RRGGBBAA'.
        """
        return f"#{self._r:02X}{self._g:02X}{self._b:02X}{self._a:02X}"

    def blend(self, other, alpha: float) -> 'Color':
        """
        Blend this color with another color based on the given alpha value.

        Args:
            other (Color): The color to blend with this color.
            alpha (float): The blend factor (0.0 to 1.0) where 0.0 is this color only and 1.0 is the other color only.

        Returns:
            Color: A new Color instance representing the blended color.

        Raises:
            TypeError: If the operand is not a Color object.
            ValueError: If alpha is not between 0.0 and 1.0.
        """
        if not (0.0 <= alpha <= 1.0):
            raise ValueError("Alpha must be between 0.0 and 1.0")
        if isinstance(other, Color):
            return Color(
                int(self._r * (1 - alpha) + other._r * alpha),
                int(self._g * (1 - alpha) + other._g * alpha),
                int(self._b * (1 - alpha) + other._b * alpha),
                int(self._a * (1 - alpha) + other._a * alpha)
            )
        raise TypeError("Operand must be of type Color")
