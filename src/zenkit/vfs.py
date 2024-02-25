__all__ = [
    "Vfs",
    "VfsNode",
    "VfsOverwriteBehavior",
]

from ctypes import c_char_p, CFUNCTYPE, c_bool, c_void_p, c_int
from enum import IntEnum
from os import PathLike
from typing import Any, Iterator

from zenkit._core import DLL

_VfsNodeEnumerator = CFUNCTYPE(c_bool, c_void_p, c_void_p)


class VfsOverwriteBehavior(IntEnum):
    NONE = 0
    ALL = 1
    NEWER = 2
    OLDER = 3


class VfsNode:
    __slots__ = ("_handle", "_delete")

    def __init__(self, **kwargs: Any):
        if "_handle" in kwargs:
            self._handle = kwargs.pop("_handle")
            self._delete = kwargs.pop("_delete", True)

    @property
    def name(self) -> str:
        DLL.ZkVfsNode_getName.restype = c_char_p
        name = DLL.ZkVfsNode_getName(self._handle)
        return name.decode("utf-8") if name is not None else ""

    @property
    def data(self) -> bytes:
        rd = self.open()

    @property
    def children(self) -> list["VfsNode"]:
        nodes = []

        enum = _VfsNodeEnumerator(
            lambda _, node: nodes.append(VfsNode(_handle=c_void_p(node), _delete=False))
        )
        DLL.ZkVfsNode_enumerateChildren.restype = None
        DLL.ZkVfsNode_enumerateChildren(self._handle, enum, c_void_p(None))

        return nodes

    def get_child(self, name: str) -> "VfsNode | None":
        DLL.ZkVfsNode_getChild.restype = c_void_p
        handle = DLL.ZkVfsNode_getChild(self._handle, name.encode("utf-8"))
        return (
            VfsNode(_handle=c_void_p(handle), _delete=False)
            if handle is not None
            else None
        )

    def is_file(self) -> bool:
        DLL.ZkVfsNode_isFile.restype = c_bool
        return DLL.ZkVfsNode_isFile(self._handle)

    def is_dir(self) -> bool:
        DLL.ZkVfsNode_isDir.restype = c_bool
        return DLL.ZkVfsNode_isDir(self._handle)

    def open(self) -> "Read":
        if not self.is_file():
            raise ValueError("Not a file node")

    def __iter__(self) -> Iterator["VfsNode"]:
        return iter(self.children)

    def __getitem__(self, item: str) -> "VfsNode | None":
        return self.get_child(item)

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkVfsNode_del(self._handle)

    def __repr__(self) -> str:
        return f"VfsNode(name={self.name!r}, children={len(self.children)})"


class Vfs:
    __slots__ = ("_handle",)

    def __init__(self) -> None:
        DLL.ZkVfs_new.restype = c_void_p
        self._handle = c_void_p(DLL.ZkVfs_new())

    def mount_path(
        self,
        path: str | PathLike,
        parent: str | PathLike = "/",
        *,
        clobber: VfsOverwriteBehavior = VfsOverwriteBehavior.OLDER,
    ):
        DLL.ZkVfs_mountHost.restype = None
        DLL.ZkVfs_mountHost(
            self._handle,
            str(path).encode("utf-8"),
            str(parent).encode("utf-8"),
            c_int(clobber.value),
        )

    def mount_disk(
        self,
        path: str | PathLike,
        *,
        clobber: VfsOverwriteBehavior = VfsOverwriteBehavior.OLDER,
    ) -> None:
        DLL.ZkVfs_mountDiskHost.restype = None
        DLL.ZkVfs_mountDiskHost(
            self._handle, str(path).encode("utf-8"), c_int(clobber.value)
        )

    @property
    def root(self) -> VfsNode:
        DLL.ZkVfs_getRoot.restype = c_void_p
        handle = c_void_p(DLL.ZkVfs_getRoot(self._handle))
        return VfsNode(_handle=handle, _delete=False)

    def __del__(self) -> None:
        DLL.ZkVfs_del(self._handle)
