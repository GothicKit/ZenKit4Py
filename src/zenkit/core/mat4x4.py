import math
from ctypes import Structure, c_float
from typing import Any, ClassVar, Union
from zenkit.core import Mat3x3
from zenkit.core import Quat

class Mat4x4(Structure):
    """
    A class to represent a 4x4 Matrix using floats, supporting various matrix operations.

    Attributes:
        m00, m01, m02, m03: The elements of the first row of the matrix.
        m10, m11, m12, m13: The elements of the second row of the matrix.
        m20, m21, m22, m23: The elements of the third row of the matrix.
        m30, m31, m32, m33: The elements of the fourth row of the matrix.
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("m00", c_float), ("m01", c_float), ("m02", c_float), ("m03", c_float),
        ("m10", c_float), ("m11", c_float), ("m12", c_float), ("m13", c_float),
        ("m20", c_float), ("m21", c_float), ("m22", c_float), ("m23", c_float),
        ("m30", c_float), ("m31", c_float), ("m32", c_float), ("m33", c_float),
    ]

    def __repr__(self) -> str:
        """
        Return a string representation of the Matrix.

        Returns:
            A string in the format 'Mat4x4([[m00, m01, m02, m03], [m10, m11, m12, m13], [m20, m21, m22, m23], [m30, m31, m32, m33]])'.
        """
        return (f"Mat4x4([[{self.m00}, {self.m01}, {self.m02}, {self.m03}], "
                f"[{self.m10}, {self.m11}, {self.m12}, {self.m13}], "
                f"[{self.m20}, {self.m21}, {self.m22}, {self.m23}], "
                f"[{self.m30}, {self.m31}, {self.m32}, {self.m33}]])")

    def __eq__(self, other: object) -> bool:
        """
        Check if two Matrices are equal element-wise.

        Args:
            other: The Matrix to compare with this Matrix.

        Returns:
            True if the Matrices are equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Mat4x4 objects.
        """
        if isinstance(other, Mat4x4):
            return (
                self.m00 == other.m00 and self.m01 == other.m01 and self.m02 == other.m02 and self.m03 == other.m03 and
                self.m10 == other.m10 and self.m11 == other.m11 and self.m12 == other.m12 and self.m13 == other.m13 and
                self.m20 == other.m20 and self.m21 == other.m21 and self.m22 == other.m22 and self.m23 == other.m23 and
                self.m30 == other.m30 and self.m31 == other.m31 and self.m32 == other.m32 and self.m33 == other.m33
            )
        return False

    def __add__(self, other: Union["Mat4x4", float, int]) -> "Mat4x4":
        """
        Add this Matrix to another Matrix or a scalar element-wise.

        Args:
            other: The Matrix to add to this Matrix, or a scalar to add to each element.

        Returns:
            A new Mat4x4 instance representing the sum.

        Raises:
            TypeError: If the operand is not a Mat4x4 object or a number.
        """
        if isinstance(other, Mat4x4):
            return Mat4x4(
                self.m00 + other.m00, self.m01 + other.m01, self.m02 + other.m02, self.m03 + other.m03,
                self.m10 + other.m10, self.m11 + other.m11, self.m12 + other.m12, self.m13 + other.m13,
                self.m20 + other.m20, self.m21 + other.m21, self.m22 + other.m22, self.m23 + other.m23,
                self.m30 + other.m30, self.m31 + other.m31, self.m32 + other.m32, self.m33 + other.m33
            )
        elif isinstance(other, (int, float)):
            return Mat4x4(
                self.m00 + other, self.m01 + other, self.m02 + other, self.m03 + other,
                self.m10 + other, self.m11 + other, self.m12 + other, self.m13 + other,
                self.m20 + other, self.m21 + other, self.m22 + other, self.m23 + other,
                self.m30 + other, self.m31 + other, self.m32 + other, self.m33 + other
            )
        raise TypeError("Operand must be of type Mat4x4, or Number")

    def __sub__(self, other: Union["Mat4x4", float, int]) -> "Mat4x4":
        """
        Subtract another Matrix or a scalar from this Matrix element-wise.

        Args:
            other: The Matrix to subtract from this Matrix, or a scalar to subtract from each element.

        Returns:
            A new Mat4x4 instance representing the difference.

        Raises:
            TypeError: If the operand is not a Mat4x4 object or a number.
        """
        if isinstance(other, Mat4x4):
            return Mat4x4(
                self.m00 - other.m00, self.m01 - other.m01, self.m02 - other.m02, self.m03 - other.m03,
                self.m10 - other.m10, self.m11 - other.m11, self.m12 - other.m12, self.m13 - other.m13,
                self.m20 - other.m20, self.m21 - other.m21, self.m22 - other.m22, self.m23 - other.m23,
                self.m30 - other.m30, self.m31 - other.m31, self.m32 - other.m32, self.m33 - other.m33
            )
        elif isinstance(other, (int, float)):
            return Mat4x4(
                self.m00 - other, self.m01 - other, self.m02 - other, self.m03 - other,
                self.m10 - other, self.m11 - other, self.m12 - other, self.m13 - other,
                self.m20 - other, self.m21 - other, self.m22 - other, self.m23 - other,
                self.m30 - other, self.m31 - other, self.m32 - other, self.m33 - other
            )
        raise TypeError("Operand must be of type Mat4x4, or Number")

    def __mul__(self, other: Union["Mat4x4", float, int]) -> "Mat4x4":
        """
        Multiply this Matrix by another Matrix element-wise or by a scalar.

        Args:
            other: The Matrix to multiply with this Matrix, or a scalar to multiply each element by.

        Returns:
            A new Mat4x4 instance representing the product.

        Raises:
            TypeError: If the operand is not a Mat4x4 object or a number.
        """
        if isinstance(other, Mat4x4):
            return Mat4x4(
                self.m00 * other.m00, self.m01 * other.m01, self.m02 * other.m02, self.m03 * other.m03,
                self.m10 * other.m10, self.m11 * other.m11, self.m12 * other.m12, self.m13 * other.m13,
                self.m20 * other.m20, self.m21 * other.m21, self.m22 * other.m22, self.m23 * other.m23,
                self.m30 * other.m30, self.m31 * other.m31, self.m32 * other.m32, self.m33 * other.m33
            )
        elif isinstance(other, (int, float)):
            return Mat4x4(
                self.m00 * other, self.m01 * other, self.m02 * other, self.m03 * other,
                self.m10 * other, self.m11 * other, self.m12 * other, self.m13 * other,
                self.m20 * other, self.m21 * other, self.m22 * other, self.m23 * other,
                self.m30 * other, self.m31 * other, self.m32 * other, self.m33 * other
            )
        raise TypeError("Operand must be of type Mat4x4, or Number")

    def __truediv__(self, other: Union["Mat4x4", float, int]) -> "Mat4x4":
        """
        Divide this Matrix by another Matrix element-wise or by a scalar.

        Args:
            other: The Matrix to divide this Matrix by, or a scalar to divide each element by.

        Returns:
            A new Mat4x4 instance representing the quotient.

        Raises:
            TypeError: If the operand is not a Mat4x4 object or a number.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, Mat4x4):
            return Mat4x4(
                self.m00 / other.m00 if other.m00 != 0 else float('inf'),
                self.m01 / other.m01 if other.m01 != 0 else float('inf'),
                self.m02 / other.m02 if other.m02 != 0 else float('inf'),
                self.m03 / other.m03 if other.m03 != 0 else float('inf'),
                self.m10 / other.m10 if other.m10 != 0 else float('inf'),
                self.m11 / other.m11 if other.m11 != 0 else float('inf'),
                self.m12 / other.m12 if other.m12 != 0 else float('inf'),
                self.m13 / other.m13 if other.m13 != 0 else float('inf'),
                self.m20 / other.m20 if other.m20 != 0 else float('inf'),
                self.m21 / other.m21 if other.m21 != 0 else float('inf'),
                self.m22 / other.m22 if other.m22 != 0 else float('inf'),
                self.m23 / other.m23 if other.m23 != 0 else float('inf'),
                self.m30 / other.m30 if other.m30 != 0 else float('inf'),
                self.m31 / other.m31 if other.m31 != 0 else float('inf'),
                self.m32 / other.m32 if other.m32 != 0 else float('inf'),
                self.m33 / other.m33 if other.m33 != 0 else float('inf')
            )
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Mat4x4(
                self.m00 / other, self.m01 / other, self.m02 / other, self.m03 / other,
                self.m10 / other, self.m11 / other, self.m12 / other, self.m13 / other,
                self.m20 / other, self.m21 / other, self.m22 / other, self.m23 / other,
                self.m30 / other, self.m31 / other, self.m32 / other, self.m33 / other
            )
        raise TypeError("Operand must be of type Mat4x4, or Number")


    def transpose(self) -> "Mat4x4":
        """
        Transpose the Matrix (swap rows and columns).

        Returns:
            A new Mat4x4 instance representing the transposed Matrix.
        """
        return Mat4x4(
            self.m00, self.m10, self.m20, self.m30,
            self.m01, self.m11, self.m21, self.m31,
            self.m02, self.m12, self.m22, self.m32,
            self.m03, self.m13, self.m23, self.m33
        )

    def determinant(self) -> float:
        """
        Calculate the determinant of the Matrix.

        Returns:
            The determinant of the Matrix.
        """
        return (
            self.m00 * (self.m11 * (self.m22 * self.m33 - self.m23 * self.m32) - self.m12 * (self.m21 * self.m33 - self.m23 * self.m31) + self.m13 * (self.m21 * self.m32 - self.m22 * self.m31)) -
            self.m01 * (self.m10 * (self.m22 * self.m33 - self.m23 * self.m32) - self.m12 * (self.m20 * self.m33 - self.m23 * self.m30) + self.m13 * (self.m20 * self.m32 - self.m22 * self.m30)) +
            self.m02 * (self.m10 * (self.m21 * self.m33 - self.m23 * self.m31) - self.m11 * (self.m20 * self.m33 - self.m23 * self.m30) + self.m13 * (self.m20 * self.m31 - self.m21 * self.m30)) -
            self.m03 * (self.m10 * (self.m21 * self.m32 - self.m22 * self.m31) - self.m11 * (self.m20 * self.m32 - self.m22 * self.m30) + self.m12 * (self.m20 * self.m31 - self.m21 * self.m30))
        )

        
    def to_mat3x3(self) -> Mat3x3:
        """
        Extract the top-left 3x3 portion of a Mat4x4 to create a Mat3x3.

        Args:
            self: The Mat4x4 instance to convert.

        Returns:
            A new Mat3x3 instance.
        """
        return Mat3x3(
            self.m00, self.m01, self.m02,
            self.m10, self.m11, self.m12,
            self.m20, self.m21, self.m22
        )

    def to_quaternion(self) -> Quat:
        """
        Convert this 4x4 rotation matrix to a quaternion by extracting the top-left 3x3 rotation matrix.

        Args:
            self: The Mat4x4 instance representing the rotation matrix.

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
        return hash((self.m00, self.m01, self.m02, self.m03,
                     self.m10, self.m11, self.m12, self.m13,
                     self.m20, self.m21, self.m22, self.m23,
                     self.m30, self.m31, self.m32, self.m33))
