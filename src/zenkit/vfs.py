__all__ = [
    "Vfs",
    "VfsNode",
    "VfsOverwriteBehavior",
]

from collections.abc import Iterator
from ctypes import CFUNCTYPE
from ctypes import c_char_p
from ctypes import c_int
from ctypes import c_long
from ctypes import c_ulong
from ctypes import c_void_p
from datetime import datetime
from datetime import timezone
from enum import IntEnum
from os import PathLike
from typing import Any
from typing import overload

from zenkit._core import DLL
from zenkit._core import GameVersion
from zenkit.stream import Read

_VfsNodeEnumerator = CFUNCTYPE(c_int, c_void_p, c_void_p)


class VfsOverwriteBehavior(IntEnum):
    NONE = 0
    ALL = 1
    NEWER = 2
    OLDER = 3


DLL.ZkVfsNode_getName.restype = c_char_p
DLL.ZkVfsNode_enumerateChildren.restype = None
DLL.ZkVfsNode_getChild.restype = c_void_p
DLL.ZkVfsNode_isFile.restype = c_int
DLL.ZkVfsNode_isDir.restype = c_int
DLL.ZkVfsNode_open.restype = c_void_p


class VfsNode:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        if "_handle" in kwargs:
            self._handle = kwargs.pop("_handle")
            self._delete = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def new_file(name: str, content: bytes | bytearray, *, timestamp: datetime | float | None = None) -> "VfsNode":
        DLL.ZkVfsNode_newFile.restype = c_void_p

        if timestamp is None:
            timestamp = datetime.now(tz=timezone.utc)
        if isinstance(timestamp, datetime):
            timestamp = timestamp.timestamp()

        handle = DLL.ZkVfsNode_newFile(name.encode("windows-1252"), content, c_ulong(len(content)), c_long(int(timestamp)))
        return VfsNode(_handle=c_void_p(handle), _delete=True)

    @staticmethod
    def new_dir(name: str, *, timestamp: datetime | float | None = None) -> "VfsNode":
        DLL.ZkVfsNode_newDir.restype = c_void_p

        if timestamp is None:
            timestamp = datetime.now(tz=timezone.utc)
        if isinstance(timestamp, datetime):
            timestamp = timestamp.timestamp()

        handle = DLL.ZkVfsNode_newDir(name.encode("windows-1252"), c_long(int(timestamp)))
        return VfsNode(_handle=c_void_p(handle), _delete=True)

    @property
    def name(self) -> str:
        return DLL.ZkVfsNode_getName(self._handle).decode("windows-1252")

    @property
    def data(self) -> bytes:
        rd = self.open()
        return rd.data

    @property
    def handle(self) -> c_void_p:
        return self._handle

    @property
    def children(self) -> list["VfsNode"]:
        if not self.is_dir():
            error = "Not a directory node"
            raise ValueError(error)

        def _enumerate(_: Any, node: int) -> int:
            nodes.append(VfsNode(_handle=c_void_p(node), _keepalive=self))
            return 0

        nodes = []
        enum = _VfsNodeEnumerator(_enumerate)
        DLL.ZkVfsNode_enumerateChildren(self._handle, enum, c_void_p(None))

        return nodes

    def get_child(self, name: str) -> "VfsNode | None":
        handle = DLL.ZkVfsNode_getChild(self._handle, name.encode("windows-1252"))
        return VfsNode(_handle=c_void_p(handle), _keepalive=self)

    def is_file(self) -> bool:
        return DLL.ZkVfsNode_isFile(self._handle) != 0

    def is_dir(self) -> bool:
        return DLL.ZkVfsNode_isDir(self._handle) != 0

    def open(self) -> "Read":
        if not self.is_file():
            error = "Not a file node"
            raise ValueError(error)

        handle = DLL.ZkVfsNode_open(self._handle)
        return Read(c_void_p(handle))

    @overload
    def create(
        self, node_or_dir_name: "VfsNode | str", /, *, timestamp: datetime | float | None = None
    ) -> "VfsNode":
        ...

    @overload
    def create(
        self, file_name: str, file_content: bytes | bytearray, /, *, timestamp: datetime | float | None = None
    ) -> "VfsNode":
        ...

    def create(self, *args: Any, **kwargs: Any) -> "VfsNode":
        DLL.ZkVfsNode_create.restype = c_void_p

        if len(args) == 1:
            if isinstance(args[0], VfsNode):
                handle = DLL.ZkVfsNode_create(self._handle, args[0].handle)
            elif isinstance(args[0], str):
                dir_ = VfsNode.new_dir(args[0], timestamp=kwargs.pop("timestamp", None))
                handle = DLL.ZkVfsNode_create(self._handle, dir_.handle)
            else:
                raise TypeError(f"Expected VfsNode instance or directory name, got {type(args[0])}")
        elif len(args) == 2:
            if not isinstance(args[0], str):
                raise TypeError(f"Expected file name (str) as the first parameter, got {type(args[0])}")
            if not isinstance(args[1], bytes | bytearray):
                raise TypeError(f"Expected content (bytes or bytearray) as the second parameter, got {type(args[0])}")
            file = VfsNode.new_file(args[0], args[1], timestamp=kwargs.pop("timestamp", None))
            handle = DLL.ZkVfsNode_create(self._handle, file.handle)
        else:
            raise ValueError(f"Expected 2 arguments, got {len(args)}")

        if handle is None or handle == 0:
            return None
        return VfsNode(_handle=c_void_p(handle), _keepalive=self)

    def remove(self, name: str) -> bool:
        DLL.ZkVfsNode_remove.restype = c_int
        return DLL.ZkVfsNode_remove(self._handle, name.encode("windows-1252")) != 0

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
            str(path).encode("windows-1252"),
            str(parent).encode("windows-1252"),
            c_int(clobber.value),
        )

    def mount_disk(
        self,
        path: str | PathLike,
        *,
        clobber: VfsOverwriteBehavior = VfsOverwriteBehavior.OLDER,
    ) -> None:
        DLL.ZkVfs_mountDiskHost.restype = None
        DLL.ZkVfs_mountDiskHost(self._handle, str(path).encode("windows-1252"), c_int(clobber.value))

    def find(self, name: str | PathLike) -> "VfsNode | None":
        DLL.ZkVfs_findNode.restype = c_void_p
        handle = DLL.ZkVfs_findNode(self._handle, str(name).encode("windows-1252"))
        return VfsNode(_handle=c_void_p(handle), _keepalive=self) if handle is not None else None

    def resolve(self, path: str | PathLike) -> "VfsNode | None":
        DLL.ZkVfs_resolvePath.restype = c_void_p
        handle = DLL.ZkVfs_resolvePath(self._handle, str(path).encode("windows-1252"))
        return VfsNode(_handle=c_void_p(handle), _keepalive=self) if handle is not None else None

    def mkdir(self, path: str | PathLike) -> VfsNode:
        DLL.ZkVfs_mkdir.restype = c_void_p
        handle = DLL.ZkVfs_mkdir(self._handle, str(path).encode("windows-1252"))
        if handle is None or handle == 0:
            return None
        return VfsNode(_handle=c_void_p(handle), _keepalive=self)

    def remove(self, path: str | PathLike) -> bool:
        DLL.ZkVfs_remove.restype = c_int
        return DLL.ZkVfs_remove(self._handle, str(path).encode("windows-1252")) != 0

    def save(self, path: str | PathLike, version: GameVersion) -> None:
        DLL.ZkVfs_save(self._handle, str(path).encode("windows-1252"), c_int(version.value))

    @property
    def root(self) -> VfsNode:
        DLL.ZkVfs_getRoot.restype = c_void_p
        handle = c_void_p(DLL.ZkVfs_getRoot(self._handle))
        return VfsNode(_handle=handle, _keepalive=self)

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkVfs_del(self._handle)
        self._handle = None
