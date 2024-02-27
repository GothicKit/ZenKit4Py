__all__ = [
    "ModelAnimation",
    "AnimationSample",
]

from ctypes import Structure
from ctypes import c_float
from ctypes import c_size_t
from ctypes import c_uint
from ctypes import c_void_p
from datetime import datetime
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import AxisAlignedBoundingBox
from zenkit._core import Date
from zenkit._core import PathOrFileLike
from zenkit._core import Quat
from zenkit._core import Vec3f
from zenkit._native import ZkString


class AnimationSample(Structure):
    _fields_ = [
        ("_position", Vec3f),
        ("_rotation", Quat),
    ]

    @property
    def position(self) -> Vec3f:
        return self._position

    @property
    def rotation(self) -> Quat:
        return self._rotation

    def __repr__(self) -> str:
        return f"<AnimationSample position={self.position} rotation={self.rotation}>"


DLL.ZkModelAnimation_getName.restype = ZkString
DLL.ZkModelAnimation_getNext.restype = ZkString
DLL.ZkModelAnimation_getLayer.restype = c_uint
DLL.ZkModelAnimation_getFrameCount.restype = c_uint
DLL.ZkModelAnimation_getNodeCount.restype = c_uint
DLL.ZkModelAnimation_getFps.restype = c_float
DLL.ZkModelAnimation_getFpsSource.restype = c_float
DLL.ZkModelAnimation_getChecksum.restype = c_uint
DLL.ZkModelAnimation_getBbox.restype = AxisAlignedBoundingBox
DLL.ZkModelAnimation_getSourcePath.restype = ZkString
DLL.ZkModelAnimation_getSourceDate.restype = Date
DLL.ZkModelAnimation_getSourceScript.restype = ZkString
DLL.ZkModelAnimation_getSampleCount.restype = c_size_t
DLL.ZkModelAnimation_getSample.restype = AnimationSample


class ModelAnimation:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "ModelAnimation":
        handle = _native.load("ZkModelAnimation_load", path_or_file_like)
        return ModelAnimation(_handle=handle, _delete=True)

    @property
    def name(self) -> str:
        return DLL.ZkModelAnimation_getName(self._handle).value

    @property
    def next(self) -> str:
        return DLL.ZkModelAnimation_getNext(self._handle).value

    @property
    def layer(self) -> int:
        return DLL.ZkModelAnimation_getLayer(self._handle)

    @property
    def frame_count(self) -> int:
        return DLL.ZkModelAnimation_getFrameCount(self._handle)

    @property
    def node_count(self) -> int:
        return DLL.ZkModelAnimation_getNodeCount(self._handle)

    @property
    def fps(self) -> float:
        return DLL.ZkModelAnimation_getFps(self._handle)

    @property
    def fps_source(self) -> float:
        return DLL.ZkModelAnimation_getFpsSource(self._handle)

    @property
    def checksum(self) -> int:
        return DLL.ZkModelAnimation_getChecksum(self._handle)

    @property
    def bbox(self) -> AxisAlignedBoundingBox:
        return DLL.ZkModelAnimation_getBbox(self._handle)

    @property
    def source_path(self) -> str:
        return DLL.ZkModelAnimation_getSourcePath(self._handle).value

    @property
    def source_date(self) -> datetime:
        return DLL.ZkModelAnimation_getSourceDate(self._handle).to_datetime()

    @property
    def source_script(self) -> str:
        return DLL.ZkModelAnimation_getSourceScript(self._handle).value

    @property
    def samples(self) -> list[AnimationSample]:
        count = DLL.ZkModelAnimation_getSampleCount(self._handle)
        return [DLL.ZkModelAnimation_getSample(self._handle, i) for i in range(count)]

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkModelAnimation_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<ModelAnimation handle={self._handle} name={self.name!r}>"
