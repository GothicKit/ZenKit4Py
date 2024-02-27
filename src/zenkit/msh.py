__all__ = [
    "Mesh",
]

from ctypes import POINTER
from ctypes import Structure
from ctypes import byref
from ctypes import c_bool
from ctypes import c_int16
from ctypes import c_int32
from ctypes import c_size_t
from ctypes import c_uint8
from ctypes import c_uint32
from ctypes import c_void_p
from datetime import datetime
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import AxisAlignedBoundingBox
from zenkit._core import Date
from zenkit._core import OrientedBoundingBox
from zenkit._core import PathOrFileLike
from zenkit._core import Vec2f
from zenkit._core import Vec3f
from zenkit._native import ZkPointer
from zenkit._native import ZkString
from zenkit.mat import Material
from zenkit.tex import Texture


class Feature(Structure):
    _fields_ = [
        ("_texture", Vec2f),
        ("_light", c_uint32),
        ("_normal", Vec3f),
    ]

    @property
    def texture(self) -> Vec2f:
        return self._texture

    @property
    def light(self) -> int:
        return self._light

    @property
    def normal(self) -> Vec3f:
        return self._normal


DLL.ZkPolygon_getMaterialIndex.restype = c_uint32
DLL.ZkPolygon_getLightMapIndex.restype = c_int32
DLL.ZkPolygon_getPositionIndices.restype = POINTER(c_uint32)
DLL.ZkPolygon_getFeatureIndices.restype = POINTER(c_uint32)
DLL.ZkPolygon_getIsPortal.restype = c_bool
DLL.ZkPolygon_getIsOccluder.restype = c_bool
DLL.ZkPolygon_getIsSector.restype = c_bool
DLL.ZkPolygon_getShouldRelight.restype = c_bool
DLL.ZkPolygon_getIsOutdoor.restype = c_bool
DLL.ZkPolygon_getIsGhostOccluder.restype = c_bool
DLL.ZkPolygon_getIsDynamicallyLit.restype = c_bool
DLL.ZkPolygon_getIsLod.restype = c_bool
DLL.ZkPolygon_getNormalAxis.restype = c_uint8
DLL.ZkPolygon_getSectorIndex.restype = c_int16


class Polygon:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def material_index(self) -> int:
        return DLL.ZkPolygon_getMaterialIndex(self._handle)

    @property
    def light_map_index(self) -> int:
        return DLL.ZkPolygon_getLightMapIndex(self._handle)

    @property
    def position_indices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkPolygon_getPositionIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def feature_indices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkPolygon_getFeatureIndices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def is_portal(self) -> bool:
        return DLL.ZkPolygon_getIsPortal(self._handle)

    @property
    def is_occluder(self) -> bool:
        return DLL.ZkPolygon_getIsOccluder(self._handle)

    @property
    def is_sector(self) -> bool:
        return DLL.ZkPolygon_getIsSector(self._handle)

    @property
    def should_relight(self) -> bool:
        return DLL.ZkPolygon_getShouldRelight(self._handle)

    @property
    def is_outdoor(self) -> bool:
        return DLL.ZkPolygon_getIsOutdoor(self._handle)

    @property
    def is_ghost_occluder(self) -> bool:
        return DLL.ZkPolygon_getIsGhostOccluder(self._handle)

    @property
    def is_dynamically_lit(self) -> bool:
        return DLL.ZkPolygon_getIsDynamicallyLit(self._handle)

    @property
    def is_lod(self) -> bool:
        return DLL.ZkPolygon_getIsLod(self._handle)

    @property
    def normal_axis(self) -> bool:
        return DLL.ZkPolygon_getNormalAxis(self._handle)

    @property
    def sector_index(self) -> bool:
        return DLL.ZkPolygon_getSectorIndex(self._handle)

    def __del__(self) -> None:
        self._keepalive = None


DLL.ZkLightMap_getImage.restype = ZkPointer
DLL.ZkLightMap_getOrigin.restype = Vec3f
DLL.ZkLightMap_getNormal.restype = Vec3f


class LightMap:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def image(self) -> Texture:
        return Texture(_handle=DLL.ZkLightMap_getImage(self._handle).value, _keepalive=self)

    @property
    def origin(self) -> Vec3f:
        return DLL.ZkLightMap_getOrigin(self._handle)

    @property
    def normal(self) -> tuple[Vec3f, Vec3f]:
        return DLL.ZkLightMap_getNormal(self._handle, 0), DLL.ZkLightMap_getNormal(self._handle, 1)

    def __del__(self) -> None:
        self._keepalive = None


DLL.ZkMesh_getSourceDate.restype = Date
DLL.ZkMesh_getName.restype = ZkString
DLL.ZkMesh_getBoundingBox.restype = AxisAlignedBoundingBox
DLL.ZkMesh_getOrientedBoundingBox.restype = ZkPointer
DLL.ZkMesh_getMaterialCount.restype = c_size_t
DLL.ZkMesh_getMaterial.restype = ZkPointer
DLL.ZkMesh_getPositionCount.restype = c_size_t
DLL.ZkMesh_getPosition.restype = Vec3f
DLL.ZkMesh_getVertexCount.restype = c_size_t
DLL.ZkMesh_getVertex.restype = Feature
DLL.ZkMesh_getPolygonCount.restype = c_size_t
DLL.ZkMesh_getPolygon.restype = ZkPointer
DLL.ZkMesh_getLightMapCount.restype = c_size_t
DLL.ZkMesh_getLightMap.restype = ZkPointer


class Mesh:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "Mesh":
        handle = _native.load("ZkMesh_load", path_or_file_like)
        return Mesh(_handle=handle, _delete=True)

    @property
    def name(self) -> str:
        return DLL.ZkMesh_getName(self._handle).value

    @property
    def bounding_box(self) -> AxisAlignedBoundingBox:
        return DLL.ZkMesh_getBoundingBox(self._handle)

    @property
    def oriented_bounding_box(self) -> OrientedBoundingBox:
        return OrientedBoundingBox(_handle=DLL.ZkMesh_getOrientedBoundingBox(self._handle).value)

    @property
    def materials(self) -> list[Material]:
        count = DLL.ZkMesh_getMaterialCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkMesh_getMaterial(self._handle, i).value
            items.append(Material(_handle=handle, _keepalive=self))

        return items

    @property
    def positions(self) -> list[Vec3f]:
        count = DLL.ZkMesh_getPositionCount(self._handle)
        return [DLL.ZkMesh_getPosition(self._handle, i) for i in range(count)]

    @property
    def features(self) -> list[Feature]:
        count = DLL.ZkMesh_getVertexCount(self._handle)
        return [DLL.ZkMesh_getVertex(self._handle, i) for i in range(count)]

    @property
    def light_maps(self) -> list[LightMap]:
        count = DLL.ZkMesh_getLightMapCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkMesh_getLightMap(self._handle, i).value
            items.append(LightMap(_handle=handle, _keepalive=self))

        return items

    @property
    def polygons(self) -> list[Polygon]:
        count = DLL.ZkMesh_getPolygonCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkMesh_getPolygon(self._handle, i).value
            items.append(Polygon(_handle=handle, _keepalive=self))

        return items

    @property
    def source_date(self) -> datetime:
        return DLL.ZkMesh_getSourceDate(self._handle).to_datetime()

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkMesh_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<Mesh handle={self._handle} name={self.name!r}>"
