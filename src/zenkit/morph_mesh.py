__all__ = [
    "MorphMesh",
    "MorphSource",
    "MorphAnimation",
]

from ctypes import POINTER
from ctypes import byref
from ctypes import c_float
from ctypes import c_int
from ctypes import c_size_t
from ctypes import c_uint8
from ctypes import c_uint32
from ctypes import c_void_p
from datetime import datetime
from datetime import timedelta
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import Date
from zenkit._core import PathOrFileLike
from zenkit._core import Vec3f
from zenkit._native import ZkPointer
from zenkit._native import ZkString
from zenkit.multi_resolution_mesh import MultiResolutionMesh

DLL.ZkMorphAnimation_getName.restype = ZkString
DLL.ZkMorphAnimation_getLayer.restype = c_int
DLL.ZkMorphAnimation_getBlendIn.restype = c_float
DLL.ZkMorphAnimation_getBlendOut.restype = c_float
DLL.ZkMorphAnimation_getDuration.restype = c_float
DLL.ZkMorphAnimation_getSpeed.restype = c_float
DLL.ZkMorphAnimation_getFlags.restype = c_uint8
DLL.ZkMorphAnimation_getFrameCount.restype = c_size_t
DLL.ZkMorphAnimation_getVertices.restype = POINTER(c_uint32)
DLL.ZkMorphAnimation_getSampleCount.restype = c_size_t
DLL.ZkMorphAnimation_getSample.restype = Vec3f


class MorphAnimation:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def name(self) -> str:
        return DLL.ZkMorphAnimation_getName(self._handle).value

    @property
    def layer(self) -> int:
        return DLL.ZkMorphAnimation_getLayer(self._handle)

    @property
    def blend_in(self) -> float:
        return DLL.ZkMorphAnimation_getBlendIn(self._handle)

    @property
    def blend_out(self) -> float:
        return DLL.ZkMorphAnimation_getBlendOut(self._handle)

    @property
    def duration(self) -> timedelta:
        return timedelta(seconds=DLL.ZkMorphAnimation_getDuration(self._handle))

    @property
    def speed(self) -> float:
        return DLL.ZkMorphAnimation_getSpeed(self._handle)

    @property
    def flags(self) -> int:
        return DLL.ZkMorphAnimation_getFlags(self._handle)

    @property
    def frame_count(self) -> int:
        return DLL.ZkMorphAnimation_getFrameCount(self._handle)

    @property
    def vertices(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkMorphAnimation_getVertices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def samples(self) -> list[Vec3f]:
        count = DLL.ZkMorphAnimation_getSampleCount(self._handle)
        return [DLL.ZkMorphAnimation_getSample(self._handle, i) for i in range(count)]

    def __del__(self) -> None:
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<MorphAnimation handle={self._handle} name={self.name!r}>"


DLL.ZkMorphSource_getFileName.restype = ZkString
DLL.ZkMorphSource_getFileDate.restype = Date


class MorphSource:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def file(self) -> str:
        return DLL.ZkMorphSource_getFileName(self._handle).value

    @property
    def date(self) -> datetime:
        return DLL.ZkMorphSource_getFileDate(self._handle).to_datetime()

    def __del__(self) -> None:
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<MorphSource handle={self._handle}>"


DLL.ZkMorphMesh_getName.restype = ZkString
DLL.ZkMorphMesh_getMesh.restype = ZkPointer
DLL.ZkMorphMesh_getMorphPositionCount.restype = c_size_t
DLL.ZkMorphMesh_getMorphPosition.restype = Vec3f
DLL.ZkMorphMesh_getAnimationCount.restype = c_size_t
DLL.ZkMorphMesh_getAnimation.restype = ZkPointer
DLL.ZkMorphMesh_getSourceCount.restype = c_size_t
DLL.ZkMorphMesh_getSource.restype = ZkPointer


class MorphMesh:
    __slots__ = ("_handle", "_delete")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "MorphMesh":
        handle = _native.load("ZkMorphMesh_load", path_or_file_like)
        return MorphMesh(_handle=handle, _delete=True)

    @property
    def name(self) -> str:
        return DLL.ZkMorphMesh_getName(self._handle).value

    @property
    def mesh(self) -> MultiResolutionMesh:
        return MultiResolutionMesh(_handle=DLL.ZkMorphMesh_getMesh(self._handle).value, _keepalive=self)

    @property
    def morph_positions(self) -> list[Vec3f]:
        count = DLL.ZkMorphMesh_getMorphPositionCount(self._handle)
        return [DLL.ZkMorphMesh_getMorphPosition(self._handle, i) for i in range(count)]

    @property
    def animations(self) -> list[MorphAnimation]:
        count = DLL.ZkMorphMesh_getAnimationCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkMorphMesh_getAnimation(self._handle, i).value
            items.append(MorphAnimation(_handle=handle, _keepalive=self))

        return items

    @property
    def sources(self) -> list[MorphSource]:
        count = DLL.ZkMorphMesh_getSourceCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkMorphMesh_getSource(self._handle, i).value
            items.append(MorphSource(_handle=handle, _keepalive=self))

        return items

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkMorphMesh_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return f"<MorphMesh handle={self._handle} name={self.name!r}>"
