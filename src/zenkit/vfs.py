__all__ = [
    "Vfs",
    "VfsNode",
    "VfsOverwriteBehavior",
]

from collections.abc import Iterator
from ctypes import CFUNCTYPE
from ctypes import c_bool
from ctypes import c_char_p
from ctypes import c_int
from ctypes import c_void_p
from enum import IntEnum
from os import PathLike
from typing import Any

from zenkit._core import DLL
from zenkit.stream import Read

_VfsNodeEnumerator = CFUNCTYPE(c_bool, c_void_p, c_void_p)


class VfsOverwriteBehavior(IntEnum):
    NONE = 0
    ALL = 1
    NEWER = 2
    OLDER = 3


DLL.ZkVfsNode_getName.restype = c_char_p
DLL.ZkVfsNode_enumerateChildren.restype = None
DLL.ZkVfsNode_getChild.restype = c_void_p
DLL.ZkVfsNode_isFile.restype = c_bool
DLL.ZkVfsNode_isDir.restype = c_bool
DLL.ZkVfsNode_open.restype = c_void_p


class VfsNode:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        if "_handle" in kwargs:
            self._handle = kwargs.pop("_handle")
            self._delete = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def name(self) -> str:
        return DLL.ZkVfsNode_getName(self._handle).decode("utf-8")

    @property
    def data(self) -> bytes:
        rd = self.open()
        return rd.data

    @property
    def children(self) -> list["VfsNode"]:
        if not self.is_dir():
            error = "Not a directory node"
            raise ValueError(error)

        nodes = []
        enum = _VfsNodeEnumerator(lambda _, node: nodes.append(VfsNode(_handle=c_void_p(node), _keepalive=self)))
        DLL.ZkVfsNode_enumerateChildren(self._handle, enum, c_void_p(None))

        return nodes

    def get_child(self, name: str) -> "VfsNode | None":
        handle = DLL.ZkVfsNode_getChild(self._handle, name.encode("utf-8"))
        return VfsNode(_handle=c_void_p(handle), _keepalive=self)

    def is_file(self) -> bool:
        return DLL.ZkVfsNode_isFile(self._handle)

    def is_dir(self) -> bool:
        return DLL.ZkVfsNode_isDir(self._handle)

    def open(self) -> "Read":
        if not self.is_file():
            error = "Not a file node"
            raise ValueError(error)

        handle = DLL.ZkVfsNode_open(self._handle)
        return Read(c_void_p(handle))

    def __iter__(self) -> Iterator["VfsNode"]:
        return iter(self.children)

    def __getitem__(self, item: str) -> "VfsNode | None":
        return self.get_child(item)

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkVfsNode_del(self._handle)
        self._keepalive = None
        self._handle = None

    def __repr__(self) -> str:
        if self.is_dir():
            return f"VfsNode(name={self.name!r}, children={len(self.children)})"
        return f"VfsNode(name={self.name!r})"


class Vfs:
    __slots__ = ("_handle", "_delete")

    def __init__(self) -> None:
        DLL.ZkVfs_new.restype = c_void_p
        self._handle = c_void_p(DLL.ZkVfs_new())
        self._delete = True

    def mount_path(
        self,
        path: str | PathLike,
        parent: str | PathLike = "/",
        *,
        clobber: VfsOverwriteBehavior = VfsOverwriteBehavior.OLDER,
    ) -> None:
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
        DLL.ZkVfs_mountDiskHost(self._handle, str(path).encode("utf-8"), c_int(clobber.value))

    def find(self, name: str | PathLike) -> "VfsNode | None":
        DLL.ZkVfs_findNode.restype = c_void_p
        handle = DLL.ZkVfs_findNode(self._handle, str(name).encode("utf-8"))
        return VfsNode(_handle=c_void_p(handle), _keepalive=self) if handle is not None else None

    def resolve(self, path: str | PathLike) -> "VfsNode | None":
        DLL.ZkVfs_resolvePath.restype = c_void_p
        handle = DLL.ZkVfs_resolvePath(self._handle, str(path).encode("utf-8"))
        return VfsNode(_handle=c_void_p(handle), _keepalive=self) if handle is not None else None

    @property
    def root(self) -> VfsNode:
        DLL.ZkVfs_getRoot.restype = c_void_p
        handle = c_void_p(DLL.ZkVfs_getRoot(self._handle))
        return VfsNode(_handle=handle, _keepalive=self)

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkVfs_del(self._handle)
        self._handle = None
