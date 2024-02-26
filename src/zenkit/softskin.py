__all__ = ["SoftSkinMesh", "SoftSkinWeight", "SoftSkinWedgeNormal"]

from _ctypes import byref
from ctypes import (
    c_void_p,
    c_size_t,
    Structure,
    c_uint8,
    c_float,
    c_uint,
    c_int,
    POINTER,
)
from typing import Any

from zenkit import MultiResolutionMesh
from zenkit._core import DLL, OrientedBoundingBox, Vec3f


class SoftSkinWeight(Structure):
    _fields_ = [
        ("weight", c_float),
        ("position", Vec3f),
        ("index", c_uint8),
    ]


class SoftSkinWedgeNormal(Structure):
    _fields_ = [("normal", Vec3f), ("index", c_uint)]


class SoftSkinMesh:
    __slots__ = ("_handle",)

    def __init__(self, **kwargs: Any) -> None:
        self._handle = kwargs.pop("_handle")

    @property
    def mesh(self) -> MultiResolutionMesh:
        DLL.ZkSoftSkinMesh_getMesh.restype = c_void_p
        return MultiResolutionMesh(
            _handle=c_void_p(DLL.ZkSoftSkinMesh_getMesh(self._handle))
        )

    @property
    def bboxes(self) -> list[OrientedBoundingBox]:
        DLL.ZkSoftSkinMesh_getNodeCount.restype = c_size_t
        count = DLL.ZkSoftSkinMesh_getNodeCount(self._handle)

        DLL.ZkSoftSkinMesh_getBbox.restype = c_void_p
        return [
            OrientedBoundingBox(
                _handle=c_void_p(DLL.ZkSoftSkinMesh_getMesh(self._handle, i))
            )
            for i in range(count)
        ]

    @property
    def weights(self) -> list[list[SoftSkinWeight]]:
        DLL.ZkSoftSkinMesh_getWeightTotal.restype = c_size_t
        count_outer = DLL.ZkSoftSkinMesh_getWeightTotal(self._handle)

        DLL.ZkSoftSkinMesh_getWeightCount.restype = c_size_t
        DLL.ZkSoftSkinMesh_getWeight.restype = SoftSkinWeight
        return [
            [
                DLL.ZkSoftSkinMesh_getWeight(self._handle, i, j)
                for j in range(DLL.ZkSoftSkinMesh_getWeightCount(self._handle, i))
            ]
            for i in range(count_outer)
        ]

    @property
    def wedge_normals(self) -> list[SoftSkinWedgeNormal]:
        DLL.ZkSoftSkinMesh_getWedgeNormalCount.restype = c_size_t
        count = DLL.ZkSoftSkinMesh_getWedgeNormalCount(self._handle)

        DLL.ZkSoftSkinMesh_getWedgeNormal.restype = SoftSkinWedgeNormal
        return [
            DLL.ZkSoftSkinMesh_getWedgeNormal(self._handle, i) for i in range(count)
        ]

    @property
    def nodes(self) -> list[int]:
        count = c_size_t(0)

        DLL.ZkSoftSkinMesh_getNodes.restype = POINTER(c_int)
        handle = DLL.ZkSoftSkinMesh_getNodes(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]
