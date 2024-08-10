import math
from ctypes import Structure, c_float
from typing import ClassVar, Any

class Vec4f(Structure):
    """
    A class to represent a 4D vector using floats, supporting various vector operations.
    
    Attributes:
        x (float): The x-component of the vector.
        y (float): The y-component of the vector.
        z (float): The z-component of the vector.
        w (float): The w-component of the vector.
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]

    def __repr__(self) -> str:
        """
        Return a string representation of the vector.

        Returns:
            str: A string in the format 'Vec4f(x, y, z, w)'.
        """
        return f"Vec4f(x={self.x}, y={self.y}, z={self.z}, w={self.w})"
    
    def __neg__(self):
        """
        Negate the vector (reverse the direction of the vector).

        Returns:
            Vec4f: A new Vec4f instance with negated components.
        """
        return Vec4f(-self.x, -self.y, -self.z, -self.w)
    
    def __eq__(self, other):
        """
        Check if two vectors are equal component-wise.

        Args:
            other (Vec4f): The vector to compare with this vector.

        Returns:
            bool: True if the vectors are equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w
        raise TypeError("Comparison is only supported between two Vec4f objects")
    
    def __lt__(self, other):
        """
        Check if this vector is less than another based on magnitude.

        Args:
            other (Vec4f): The vector to compare with this vector.

        Returns:
            bool: True if this vector's magnitude is less, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.length() < other.length()
        raise TypeError("Comparison is only supported between two Vec4f objects")

    def __le__(self, other):
        """
        Check if this vector is less than or equal to another based on magnitude.

        Args:
            other (Vec4f): The vector to compare with this vector.

        Returns:
            bool: True if this vector's magnitude is less or equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.length() <= other.length()
        raise TypeError("Comparison is only supported between two Vec4f objects")

    def __gt__(self, other):
        """
        Check if this vector is greater than another based on magnitude.

        Args:
            other (Vec4f): The vector to compare with this vector.

        Returns:
            bool: True if this vector's magnitude is greater, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.length() > other.length()
        raise TypeError("Comparison is only supported between two Vec4f objects")

    def __ge__(self, other):
        """
        Check if this vector is greater than or equal to another based on magnitude.

        Args:
            other (Vec4f): The vector to compare with this vector.

        Returns:
            bool: True if this vector's magnitude is greater or equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Vec4f objects.
        """
        if isinstance(other, Vec4f):
            return self.length() >= other.length()
        raise TypeError("Comparison is only supported between two Vec4f objects")
    
    def __add__(self, other):
        """
        Add this vector to another vector or a scalar component-wise.

        Args:
            other (Vec4f or float): The vector to add to this vector, or a scalar to add to each component.

        Returns:
            Vec4f: A new Vec4f instance representing the sum.

        Raises:
            TypeError: If the operand is not a Vec4f object or a number.
        """
        if isinstance(other, Vec4f):
            return Vec4f(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
        elif isinstance(other, (int, float)):
            return Vec4f(self.x + other, self.y + other, self.z + other, self.w + other)
        raise TypeError("Operand must be of type Vec4f, or Number")

    def __sub__(self, other):
        """
        Subtract another vector or a scalar from this vector component-wise.

        Args:
            other (Vec4f or float): The vector to subtract from this vector, or a scalar to subtract from each component.

        Returns:
            Vec4f: A new Vec4f instance representing the difference.

        Raises:
            TypeError: If the operand is not a Vec4f object or a number.
        """
        if isinstance(other, Vec4f):
            return Vec4f(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
        elif isinstance(other, (int, float)):
            return Vec4f(self.x - other, self.y - other, self.z - other, self.w - other)
        raise TypeError("Operand must be of type Vec4f, or Number")

    def __mul__(self, other):
        """
        Multiply this vector by another vector component-wise or by a scalar.

        Args:
            other (Vec4f or float): The vector to multiply with this vector, or a scalar to multiply each component by.

        Returns:
            Vec4f: A new Vec4f instance representing the product.

        Raises:
            TypeError: If the operand is not a Vec4f object or a number.
        """
        if isinstance(other, Vec4f):
            return Vec4f(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
        elif isinstance(other, (int, float)):
            return Vec4f(self.x * other, self.y * other, self.z * other, self.w * other)
        raise TypeError("Operand must be of type Vec4f, or Number")
    
    def __truediv__(self, other):
        """
        Divide this vector by another vector component-wise or by a scalar.

        Args:
            other (Vec4f or float): The vector to divide this vector by, or a scalar to divide each component by.

        Returns:
            Vec4f: A new Vec4f instance representing the quotient.

        Raises:
            TypeError: If the operand is not a Vec4f object or a number.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, Vec4f):
            if other.x == 0 or other.y == 0 or other.z == 0 or other.w == 0:
                raise ValueError("Cannot divide by a vector with zero components")
            return Vec4f(self.x / other.x, self.y / other.y, self.z / other.z, self.w / other.w)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Vec4f(self.x / other, self.y / other, self.z / other, self.w / other)
        raise TypeError("Operand must be of type Vec4f, or Number")
    
    def length(self):
        """
        Calculate the magnitude (length) of the vector.

        Returns:
            float: The length of the vector.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

    def normalize(self):
        """
        Normalize the vector to a unit vector (length of 1).

        Returns:
            Vec4f: A new Vec4f instance representing the normalized vector.
        """
        l = self.length()
        if l > 0:
            return self / l
        return Vec4f()