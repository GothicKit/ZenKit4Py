__all__ = [
    "ModelHierarchy",
    "ModelHierarchyNode",
]

from ctypes import Structure
from ctypes import c_int16
from ctypes import c_size_t
from ctypes import c_uint
from ctypes import c_void_p
from datetime import datetime
from typing import Any
from typing import ClassVar

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import AxisAlignedBoundingBox
from zenkit._core import Date
from zenkit._core import Mat4x4
from zenkit._core import PathOrFileLike
from zenkit._core import Vec3f
from zenkit._native import ZkString


class ModelHierarchyNode(Structure):
    _fields_: ClassVar[tuple[str, Any]] = [
        ("_parent", c_int16),
        ("_name", ZkString),
        ("_transform", Mat4x4),
    ]

    @property
    def parent(self) -> int:
        return self._parent

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def transform(self) -> Mat4x4:
        return self._transform

    def __repr__(self) -> str:
        return f"<ModelHierarchyNode name={self.name!r}>"


DLL.ZkModelHierarchy_getNodeCount.restype = c_size_t
DLL.ZkModelHierarchy_getNode.restype = ModelHierarchyNode
DLL.ZkModelHierarchy_getBbox.restype = AxisAlignedBoundingBox
DLL.ZkModelHierarchy_getCollisionBbox.restype = AxisAlignedBoundingBox
DLL.ZkModelHierarchy_getRootTranslation.restype = Vec3f
DLL.ZkModelHierarchy_getChecksum.restype = c_uint
DLL.ZkModelHierarchy_getSourceDate.restype = Date
DLL.ZkModelHierarchy_getSourcePath.restype = ZkString


class ModelHierarchy:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "ModelHierarchy":
        handle = _native.load("ZkModelHierarchy_load", path_or_file_like)
        return ModelHierarchy(_handle=handle, _delete=True)

    @property
    def nodes(self) -> list[ModelHierarchyNode]:
        count = DLL.ZkModelHierarchy_getNodeCount(self._handle)
        return [DLL.ZkModelHierarchy_getNode(self._handle, i) for i in range(count)]

    @property
    def bbox(self) -> AxisAlignedBoundingBox:
        return DLL.ZkModelHierarchy_getBbox(self._handle)

    @property
    def collision_bbox(self) -> AxisAlignedBoundingBox:
        return DLL.ZkModelHierarchy_getCollisionBbox(self._handle)

    @property
    def root_translation(self) -> Vec3f:
        return DLL.ZkModelHierarchy_getRootTranslation(self._handle)

    @property
    def checksum(self) -> int:
        return DLL.ZkModelHierarchy_getChecksum(self._handle)

    @property
    def source_date(self) -> datetime:
        return DLL.ZkModelHierarchy_getSourceDate(self._handle).to_datetime()

    @property
    def source_path(self) -> str:
        return DLL.ZkModelHierarchy_getSourcePath(self._handle).value

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkModelHierarchy_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<ModelHierarchy handle={self._handle} checksum={self.checksum}>"
