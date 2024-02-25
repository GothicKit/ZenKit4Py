__all__ = [
    "MultiResolutionMesh",
    "SubMesh",
    "MeshEdge",
    "MeshPlane",
    "MeshTriangle",
    "MeshWedge",
    "MeshTriangleEdge",
]

from _ctypes import byref
from ctypes import (
    c_void_p,
    c_size_t,
    c_bool,
    POINTER,
    c_float,
    c_uint16,
    Structure,
)
from os import PathLike
from typing import Any

from zenkit import Read, VfsNode
from zenkit._core import DLL, Vec3f, AxisAlignedBoundingBox, Vec2f, OrientedBoundingBox
from zenkit.material import Material


class MeshTriangle(Structure):
    _fields_ = [("wedges", c_uint16 * 3)]


class MeshTriangleEdge(Structure):
    _fields_ = [("edges", c_uint16 * 3)]


class MeshEdge(Structure):
    _fields_ = [("edges", c_uint16 * 2)]


class MeshWedge(Structure):
    _fields_ = [
        ("normal", Vec3f),
        ("texture", Vec2f),
        ("index", c_uint16),
    ]


class MeshPlane(Structure):
    _fields_ = [
        ("distance", c_float),
        ("normal", Vec3f),
    ]


class SubMesh:
    __slots__ = ("_handle",)

    def __init__(self, **kwargs: Any) -> None:
        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")

    @property
    def material(self) -> Material:
        DLL.ZkSubMesh_getMaterial.restype = c_void_p
        return Material(_handle=c_void_p(DLL.ZkSubMesh_getMaterial(self._handle)))

    @property
    def triangles(self) -> list[MeshTriangle]:
        count = c_size_t(0)

        DLL.ZkSubMesh_getTriangles.restype = POINTER(MeshTriangle)
        handle = DLL.ZkSubMesh_getTriangles(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def colors(self) -> list[float]:
        count = c_size_t(0)

        DLL.ZkSubMesh_getColors.restype = POINTER(c_float)
        handle = DLL.ZkSubMesh_getColors(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def triangle_plane_indices(self) -> list[int]:
        count = c_size_t(0)

        DLL.ZkSubMesh_getTrianglePlaneIndices.restype = POINTER(c_uint16)
        handle = DLL.ZkSubMesh_getTrianglePlaneIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def wedges(self) -> list[MeshWedge]:
        DLL.ZkSubMesh_getWedgeCount.restype = c_size_t
        count = DLL.ZkSubMesh_getWedgeCount(self._handle)

        DLL.ZkSubMesh_getWedge.restype = MeshWedge
        return [DLL.ZkSubMesh_getWedge(self._handle, i) for i in range(count)]

    @property
    def triangle_planes(self) -> list[MeshPlane]:
        DLL.ZkSubMesh_getTrianglePlaneCount.restype = c_size_t
        count = DLL.ZkSubMesh_getTrianglePlaneCount(self._handle)

        DLL.ZkSubMesh_getTrianglePlane.restype = MeshPlane
        return [DLL.ZkSubMesh_getTrianglePlane(self._handle, i) for i in range(count)]

    @property
    def triangle_edges(self) -> list[MeshTriangleEdge]:
        count = c_size_t(0)

        DLL.ZkSubMesh_getTriangleEdges.restype = POINTER(MeshTriangleEdge)
        handle = DLL.ZkSubMesh_getTriangleEdges(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def edge_scores(self) -> list[float]:
        count = c_size_t(0)

        DLL.ZkSubMesh_getEdgeScores.restype = POINTER(c_float)
        handle = DLL.ZkSubMesh_getEdgeScores(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def wedge_map(self) -> list[int]:
        count = c_size_t(0)

        DLL.ZkSubMesh_getWedgeMap.restype = POINTER(c_uint16)
        handle = DLL.ZkSubMesh_getWedgeMap(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def edges(self) -> list[MeshEdge]:
        count = c_size_t(0)

        DLL.ZkSubMesh_getEdges.restype = POINTER(MeshEdge)
        handle = DLL.ZkSubMesh_getEdges(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]


class MultiResolutionMesh:
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

        DLL.ZkMultiResolutionMesh_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkMultiResolutionMesh_load(rd.handle))

    @property
    def positions(self) -> list[Vec3f]:
        DLL.ZkMultiResolutionMesh_getPositionCount.restype = c_size_t
        count = DLL.ZkMultiResolutionMesh_getPositionCount(self._handle)

        DLL.ZkMultiResolutionMesh_getPosition.restype = Vec3f
        return [
            DLL.ZkMultiResolutionMesh_getPosition(self._handle, i) for i in range(count)
        ]

    @property
    def normals(self) -> list[Vec3f]:
        DLL.ZkMultiResolutionMesh_getNormalCount.restype = c_size_t
        count = DLL.ZkMultiResolutionMesh_getNormalCount(self._handle)

        DLL.ZkMultiResolutionMesh_getNormal.restype = Vec3f
        return [
            DLL.ZkMultiResolutionMesh_getNormal(self._handle, i) for i in range(count)
        ]

    @property
    def submeshes(self) -> list[SubMesh]:
        DLL.ZkMultiResolutionMesh_getSubMeshCount.restype = c_size_t
        count = DLL.ZkMultiResolutionMesh_getSubMeshCount(self._handle)

        DLL.ZkMultiResolutionMesh_getSubMesh.restype = c_void_p
        return [
            SubMesh(
                _handle=c_void_p(DLL.ZkMultiResolutionMesh_getSubMesh(self._handle, i))
            )
            for i in range(count)
        ]

    @property
    def material(self) -> list[Material]:
        DLL.ZkMultiResolutionMesh_getMaterialCount.restype = c_size_t
        count = DLL.ZkMultiResolutionMesh_getMaterialCount(self._handle)

        DLL.ZkMultiResolutionMesh_getMaterial.restype = c_void_p
        return [
            Material(
                _handle=c_void_p(DLL.ZkMultiResolutionMesh_getMaterial(self._handle, i))
            )
            for i in range(count)
        ]

    @property
    def alpha_test(self) -> bool:
        DLL.ZkMultiResolutionMesh_getAlphaTest.restype = c_bool
        return DLL.ZkMultiResolutionMesh_getAlphaTest(self._handle)

    @property
    def bbox(self) -> bool:
        DLL.ZkMultiResolutionMesh_getBbox.restype = AxisAlignedBoundingBox
        return DLL.ZkMultiResolutionMesh_getBbox(self._handle)

    @property
    def oriented_bbox(self) -> OrientedBoundingBox:
        DLL.ZkMultiResolutionMesh_getOrientedBbox.restype = c_void_p
        return OrientedBoundingBox(
            _handle=c_void_p(DLL.ZkMultiResolutionMesh_getOrientedBbox(self._handle))
        )

    def __del__(self) -> None:
        DLL.ZkMultiResolutionMesh_del.restype = None
        DLL.ZkMultiResolutionMesh_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return f"MultiResolutionMesh({self._handle.value:x})"
