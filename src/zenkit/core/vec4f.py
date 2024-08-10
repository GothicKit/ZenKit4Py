import math
from ctypes import Structure, c_float
from typing import ClassVar, Any, Union

class Vec4f(Structure):
    """
    A class to represent a 4D Vector using floats, supporting various Vector operations.
    
    Attributes:
        x: The x-component of the Vector.
        y: The y-component of the Vector.
        z: The z-component of the Vector.
        w: The w-component of the Vector.
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]

    def __repr__(self) -> str:
        """
        Return a string representation of the Vector.

        Returns:
            A string in the format 'Vec4f(x, y, z, w)'.
        """
        return f"Vec4f(x={self.x}, y={self.y}, z={self.z}, w={self.w})"
    
    def __neg__(self) -> "Vec4f":
        """
        Negate the Vector (reverse the direction of the Vector).

        Returns:
            A new Vec4f instance with negated components.
        """
        return Vec4f(-self.x, -self.y, -self.z, -self.w)
    
    def __eq__(self, other: Any) -> bool:
        """
        Check if two Vectors are equal component-wise.

        Args:
            other: The Vector to compare with this Vector.

        Returns:
            True if the Vectors are equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w
        return False
    
    def __lt__(self, other: "Vec4f") -> bool:
        """
        Check if this Vector is less than another based on magnitude.

        Args:
            other: The Vector to compare with this Vector.

        Returns:
            True if this Vector's magnitude is less, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.length() < other.length()
        return False

    def __le__(self, other: "Vec4f") -> bool:
        """
        Check if this Vector is less than or equal to another based on magnitude.

        Args:
            other: The Vector to compare with this Vector.

        Returns:
            True if this Vector's magnitude is less or equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.length() <= other.length()
        return False

    def __gt__(self, other: "Vec4f") -> bool:
        """
        Check if this Vector is greater than another based on magnitude.

        Args:
            other: The Vector to compare with this Vector.

        Returns:
            True if this Vector's magnitude is greater, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.length() > other.length()
        return False

    def __ge__(self, other: "Vec4f") -> bool:
        """
        Check if this Vector is greater than or equal to another based on magnitude.

        Args:
            other: The Vector to compare with this Vector.

        Returns:
            True if this Vector's magnitude is greater or equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.length() >= other.length()
        return False
    
    def __add__(self, other: Union["Vec4f", float, int]) -> "Vec4f":
        """
        Add this Vector to another Vector or a scalar component-wise.

        Args:
            other: The Vector to add to this Vector, or a scalar to add to each component.

        Returns:
            A new Vec4f instance representing the sum.

        Raises:
            TypeError: If the operand is not a Vec4f object or a number.
        """
        if isinstance(other, Vec4f):
            return Vec4f(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
        elif isinstance(other, (int, float)):
            return Vec4f(self.x + other, self.y + other, self.z + other, self.w + other)
        raise TypeError("Operand must be of type Vec4f, or Number")

    def __sub__(self, other: Union["Vec4f", float, int]) -> "Vec4f":
        """
        Subtract another Vector or a scalar from this Vector component-wise.

        Args:
            other: The Vector to subtract from this Vector, or a scalar to subtract from each component.

        Returns:
            A new Vec4f instance representing the difference.

        Raises:
            TypeError: If the operand is not a Vec4f object or a number.
        """
        if isinstance(other, Vec4f):
            return Vec4f(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
        elif isinstance(other, (int, float)):
            return Vec4f(self.x - other, self.y - other, self.z - other, self.w - other)
        raise TypeError("Operand must be of type Vec4f, or Number")

    def __mul__(self, other: Union["Vec4f", float, int]) -> "Vec4f":
        """
        Multiply this Vector by another Vector component-wise or by a scalar.

        Args:
            other: The Vector to multiply with this Vector, or a scalar to multiply each component by.

        Returns:
            A new Vec4f instance representing the product.

        Raises:
            TypeError: If the operand is not a Vec4f object or a number.
        """
        if isinstance(other, Vec4f):
            return Vec4f(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
        elif isinstance(other, (int, float)):
            return Vec4f(self.x * other, self.y * other, self.z * other, self.w * other)
        raise TypeError("Operand must be of type Vec4f, or Number")
    
    def __truediv__(self, other: Union["Vec4f", float, int]) -> "Vec4f":
        """
        Divide this Vector by another Vector component-wise or by a scalar.

        Args:
            other: The Vector to divide this Vector by, or a scalar to divide each component by.

        Returns:
            A new Vec4f instance representing the quotient.

        Raises:
            TypeError: If the operand is not a Vec4f object or a number.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, Vec4f):
            if other.x == 0 or other.y == 0 or other.z == 0 or other.w == 0:
                raise ValueError("Cannot divide by a Vector with zero components")
            return Vec4f(self.x / other.x, self.y / other.y, self.z / other.z, self.w / other.w)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Vec4f(self.x / other, self.y / other, self.z / other, self.w / other)
        raise TypeError("Operand must be of type Vec4f, or Number")
    
    def length(self) -> float:
        """
        Calculate the magnitude (length) of the Vector.

        Returns:
            The length of the Vector.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

    def normalize(self) -> "Vec4f":
        """
        Normalize the Vector to a unit Vector (length of 1).

        Returns:
            A new Vec4f instance representing the normalized Vector.
        """
        l = self.length()
        if l > 0:
            return self / l
        return Vec4f()

    def __hash__(self) -> int:
        """
        Return a hash value for this Vector based on its components.

        Returns:
            The hash value of the Vector.
        """
        return hash((self.x, self.y, self.z, self.w))