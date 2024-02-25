__all__ = ["DLL", "Vec2f", "Vec3f", "Quat", "AxisAlignedBoundingBox", "Date"]

import atexit
import functools
from ctypes import CDLL, c_float, Structure, c_uint32, c_uint16
from datetime import datetime
from pathlib import Path
from typing import Final

_PATH = Path(__file__).parent / "native" / "linux-x64.so"
DLL: Final[CDLL] = CDLL(str(_PATH))

atexit.register(functools.partial(print, DLL))


class Date(Structure):
    _pack_ = 1
    _fields_ = [
        ("year", c_uint32),
        ("month", c_uint16),
        ("day", c_uint16),
        ("hour", c_uint16),
        ("minute", c_uint16),
        ("second", c_uint16),
    ]

    def to_datetime(self) -> datetime:
        return datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            hour=self.hour,
            minute=self.minute,
            second=self.second,
        )

    def __repr__(self) -> str:
        return f"Date(year={self.year}, month={self.month}, day={self.day}, hour={self.hour}, minute={self.minute}, second={self.second})"


class Vec2f(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
    ]

    def __repr__(self) -> str:
        return f"Vec2f(x={self.x}, y={self.y})"


class Vec3f(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]

    def __repr__(self) -> str:
        return f"Vec3f(x={self.x}, y={self.y}, z={self.z})"


class Vec4f(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]

    def __repr__(self) -> str:
        return f"Vec4f(x={self.x}, y={self.y}, z={self.z}, w={self.w})"


class Quat(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]

    def __repr__(self) -> str:
        return f"Quat(x={self.x}, y={self.y}, z={self.z}, w={self.w})"


class Mat4x4(Structure):
    _fields_ = [
        ("columns", Vec4f * 4),
    ]


class AxisAlignedBoundingBox(Structure):
    _fields_ = [
        ("min", Vec3f),
        ("max", Vec3f),
    ]

    def __repr__(self) -> str:
        return f"AxisAlignedBoundingBox(min={self.min}, max={self.max})"
