__all__ = ["Font", "FontGlyph"]

from ctypes import c_void_p, Structure, c_uint8, c_uint, c_size_t, c_char_p
from os import PathLike

from zenkit._core import DLL, Vec2f
from zenkit.stream import Read
from zenkit.vfs import VfsNode


class FontGlyph(Structure):
    _fields_ = [
        ("width", c_uint8),
        ("top_left", Vec2f),
        ("bottom_right", Vec2f),
    ]

    def __repr__(self) -> str:
        return f"FontGlyph(width={self.width}, top_left={self.top_left}, bottom_right={self.bottom_right})"


class Font:
    __slots__ = ("_handle",)

    def __init__(
        self, src: str | PathLike | Read | bytes | bytearray | VfsNode
    ) -> None:
        if src is None:
            raise ValueError("No source provided")

        rd: Read
        if isinstance(src, VfsNode):
            rd = src.open()
        elif isinstance(src, Read):
            rd = src
        else:
            rd = Read(src)

        DLL.ZkFont_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkFont_load(rd.handle))

    @property
    def name(self) -> str:
        DLL.ZkFont_getName.restype = c_char_p
        return DLL.ZkFont_getName(self._handle).decode("utf-8")

    @property
    def height(self) -> int:
        DLL.ZkFont_getHeight.restype = c_uint
        return DLL.ZkFont_getHeight(self._handle)

    @property
    def glyphs(self) -> list[FontGlyph]:
        DLL.ZkFont_getGlyphCount.restype = c_size_t
        count = DLL.ZkFont_getGlyphCount(self._handle)

        DLL.ZkFont_getGlyph.restype = FontGlyph
        return [DLL.ZkFont_getGlyph(self._handle, c_size_t(i)) for i in range(count)]

    def __del__(self) -> None:
        DLL.ZkFont_del.restype = None
        DLL.ZkFont_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return (
            f"Font(name={self.name!r}, height={self.height}, glyphs={len(self.glyphs)})"
        )
