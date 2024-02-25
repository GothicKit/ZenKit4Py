__all__ = [
    "Texture",
    "TextureFormat",
]

from _ctypes import byref
from ctypes import c_void_p, c_int, c_uint, c_size_t, c_char_p, string_at
from enum import IntEnum
from os import PathLike

from zenkit._core import DLL
from zenkit.stream import Read
from zenkit.vfs import VfsNode


class TextureFormat(IntEnum):
    B8G8R8A8 = (0x0,)
    R8G8B8A8 = (0x1,)
    A8B8G8R8 = (0x2,)
    A8R8G8B8 = (0x3,)
    B8G8R8 = (0x4,)
    R8G8B8 = (0x5,)
    A4R4G4B4 = (0x6,)
    A1R5G5B5 = (0x7,)
    R5G6B5 = (0x8,)
    P8 = (0x9,)
    DXT1 = (0xA,)
    DXT2 = (0xB,)
    DXT3 = (0xC,)
    DXT4 = (0xD,)
    DXT5 = (0xE,)


class Texture:
    __slots__ = ("_handle",)

    def __init__(self, src: str | PathLike | Read | bytes | bytearray | VfsNode):
        rd: Read
        if isinstance(src, VfsNode):
            rd = src.open()
        elif isinstance(src, Read):
            rd = src
        else:
            rd = Read(src)

        DLL.ZkTexture_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkTexture_load(rd.handle))

    @property
    def format(self) -> TextureFormat:
        DLL.ZkTexture_getFormat.restype = c_int
        return TextureFormat(DLL.ZkTexture_getFormat(self._handle))

    @property
    def palette(self) -> list[int]:
        if self.format != TextureFormat.P8:
            raise ValueError("Not a palette texture")

        DLL.ZkTexture_getPaletteSize.restype = c_size_t
        size = DLL.ZkTexture_getPaletteSize(self._handle)

        DLL.ZkTexture_getPaletteItem.restype = c_uint
        palette = [
            DLL.ZkTexture_getPaletteItem(self._handle, c_size_t(i)) for i in range(size)
        ]

        return palette

    @property
    def width(self) -> int:
        DLL.ZkTexture_getWidth.restype = c_uint
        return DLL.ZkTexture_getWidth(self._handle)

    @property
    def height(self) -> int:
        DLL.ZkTexture_getHeight.restype = c_uint
        return DLL.ZkTexture_getHeight(self._handle)

    @property
    def width_ref(self) -> int:
        DLL.ZkTexture_getWidthRef.restype = c_uint
        return DLL.ZkTexture_getWidthRef(self._handle)

    @property
    def height_ref(self) -> int:
        DLL.ZkTexture_getHeightRef.restype = c_uint
        return DLL.ZkTexture_getHeightRef(self._handle)

    @property
    def average_color(self) -> int:
        DLL.ZkTexture_getAverageColor.restype = c_uint
        return DLL.ZkTexture_getAverageColor(self._handle)

    @property
    def mipmap_count(self) -> int:
        DLL.ZkTexture_getMipmapCount.restype = c_size_t
        return DLL.ZkTexture_getMipmapCount(self._handle)

    def width_mipmap(self, level: int) -> int:
        DLL.ZkTexture_getWidthMipmap.restype = c_uint
        return DLL.ZkTexture_getWidthMipmap(self._handle, c_size_t(level))

    def height_mipmap(self, level: int) -> int:
        DLL.ZkTexture_getHeightMipmap.restype = c_uint
        return DLL.ZkTexture_getHeightMipmap(self._handle, c_size_t(level))

    def mipmap_raw(self, level: int) -> bytes:
        DLL.ZkTexture_getMipmapRaw.restype = c_char_p
        size = c_size_t(0)
        data = c_char_p(
            DLL.ZkTexture_getMipmapRaw(self._handle, c_size_t(level), byref(size))
        )

        return bytes(string_at(data, size.value))

    def mipmap_rgba(self, level: int) -> bytes:
        size = self.width_mipmap(level) * self.height_mipmap(level) * 4
        data = bytes(size)

        DLL.ZkTexture_getMipmapRgba.restype = c_size_t
        DLL.ZkTexture_getMipmapRgba(self._handle, c_size_t(level), data, c_size_t(size))

        return data

    def __del__(self) -> None:
        DLL.ZkTexture_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return f"Texture(format={self.format!r}, width={self.width}, height={self.height}, average_color={hex(self.average_color)}, mipmap_count={self.mipmap_count})"
