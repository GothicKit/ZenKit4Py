import math
from ctypes import Structure, c_float
from typing import ClassVar, Any

class Quat(Structure):
    """
    A class to represent a quaternion using four components: w, x, y, z.

    Attributes:
        w (float): The scalar part of the quaternion.
        x (float): The x-component of the imaginary part.
        y (float): The y-component of the imaginary part.
        z (float): The z-component of the imaginary part.
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("w", c_float),
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]

    def __repr__(self) -> str:
        """
        Return a string representation of the quaternion.

        Returns:
            str: A string in the format 'Quaternion(w, x, y, z)'.
        """
        return f"Quaternion(w={self.w}, x={self.x}, y={self.y}, z={self.z})"

    def conjugate(self):
        """
        Calculate the conjugate of the quaternion.

        Returns:
            Quaternion: The conjugate of the quaternion.
        """
        return Quat(self.w, -self.x, -self.y, -self.z)

    def length(self) -> float:
        """
        Calculate the magnitude (length) of the quaternion.

        Returns:
            float: The length of the quaternion.
        """
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """
        Normalize the quaternion to a unit quaternion (length of 1).

        Returns:
            Quaternion: A new quaternion representing the normalized quaternion.
        """
        l = self.length()
        if l > 0:
            return self / l
        return Quat(1.0, 0.0, 0.0, 0.0)  # Default to identity quaternion

    def __add__(self, other):
        """
        Add this quaternion to another quaternion component-wise.

        Args:
            other (Quaternion): The quaternion to add to this quaternion.

        Returns:
            Quaternion: A new quaternion representing the sum.

        Raises:
            TypeError: If the operand is not a Quaternion object.
        """
        if isinstance(other, Quat):
            return Quat(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Operand must be of type Quaternion")

    def __sub__(self, other):
        """
        Subtract another quaternion from this quaternion component-wise.

        Args:
            other (Quaternion): The quaternion to subtract from this quaternion.

        Returns:
            Quaternion: A new quaternion representing the difference.

        Raises:
            TypeError: If the operand is not a Quaternion object.
        """
        if isinstance(other, Quat):
            return Quat(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Operand must be of type Quaternion")

    def __mul__(self, other):
        """
        Multiply this quaternion by another quaternion or a scalar.

        Args:
            other (Quaternion or float): The quaternion to multiply with this quaternion,
                                         or a scalar to multiply each component by.

        Returns:
            Quaternion: A new quaternion representing the product.

        Raises:
            TypeError: If the operand is not a Quaternion object or a number.
        """
        if isinstance(other, Quat):
            # Quaternion multiplication
            w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
            x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
            y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
            z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
            return Quat(w, x, y, z)
        elif isinstance(other, (int, float)):
            return Quat(self.w * other, self.x * other, self.y * other, self.z * other)
        raise TypeError("Operand must be of type Quaternion or Number")

    def __truediv__(self, other):
        """
        Divide this quaternion by a scalar.

        Args:
            other (float): The scalar to divide each component by.

        Returns:
            Quaternion: A new quaternion representing the quotient.

        Raises:
            TypeError: If the operand is not a number.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Quat(self.w / other, self.x / other, self.y / other, self.z / other)
        raise TypeError("Operand must be a number")
