__all__ = [
    "WayNet",
    "WayEdge",
    "WayPoint",
]

from ctypes import POINTER
from ctypes import Structure
from ctypes import byref
from ctypes import c_bool
from ctypes import c_int
from ctypes import c_size_t
from ctypes import c_uint32
from ctypes import c_void_p
from typing import Any

from zenkit._core import DLL
from zenkit._core import Vec3f
from zenkit._native import ZkPointer
from zenkit._native import ZkString


class WayEdge(Structure):
    _fields_ = [
        ("_a", c_uint32),
        ("_b", c_uint32),
    ]

    @property
    def a(self) -> int:
        return self._a

    @property
    def b(self) -> int:
        return self._b

    def __repr__(self) -> str:
        return f"<WayEdge a={self.a} b={self.b}>"


DLL.ZkWayPoint_getName.restype = ZkString
DLL.ZkWayPoint_getWaterDepth.restype = c_int
DLL.ZkWayPoint_getUnderWater.restype = c_bool
DLL.ZkWayPoint_getPosition.restype = Vec3f
DLL.ZkWayPoint_getDirection.restype = Vec3f
DLL.ZkWayPoint_getFreePoint.restype = c_bool


class WayPoint:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def name(self) -> str:
        return DLL.ZkWayPoint_getName(self._handle).value

    @property
    def water_depth(self) -> int:
        return DLL.ZkWayPoint_getWaterDepth(self._handle)

    @property
    def under_water(self) -> bool:
        return DLL.ZkWayPoint_getUnderWater(self._handle)

    @property
    def position(self) -> Vec3f:
        return DLL.ZkWayPoint_getPosition(self._handle)

    @property
    def direction(self) -> Vec3f:
        return DLL.ZkWayPoint_getDirection(self._handle)

    @property
    def free_point(self) -> bool:
        return DLL.ZkWayPoint_getFreePoint(self._handle)

    def __del__(self) -> None:
        self._handle = None

    def __repr__(self) -> str:
        return f"<WayPoint handle={self._handle} name={self.name!r}>"


DLL.ZkWayNet_getEdges.restype = POINTER(WayEdge)
DLL.ZkWayNet_getPointCount.restype = c_size_t
DLL.ZkWayNet_getPoint.restype = ZkPointer


class WayNet:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def edges(self) -> list[WayEdge]:
        count = c_size_t(0)
        handle = DLL.ZkWayNet_getEdges(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def points(self) -> list[WayPoint]:
        count = DLL.ZkWayNet_getPointCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkWayNet_getPoint(self._handle, c_size_t(i)).value
            items.append(WayPoint(_handle=handle, _keepalive=self))

        return items

    def __del__(self) -> None:
        self._handle = None

    def __repr__(self) -> str:
        return f"<WayNet handle={self._handle}>"
