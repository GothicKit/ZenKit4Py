__all__ = ["Font", "FontGlyph"]

from ctypes import Structure
from ctypes import c_size_t
from ctypes import c_uint
from ctypes import c_uint8
from ctypes import c_void_p
from typing import Any
from typing import ClassVar

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._core import Vec2f
from zenkit._native import ZkString


class FontGlyph(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("_width", c_uint8),
        ("_top_left", Vec2f),
        ("_bottom_right", Vec2f),
    ]

    @property
    def width(self) -> int:
        return self._width

    @property
    def top_left(self) -> Vec2f:
        return self._top_left

    @property
    def bottom_right(self) -> Vec2f:
        return self._bottom_right

    def __repr__(self) -> str:
        return f"<FontGlyph width={self.width} top_left={self.top_left} bottom_right={self.bottom_right}>"


DLL.ZkFont_getName.restype = ZkString
DLL.ZkFont_getHeight.restype = c_uint
DLL.ZkFont_getGlyphCount.restype = c_size_t
DLL.ZkFont_getGlyph.restype = FontGlyph


class Font:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "Font":
        handle = _native.load("ZkFont_load", path_or_file_like)
        return Font(_handle=handle, _delete=True)

    @property
    def name(self) -> str:
        return DLL.ZkFont_getName(self._handle).value

    @property
    def height(self) -> int:
        return DLL.ZkFont_getHeight(self._handle)

    @property
    def glyphs(self) -> list[FontGlyph]:
        count = DLL.ZkFont_getGlyphCount(self._handle)
        return [DLL.ZkFont_getGlyph(self._handle, c_size_t(i)) for i in range(count)]

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkFont_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<Font handle={self._handle} name={self.name!r}>"
