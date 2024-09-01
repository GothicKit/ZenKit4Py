import math
from ctypes import Structure
from typing import Any
from typing import ClassVar
from typing import Union

from zenkit.core import Quat
from zenkit.core.vector import Vec3f
from zenkit.core.vector import Vec4f


class Mat3x3(Structure):
    """
    A class to represent a 3x3 Matrix using 3 Vec3f columns.

    Attributes:
        columns: The columns of the Matrix, each being a Vec3f.
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("columns", Vec3f * 3),
    ]

    def __init__(self, c0: Vec3f = None, c1: Vec3f = None, c2: Vec3f = None) -> "Mat3x3":
        if c0 is None or c1 is None or c2 is None:
            c0 = (1.0, 0.0, 0.0)
            c1 = (0.0, 1.0, 0.0)
            c2 = (0.0, 0.0, 1.0)
        self.columns = (c0, c1, c2)

    def __repr__(self) -> str:
        """
        Return a string representation of the Matrix.

        Returns:
            A string in the format 'Mat3x3(columns)'.
        """
        return f"Mat3x3(columns=[\n" f"  {self.columns[0]},\n" f"  {self.columns[1]},\n" f"  {self.columns[2]}\n" f"])"

    def columns(self) -> tuple[Vec3f, Vec3f, Vec3f]:
        """
        Return the columns of the Matrix as a tuple of Vec3f.

        Returns:
            A tuple containing the three Vec3f columns of the Matrix.
        """
        return self.columns[0], self.columns[1], self.columns[2]

    def __eq__(self, other: object) -> bool:
        """
        Check if two Matrices are equal component-wise.

        Args:
            other: The Matrix to compare with this Matrix.

        Returns:
            True if the Matrices are equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Mat3x3 objects.
        """
        if isinstance(other, Mat3x3):
            return all(self.columns[i] == other.columns[i] for i in range(3))
        return False

    def __add__(self, other: "Mat3x3") -> "Mat3x3":
        """
        Add this Matrix to another Matrix component-wise.

        Args:
            other: The Matrix to add to this Matrix.

        Returns:
            A new Mat3x3 instance representing the sum.

        Raises:
            TypeError: If the operand is not a Mat3x3 object.
        """
        if isinstance(other, Mat3x3):
            return Mat3x3(Vec3f(self.columns[i] + other.columns[i]) for i in range(3))
        raise TypeError("Operand must be of type Mat3x3")

    def __sub__(self, other: "Mat3x3") -> "Mat3x3":
        """
        Subtract another Matrix from this Matrix component-wise.

        Args:
            other: The Matrix to subtract from this Matrix.

        Returns:
            A new Mat3x3 instance representing the difference.

        Raises:
            TypeError: If the operand is not a Mat3x3 object.
        """
        if isinstance(other, Mat3x3):
            return Mat3x3(Vec3f(self.columns[i] - other.columns[i]) for i in range(3))
        raise TypeError("Operand must be of type Mat3x3")

    def __mul__(self, other: Union["Mat3x3", Vec3f, float, int]) -> Union["Mat3x3", Vec3f]:
        """
        Multiply this Matrix by another Matrix, Vector, or scalar.

        Args:
            other: The Matrix, Vector, or scalar to multiply with this Matrix.

        Returns:
            A new Mat3x3 or Vec3f instance representing the product.

        Raises:
            TypeError: If the operand is not a Mat3x3, Vec3f object, or a number.
        """
        if isinstance(other, Mat3x3):
            result_columns = [
                Vec3f(*[sum(self.columns[j][k] * other.columns[i][j] for j in range(3)) for k in range(3)])
                for i in range(3)
            ]
            return Mat3x3(*result_columns)
        elif isinstance(other, Vec3f):
            return Vec3f(*[sum(self.columns[i][j] * other[i] for i in range(3)) for j in range(3)])
        elif isinstance(other, (int, float)):
            return Mat3x3(Vec3f(self.columns[i] * other) for i in range(3))
        raise TypeError("Operand must be of type Mat3x3, Vec3f, or Number")

    def transpose(self) -> "Mat3x3":
        """
        Transpose the Matrix (swap rows and columns).

        Returns:
            A new Mat3x3 instance representing the transposed Matrix.
        """
        transposed_columns = [Vec3f(self.columns[0][i], self.columns[1][i], self.columns[2][i]) for i in range(3)]
        return Mat3x3(*transposed_columns)

    def to_euler(self) -> Vec3f:
        """
        Convert the Matrix to Euler angles (roll, pitch, yaw).

        Returns:
            A tuple containing the Euler angles (roll, pitch, yaw) in radians.
        """
        m = [[self.columns[i][j] for j in range(3)] for i in range(3)]

        if m[0][2] < 1:
            if m[0][2] > -1:
                yaw = math.atan2(-m[0][1], m[0][0])
                pitch = math.asin(m[0][2])
                roll = math.atan2(-m[1][2], m[2][2])
            else:
                yaw = -math.atan2(m[1][0], m[1][1])
                pitch = -math.pi / 2
                roll = 0
        else:
            yaw = math.atan2(m[1][0], m[1][1])
            pitch = math.pi / 2
            roll = 0

        return Vec3f(roll, pitch, yaw)

    def to_quaternion(self) -> Quat:
        """
        Convert the Matrix to a Quaternion.

        Returns:
            A Quat representing the Quaternion (w, x, y, z).
        """
        m = [[self.columns[i][j] for j in range(3)] for i in range(3)]
        trace = m[0][0] + m[1][1] + m[2][2]

        if trace > 0:
            s = 0.5 / math.sqrt(trace + 1.0)
            w = 0.25 / s
            x = (m[2][1] - m[1][2]) * s
            y = (m[0][2] - m[2][0]) * s
            z = (m[1][0] - m[0][1]) * s
        elif m[0][0] > m[1][1] and m[0][0] > m[2][2]:
            s = 2.0 * math.sqrt(1.0 + m[0][0] - m[1][1] - m[2][2])
            w = (m[2][1] - m[1][2]) / s
            x = 0.25 * s
            y = (m[0][1] + m[1][0]) / s
            z = (m[0][2] + m[2][0]) / s
        elif m[1][1] > m[2][2]:
            s = 2.0 * math.sqrt(1.0 + m[1][1] - m[0][0] - m[2][2])
            w = (m[0][2] - m[2][0]) / s
            x = (m[0][1] + m[1][0]) / s
            y = 0.25 * s
            z = (m[1][2] + m[2][1]) / s
        else:
            s = 2.0 * math.sqrt(1.0 + m[2][2] - m[0][0] - m[1][1])
            w = (m[1][0] - m[0][1]) / s
            x = (m[0][2] + m[2][0]) / s
            y = (m[1][2] + m[2][1]) / s
            z = 0.25 * s

        return Quat(w, x, y, z)

    def rotation(self, angle: float, axis: Vec3f) -> "Mat3x3":
        """
        Apply a rotation to the current matrix around the given axis by the specified angle in radians.

        Args:
            angle: The angle of rotation in radians.
            axis: The axis to rotate around as a Vec3f. This vector will be normalized before applying the rotation.

        Returns:
            A new Mat3x3 instance with the applied rotation.
        """
        axis = axis.normalize()
        x, y, z = axis.x, axis.y, axis.z
        c = math.cos(angle)
        s = math.sin(angle)
        t = 1 - c

        rot_matrix = Mat3x3(
            Vec3f(t * x * x + c, t * x * y - s * z, t * x * z + s * y),
            Vec3f(t * x * y + s * z, t * y * y + c, t * y * z - s * x),
            Vec3f(t * x * z - s * y, t * y * z + s * x, t * z * z + c),
        )
        return self * rot_matrix

    def scale(self, scale: Vec3f) -> "Mat3x3":
        """
        Apply scaling to the current matrix by the specified scale vector.

        Args:
            scale: The scaling factors along the x, y, and z axes as a Vec3f.

        Returns:
            A new Mat3x3 instance with the applied scaling.
        """
        scale_matrix = Mat3x3(Vec3f(scale.x, 0, 0), Vec3f(0, scale.y, 0), Vec3f(0, 0, scale.z))
        return self * scale_matrix

    def to_mat4x4(self) -> "Mat4x4":
        """
        Convert the 3x3 Matrix to a 4x4 Matrix.

        Returns:
            A Mat4x4 instance representing the 3x3 Matrix with a 4th row and column for homogeneous coordinates.
        """
        col0 = Vec4f(self.columns[0].x, self.columns[0].y, self.columns[0].z, 0.0)
        col1 = Vec4f(self.columns[1].x, self.columns[1].y, self.columns[1].z, 0.0)
        col2 = Vec4f(self.columns[2].x, self.columns[2].y, self.columns[2].z, 0.0)
        col3 = Vec4f(0.0, 0.0, 0.0, 1.0)

        return Mat4x4(col0, col1, col2, col3)

    def __hash__(self) -> int:
        """
        Return a hash value for this Matrix based on its columns.

        Returns:
            The hash value of the Matrix.
        """
        return hash(tuple(self.columns))


class Mat4x4(Structure):
    """
    A class to represent a 4x4 Matrix using 4 Vec4f columns.

    Attributes:
        columns: The columns of the Matrix, each being a Vec4f.
    """

    _fields_: ClassVar[tuple[str, Any]] = [
        ("columns", Vec4f * 4),
    ]

    def __init__(self, c0: Vec4f = None, c1: Vec4f = None, c2: Vec4f = None, c3: Vec4f = None) -> "Mat4x4":
        if c0 is None or c1 is None or c2 is None or c3 is None:
            c0 = Vec4f(1.0, 0.0, 0.0, 0.0)
            c1 = Vec4f(0.0, 1.0, 0.0, 0.0)
            c2 = Vec4f(0.0, 0.0, 1.0, 0.0)
            c3 = Vec4f(0.0, 0.0, 0.0, 1.0)
        self.columns = (c0, c1, c2, c3)

    def __repr__(self) -> str:
        """
        Return a string representation of the Matrix.

        Returns:
            A string in the format 'Mat4x4(columns)'.
        """
        return (
            f"Mat4x4(columns=[\n"
            f"  {self.columns[0]},\n"
            f"  {self.columns[1]},\n"
            f"  {self.columns[2]},\n"
            f"  {self.columns[3]}\n"
            f"])"
        )

    def columns(self) -> tuple[Vec4f, Vec4f, Vec4f, Vec4f]:
        """
        Return the columns of the Matrix as a tuple of Vec4f.

        Returns:
            A tuple containing the four Vec4f columns of the Matrix.
        """
        return self.columns[0], self.columns[1], self.columns[2], self.columns[3]

    def __eq__(self, other: object) -> bool:
        """
        Check if two Matrices are equal component-wise.

        Args:
            other: The Matrix to compare with this Matrix.

        Returns:
            True if the Matrices are equal, False otherwise.

        Raises:
            TypeError: If the comparison is not between two Mat4x4 objects.
        """
        if isinstance(other, Mat4x4):
            return all(self.columns[i] == other.columns[i] for i in range(4))
        return False

    def __add__(self, other: "Mat4x4") -> "Mat4x4":
        """
        Add this Matrix to another Matrix component-wise.

        Args:
            other: The Matrix to add to this Matrix.

        Returns:
            A new Mat4x4 instance representing the sum.

        Raises:
            TypeError: If the operand is not a Mat4x4 object.
        """
        if isinstance(other, Mat4x4):
            return Mat4x4(Vec4f(self.columns[i] + other.columns[i]) for i in range(4))
        raise TypeError("Operand must be of type Mat4x4")

    def __sub__(self, other: "Mat4x4") -> "Mat4x4":
        """
        Subtract another Matrix from this Matrix component-wise.

        Args:
            other: The Matrix to subtract from this Matrix.

        Returns:
            A new Mat4x4 instance representing the difference.

        Raises:
            TypeError: If the operand is not a Mat4x4 object.
        """
        if isinstance(other, Mat4x4):
            return Mat4x4(Vec4f(self.columns[i] - other.columns[i]) for i in range(4))
        raise TypeError("Operand must be of type Mat4x4")

    def __mul__(self, other: Union["Mat4x4", Vec4f, float, int]) -> Union["Mat4x4", Vec4f]:
        """
        Multiply this Matrix by another Matrix, Vector, or scalar.

        Args:
            other: The Matrix, Vector, or scalar to multiply with this Matrix.

        Returns:
            A new Mat4x4 or Vec4f instance representing the product.

        Raises:
            TypeError: If the operand is not a Mat4x4, Vec4f object, or a number.
        """
        if isinstance(other, Mat4x4):
            result_columns = [
                Vec4f(*[sum(self.columns[j][k] * other.columns[i][j] for j in range(4)) for k in range(4)])
                for i in range(4)
            ]
            return Mat4x4(*result_columns)
        elif isinstance(other, Vec4f):
            return Vec4f(*[sum(self.columns[i][j] * other[i] for i in range(4)) for j in range(4)])
        elif isinstance(other, (int, float)):
            return Mat4x4(Vec4f(self.columns[i] * other) for i in range(4))
        raise TypeError("Operand must be of type Mat4x4, Vec4f, or Number")

    def transpose(self) -> "Mat4x4":
        """
        Transpose the Matrix (swap rows and columns).

        Returns:
            A new Mat4x4 instance representing the transposed Matrix.
        """
        transposed_columns = [
            Vec4f(self.columns[0][i], self.columns[1][i], self.columns[2][i], self.columns[3][i]) for i in range(4)
        ]
        return Mat4x4(*transposed_columns)

    def to_euler(self) -> Vec3f:
        """
        Convert the Matrix to Euler angles (roll, pitch, yaw).

        Returns:
            A tuple containing the Euler angles (roll, pitch, yaw) in radians.
        """
        m = [[self.columns[i][j] for j in range(4)] for i in range(4)]

        if m[0][2] < 1:
            if m[0][2] > -1:
                yaw = math.atan2(-m[0][1], m[0][0])
                pitch = math.asin(m[0][2])
                roll = math.atan2(-m[1][2], m[2][2])
            else:
                yaw = -math.atan2(m[1][0], m[1][1])
                pitch = -math.pi / 2
                roll = 0
        else:
            yaw = math.atan2(m[1][0], m[1][1])
            pitch = math.pi / 2
            roll = 0

        return Vec3f(roll, pitch, yaw)

    def to_quaternion(self) -> Quat:
        """
        Convert the Matrix to a Quaternion.

        Returns:
            A Quat instance representing the Quaternion (w, x, y, z).
        """
        m = [[self.columns[i][j] for j in range(4)] for i in range(4)]

        trace = m[0][0] + m[1][1] + m[2][2]
        if trace > 0:
            s = 0.5 / math.sqrt(trace + 1.0)
            w = 0.25 / s
            x = (m[2][1] - m[1][2]) * s
            y = (m[0][2] - m[2][0]) * s
            z = (m[1][0] - m[0][1]) * s
        elif m[0][0] > m[1][1] and m[0][0] > m[2][2]:
            s = 2.0 * math.sqrt(1.0 + m[0][0] - m[1][1] - m[2][2])
            w = (m[2][1] - m[1][2]) / s
            x = 0.25 * s
            y = (m[0][1] + m[1][0]) / s
            z = (m[0][2] + m[2][0]) / s
        elif m[1][1] > m[2][2]:
            s = 2.0 * math.sqrt(1.0 + m[1][1] - m[0][0] - m[2][2])
            w = (m[0][2] - m[2][0]) / s
            x = (m[0][1] + m[1][0]) / s
            y = 0.25 * s
            z = (m[1][2] + m[2][1]) / s
        else:
            s = 2.0 * math.sqrt(1.0 + m[2][2] - m[0][0] - m[1][1])
            w = (m[1][0] - m[0][1]) / s
            x = (m[0][2] + m[2][0]) / s
            y = (m[1][2] + m[2][1]) / s
            z = 0.25 * s

        return Quat(w, x, y, z)

    def rotation(self, angle: float, axis: Vec3f) -> "Mat4x4":
        """
        Apply a rotation to the current matrix.

        Args:
            angle: The rotation angle in radians.
            axis: The rotation axis as a Vec3f.

        Returns:
            A new Mat4x4 instance with the additional rotation applied.
        """
        axis = axis.normalize()
        x, y, z = axis.x, axis.y, axis.z
        c = math.cos(angle)
        s = math.sin(angle)
        t = 1 - c

        rot_matrix = Mat4x4(
            Vec4f(t * x * x + c, t * x * y - s * z, t * x * z + s * y, 0),
            Vec4f(t * x * y + s * z, t * y * y + c, t * y * z - s * x, 0),
            Vec4f(t * x * z - s * y, t * y * z + s * x, t * z * z + c, 0),
            Vec4f(0, 0, 0, 1),
        )
        return self * rot_matrix

    def scale(self, scale: Vec3f) -> "Mat4x4":
        """
        Apply scaling to the current matrix.

        Args:
            scale: The scaling vector as a Vec3f.

        Returns:
            A new Mat4x4 instance with the additional scaling applied.
        """
        scale_matrix = Mat4x4(
            Vec4f(scale.x, 0, 0, 0), Vec4f(0, scale.y, 0, 0), Vec4f(0, 0, scale.z, 0), Vec4f(0, 0, 0, 1)
        )
        return self * scale_matrix

    def translation(self, translation: Vec3f) -> "Mat4x4":
        """
        Apply translation to the current matrix.

        Args:
            translation: The translation vector as a Vec3f.

        Returns:
            A new Mat4x4 instance with the additional translation applied.
        """
        translation_matrix = Mat4x4(
            Vec4f(1, 0, 0, translation.x),
            Vec4f(0, 1, 0, translation.y),
            Vec4f(0, 0, 1, translation.z),
            Vec4f(0, 0, 0, 1),
        )
        return self * translation_matrix

    def to_mat3x3(self) -> "Mat3x3":
        """
        Convert the 4x4 Matrix to a 3x3 Matrix by extracting the top-left 3x3 portion.

        Returns:
            A Mat3x3 instance representing the top-left 3x3 portion of the 4x4 Matrix.
        """
        col0 = Vec3f(self.columns[0].x, self.columns[0].y, self.columns[0].z)
        col1 = Vec3f(self.columns[1].x, self.columns[1].y, self.columns[1].z)
        col2 = Vec3f(self.columns[2].x, self.columns[2].y, self.columns[2].z)

        return Mat3x3(col0, col1, col2)

    def __hash__(self) -> int:
        """
        Return a hash value for this Matrix based on its columns.

        Returns:
            The hash value of the Matrix.
        """
        return hash(tuple(self.columns))
