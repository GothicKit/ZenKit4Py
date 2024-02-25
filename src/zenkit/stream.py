from ctypes import c_void_p, c_char_p, c_size_t
from os import PathLike

from zenkit._core import DLL


class Read:
    __slots__ = ("_handle", "_native")

    def __init__(self, source: str | PathLike | bytes | bytearray | c_void_p) -> None:
        if isinstance(source, (bytes, bytearray)):
            DLL.ZkRead_newMem.restype = c_void_p

            self._native = source
            self._handle = c_void_p(DLL.ZkRead_newMem(c_char_p(source), len(source)))
        elif isinstance(source, c_void_p):
            self._native = None
            self._handle = source
        else:
            DLL.ZkRead_newFile.restype = c_void_p

            self._native = source
            self._handle = c_void_p(
                DLL.ZkRead_newFile(c_char_p(source.encode("utf-8")))
            )

        if self._handle.value is None:
            raise ValueError("Failed to create input stream, see logs.")

    @property
    def handle(self) -> c_void_p:
        return self._handle

    @property
    def size(self) -> int:
        DLL.ZkRead_getSize.restype = c_size_t
        return DLL.ZkRead_getSize(self._handle)

    @property
    def data(self) -> bytes:
        data = bytes(self.size)

        DLL.ZkRead_getBytes.restype = c_size_t
        DLL.ZkRead_getBytes(self._handle, data, len(data))

        return data

    def __del__(self) -> None:
        DLL.ZkRead_del(self._handle)
        self._handle = None
