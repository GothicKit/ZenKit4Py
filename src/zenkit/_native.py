__all__ = ["ZkString", "ZkPointer", "load"]

from ctypes import c_char_p
from ctypes import c_void_p

from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit.stream import Read
from zenkit.vfs import VfsNode


class ZkString(c_char_p):
    @property
    def value(self) -> str:
        value = super().value

        if value is None:
            raise ValueError("Failed to load native string")

        return value.decode("utf-8")


class ZkPointer(c_void_p):
    @property
    def value(self) -> c_void_p:
        return c_void_p(super().value)


def load(load: str, src: PathOrFileLike) -> c_void_p:
    if src is None:
        return c_void_p(None)

    rd: Read
    if isinstance(src, VfsNode):
        rd = src.open()
    elif isinstance(src, Read):
        rd = src
    else:
        rd = Read(src)

    fn = getattr(DLL, load)
    fn.restype = c_void_p
    return c_void_p(fn(rd.handle))
