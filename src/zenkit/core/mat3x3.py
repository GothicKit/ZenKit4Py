import math
from ctypes import Structure, c_float
from typing import Any, ClassVar, Union
from mat4x4 import Mat4x4
from quat import Quat

class Mat3x3(Structure):
    """
    A class to represent a 3x3 Matrix using floats, supporting various matrix operations.

    Attributes:
        m00, m01, m02: The elements of the first row of the matrix.
        m10, m11, m12: The elements of the second row of the matrix.
        m20, m21, m22: The elements of the third row of the matrix.
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("m00", c_float), ("m01", c_float), ("m02", c_float),
        ("m10", c_float), ("m11", c_float), ("m12", c_float),
        ("m20", c_float), ("m21", c_float), ("m22", c_float),
    ]

    def __repr__(self) -> str:
        """
        Return a string representation of the Matrix.

        Returns:
            A string in the format 'Mat3x3([[m00, m01, m02], [m10, m11, m12], [m20, m21, m22]])'.
        """
        return (f"Mat3x3([[{self.m00}, {self.m01}, {self.m02}], "
                f"[{self.m10}, {self.m11}, {self.m12}], "
                f"[{self.m20}, {self.m21}, {self.m22}]])")

    def __eq__(self, other: object) -> bool:
        """
        Check if two Matrices are equal element-wise.

        Args:
            other: The Matrix to compare with this Matrix.

        Returns:
            True if the Matrices are equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Mat3x3 objects.
        """
        if isinstance(other, Mat3x3):
            return (
                self.m00 == other.m00 and self.m01 == other.m01 and self.m02 == other.m02 and
                self.m10 == other.m10 and self.m11 == other.m11 and self.m12 == other.m12 and
                self.m20 == other.m20 and self.m21 == other.m21 and self.m22 == other.m22
            )
        return False

    def __add__(self, other: Union["Mat3x3", float, int]) -> "Mat3x3":
        """
        Add this Matrix to another Matrix or a scalar element-wise.

        Args:
            other: The Matrix to add to this Matrix, or a scalar to add to each element.

        Returns:
            A new Mat3x3 instance representing the sum.

        Raises:
            TypeError: If the operand is not a Mat3x3 object or a number.
        """
        if isinstance(other, Mat3x3):
            return Mat3x3(
                self.m00 + other.m00, self.m01 + other.m01, self.m02 + other.m02,
                self.m10 + other.m10, self.m11 + other.m11, self.m12 + other.m12,
                self.m20 + other.m20, self.m21 + other.m21, self.m22 + other.m22
            )
        elif isinstance(other, (int, float)):
            return Mat3x3(
                self.m00 + other, self.m01 + other, self.m02 + other,
                self.m10 + other, self.m11 + other, self.m12 + other,
                self.m20 + other, self.m21 + other, self.m22 + other
            )
        raise TypeError("Operand must be of type Mat3x3, or Number")

    def __sub__(self, other: Union["Mat3x3", float, int]) -> "Mat3x3":
        """
        Subtract another Matrix or a scalar from this Matrix element-wise.

        Args:
            other: The Matrix to subtract from this Matrix, or a scalar to subtract from each element.

        Returns:
            A new Mat3x3 instance representing the difference.

        Raises:
            TypeError: If the operand is not a Mat3x3 object or a number.
        """
        if isinstance(other, Mat3x3):
            return Mat3x3(
                self.m00 - other.m00, self.m01 - other.m01, self.m02 - other.m02,
                self.m10 - other.m10, self.m11 - other.m11, self.m12 - other.m12,
                self.m20 - other.m20, self.m21 - other.m21, self.m22 - other.m22
            )
        elif isinstance(other, (int, float)):
            return Mat3x3(
                self.m00 - other, self.m01 - other, self.m02 - other,
                self.m10 - other, self.m11 - other, self.m12 - other,
                self.m20 - other, self.m21 - other, self.m22 - other
            )
        raise TypeError("Operand must be of type Mat3x3, or Number")

    def __mul__(self, other: Union["Mat3x3", float, int]) -> "Mat3x3":
        """
        Multiply this Matrix by another Matrix element-wise or by a scalar.

        Args:
            other: The Matrix to multiply with this Matrix, or a scalar to multiply each element by.

        Returns:
            A new Mat3x3 instance representing the product.

        Raises:
            TypeError: If the operand is not a Mat3x3 object or a number.
        """
        if isinstance(other, Mat3x3):
            return Mat3x3(
                self.m00 * other.m00, self.m01 * other.m01, self.m02 * other.m02,
                self.m10 * other.m10, self.m11 * other.m11, self.m12 * other.m12,
                self.m20 * other.m20, self.m21 * other.m21, self.m22 * other.m22
            )
        elif isinstance(other, (int, float)):
            return Mat3x3(
                self.m00 * other, self.m01 * other, self.m02 * other,
                self.m10 * other, self.m11 * other, self.m12 * other,
                self.m20 * other, self.m21 * other, self.m22 * other
            )
        raise TypeError("Operand must be of type Mat3x3, or Number")

    def __truediv__(self, other: Union["Mat3x3", float, int]) -> "Mat3x3":
        """
        Divide this Matrix by another Matrix element-wise or by a scalar.

        Args:
            other: The Matrix to divide this Matrix by, or a scalar to divide each element by.

        Returns:
            A new Mat3x3 instance representing the quotient.

        Raises:
            TypeError: If the operand is not a Mat3x3 object or a number.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, Mat3x3):
            return Mat3x3(
                self.m00 / other.m00, self.m01 / other.m01, self.m02 / other.m02,
                self.m10 / other.m10, self.m11 / other.m11, self.m12 / other.m12,
                self.m20 / other.m20, self.m21 / other.m21, self.m22 / other.m22
            )
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Mat3x3(
                self.m00 / other, self.m01 / other, self.m02 / other,
                self.m10 / other, self.m11 / other, self.m12 / other,
                self.m20 / other, self.m21 / other, self.m22 / other
            )
        raise TypeError("Operand must be of type Mat3x3, or Number")

    def determinant(self) -> float:
        """
        Calculate the determinant of the Matrix.

        Returns:
            The determinant of the Matrix.
        """
        return (self.m00 * (self.m11 * self.m22 - self.m12 * self.m21) -
                self.m01 * (self.m10 * self.m22 - self.m12 * self.m20) +
                self.m02 * (self.m10 * self.m21 - self.m11 * self.m20))

    def transpose(self) -> "Mat3x3":
        """
        Transpose the Matrix (swap rows with columns).

        Returns:
            A new Mat3x3 instance representing the transposed Matrix.
        """
        return Mat3x3(
            self.m00, self.m10, self.m20,
            self.m01, self.m11, self.m21,
            self.m02, self.m12, self.m22
        )
        
    def to_mat4x4(self) -> "Mat4x4":
        """
        Create a Mat4x4 from a Mat3x3 by embedding the 3x3 matrix into the top-left corner of the 4x4 matrix,
        with the remaining elements set to the identity matrix.

        Returns:
            A new Mat4x4 instance.
        """
        return Mat4x4(
            self.m00, self.m01, self.m02, 0.0,
            self.m10, self.m11, self.m12, 0.0,
            self.m20, self.m21, self.m22, 0.0,
            0.0,    0.0,    0.0,    1.0
        )
        
    def to_quaternion(self) -> Quat:
        """
        Convert this 3x3 rotation matrix to a quaternion.

        Returns:
            A Quat instance representing the same rotation.
        """
        trace = self.m00 + self.m11 + self.m22

        if trace > 0:
            s = 0.5 / math.sqrt(trace + 1.0)
            w = 0.25 / s
            x = (self.m21 - self.m12) * s
            y = (self.m02 - self.m20) * s
            z = (self.m10 - self.m01) * s
        elif self.m00 > self.m11 and self.m00 > self.m22:
            s = 2.0 * math.sqrt(1.0 + self.m00 - self.m11 - self.m22)
            w = (self.m21 - self.m12) / s
            x = 0.25 * s
            y = (self.m01 + self.m10) / s
            z = (self.m02 + self.m20) / s
        elif self.m11 > self.m22:
            s = 2.0 * math.sqrt(1.0 + self.m11 - self.m00 - self.m22)
            w = (self.m02 - self.m20) / s
            x = (self.m01 + self.m10) / s
            y = 0.25 * s
            z = (self.m12 + self.m21) / s
        else:
            s = 2.0 * math.sqrt(1.0 + self.m22 - self.m00 - self.m11)
            w = (self.m10 - self.m01) / s
            x = (self.m02 + self.m20) / s
            y = (self.m12 + self.m21) / s
            z = 0.25 * s

        return Quat(w, x, y, z)

    def __hash__(self) -> int:
        """
        Return a hash value for this Matrix based on its elements.

        Returns:
            The hash value of the Matrix.
        """
        return hash((self.m00, self.m01, self.m02,
                     self.m10, self.m11, self.m12,
                     self.m20, self.m21, self.m22))
