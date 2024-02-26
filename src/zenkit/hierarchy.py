__all__ = [
    "ModelHierarchy",
    "ModelHierarchyNode",
]

from ctypes import c_void_p, c_uint, c_char_p, c_int16, Structure, c_size_t
from datetime import datetime
from os import PathLike
from typing import Any

from zenkit.vfs import VfsNode
from zenkit.stream import Read
from zenkit._core import DLL, AxisAlignedBoundingBox, Vec3f, Date, Mat4x4


class ModelHierarchyNode(Structure):
    _fields_ = [
        ("parent_index", c_int16),
        ("_name", c_char_p),
        ("transform", Mat4x4),
    ]

    @property
    def name(self) -> str:
        return self._name.decode("utf-8")

    def __repr__(self) -> str:
        return (
            f"ModelHierarchyNode(name={self.name!r}, parent_index={self.parent_index})"
        )


class ModelHierarchy:
    __slots__ = ("_handle", "_delete")

    def __init__(
        self, src: str | PathLike | Read | bytes | bytearray | VfsNode = None,
        **kwargs: Any
    ) -> None:
        if "_handle" in kwargs:
            self._handle = kwargs.pop("_handle")
            self._delete = False
            return

        if src is None:
            raise ValueError("No source provided")

        rd: Read
        if isinstance(src, VfsNode):
            rd = src.open()
        elif isinstance(src, Read):
            rd = src
        else:
            rd = Read(src)

        DLL.ZkModelHierarchy_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkModelHierarchy_load(rd.handle))
        self._delete = True

    @property
    def nodes(self) -> list[ModelHierarchyNode]:
        DLL.ZkModelHierarchy_getNodeCount.restype = c_size_t
        count = DLL.ZkModelHierarchy_getNodeCount(self._handle)

        DLL.ZkModelHierarchy_getNode.restype = ModelHierarchyNode
        return [DLL.ZkModelHierarchy_getNode(self._handle, i) for i in range(count)]

    @property
    def bbox(self) -> AxisAlignedBoundingBox:
        DLL.ZkModelHierarchy_getBbox.restype = AxisAlignedBoundingBox
        return DLL.ZkModelHierarchy_getBbox(self._handle)

    @property
    def collision_bbox(self) -> AxisAlignedBoundingBox:
        DLL.ZkModelHierarchy_getCollisionBbox.restype = AxisAlignedBoundingBox
        return DLL.ZkModelHierarchy_getCollisionBbox(self._handle)

    @property
    def root_translation(self) -> Vec3f:
        DLL.ZkModelHierarchy_getRootTranslation.restype = Vec3f
        return DLL.ZkModelHierarchy_getRootTranslation(self._handle)

    @property
    def checksum(self) -> int:
        DLL.ZkModelHierarchy_getChecksum.restype = c_uint
        return DLL.ZkModelHierarchy_getChecksum(self._handle)

    @property
    def source_date(self) -> datetime:
        DLL.ZkModelHierarchy_getSourceDate.restype = Date
        return DLL.ZkModelHierarchy_getSourceDate(self._handle).to_datetime()

    @property
    def source_path(self) -> str:
        DLL.ZkModelHierarchy_getSourcePath.restype = c_char_p
        return DLL.ZkModelHierarchy_getSourcePath(self._handle).decode("utf-8")

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkModelHierarchy_del.restype = None
            DLL.ZkModelHierarchy_del(self._handle)
            self._handle = None

    def __repr__(self) -> str:
        return f"ModelHierarchy(checksum={self.checksum})"
