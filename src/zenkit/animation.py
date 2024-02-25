__all__ = [
    "ModelAnimation",
    "AnimationSample",
]

from ctypes import c_void_p, c_char_p, c_uint, c_float, c_size_t, Structure
from datetime import datetime
from os import PathLike

from zenkit import Read, VfsNode
from zenkit._core import DLL, AxisAlignedBoundingBox, Date, Vec3f, Quat


class AnimationSample(Structure):
    _fields_ = [
        ("position", Vec3f),
        ("rotation", Quat),
    ]

    def __repr__(self) -> str:
        return f"AnimationSample(position={self.position}, rotation={self.rotation})"


class ModelAnimation:
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

        DLL.ZkModelAnimation_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkModelAnimation_load(rd.handle))

    @property
    def name(self) -> str:
        DLL.ZkModelAnimation_getName.restype = c_char_p
        handle = DLL.ZkModelAnimation_getName(self._handle)
        return handle.decode("utf-8")

    @property
    def next(self) -> str:
        DLL.ZkModelAnimation_getNext.restype = c_char_p
        handle = DLL.ZkModelAnimation_getNext(self._handle)
        return handle.decode("utf-8")

    @property
    def layer(self) -> int:
        DLL.ZkModelAnimation_getLayer.restype = c_uint
        return DLL.ZkModelAnimation_getLayer(self._handle)

    @property
    def frame_count(self) -> int:
        DLL.ZkModelAnimation_getFrameCount.restype = c_uint
        return DLL.ZkModelAnimation_getFrameCount(self._handle)

    @property
    def node_count(self) -> int:
        DLL.ZkModelAnimation_getNodeCount.restype = c_uint
        return DLL.ZkModelAnimation_getNodeCount(self._handle)

    @property
    def fps(self) -> float:
        DLL.ZkModelAnimation_getFps.restype = c_float
        return DLL.ZkModelAnimation_getFps(self._handle)

    @property
    def fps_source(self) -> float:
        DLL.ZkModelAnimation_getFpsSource.restype = c_float
        return DLL.ZkModelAnimation_getFpsSource(self._handle)

    @property
    def checksum(self) -> int:
        DLL.ZkModelAnimation_getChecksum.restype = c_uint
        return DLL.ZkModelAnimation_getChecksum(self._handle)

    @property
    def bbox(self) -> AxisAlignedBoundingBox:
        DLL.ZkModelAnimation_getBbox.restype = AxisAlignedBoundingBox
        return DLL.ZkModelAnimation_getBbox(self._handle)

    @property
    def source_path(self) -> str:
        DLL.ZkModelAnimation_getSourcePath.restype = c_char_p
        handle = DLL.ZkModelAnimation_getSourcePath(self._handle)
        return handle.decode("utf-8")

    @property
    def source_date(self) -> datetime:
        DLL.ZkModelAnimation_getSourceDate.restype = Date
        return DLL.ZkModelAnimation_getSourceDate(self._handle).to_datetime()

    @property
    def source_script(self) -> str:
        DLL.ZkModelAnimation_getSourceScript.restype = c_char_p
        handle = DLL.ZkModelAnimation_getSourceScript(self._handle)
        return handle.decode("utf-8")

    @property
    def samples(self) -> list[AnimationSample]:
        DLL.ZkModelAnimation_getSampleCount.restype = c_size_t
        count = DLL.ZkModelAnimation_getSampleCount(self._handle)

        DLL.ZkModelAnimation_getSample.restype = AnimationSample
        return [DLL.ZkModelAnimation_getSample(self._handle, i) for i in range(count)]

    def __del__(self) -> None:
        DLL.ZkModelAnimation_del.restype = None
        DLL.ZkModelAnimation_del(self._handle)
        self._handle = None

    def __repr__(self) -> str:
        return f"ModelAnimation(name={self.name!r}, next={self.next!r}, fps={self.fps}, samples={len(self.samples)})"
