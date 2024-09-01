import math
from ctypes import Structure
from ctypes import c_float
from typing import Any
from typing import ClassVar
from typing import Union

comp = {0: "x", 1: "y", 2: "z", 3: "w"}


class Vector(Structure):
    """
    A class to represent a Vector using floats, supporting various Vector operations.

    Attributes:
        components: The components of the Vector.
    """

    _fields_: ClassVar[tuple[str, Any]] = []

    def __init__(self, *components: float):
        """
        Initialize the Vector with the given components.

        Args:
            components: The components of the Vector. Must be 2, 3, or 4 components.

        Raises:
            ValueError: If the number of components is not 2, 3, or 4.
        """
        if len(components) not in {2, 3, 4}:
            raise ValueError("Vector must have 2, 3, or 4 components.")
        self._fields_ = [(comp[i], c_float) for i in range(len(components))]
        for i, value in enumerate(components):
            setattr(self, comp[i], value)

    def __repr__(self) -> str:
        """
        Get a string representation of the Vector.

        Returns:
            A string representation of the Vector.
        """
        components = ", ".join(f"{getattr(self, comp[i])}" for i in range(len(self._fields_)))
        return f"Vector({components})"

    def __getitem__(self, index: int) -> float:
        """
        Retrieve a vector component by index.

        Args:
            index: The index of the vector component to retrieve.

        Returns:
            The value of the vector component at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self._fields_):
            return getattr(self, comp[index])
        else:
            raise IndexError("Index out of range.")

    def __neg__(self) -> "Vector":
        """
        Negate the vector.

        Returns:
            A new Vector with each component negated.
        """
        return Vector(*(-getattr(self, comp[i]) for i in range(len(self._fields_))))

    def __eq__(self, other: object) -> bool:
        """
        Check if two vectors are equal component-wise.

        Args:
            other: The vector to compare with this vector.

        Returns:
            True if the vectors are equal, False otherwise.

        Raises:
            ValueError: If the vectors do not have the same number of components.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            return all(getattr(self, comp[i]) == getattr(other, comp[i]) for i in range(len(self._fields_)))
        return False

    def __lt__(self, other: "Vector") -> bool:
        """
        Check if this vector is less than another vector based on length.

        Args:
            other: The vector to compare with this vector.

        Returns:
            True if this vector is shorter, False otherwise.

        Raises:
            ValueError: If the vectors do not have the same number of components.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            return self.length() < other.length()
        return False

    def __le__(self, other: "Vector") -> bool:
        """
        Check if this vector is less than or equal to another vector based on length.

        Args:
            other: The vector to compare with this vector.

        Returns:
            True if this vector is shorter or equal in length, False otherwise.

        Raises:
            ValueError: If the vectors do not have the same number of components.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            return self.length() <= other.length()
        return False

    def __gt__(self, other: "Vector") -> bool:
        """
        Check if this vector is greater than another vector based on length.

        Args:
            other: The vector to compare with this vector.

        Returns:
            True if this vector is longer, False otherwise.

        Raises:
            ValueError: If the vectors do not have the same number of components.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            return self.length() > other.length()
        return False

    def __ge__(self, other: "Vector") -> bool:
        """
        Check if this vector is greater than or equal to another vector based on length.

        Args:
            other: The vector to compare with this vector.

        Returns:
            True if this vector is longer or equal in length, False otherwise.

        Raises:
            ValueError: If the vectors do not have the same number of components.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            return self.length() >= other.length()
        return False

    def __add__(self, other: Union["Vector", float, int]) -> "Vector":
        """
        Add another vector or a scalar to this vector.

        Args:
            other: The vector or scalar to add.

        Returns:
            A new Vector with the result of the addition.

        Raises:
            ValueError: If the vectors do not have the same number of components.
            TypeError: If the operand is not a Vector or a scalar.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            return Vector(*(getattr(self, comp[i]) + getattr(other, comp[i]) for i in range(len(self._fields_))))
        elif isinstance(other, (int, float)):
            return Vector(*(getattr(self, comp[i]) + other for i in range(len(self._fields_))))
        raise TypeError("Operand must be of type Vector, or Number")

    def __sub__(self, other: Union["Vector", float, int]) -> "Vector":
        """
        Subtract another vector or a scalar from this vector.

        Args:
            other: The vector or scalar to subtract.

        Returns:
            A new Vector with the result of the subtraction.

        Raises:
            ValueError: If the vectors do not have the same number of components.
            TypeError: If the operand is not a Vector or a scalar.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            return Vector(*(getattr(self, comp[i]) - getattr(other, comp[i]) for i in range(len(self._fields_))))
        elif isinstance(other, (int, float)):
            return Vector(*(getattr(self, comp[i]) - other for i in range(len(self._fields_))))
        raise TypeError("Operand must be of type Vector, or Number")

    def __mul__(self, other: Union["Vector", float, int]) -> "Vector":
        """
        Multiply this vector by another vector or a scalar.

        Args:
            other: The vector or scalar to multiply by.

        Returns:
            A new Vector with the result of the multiplication.

        Raises:
            ValueError: If the vectors do not have the same number of components.
            TypeError: If the operand is not a Vector or a scalar.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            return Vector(*(getattr(self, comp[i]) * getattr(other, comp[i]) for i in range(len(self._fields_))))
        elif isinstance(other, (int, float)):
            return Vector(*(getattr(self, comp[i]) * other for i in range(len(self._fields_))))
        raise TypeError("Operand must be of type Vector, or Number")

    def __truediv__(self, other: Union["Vector", float, int]) -> "Vector":
        """
        Divide this vector by another vector or a scalar.

        Args:
            other: The vector or scalar to divide by.

        Returns:
            A new Vector with the result of the division.

        Raises:
            ValueError: If the vectors do not have the same number of components or if dividing by zero.
            TypeError: If the operand is not a Vector or a scalar.
        """
        if isinstance(other, Vector):
            if len(self._fields_) != len(other._fields_):
                raise ValueError("Vectors must have the same number of components.")
            if any(getattr(other, comp[i]) == 0 for i in range(len(self._fields_))):
                raise ValueError("Cannot divide by a Vector with zero components")
            return Vector(*(getattr(self, comp[i]) / getattr(other, comp[i]) for i in range(len(self._fields_))))
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Vector(*(getattr(self, comp[i]) / other for i in range(len(self._fields_))))
        raise TypeError("Operand must be of type Vector, or Number")

    def length(self) -> float:
        """
        Calculate the length (magnitude) of the vector.

        Returns:
            The length of the vector.
        """
        return math.sqrt(sum(getattr(self, comp[i]) ** 2 for i in range(len(self._fields_))))

    def normalize(self) -> "Vector":
        """
        Normalize the vector (make it unit length).

        Returns:
            A new Vector with the same direction but unit length.
        """
        l = self.length()
        if l > 0:
            return self / l
        return Vector(*(0.0 for _ in range(len(self._fields_))))

    def __hash__(self) -> int:
        """
        Get the hash value of the vector.

        Returns:
            The hash value of the vector.
        """
        return hash(tuple(getattr(self, comp[i]) for i in range(len(self._fields_))))


class Vec2f(Vector):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
    ]

    def __init__(self, x: float = 0.0, y: float = None):
        if y is None:
            y = x
        super().__init__(x, y)


class Vec3f(Vector):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]

    def __init__(self, x: float = 0.0, y: float = None, z: float = None):
        if y is None and z is None:
            y = z = x
        elif y is None or z is None:
            raise ValueError("Vec3f requires all intermediate components to be provided.")
        super().__init__(x, y, z)


class Vec4f(Vector):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]

    def __init__(self, x: float = 0.0, y: float = None, z: float = None, w: float = None):
        if y is None and z is None and w is None:
            y = z = w = x
        elif y is None or z is None or w is None:
            raise ValueError("Vec4f requires all intermediate components to be provided.")
        super().__init__(x, y, z, w)
