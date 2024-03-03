__all__ = [
    "CutsceneLibrary",
    "CutsceneMessage",
    "CutsceneBlock",
]

from ctypes import c_size_t
from ctypes import c_uint
from ctypes import c_void_p
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._native import ZkPointer
from zenkit._native import ZkString

DLL.ZkCutsceneMessage_getType.restype = c_uint
DLL.ZkCutsceneMessage_getName.restype = ZkString
DLL.ZkCutsceneMessage_getText.restype = ZkString


class CutsceneMessage:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def type(self) -> int:
        return DLL.ZkCutsceneMessage_getType(self._handle)

    @property
    def name(self) -> str:
        return DLL.ZkCutsceneMessage_getName(self._handle).value

    @property
    def text(self) -> str:
        return DLL.ZkCutsceneMessage_getText(self._handle).value

    def __del__(self) -> None:
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<CutsceneMessage handle={self._handle} name={self.name!r}>"


DLL.ZkCutsceneBlock_getName.restype = ZkString
DLL.ZkCutsceneBlock_getMessage.restype = ZkPointer


class CutsceneBlock:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive")

    @property
    def name(self) -> str:
        return DLL.ZkCutsceneBlock_getName(self._handle).value

    @property
    def message(self) -> CutsceneMessage:
        handle = DLL.ZkCutsceneBlock_getMessage(self._handle).value
        return CutsceneMessage(_handle=handle, _keepalive=self)

    def __del__(self) -> None:
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<CutsceneBlock handle={self._handle} name={self.name!r}>"


DLL.ZkCutsceneLibrary_getBlockCount.restype = c_size_t
DLL.ZkCutsceneLibrary_getBlockByIndex.restype = ZkPointer
DLL.ZkCutsceneLibrary_getBlock.restype = ZkPointer


class CutsceneLibrary:
    __slots__ = ("_handle", "_delete")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "CutsceneLibrary":
        handle = _native.load("ZkCutsceneLibrary_load", path_or_file_like)
        return CutsceneLibrary(_handle=handle, _delete=True)

    @property
    def blocks(self) -> list[CutsceneBlock]:
        count = DLL.ZkCutsceneLibrary_getBlockCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkCutsceneLibrary_getBlockByIndex(self._handle, i).value
            items.append(CutsceneBlock(_handle=handle, _keepalive=self))

        return items

    def get(self, name: str) -> "CutsceneBlock | None":
        handle = DLL.ZkCutsceneLibrary_getBlock(self._handle, name.encode("utf-8")).value
        if handle is None:
            return None
        return CutsceneBlock(_handle=handle, _keepalive=self)

    def __getitem__(self, name: str) -> "CutsceneBlock | None":
        return self.get(name)

    def __contains__(self, name: str) -> bool:
        return self.get(name) is not None

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkCutsceneLibrary_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return f"<CutsceneLibrary handle={self._handle}>"
