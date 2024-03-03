__all__ = ["SoftSkinMesh", "SoftSkinWeight", "SoftSkinWedgeNormal"]

from ctypes import POINTER
from ctypes import Structure
from ctypes import byref
from ctypes import c_float
from ctypes import c_int
from ctypes import c_size_t
from ctypes import c_uint
from ctypes import c_uint8
from ctypes import c_void_p
from typing import Any
from typing import ClassVar

from zenkit._core import DLL
from zenkit._core import OrientedBoundingBox
from zenkit._core import Vec3f
from zenkit._native import ZkPointer
from zenkit.multi_resolution_mesh import MultiResolutionMesh


class SoftSkinWeight(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("_weight", c_float),
        ("_position", Vec3f),
        ("_index", c_uint8),
    ]

    @property
    def weight(self) -> float:
        return self._weight

    @property
    def position(self) -> Vec3f:
        return self._position

    @property
    def index(self) -> int:
        return self._index

    def __repr__(self) -> str:
        return f"<SoftSkinWeight weight={self.weight} position={self.position} index={self.index}>"


class SoftSkinWedgeNormal(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("_normal", Vec3f),
        ("_index", c_uint),
    ]

    @property
    def normal(self) -> Vec3f:
        return self._normal

    @property
    def index(self) -> int:
        return self._index

    def __repr__(self) -> str:
        return f"<SoftSkinWedgeNormal normal={self.normal} index={self.index}>"


DLL.ZkSoftSkinMesh_getMesh.restype = ZkPointer
DLL.ZkSoftSkinMesh_getNodeCount.restype = c_size_t
DLL.ZkSoftSkinMesh_getBbox.restype = ZkPointer
DLL.ZkSoftSkinMesh_getWeightTotal.restype = c_size_t
DLL.ZkSoftSkinMesh_getWeightCount.restype = c_size_t
DLL.ZkSoftSkinMesh_getWeight.restype = SoftSkinWeight
DLL.ZkSoftSkinMesh_getWedgeNormalCount.restype = c_size_t
DLL.ZkSoftSkinMesh_getWedgeNormal.restype = SoftSkinWedgeNormal
DLL.ZkSoftSkinMesh_getNodes.restype = POINTER(c_int)


class SoftSkinMesh:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def mesh(self) -> MultiResolutionMesh:
        handle = DLL.ZkSoftSkinMesh_getMesh(self._handle).value
        return MultiResolutionMesh(_handle=handle, _keepalive=self)

    @property
    def bboxes(self) -> list[OrientedBoundingBox]:
        count = DLL.ZkSoftSkinMesh_getNodeCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkSoftSkinMesh_getMesh(self._handle, i).value
            items.append(OrientedBoundingBox(_handle=handle))

        return items

    @property
    def weights(self) -> list[list[SoftSkinWeight]]:
        count = DLL.ZkSoftSkinMesh_getWeightTotal(self._handle)
        items = []

        for i in range(count):
            length = DLL.ZkSoftSkinMesh_getWeightCount(self._handle, i)
            items.append([DLL.ZkSoftSkinMesh_getWeight(self._handle, i, j) for j in range(length)])

        return items

    @property
    def wedge_normals(self) -> list[SoftSkinWedgeNormal]:
        count = DLL.ZkSoftSkinMesh_getWedgeNormalCount(self._handle)
        return [DLL.ZkSoftSkinMesh_getWedgeNormal(self._handle, i) for i in range(count)]

    @property
    def nodes(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkSoftSkinMesh_getNodes(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    def __del__(self) -> None:
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<SoftSkinMesh handle={self._handle}>"
