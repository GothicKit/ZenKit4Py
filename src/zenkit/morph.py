__all__ = [
    "MorphMesh",
    "MorphSource",
    "MorphAnimation",
]

from ctypes import (
    c_void_p,
    c_char_p,
    c_size_t,
    c_int,
    c_float,
    c_uint8,
    c_uint32,
    POINTER,
    byref,
)
from datetime import timedelta, datetime
from os import PathLike
from typing import Any

from zenkit import MultiResolutionMesh
from zenkit._core import DLL, Vec3f, Date
from zenkit.stream import Read
from zenkit.vfs import VfsNode


class MorphAnimation:
    __slots__ = ("_handle",)

    def __init__(self, **kwargs: Any) -> None:
        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")

    @property
    def name(self) -> str:
        DLL.ZkMorphAnimation_getName.restype = c_char_p
        return DLL.ZkMorphAnimation_getName(self._handle).decode("utf-8")

    @property
    def layer(self) -> int:
        DLL.ZkMorphAnimation_getLayer.restype = c_int
        return DLL.ZkMorphAnimation_getLayer(self._handle)

    @property
    def blend_in(self) -> float:
        DLL.ZkMorphAnimation_getBlendIn.restype = c_float
        return DLL.ZkMorphAnimation_getBlendIn(self._handle)

    @property
    def blend_out(self) -> float:
        DLL.ZkMorphAnimation_getBlendOut.restype = c_float
        return DLL.ZkMorphAnimation_getBlendOut(self._handle)

    @property
    def duration(self) -> timedelta:
        DLL.ZkMorphAnimation_getDuration.restype = c_float
        return timedelta(seconds=DLL.ZkMorphAnimation_getDuration(self._handle))

    @property
    def speed(self) -> float:
        DLL.ZkMorphAnimation_getSpeed.restype = c_float
        return DLL.ZkMorphAnimation_getSpeed(self._handle)

    @property
    def flags(self) -> int:
        DLL.ZkMorphAnimation_getFlags.restype = c_uint8
        return DLL.ZkMorphAnimation_getFlags(self._handle)

    @property
    def frame_count(self) -> int:
        DLL.ZkMorphAnimation_getFrameCount.restype = c_size_t
        return DLL.ZkMorphAnimation_getFrameCount(self._handle)

    @property
    def vertices(self) -> list[int]:
        count = c_size_t(0)

        DLL.ZkMorphAnimation_getVertices.restype = POINTER(c_uint32)
        handle = DLL.ZkMorphAnimation_getVertices(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def samples(self) -> list[Vec3f]:
        DLL.ZkMorphAnimation_getSampleCount.restype = c_size_t
        count = DLL.ZkMorphAnimation_getSampleCount(self._handle)

        DLL.ZkMorphAnimation_getSample.restype = Vec3f
        return [DLL.ZkMorphAnimation_getSample(self._handle, i) for i in range(count)]

    def __repr__(self) -> str:
        return f"MorphAnimation(name={self.name!r}, samples={len(self.samples)}"


class MorphSource:
    __slots__ = ("_handle",)

    def __init__(self, **kwargs: Any) -> None:
        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")

    @property
    def file(self) -> str:
        DLL.ZkMorphSource_getFileName.restype = c_char_p
        return DLL.ZkMorphSource_getFileName(self._handle).decode("utf-8")

    @property
    def date(self) -> datetime:
        DLL.ZkMorphSource_getFileDate.restype = Date
        return DLL.ZkMorphSource_getFileDate(self._handle).to_datetime()

    def __repr__(self) -> str:
        return f"MorphSource(file={self.file}, date={self.date})"


class MorphMesh:
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

        DLL.ZkMorphMesh_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkMorphMesh_load(rd.handle))

    @property
    def name(self) -> str:
        DLL.ZkMorphMesh_getName.restype = c_char_p
        return DLL.ZkMorphMesh_getName(self._handle).decode("utf-8")

    @property
    def mesh(self) -> MultiResolutionMesh:
        DLL.ZkMorphMesh_getMesh.restype = c_void_p
        return MultiResolutionMesh(
            _handle=c_void_p(DLL.ZkMorphMesh_getMesh(self._handle))
        )

    @property
    def morph_positions(self) -> list[Vec3f]:
        DLL.ZkMorphMesh_getMorphPositionCount.restype = c_size_t
        count = DLL.ZkMorphMesh_getMorphPositionCount(self._handle)

        DLL.ZkMorphMesh_getMorphPosition.restype = Vec3f
        return [DLL.ZkMorphMesh_getMorphPosition(self._handle, i) for i in range(count)]

    @property
    def animations(self) -> list[MorphAnimation]:
        DLL.ZkMorphMesh_getAnimationCount.restype = c_size_t
        count = DLL.ZkMorphMesh_getAnimationCount(self._handle)

        DLL.ZkMorphMesh_getAnimation.restype = c_void_p
        return [
            MorphAnimation(
                _handle=c_void_p(DLL.ZkMorphMesh_getAnimation(self._handle, i))
            )
            for i in range(count)
        ]

    @property
    def sources(self) -> list[MorphSource]:
        DLL.ZkMorphMesh_getSourceCount.restype = c_size_t
        count = DLL.ZkMorphMesh_getSourceCount(self._handle)

        DLL.ZkMorphMesh_getSource.restype = c_void_p
        return [
            MorphSource(_handle=c_void_p(DLL.ZkMorphMesh_getSource(self._handle, i)))
            for i in range(count)
        ]

    def __del__(self) -> None:
        DLL.ZkMorphMesh_del.restype = None
        DLL.ZkMorphMesh_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return f"MorphMesh(name={self.name!r}, animations={len(self.animations)})"
