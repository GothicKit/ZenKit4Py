__all__ = [
    "Sound",
    "SoundDaytime",
    "SoundTriggerVolumeType",
    "SoundMode",
]

from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.vob.virtual_object import VirtualObject


class SoundMode(IntEnum):
    LOOP = 0
    ONCE = 1
    RANDOM = 2


class SoundTriggerVolumeType(IntEnum):
    SPHERICAL = 0
    ELLIPSOIDAL = 1


DLL.ZkSound_getVolume.restype = c_float
DLL.ZkSound_getMode.restype = c_int
DLL.ZkSound_getRandomDelay.restype = c_float
DLL.ZkSound_getRandomDelayVar.restype = c_float
DLL.ZkSound_getInitiallyPlaying.restype = c_bool
DLL.ZkSound_getAmbient3d.restype = c_bool
DLL.ZkSound_getObstruction.restype = c_bool
DLL.ZkSound_getConeAngle.restype = c_float
DLL.ZkSound_getVolumeType.restype = c_int
DLL.ZkSound_getRadius.restype = c_float
DLL.ZkSound_getSoundName.restype = ZkString
DLL.ZkSound_getIsRunning.restype = c_bool
DLL.ZkSound_getIsAllowedToRun.restype = c_bool


class Sound(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def volume(self) -> float:
        return DLL.ZkSound_getVolume(self._handle)

    @volume.setter
    def volume(self, value: float) -> None:
        DLL.ZkSound_setVolume(self._handle, c_float(value))

    @property
    def mode(self) -> SoundMode:
        return SoundMode(DLL.ZkSound_getMode(self._handle))

    @mode.setter
    def mode(self, value: SoundMode) -> None:
        DLL.ZkSound_setMode(self._handle, value.value)

    @property
    def random_delay(self) -> float:
        return DLL.ZkSound_getRandomDelay(self._handle)

    @random_delay.setter
    def random_delay(self, value: float) -> None:
        DLL.ZkSound_setRandomDelay(self._handle, c_float(value))

    @property
    def random_delay_var(self) -> float:
        return DLL.ZkSound_getRandomDelayVar(self._handle)

    @random_delay_var.setter
    def random_delay_var(self, value: float) -> None:
        DLL.ZkSound_setRandomDelayVar(self._handle, c_float(value))

    @property
    def initially_playing(self) -> bool:
        return DLL.ZkSound_getInitiallyPlaying(self._handle)

    @initially_playing.setter
    def initially_playing(self, value: bool) -> None:
        DLL.ZkSound_setInitiallyPlaying(self._handle, c_bool(value))

    @property
    def ambient3d(self) -> bool:
        return DLL.ZkSound_getAmbient3d(self._handle)

    @ambient3d.setter
    def ambient3d(self, value: bool) -> None:
        DLL.ZkSound_setAmbient3d(self._handle, c_bool(value))

    @property
    def obstruction(self) -> bool:
        return DLL.ZkSound_getObstruction(self._handle)

    @obstruction.setter
    def obstruction(self, value: bool) -> None:
        DLL.ZkSound_setObstruction(self._handle, c_bool(value))

    @property
    def cone_angle(self) -> float:
        return DLL.ZkSound_getConeAngle(self._handle)

    @cone_angle.setter
    def cone_angle(self, value: float) -> None:
        DLL.ZkSound_setConeAngle(self._handle, c_float(value))

    @property
    def volume_type(self) -> SoundTriggerVolumeType:
        return SoundTriggerVolumeType(DLL.ZkSound_getVolumeType(self._handle))

    @volume_type.setter
    def volume_type(self, value: SoundTriggerVolumeType) -> None:
        DLL.ZkSound_setVolumeType(self._handle, value.value)

    @property
    def radius(self) -> float:
        return DLL.ZkSound_getRadius(self._handle)

    @radius.setter
    def radius(self, value: float) -> None:
        DLL.ZkSound_setRadius(self._handle, c_float(value))

    @property
    def sound_name(self) -> str:
        return DLL.ZkSound_getSoundName(self._handle).value

    @sound_name.setter
    def sound_name(self, value: str) -> None:
        DLL.ZkSound_setSoundName(self._handle, value.encode("utf-8"))

    @property
    def is_running(self) -> bool:
        return DLL.ZkSound_getIsRunning(self._handle)

    @is_running.setter
    def is_running(self, value: bool) -> None:
        DLL.ZkSound_setIsRunning(self._handle, c_bool(value))

    @property
    def is_allowed_to_run(self) -> bool:
        return DLL.ZkSound_getIsAllowedToRun(self._handle)

    @is_allowed_to_run.setter
    def is_allowed_to_run(self, value: bool) -> None:
        DLL.ZkSound_setIsAllowedToRun(self._handle, c_bool(value))


DLL.ZkSoundDaytime_getStartTime.restype = c_float
DLL.ZkSoundDaytime_getEndTime.restype = c_float
DLL.ZkSoundDaytime_getSoundNameDaytime.restype = ZkString


class SoundDaytime(Sound):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def start_time(self) -> float:
        return DLL.ZkSoundDaytime_getStartTime(self._handle)

    @start_time.setter
    def start_time(self, value: float) -> None:
        DLL.ZkSoundDaytime_setStartTime(self._handle, c_float(value))

    @property
    def end_time(self) -> float:
        return DLL.ZkSoundDaytime_getEndTime(self._handle)

    @end_time.setter
    def end_time(self, value: float) -> None:
        DLL.ZkSoundDaytime_setEndTime(self._handle, c_float(value))

    @property
    def sound_name_daytime(self) -> str:
        return DLL.ZkSoundDaytime_getSoundNameDaytime(self._handle).value

    @sound_name_daytime.setter
    def sound_name_daytime(self, value: str) -> None:
        DLL.ZkSoundDaytime_setSoundNameDaytime(self._handle, value.encode("utf-8"))
