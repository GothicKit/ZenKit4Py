__all__ = [
    "MusicTransitionType",
    "MusicTransitionEffect",
    "MusicThemeInstance",
]

from ctypes import c_float
from ctypes import c_int
from ctypes import c_int32
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class MusicTransitionEffect(IntEnum):
    UNKNOWN = 0
    NONE = 1
    GROOVE = 2
    FILL = 3
    BREAK = 4
    INTRO = 5
    END = 6
    END_AND_INTO = 7


class MusicTransitionType(IntEnum):
    UNKNOWN = 0
    IMMEDIATE = 1
    BEAT = 2
    MEASURE = 3


class MusicThemeInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def file(self) -> str:
        DLL.ZkMusicThemeInstance_getFile.restype = ZkString
        return DLL.ZkMusicThemeInstance_getFile(self._handle).value

    @file.setter
    def file(self, value: str) -> None:
        DLL.ZkMusicThemeInstance_setFile(self._handle, value.encode("utf-8"))

    @property
    def vol(self) -> float:
        DLL.ZkMusicThemeInstance_getVol.restype = c_float
        return DLL.ZkMusicThemeInstance_getVol(self._handle)

    @vol.setter
    def vol(self, value: float) -> None:
        DLL.ZkMusicThemeInstance_setVol(self._handle, c_float(value))

    @property
    def loop(self) -> int:
        DLL.ZkMusicThemeInstance_getLoop.restype = c_int32
        return DLL.ZkMusicThemeInstance_getLoop(self._handle)

    @loop.setter
    def loop(self, value: int) -> None:
        DLL.ZkMusicThemeInstance_setLoop(self._handle, c_int32(value))

    @property
    def reverbmix(self) -> float:
        DLL.ZkMusicThemeInstance_getReverbmix.restype = c_float
        return DLL.ZkMusicThemeInstance_getReverbmix(self._handle)

    @reverbmix.setter
    def reverbmix(self, value: float) -> None:
        DLL.ZkMusicThemeInstance_setReverbmix(self._handle, c_float(value))

    @property
    def reverbtime(self) -> float:
        DLL.ZkMusicThemeInstance_getReverbtime.restype = c_float
        return DLL.ZkMusicThemeInstance_getReverbtime(self._handle)

    @reverbtime.setter
    def reverbtime(self, value: float) -> None:
        DLL.ZkMusicThemeInstance_setReverbtime(self._handle, c_float(value))

    @property
    def transtype(self) -> MusicTransitionEffect:
        DLL.ZkMusicThemeInstance_getTranstype.restype = c_int
        return MusicTransitionEffect(DLL.ZkMusicThemeInstance_getTranstype(self._handle))

    @transtype.setter
    def transtype(self, value: MusicTransitionEffect) -> None:
        DLL.ZkMusicThemeInstance_setTranstype(self._handle, value.value)

    @property
    def transsubtype(self) -> MusicTransitionType:
        DLL.ZkMusicThemeInstance_getTranssubtype.restype = c_int
        return MusicTransitionType(DLL.ZkMusicThemeInstance_getTranssubtype(self._handle))

    @transsubtype.setter
    def transsubtype(self, value: MusicTransitionType) -> None:
        DLL.ZkMusicThemeInstance_setTranssubtype(self._handle, value.value)
