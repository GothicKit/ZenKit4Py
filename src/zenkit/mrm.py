__all__ = [
    "MultiResolutionMesh",
    "SubMesh",
    "MeshEdge",
    "MeshPlane",
    "MeshTriangle",
    "MeshWedge",
    "MeshTriangleEdge",
]

from ctypes import POINTER
from ctypes import Structure
from ctypes import byref
from ctypes import c_bool
from ctypes import c_float
from ctypes import c_size_t
from ctypes import c_uint16
from ctypes import c_void_p
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import AxisAlignedBoundingBox
from zenkit._core import OrientedBoundingBox
from zenkit._core import PathOrFileLike
from zenkit._core import Vec2f
from zenkit._core import Vec3f
from zenkit._native import ZkPointer
from zenkit.mat import Material


class MeshTriangle(Structure):
    _fields_ = [("_wedges", c_uint16 * 3)]

    @property
    def wedges(self) -> tuple[int, int, int]:
        return self._wedges[0], self._wedges[1], self._wedges[2]

    def __repr__(self) -> str:
        return f"<MeshTriangle wedges={self._wedges}>"


class MeshTriangleEdge(Structure):
    _fields_ = [("_edges", c_uint16 * 3)]

    @property
    def edges(self) -> tuple[int, int, int]:
        return self._edges[0], self._edges[1], self._edges[2]

    def __repr__(self) -> str:
        return f"<MeshTriangleEdge edges={self._wedges}>"


class MeshEdge(Structure):
    _fields_ = [("_edges", c_uint16 * 2)]

    @property
    def edges(self) -> tuple[int, int, int]:
        return self._edges[0], self._edges[1], self._edges[2]

    def __repr__(self) -> str:
        return f"<MeshEdge edges={self._wedges}>"


class MeshWedge(Structure):
    _fields_ = [
        ("_normal", Vec3f),
        ("_texture", Vec2f),
        ("_index", c_uint16),
    ]

    @property
    def normal(self) -> Vec3f:
        return self._normal

    @property
    def texture(self) -> Vec2f:
        return self._texture

    @property
    def index(self) -> int:
        return self._index

    def __repr__(self) -> str:
        return f"<MeshWedge normal={self._normal} texture={self._texture} index={self.index}>"


class MeshPlane(Structure):
    _fields_ = [
        ("_distance", c_float),
        ("_normal", Vec3f),
    ]

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def normal(self) -> Vec3f:
        return self._normal

    def __repr__(self) -> str:
        return f"<MeshPlane distance={self.distance} normal={self.normal}>"


DLL.ZkSubMesh_getMaterial.restype = ZkPointer
DLL.ZkSubMesh_getTriangles.restype = POINTER(MeshTriangle)
DLL.ZkSubMesh_getColors.restype = POINTER(c_float)
DLL.ZkSubMesh_getTrianglePlaneIndices.restype = POINTER(c_uint16)
DLL.ZkSubMesh_getWedgeCount.restype = c_size_t
DLL.ZkSubMesh_getWedge.restype = MeshWedge
DLL.ZkSubMesh_getTrianglePlaneCount.restype = c_size_t
DLL.ZkSubMesh_getTrianglePlane.restype = MeshPlane
DLL.ZkSubMesh_getTriangleEdges.restype = POINTER(MeshTriangleEdge)
DLL.ZkSubMesh_getEdgeScores.restype = POINTER(c_float)
DLL.ZkSubMesh_getWedgeMap.restype = POINTER(c_uint16)
DLL.ZkSubMesh_getEdges.restype = POINTER(MeshEdge)


class SubMesh:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def material(self) -> Material:
        return Material(_handle=DLL.ZkSubMesh_getMaterial(self._handle).value, _keepalive=self)

    @property
    def triangles(self) -> list[MeshTriangle]:
        count = c_size_t(0)
        handle = DLL.ZkSubMesh_getTriangles(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def colors(self) -> list[float]:
        count = c_size_t(0)
        handle = DLL.ZkSubMesh_getColors(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def triangle_plane_indices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkSubMesh_getTrianglePlaneIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def wedges(self) -> list[MeshWedge]:
        count = DLL.ZkSubMesh_getWedgeCount(self._handle)
        return [DLL.ZkSubMesh_getWedge(self._handle, i) for i in range(count)]

    @property
    def triangle_planes(self) -> list[MeshPlane]:
        count = DLL.ZkSubMesh_getTrianglePlaneCount(self._handle)
        return [DLL.ZkSubMesh_getTrianglePlane(self._handle, i) for i in range(count)]

    @property
    def triangle_edges(self) -> list[MeshTriangleEdge]:
        count = c_size_t(0)
        handle = DLL.ZkSubMesh_getTriangleEdges(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def edge_scores(self) -> list[float]:
        count = c_size_t(0)
        handle = DLL.ZkSubMesh_getEdgeScores(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def wedge_map(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkSubMesh_getWedgeMap(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def edges(self) -> list[MeshEdge]:
        count = c_size_t(0)
        handle = DLL.ZkSubMesh_getEdges(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    def __del__(self) -> None:
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<SubMesh handle={self._handle} material={self.material}>"


DLL.ZkMultiResolutionMesh_getPositionCount.restype = c_size_t
DLL.ZkMultiResolutionMesh_getPosition.restype = Vec3f
DLL.ZkMultiResolutionMesh_getNormalCount.restype = c_size_t
DLL.ZkMultiResolutionMesh_getNormal.restype = Vec3f
DLL.ZkMultiResolutionMesh_getSubMeshCount.restype = c_size_t
DLL.ZkMultiResolutionMesh_getSubMesh.restype = ZkPointer
DLL.ZkMultiResolutionMesh_getMaterialCount.restype = c_size_t
DLL.ZkMultiResolutionMesh_getMaterial.restype = ZkPointer
DLL.ZkMultiResolutionMesh_getAlphaTest.restype = c_bool
DLL.ZkMultiResolutionMesh_getBbox.restype = AxisAlignedBoundingBox
DLL.ZkMultiResolutionMesh_getOrientedBbox.restype = ZkPointer


class MultiResolutionMesh:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "MultiResolutionMesh":
        handle = _native.load("ZkMultiResolutionMesh_load", path_or_file_like)
        return MultiResolutionMesh(_handle=handle, _delete=True)

    @property
    def positions(self) -> list[Vec3f]:
        count = DLL.ZkMultiResolutionMesh_getPositionCount(self._handle)
        return [DLL.ZkMultiResolutionMesh_getPosition(self._handle, i) for i in range(count)]

    @property
    def normals(self) -> list[Vec3f]:
        count = DLL.ZkMultiResolutionMesh_getNormalCount(self._handle)
        return [DLL.ZkMultiResolutionMesh_getNormal(self._handle, i) for i in range(count)]

    @property
    def submeshes(self) -> list[SubMesh]:
        count = DLL.ZkMultiResolutionMesh_getSubMeshCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkMultiResolutionMesh_getSubMesh(self._handle, i).value
            items.append(SubMesh(_handle=handle, _keepalive=self))

        return items

    @property
    def material(self) -> list[Material]:
        count = DLL.ZkMultiResolutionMesh_getMaterialCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkMultiResolutionMesh_getMaterial(self._handle, i).value
            items.append(Material(_handle=handle, _keepalive=self))

        return items

    @property
    def alpha_test(self) -> bool:
        return DLL.ZkMultiResolutionMesh_getAlphaTest(self._handle)

    @property
    def bbox(self) -> bool:
        return DLL.ZkMultiResolutionMesh_getBbox(self._handle)

    @property
    def oriented_bbox(self) -> OrientedBoundingBox:
        handle = DLL.ZkMultiResolutionMesh_getOrientedBbox(self._handle).value
        return OrientedBoundingBox(_handle=handle)

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkMultiResolutionMesh_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<MultiResolutionMesh handle={self._handle}>"
