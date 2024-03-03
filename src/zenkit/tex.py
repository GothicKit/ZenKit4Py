__all__ = [
    "Texture",
    "TextureFormat",
    "TextureBuilder",
]

from ctypes import byref
from ctypes import c_bool
from ctypes import c_char_p
from ctypes import c_int
from ctypes import c_size_t
from ctypes import c_uint
from ctypes import c_void_p
from ctypes import string_at
from enum import IntEnum
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._native import ZkPointer


class TextureFormat(IntEnum):
    B8G8R8A8 = 0x0
    R8G8B8A8 = 0x1
    A8B8G8R8 = 0x2
    A8R8G8B8 = 0x3
    B8G8R8 = 0x4
    R8G8B8 = 0x5
    A4R4G4B4 = 0x6
    A1R5G5B5 = 0x7
    R5G6B5 = 0x8
    P8 = 0x9
    DXT1 = 0xA
    DXT2 = 0xB
    DXT3 = 0xC
    DXT4 = 0xD
    DXT5 = 0xE


DLL.ZkTexture_getFormat.restype = c_int
DLL.ZkTexture_getPaletteSize.restype = c_size_t
DLL.ZkTexture_getPaletteItem.restype = c_uint
DLL.ZkTexture_getHeight.restype = c_uint
DLL.ZkTexture_getWidth.restype = c_uint
DLL.ZkTexture_getWidthRef.restype = c_uint
DLL.ZkTexture_getHeightRef.restype = c_uint
DLL.ZkTexture_getAverageColor.restype = c_uint
DLL.ZkTexture_getMipmapCount.restype = c_size_t
DLL.ZkTexture_getWidthMipmap.restype = c_uint
DLL.ZkTexture_getHeightMipmap.restype = c_uint
DLL.ZkTexture_getMipmapRaw.restype = c_char_p
DLL.ZkTexture_getMipmapRgba.restype = c_size_t


class Texture:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "Texture":
        handle = _native.load("ZkTexture_load", path_or_file_like)
        return Texture(_handle=handle, _delete=True)

    @property
    def format(self) -> TextureFormat:
        return TextureFormat(DLL.ZkTexture_getFormat(self._handle))

    @property
    def palette(self) -> list[int]:
        if self.format != TextureFormat.P8:
            raise ValueError("Not a palette texture")

        size = DLL.ZkTexture_getPaletteSize(self._handle)
        palette = [DLL.ZkTexture_getPaletteItem(self._handle, c_size_t(i)) for i in range(size)]

        return palette

    @property
    def width(self) -> int:
        return DLL.ZkTexture_getWidth(self._handle)

    @property
    def height(self) -> int:
        return DLL.ZkTexture_getHeight(self._handle)

    @property
    def width_ref(self) -> int:
        return DLL.ZkTexture_getWidthRef(self._handle)

    @property
    def height_ref(self) -> int:
        return DLL.ZkTexture_getHeightRef(self._handle)

    @property
    def average_color(self) -> int:
        return DLL.ZkTexture_getAverageColor(self._handle)

    @property
    def mipmap_count(self) -> int:
        return DLL.ZkTexture_getMipmapCount(self._handle)

    def width_mipmap(self, level: int) -> int:
        return DLL.ZkTexture_getWidthMipmap(self._handle, c_size_t(level))

    def height_mipmap(self, level: int) -> int:
        return DLL.ZkTexture_getHeightMipmap(self._handle, c_size_t(level))

    def mipmap_raw(self, level: int) -> bytes:
        size = c_size_t(0)
        data = c_char_p(DLL.ZkTexture_getMipmapRaw(self._handle, c_size_t(level), byref(size)))

        return bytes(string_at(data, size.value))

    def mipmap_rgba(self, level: int) -> bytes:
        size = self.width_mipmap(level) * self.height_mipmap(level) * 4
        data = bytes(size)

        DLL.ZkTexture_getMipmapRgba(self._handle, c_size_t(level), data, c_size_t(size))

        return data

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkTexture_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<Texture handle={self._handle}>"


DLL.ZkTextureBuilder_new.restype = ZkPointer
DLL.ZkTextureBuilder_addMipmap.restype = c_bool
DLL.ZkTextureBuilder_build.restype = ZkPointer


class TextureBuilder:
    __slots__ = ("_handle",)

    def __init__(self, width: int, height: int) -> None:
        self._handle = DLL.ZkTextureBuilder_new(c_size_t(width), c_size_t(height)).value

    def add_mipmap(self, data: bytes | bytearray, fmt: TextureFormat) -> "TextureBuilder":
        res = DLL.ZkTextureBuilder_addMipmap(self._handle, data, c_size_t(len(data)), fmt.value)
        if not res:
            raise ValueError("Cannot process mipmap texture; see log")
        return self

    def build(self, fmt: TextureFormat) -> Texture:
        handle = DLL.ZkTextureBuilder_build(self._handle, fmt.value).value
        return Texture(_handle=handle, _delete=False)

    def __del__(self) -> None:
        DLL.ZkTextureBuilder_del(self._handle)
        self._handle = None
