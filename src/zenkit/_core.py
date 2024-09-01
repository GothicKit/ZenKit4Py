__all__ = [
    "DLL",
    "Quat",
    "Vec2f",
    "Vec3f",
    "Vec4f",
    "Mat3x3",
    "Mat4x4",
    "AxisAlignedBoundingBox",
    "OrientedBoundingBox",
    "Date",
    "PathOrFileLike",
    "Color",
    "GameVersion",
]

import platform
from ctypes import CDLL
from ctypes import Structure
from ctypes import c_size_t
from ctypes import c_uint16
from ctypes import c_uint32
from ctypes import c_void_p
from datetime import datetime
from datetime import timezone
from enum import IntEnum
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Any
from typing import ClassVar
from typing import Final
from typing import Union

from .core.color import Color
from .core.matrix import Mat3x3
from .core.matrix import Mat4x4
from .core.quat import Quat
from .core.vector import Vec2f
from .core.vector import Vec3f
from .core.vector import Vec4f

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


class GameVersion(IntEnum):
    GOTHIC1 = 0
    GOTHIC2 = 1


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
            tzinfo=timezone.utc,
        )

    def __repr__(self) -> str:
        return (
            f"Date(year={self.year}, month={self.month}, day={self.day}, "
            f"hour={self.hour}, minute={self.minute}, second={self.second})"
        )


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
