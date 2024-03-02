__all__ = ["SoundEffectInstance"]

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class SoundEffectInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def file(self) -> str:
        DLL.ZkSoundEffectInstance_getFile.restype = ZkString
        return DLL.ZkSoundEffectInstance_getFile(self._handle).value

    @file.setter
    def file(self, value: str) -> None:
        DLL.ZkSoundEffectInstance_setFile(self._handle, value.encode("utf-8"))

    @property
    def pitch_off(self) -> int:
        DLL.ZkSoundEffectInstance_getPitchOff.restype = c_int32
        return DLL.ZkSoundEffectInstance_getPitchOff(self._handle)

    @pitch_off.setter
    def pitch_off(self, value: int) -> None:
        DLL.ZkSoundEffectInstance_setPitchOff(self._handle, c_int32(value))

    @property
    def pitch_var(self) -> int:
        DLL.ZkSoundEffectInstance_getPitchVar.restype = c_int32
        return DLL.ZkSoundEffectInstance_getPitchVar(self._handle)

    @pitch_var.setter
    def pitch_var(self, value: int) -> None:
        DLL.ZkSoundEffectInstance_setPitchVar(self._handle, c_int32(value))

    @property
    def volume(self) -> int:
        DLL.ZkSoundEffectInstance_getVolume.restype = c_int32
        return DLL.ZkSoundEffectInstance_getVolume(self._handle)

    @volume.setter
    def volume(self, value: int) -> None:
        DLL.ZkSoundEffectInstance_setVolume(self._handle, c_int32(value))

    @property
    def loop(self) -> int:
        DLL.ZkSoundEffectInstance_getLoop.restype = c_int32
        return DLL.ZkSoundEffectInstance_getLoop(self._handle)

    @loop.setter
    def loop(self, value: int) -> None:
        DLL.ZkSoundEffectInstance_setLoop(self._handle, c_int32(value))

    @property
    def loop_start_offset(self) -> int:
        DLL.ZkSoundEffectInstance_getLoopStartOffset.restype = c_int32
        return DLL.ZkSoundEffectInstance_getLoopStartOffset(self._handle)

    @loop_start_offset.setter
    def loop_start_offset(self, value: int) -> None:
        DLL.ZkSoundEffectInstance_setLoopStartOffset(self._handle, c_int32(value))

    @property
    def loop_end_offset(self) -> int:
        DLL.ZkSoundEffectInstance_getLoopEndOffset.restype = c_int32
        return DLL.ZkSoundEffectInstance_getLoopEndOffset(self._handle)

    @loop_end_offset.setter
    def loop_end_offset(self, value: int) -> None:
        DLL.ZkSoundEffectInstance_setLoopEndOffset(self._handle, c_int32(value))

    @property
    def reverb_level(self) -> float:
        DLL.ZkSoundEffectInstance_getReverbLevel.restype = c_float
        return DLL.ZkSoundEffectInstance_getReverbLevel(self._handle)

    @reverb_level.setter
    def reverb_level(self, value: float) -> None:
        DLL.ZkSoundEffectInstance_setReverbLevel(self._handle, c_float(value))

    @property
    def pfx_name(self) -> str:
        DLL.ZkSoundEffectInstance_getPfxName.restype = ZkString
        return DLL.ZkSoundEffectInstance_getPfxName(self._handle).value

    @pfx_name.setter
    def pfx_name(self, value: str) -> None:
        DLL.ZkSoundEffectInstance_setPfxName(self._handle, value.encode("utf-8"))
