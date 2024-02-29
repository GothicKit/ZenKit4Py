__all__ = [
    "World",
]

from ctypes import c_size_t
from ctypes import c_void_p
from typing import Any

from zenkit import Mesh
from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._native import ZkPointer
from zenkit.vob.virtual_object import VirtualObject
from zenkit.world.bsptree import BspTree
from zenkit.world.waynet import WayNet

DLL.ZkWorld_getMesh.restype = ZkPointer
DLL.ZkWorld_getWayNet.restype = ZkPointer
DLL.ZkWorld_getBspTree.restype = ZkPointer
DLL.ZkWorld_getRootObjectCount.restype = c_size_t
DLL.ZkWorld_getRootObject.restype = ZkPointer


class World:
    __slots__ = ("_handle", "_delete")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "World":
        handle = _native.load("ZkWorld_load", path_or_file_like)
        return World(_handle=handle, _delete=True)

    @property
    def mesh(self) -> Mesh:
        return Mesh(_handle=DLL.ZkWorld_getMesh(self._handle).value, _delete=False, _keepalive=self)

    @property
    def way_net(self) -> WayNet:
        return WayNet(_handle=DLL.ZkWorld_getWayNet(self._handle).value, _delete=False, _keepalive=self)

    @property
    def bsp_tree(self) -> BspTree:
        return BspTree(_handle=DLL.ZkWorld_getBspTree(self._handle).value, _delete=False, _keepalive=self)

    @property
    def root_objects(self) -> list[VirtualObject]:
        count = DLL.ZkWorld_getRootObjectCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkWorld_getRootObject(self._handle, i).value
            items.append(VirtualObject.from_native(handle=handle, takeref=True))

        return items

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkWorld_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return f"<World handle={self._handle}>"
