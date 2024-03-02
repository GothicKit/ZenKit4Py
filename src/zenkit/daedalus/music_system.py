__all__ = [
    "MusicSystemInstance",
]

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit.daedalus.base import DaedalusInstance


class MusicSystemInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def volume(self) -> float:
        DLL.ZkMusicSystemInstance_getVolume.restype = c_float
        return DLL.ZkMusicSystemInstance_getVolume(self._handle)

    @volume.setter
    def volume(self, value: float) -> None:
        DLL.ZkMusicSystemInstance_setVolume(self._handle, c_float(value))

    @property
    def bit_resolution(self) -> int:
        DLL.ZkMusicSystemInstance_getBitResolution.restype = c_int32
        return DLL.ZkMusicSystemInstance_getBitResolution(self._handle)

    @bit_resolution.setter
    def bit_resolution(self, value: int) -> None:
        DLL.ZkMusicSystemInstance_setBitResolution(self._handle, c_int32(value))

    @property
    def global_reverb_enabled(self) -> int:
        DLL.ZkMusicSystemInstance_getGlobalReverbEnabled.restype = c_int32
        return DLL.ZkMusicSystemInstance_getGlobalReverbEnabled(self._handle)

    @global_reverb_enabled.setter
    def global_reverb_enabled(self, value: int) -> None:
        DLL.ZkMusicSystemInstance_setGlobalReverbEnabled(self._handle, c_int32(value))

    @property
    def sample_rate(self) -> int:
        DLL.ZkMusicSystemInstance_getSampleRate.restype = c_int32
        return DLL.ZkMusicSystemInstance_getSampleRate(self._handle)

    @sample_rate.setter
    def sample_rate(self, value: int) -> None:
        DLL.ZkMusicSystemInstance_setSampleRate(self._handle, c_int32(value))

    @property
    def num_channels(self) -> int:
        DLL.ZkMusicSystemInstance_getNumChannels.restype = c_int32
        return DLL.ZkMusicSystemInstance_getNumChannels(self._handle)

    @num_channels.setter
    def num_channels(self, value: int) -> None:
        DLL.ZkMusicSystemInstance_setNumChannels(self._handle, c_int32(value))

    @property
    def reverb_buffer_size(self) -> int:
        DLL.ZkMusicSystemInstance_getReverbBufferSize.restype = c_int32
        return DLL.ZkMusicSystemInstance_getReverbBufferSize(self._handle)

    @reverb_buffer_size.setter
    def reverb_buffer_size(self, value: int) -> None:
        DLL.ZkMusicSystemInstance_setReverbBufferSize(self._handle, c_int32(value))
