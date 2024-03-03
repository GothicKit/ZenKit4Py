__all__ = [
    "DLL",
    "Vec2f",
    "Vec3f",
    "Quat",
    "Mat4x4",
    "Mat3x3",
    "AxisAlignedBoundingBox",
    "OrientedBoundingBox",
    "Date",
    "PathOrFileLike",
    "Color",
]

import platform
from ctypes import CDLL
from ctypes import Structure
from ctypes import c_float
from ctypes import c_size_t
from ctypes import c_uint8
from ctypes import c_uint16
from ctypes import c_uint32
from ctypes import c_void_p
from datetime import datetime
from datetime import timezone
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Any
from typing import ClassVar
from typing import Final
from typing import Union

if TYPE_CHECKING:
    from zenkit.stream import Read
    from zenkit.vfs import VfsNode

_NAME = {
    "Windows": "win-x64.dll",
    "Linux": "linux-x64.so",
    "Darwin": "osx-x64.dylib",
}[platform.system()]

_PATH = Path(__file__).parent / "native" / _NAME
DLL: Final[CDLL] = CDLL(str(_PATH))

PathOrFileLike = Union[str, PathLike, "Read", bytes, bytearray, "VfsNode"]


class Date(Structure):
    _pack_ = 1
    _fields_: ClassVar[tuple[str, Any]] = [
        ("year", c_uint32),
        ("month", c_uint16),
        ("day", c_uint16),
        ("hour", c_uint16),
        ("minute", c_uint16),
        ("second", c_uint16),
    ]

    def to_datetime(self) -> datetime:
        return datetime(
            year=self.year + 1,
            month=self.month + 1,
            day=self.day + 1,
            hour=self.hour,
            minute=self.minute,
            second=self.second,
            tzinfo=timezone.utc
        )

    def __repr__(self) -> str:
        return (f"Date(year={self.year}, month={self.month}, day={self.day}, "
                f"hour={self.hour}, minute={self.minute}, second={self.second})")


class Vec2f(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
    ]

    def __repr__(self) -> str:
        return f"Vec2f(x={self.x}, y={self.y})"


class Vec3f(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]

    def __repr__(self) -> str:
        return f"Vec3f(x={self.x}, y={self.y}, z={self.z})"


class Vec4f(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]

    def __repr__(self) -> str:
        return f"Vec4f(x={self.x}, y={self.y}, z={self.z}, w={self.w})"


class Quat(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]

    def __repr__(self) -> str:
        return f"Quat(x={self.x}, y={self.y}, z={self.z}, w={self.w})"


class Mat3x3(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("_columns", Vec3f * 3),
    ]

    def columns(self) -> tuple[Vec3f, Vec3f, Vec3f]:
        return self._columns[0], self._columns[1], self._columns[2]


class Mat4x4(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("columns", Vec4f * 4),
    ]

    def columns(self) -> tuple[Vec4f, Vec4f, Vec4f, Vec4f]:
        return self._columns[0], self._columns[1], self._columns[2], self._columns[3]


class AxisAlignedBoundingBox(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("_min", Vec3f),
        ("_max", Vec3f),
    ]

    @property
    def min(self) -> Vec3f:
        return self._min

    @property
    def max(self) -> Vec3f:
        return self._max

    def __repr__(self) -> str:
        return f"AxisAlignedBoundingBox(min={self.min}, max={self.max})"


class OrientedBoundingBox:
    __slots__ = ("_handle",)

    def __init__(self, **kwargs: Any) -> None:
        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")

    @property
    def center(self) -> Vec3f:
        DLL.ZkOrientedBoundingBox_getCenter.restype = Vec3f
        return DLL.ZkOrientedBoundingBox_getCenter(self._handle)

    @property
    def axis(self) -> Vec3f:
        DLL.ZkOrientedBoundingBox_getAxis.restype = Vec3f
        return DLL.ZkOrientedBoundingBox_getAxis(self._handle)

    @property
    def half_width(self) -> Vec3f:
        DLL.ZkOrientedBoundingBox_getHalfWidth.restype = Vec3f
        return DLL.ZkOrientedBoundingBox_getHalfWidth(self._handle)

    @property
    def children(self) -> list["OrientedBoundingBox"]:
        DLL.ZkOrientedBoundingBox_getChildCount.restype = c_size_t
        count = DLL.ZkOrientedBoundingBox_getChildCount(self._handle)

        DLL.ZkOrientedBoundingBox_getChild.restype = c_void_p
        return [
            OrientedBoundingBox(_handle=c_void_p(DLL.ZkOrientedBoundingBox_getChild(self._handle, i)))
            for i in range(count)
        ]

    def to_aabb(self) -> AxisAlignedBoundingBox:
        DLL.ZkOrientedBoundingBox_toAabb.restype = AxisAlignedBoundingBox
        return DLL.ZkOrientedBoundingBox_toAabb(self._handle)


class Color(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("_r", c_uint8),
        ("_g", c_uint8),
        ("_b", c_uint8),
        ("_a", c_uint8),
    ]

    @property
    def r(self) -> int:
        return self._r

    @property
    def g(self) -> int:
        return self._g

    @property
    def b(self) -> int:
        return self._b

    @property
    def a(self) -> int:
        return self._a

    def __repr__(self) -> str:
        return f"<Color r={self._r} g={self._g} b={self._b} a={self._a}>"
