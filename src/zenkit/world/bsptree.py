__all__ = ["BspTree", "BspNode", "BspSector", "BspTreeType"]

from ctypes import POINTER
from ctypes import Structure
from ctypes import byref
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from ctypes import c_uint32
from ctypes import c_void_p
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._core import AxisAlignedBoundingBox
from zenkit._core import Vec3f
from zenkit._core import Vec4f
from zenkit._native import ZkPointer
from zenkit._native import ZkString


class BspTreeType(IntEnum):
    INDOOR = 0
    OUTDOOR = 1


class BspNode(Structure):
    _fields_ = [
        ("_plane", Vec4f),
        ("_bbox", AxisAlignedBoundingBox),
        ("_polygon_index", c_uint32),
        ("_polygon_count", c_uint32),
        ("_front_index", c_int32),
        ("_back_index", c_int32),
        ("_parent_index", c_int32),
    ]

    @property
    def plane(self) -> Vec4f:
        return self._plane

    @property
    def bbox(self) -> AxisAlignedBoundingBox:
        return self._bbox

    @property
    def polygon_index(self) -> int:
        return self._polygon_index

    @property
    def polygon_count(self) -> int:
        return self._polygon_count

    @property
    def front_index(self) -> int:
        return self._front_index

    @property
    def back_index(self) -> int:
        return self._back_index

    @property
    def parent_index(self) -> int:
        return self._parent_index


DLL.ZkBspSector_getName.restype = ZkString
DLL.ZkBspSector_getNodeIndices.restype = POINTER(c_uint32)
DLL.ZkBspSector_getPortalPolygonIndices.restype = POINTER(c_uint32)


class BspSector:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def name(self) -> str:
        return DLL.ZkBspSector_getName(self._handle).value

    @property
    def node_indices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkBspSector_getNodeIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def portal_polygon_indices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkBspSector_getPortalPolygonIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    def __del__(self) -> None:
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<BspSector handle={self._handle} name={self.name!r}>"


DLL.ZkBspTree_getType.restype = c_int
DLL.ZkBspTree_getPolygonIndices.restype = POINTER(c_uint32)
DLL.ZkBspTree_getLeafPolygonIndices.restype = POINTER(c_uint32)
DLL.ZkBspTree_getPortalPolygonIndices.restype = POINTER(c_uint32)
DLL.ZkBspTree_getLightPointCount.restype = c_size_t
DLL.ZkBspTree_getLightPoint.restype = Vec3f
DLL.ZkBspTree_getNodeCount.restype = c_size_t
DLL.ZkBspTree_getNode.restype = BspNode
DLL.ZkBspTree_getSectorCount.restype = c_size_t
DLL.ZkBspTree_getSector.restype = ZkPointer


class BspTree:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def type(self) -> BspTreeType:
        return BspTreeType(DLL.ZkBspTree_getType(self._handle))

    @property
    def polygon_indices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkBspTree_getPolygonIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def leaf_polygon_indices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkBspTree_getLeafPolygonIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def portal_polygon_indices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkBspTree_getPortalPolygonIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def light_points(self) -> list[Vec3f]:
        count = DLL.ZkBspTree_getLightPointCount(self._handle)
        return [DLL.ZkBspTree_getLightPoint(self._handle, i) for i in range(count)]

    @property
    def nodes(self) -> list[BspNode]:
        count = DLL.ZkBspTree_getNodeCount(self._handle)
        return [DLL.ZkBspTree_getNode(self._handle, i) for i in range(count)]

    @property
    def sectors(self) -> list[BspSector]:
        count = DLL.ZkBspTree_getSectorCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkBspTree_getSector(self._handle, i).value
            items.append(BspSector(_handle=handle, _keepalive=self))

        return items

    def __del__(self) -> None:
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<BspTree handle={self._handle}>"
