__all__ = []

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class MusicJingleInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def name(self) -> str:
        DLL.ZkMusicJingleInstance_getName.restype = ZkString
        return DLL.ZkMusicJingleInstance_getName(self._handle).value

    @name.setter
    def name(self, value: str) -> None:
        DLL.ZkMusicJingleInstance_setName(self._handle, value.encode("utf-8"))

    @property
    def loop(self) -> int:
        DLL.ZkMusicJingleInstance_getLoop.restype = c_int32
        return DLL.ZkMusicJingleInstance_getLoop(self._handle)

    @loop.setter
    def loop(self, value: int) -> None:
        DLL.ZkMusicJingleInstance_setLoop(self._handle, c_int32(value))

    @property
    def vol(self) -> float:
        DLL.ZkMusicJingleInstance_getVol.restype = c_float
        return DLL.ZkMusicJingleInstance_getVol(self._handle)

    @vol.setter
    def vol(self, value: float) -> None:
        DLL.ZkMusicJingleInstance_setVol(self._handle, c_float(value))

    @property
    def transsubtype(self) -> int:
        DLL.ZkMusicJingleInstance_getTranssubtype.restype = c_int32
        return DLL.ZkMusicJingleInstance_getTranssubtype(self._handle)

    @transsubtype.setter
    def transsubtype(self, value: int) -> None:
        DLL.ZkMusicJingleInstance_setTranssubtype(self._handle, c_int32(value))
