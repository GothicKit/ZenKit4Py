from ctypes import Structure
from ctypes import c_uint8
from typing import Any
from typing import ClassVar
from typing import Union


class Color(Structure):
    """
    A class to represent a color with Red, Green, Blue, and Alpha (transparency) components.

    Attributes:
        _r: The Red component of the color (0 to 255).
        _g: The Green component of the color (0 to 255).
        _b: The Blue component of the color (0 to 255).
        _a: The Alpha (transparency) component of the color (0 to 255).
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("_r", c_uint8),
        ("_g", c_uint8),
        ("_b", c_uint8),
        ("_a", c_uint8),
    ]

    @property
    def r(self) -> int:
        """Return the Red component of the color."""
        return self._r

    @property
    def g(self) -> int:
        """Return the Green component of the color."""
        return self._g

    @property
    def b(self) -> int:
        """Return the Blue component of the color."""
        return self._b

    @property
    def a(self) -> int:
        """Return the Alpha (transparency) component of the color."""
        return self._a

    def __repr__(self) -> str:
        """Return a string representation of the color."""
        return f"<Color r={self._r} g={self._g} b={self._b} a={self._a}>"

    def __getitem__(self, index: int) -> float:
        """
        Retrieve a color component by index.

        Args:
            index: The index of the color component to retrieve.
                Valid indices are 0 (red), 1 (green), 2 (blue), and 3 (alpha).

        Returns:
            The value of the color component at the specified index.

        Raises:
            IndexError: If the index is out of range (not 0, 1, 2, or 3).
        """
        if index == 0:
            return self._r
        elif index == 1:
            return self._g
        elif index == 2:
            return self._b
        elif index == 3:
            return self._a
        else:
            raise IndexError("Index out of range. Valid indices are 0, 1, 2, and 3.")

    def __eq__(self, other: object) -> bool:
        """
        Check if two Colors are equal component-wise.

        Args:
            other: The Color to compare with this Color.

        Returns:
            True if the Colors are equal, False otherwise.
        """
        if isinstance(other, Color):
            return self._r == other._r and self._g == other._g and self._b == other._b and self._a == other._a
        return False

    def __lt__(self, other: "Color") -> bool:
        """
        Check if this Color is less than another based on magnitude.

        Args:
            other: The Color to compare with this Color.

        Returns:
            True if this Color's magnitude is less, False otherwise.
        """
        return self.average() < other.average()

    def __le__(self, other: "Color") -> bool:
        """
        Check if this Color is less than or equal to another based on magnitude.

        Args:
            other: The Color to compare with this Color.

        Returns:
            True if this Color's magnitude is less or equal, False otherwise.
        """
        return self.average() <= other.average()

    def __gt__(self, other: "Color") -> bool:
        """
        Check if this Color is greater than another based on magnitude.

        Args:
            other: The Color to compare with this Color.

        Returns:
            True if this Color's magnitude is greater, False otherwise.
        """
        return self.average() > other.average()

    def __ge__(self, other: "Color") -> bool:
        """
        Check if this Color is greater than or equal to another based on magnitude.

        Args:
            other: The Color to compare with this Color.

        Returns:
            True if this Color's magnitude is greater or equal, False otherwise.
        """
        return self.average() >= other.average()

    def __add__(self, other: Union["Color", float, int]) -> "Color":
        """
        Add this color to another color or scalar component-wise.

        Args:
            other: The color or scalar to add to this color.

        Returns:
            A new Color instance representing the sum.
        """
        if isinstance(other, Color):
            return Color(
                min(self._r + other._r, 255),
                min(self._g + other._g, 255),
                min(self._b + other._b, 255),
                min(self._a + other._a, 255),
            )
        elif isinstance(other, (int, float)):
            return Color(
                min(int(self._r + other), 255),
                min(int(self._g + other), 255),
                min(int(self._b + other), 255),
                min(int(self._a + other), 255),
            )
        raise TypeError("Operand must be of type Color or a number")

    def __sub__(self, other: Union["Color", float, int]) -> "Color":
        """
        Subtract another color or scalar from this color component-wise.

        Args:
            other: The color or scalar to subtract from this color.

        Returns:
            A new Color instance representing the difference.
        """
        if isinstance(other, Color):
            return Color(
                max(self._r - other._r, 0),
                max(self._g - other._g, 0),
                max(self._b - other._b, 0),
                max(self._a - other._a, 0),
            )
        elif isinstance(other, (int, float)):
            return Color(
                max(int(self._r - other), 0),
                max(int(self._g - other), 0),
                max(int(self._b - other), 0),
                max(int(self._a - other), 0),
            )
        raise TypeError("Operand must be of type Color or a number")

    def __mul__(self, other: Union["Color", float, int]) -> "Color":
        """
        Multiply this color by a scalar or another color component-wise.

        Args:
            other: The color to multiply with this color or a scalar to multiply each component by.

        Returns:
            A new Color instance representing the product.
        """
        if isinstance(other, Color):
            return Color(
                min(self._r * other._r // 255, 255),
                min(self._g * other._g // 255, 255),
                min(self._b * other._b // 255, 255),
                min(self._a * other._a // 255, 255),
            )
        elif isinstance(other, (int, float)):
            return Color(
                min(int(self._r * other), 255),
                min(int(self._g * other), 255),
                min(int(self._b * other), 255),
                min(int(self._a * other), 255),
            )
        raise TypeError("Operand must be of type Color or Number")

    def __truediv__(self, other: float | int) -> "Color":
        """
        Divide this color by a scalar.

        Args:
            other: The scalar to divide each component by.

        Returns:
            A new Color instance representing the quotient.
        """
        if other == 0:
            raise ValueError("Cannot divide by zero")
        return Color(
            min(int(self._r / other), 255),
            min(int(self._g / other), 255),
            min(int(self._b / other), 255),
            min(int(self._a / other), 255),
        )

    def to_hex(self) -> str:
        """
        Convert the color to a hexadecimal string.

        Returns:
            The color as a hexadecimal string in the format '#RRGGBBAA'.
        """
        return f"#{self._r:02X}{self._g:02X}{self._b:02X}{self._a:02X}"

    def blend(self, other: "Color", alpha: float) -> "Color":
        """
        Blend this color with another color based on the given Alpha value.

        Args:
            other: The color to blend with this color.
            alpha: The blend factor (0.0 to 1.0) where 0.0 is this color only and 1.0 is the other color only.

        Returns:
            A new Color instance representing the blended color.
        """
        if not (0.0 <= alpha <= 1.0):
            raise ValueError("Alpha must be between 0.0 and 1.0")
        return Color(
            int(self._r * (1 - alpha) + other._r * alpha),
            int(self._g * (1 - alpha) + other._g * alpha),
            int(self._b * (1 - alpha) + other._b * alpha),
            int(self._a * (1 - alpha) + other._a * alpha),
        )

    def average(self) -> float:
        """
        Calculate the average intensity of the RGB components.

        Returns:
            The average intensity of the color.
        """
        return (self._r + self._g + self._b + self._a) / 4.0

    def __hash__(self) -> int:
        """
        Return a hash value for this Color based on its components.

        Returns:
            The hash value of the Color.
        """
        return hash((self._r, self._g, self._b, self._a))
