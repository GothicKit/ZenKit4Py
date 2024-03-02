__all__ = ["SoundSystemInstance"]

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class SoundSystemInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def volume(self) -> float:
        DLL.ZkSoundSystemInstance_getVolume.restype = c_float
        return DLL.ZkSoundSystemInstance_getVolume(self._handle)

    @volume.setter
    def volume(self, value: float) -> None:
        DLL.ZkSoundSystemInstance_setVolume(self._handle, c_float(value))

    @property
    def bit_resolution(self) -> int:
        DLL.ZkSoundSystemInstance_getBitResolution.restype = c_int32
        return DLL.ZkSoundSystemInstance_getBitResolution(self._handle)

    @bit_resolution.setter
    def bit_resolution(self, value: int) -> None:
        DLL.ZkSoundSystemInstance_setBitResolution(self._handle, c_int32(value))

    @property
    def sample_rate(self) -> int:
        DLL.ZkSoundSystemInstance_getSampleRate.restype = c_int32
        return DLL.ZkSoundSystemInstance_getSampleRate(self._handle)

    @sample_rate.setter
    def sample_rate(self, value: int) -> None:
        DLL.ZkSoundSystemInstance_setSampleRate(self._handle, c_int32(value))

    @property
    def use_stereo(self) -> int:
        DLL.ZkSoundSystemInstance_getUseStereo.restype = c_int32
        return DLL.ZkSoundSystemInstance_getUseStereo(self._handle)

    @use_stereo.setter
    def use_stereo(self, value: int) -> None:
        DLL.ZkSoundSystemInstance_setUseStereo(self._handle, c_int32(value))

    @property
    def num_sfx_channels(self) -> int:
        DLL.ZkSoundSystemInstance_getNumSfxChannels.restype = c_int32
        return DLL.ZkSoundSystemInstance_getNumSfxChannels(self._handle)

    @num_sfx_channels.setter
    def num_sfx_channels(self, value: int) -> None:
        DLL.ZkSoundSystemInstance_setNumSfxChannels(self._handle, c_int32(value))

    @property
    def used_3d_provider_name(self) -> str:
        DLL.ZkSoundSystemInstance_getUsed3DProviderName.restype = ZkString
        return DLL.ZkSoundSystemInstance_getUsed3DProviderName(self._handle).value

    @used_3d_provider_name.setter
    def used_3d_provider_name(self, value: str) -> None:
        DLL.ZkSoundSystemInstance_setUsed3DProviderName(self._handle, value.encode("utf-8"))
