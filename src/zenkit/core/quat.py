import math
from ctypes import Structure
from ctypes import c_float
from typing import Any
from typing import ClassVar
from typing import Union


class Quat(Structure):
    """
    A class to represent a Quaternion using four components: w, x, y, z.

    Attributes:
        w: The scalar part of the Quaternion.
        x: The x-component of the imaginary part.
        y: The y-component of the imaginary part.
        z: The z-component of the imaginary part.
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("w", c_float),
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]

    def __repr__(self) -> str:
        """
        Return a string representation of the Quaternion.

        Returns:
            A string in the format 'Quat(w, x, y, z)'.
        """
        return f"Quat(w={self.w}, x={self.x}, y={self.y}, z={self.z})"

    def __neg__(self) -> "Quat":
        """
        Negate the Quaternion (reverse the direction of the Quaternion).

        Returns:
            A new Quat instance with negated components.
        """
        return Quat(-self.w, -self.x, -self.y, -self.z)

    def __eq__(self, other: object) -> bool:
        """
        Check if two Quaternions are equal component-wise.

        Args:
            other: The Quaternion to compare with this Quaternion.

        Returns:
            True if the Quaternions are equal, False otherwise.
        """
        if isinstance(other, Quat):
            return self.w == other.w and self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __lt__(self, other: "Quat") -> bool:
        """
        Check if this Quaternion is less than another based on magnitude.

        Args:
            other: The Quaternion to compare with this Quaternion.

        Returns:
            True if this Quaternion's magnitude is less, False otherwise.
        """
        if isinstance(other, Quat):
            return self.length() < other.length()
        return False

    def __le__(self, other: "Quat") -> bool:
        """
        Check if this Quaternion is less than or equal to another based on magnitude.

        Args:
            other: The Quaternion to compare with this Quaternion.

        Returns:
            True if this Quaternion's magnitude is less or equal, False otherwise.
        """
        if isinstance(other, Quat):
            return self.length() <= other.length()
        return False

    def __gt__(self, other: "Quat") -> bool:
        """
        Check if this Quaternion is greater than another based on magnitude.

        Args:
            other: The Quaternion to compare with this Quaternion.

        Returns:
            True if this Quaternion's magnitude is greater, False otherwise.
        """
        if isinstance(other, Quat):
            return self.length() > other.length()
        return False

    def __ge__(self, other: "Quat") -> bool:
        """
        Check if this Quaternion is greater than or equal to another based on magnitude.

        Args:
            other: The Quaternion to compare with this Quaternion.

        Returns:
            True if this Quaternion's magnitude is greater or equal, False otherwise.
        """
        if isinstance(other, Quat):
            return self.length() >= other.length()
        return False

    def __add__(self, other: "Quat") -> "Quat":
        """
        Add this Quaternion to another Quaternion component-wise.

        Args:
            other: The Quaternion to add to this Quaternion.

        Returns:
            A new Quat instance representing the sum.

        Raises:
            TypeError: If the operand is not a Quat object.
        """
        if isinstance(other, Quat):
            return Quat(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Operand must be of type Quat")

    def __sub__(self, other: "Quat") -> "Quat":
        """
        Subtract another Quaternion from this Quaternion component-wise.

        Args:
            other: The Quaternion to subtract from this Quaternion.

        Returns:
            A new Quat instance representing the difference.

        Raises:
            TypeError: If the operand is not a Quat object.
        """
        if isinstance(other, Quat):
            return Quat(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Operand must be of type Quat")

    def __mul__(self, other: Union["Quat", float, int]) -> "Quat":
        """
        Multiply this Quaternion by another Quaternion or a scalar.

        Args:
            other: The Quaternion to multiply with this Quaternion,
                   or a scalar to multiply each component by.

        Returns:
            A new Quat instance representing the product.

        Raises:
            TypeError: If the operand is not a Quat object or a number.
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
        raise TypeError("Operand must be of type Quat or Number")

    def __truediv__(self, other: float | int) -> "Quat":
        """
        Divide this Quaternion by a scalar.

        Args:
            other: The scalar to divide each component by.

        Returns:
            A new Quat instance representing the quotient.

        Raises:
            TypeError: If the operand is not a number.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Quat(self.w / other, self.x / other, self.y / other, self.z / other)
        raise TypeError("Operand must be a number")

    def conjugate(self) -> "Quat":
        """
        Calculate the conjugate of the Quaternion.

        Returns:
            The conjugate of the Quaternion.
        """
        return Quat(self.w, -self.x, -self.y, -self.z)

    def length(self) -> float:
        """
        Calculate the magnitude (length) of the Quaternion.

        Returns:
            The length of the Quaternion.
        """
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> "Quat":
        """
        Normalize the Quaternion to a unit Quaternion (length of 1).

        Returns:
            A new Quat instance representing the normalized Quaternion.
        """
        l = self.length()
        if l > 0:
            return self / l
        return Quat(1.0, 0.0, 0.0, 0.0)  # Default to identity Quaternion

    def __hash__(self) -> int:
        """
        Return a hash value for this Quaternion based on its components.

        Returns:
            The hash value of the Quaternion.
        """
        return hash((self.w, self.x, self.y, self.z))
