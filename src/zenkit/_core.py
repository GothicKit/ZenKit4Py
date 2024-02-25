__all__ = ["DLL", "Vec2f"]

import atexit
import functools
from ctypes import CDLL, c_float, Structure
from pathlib import Path
from typing import Final

_PATH = Path(__file__).parent / "native" / "linux-x64.so"
DLL: Final[CDLL] = CDLL(str(_PATH))

atexit.register(functools.partial(print, DLL))


class Vec2f(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
    ]

    def __repr__(self) -> str:
        return f"Vec2f(x={self.x}, y={self.y})"
