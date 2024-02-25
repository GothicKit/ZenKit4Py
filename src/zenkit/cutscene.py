__all__ = [
    "CutsceneLibrary",
    "CutsceneMessage",
    "CutsceneBlock",
]

from ctypes import c_void_p, c_char_p, c_size_t, c_uint
from os import PathLike

from zenkit import Read, VfsNode
from zenkit._core import DLL


class CutsceneMessage:
    __slots__ = ("_handle",)

    def __init__(self, handle: c_void_p) -> None:
        self._handle = handle

    @property
    def type(self) -> int:
        DLL.ZkCutsceneMessage_getType.restype = c_uint
        return DLL.ZkCutsceneMessage_getType(self._handle)

    @property
    def name(self) -> str:
        DLL.ZkCutsceneMessage_getName.restype = c_char_p
        handle = DLL.ZkCutsceneMessage_getName(self._handle)
        return handle.decode("utf-8")

    @property
    def text(self) -> str:
        DLL.ZkCutsceneMessage_getText.restype = c_char_p
        handle = DLL.ZkCutsceneMessage_getText(self._handle)
        return handle.decode("utf-8")

    def __repr__(self) -> str:
        return (
            f"CutsceneMessage(type={self.type}, name={self.name!r}, text={self.text!r})"
        )


class CutsceneBlock:
    __slots__ = ("_handle",)

    def __init__(self, handle: c_void_p) -> None:
        self._handle = handle

    @property
    def name(self) -> str:
        DLL.ZkCutsceneBlock_getName.restype = c_char_p
        handle = DLL.ZkCutsceneBlock_getName(self._handle)
        return handle.decode("utf-8")

    @property
    def message(self) -> CutsceneMessage:
        DLL.ZkCutsceneBlock_getMessage.restype = c_void_p
        handle = c_void_p(DLL.ZkCutsceneBlock_getMessage(self._handle))
        return CutsceneMessage(handle)

    def __repr__(self) -> str:
        return f"CutsceneBlock(name={self.name!r}, message={self.message})"


class CutsceneLibrary:
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

        DLL.ZkCutsceneLibrary_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkCutsceneLibrary_load(rd.handle))

    @property
    def blocks(self) -> list[CutsceneBlock]:
        DLL.ZkCutsceneLibrary_getBlockCount.restype = c_size_t
        count = DLL.ZkCutsceneLibrary_getBlockCount(self._handle)

        DLL.ZkCutsceneLibrary_getBlockByIndex.restype = c_void_p
        return [
            CutsceneBlock(
                c_void_p(DLL.ZkCutsceneLibrary_getBlockByIndex(self._handle, i))
            )
            for i in range(count)
        ]

    def get(self, name: str) -> "CutsceneBlock | None":
        DLL.ZkCutsceneLibrary_getBlock.restype = c_void_p
        handle = DLL.ZkCutsceneLibrary_getBlock(self._handle, name.encode("utf-8"))
        return CutsceneBlock(c_void_p(handle)) if handle is not None else None

    def __getitem__(self, name: str) -> "CutsceneBlock | None":
        return self.get(name)

    def __contains__(self, name: str) -> bool:
        return self.get(name) is not None

    def __del__(self) -> None:
        DLL.ZkCutsceneLibrary_del.restype = None
        DLL.ZkCutsceneLibrary_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return f"CutsceneBlock(blocks={len(self.blocks)})"
