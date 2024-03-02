__all__ = [
    "ZoneMusic",
    "ZoneFog",
    "ZoneFarPlane",
]

from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit._core import Color
from zenkit.vob.virtual_object import VirtualObject

DLL.ZkZoneMusic_getIsEnabled.restype = c_bool
DLL.ZkZoneMusic_getPriority.restype = c_int32
DLL.ZkZoneMusic_getIsEllipsoid.restype = c_bool
DLL.ZkZoneMusic_getReverb.restype = c_float
DLL.ZkZoneMusic_getVolume.restype = c_float
DLL.ZkZoneMusic_getIsLoop.restype = c_bool
DLL.ZkZoneMusic_getLocalEnabled.restype = c_bool
DLL.ZkZoneMusic_getDayEntranceDone.restype = c_bool
DLL.ZkZoneMusic_getNightEntranceDone.restype = c_bool


class ZoneMusic(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def is_enabled(self) -> bool:
        return DLL.ZkZoneMusic_getIsEnabled(self._handle)

    @is_enabled.setter
    def is_enabled(self, value: bool) -> None:
        DLL.ZkZoneMusic_setIsEnabled(self._handle, c_bool(value))

    @property
    def priority(self) -> int:
        return DLL.ZkZoneMusic_getPriority(self._handle)

    @priority.setter
    def priority(self, value: int) -> None:
        DLL.ZkZoneMusic_setPriority(self._handle, c_int32(value))

    @property
    def is_ellipsoid(self) -> bool:
        return DLL.ZkZoneMusic_getIsEllipsoid(self._handle)

    @is_ellipsoid.setter
    def is_ellipsoid(self, value: bool) -> None:
        DLL.ZkZoneMusic_setIsEllipsoid(self._handle, c_bool(value))

    @property
    def reverb(self) -> float:
        return DLL.ZkZoneMusic_getReverb(self._handle)

    @reverb.setter
    def reverb(self, value: float) -> None:
        DLL.ZkZoneMusic_setReverb(self._handle, c_float(value))

    @property
    def volume(self) -> float:
        return DLL.ZkZoneMusic_getVolume(self._handle)

    @volume.setter
    def volume(self, value: float) -> None:
        DLL.ZkZoneMusic_setVolume(self._handle, c_float(value))

    @property
    def is_loop(self) -> bool:
        return DLL.ZkZoneMusic_getIsLoop(self._handle)

    @is_loop.setter
    def is_loop(self, value: bool) -> None:
        DLL.ZkZoneMusic_setIsLoop(self._handle, c_bool(value))

    @property
    def local_enabled(self) -> bool:
        return DLL.ZkZoneMusic_getLocalEnabled(self._handle)

    @property
    def day_entrance_done(self) -> bool:
        return DLL.ZkZoneMusic_getDayEntranceDone(self._handle)

    @property
    def night_entrance_done(self) -> bool:
        return DLL.ZkZoneMusic_getNightEntranceDone(self._handle)

    @local_enabled.setter
    def local_enabled(self, value: bool) -> None:
        DLL.ZkZoneMusic_setLocalEnabled(self._handle, c_bool(value))

    @day_entrance_done.setter
    def day_entrance_done(self, value: bool) -> None:
        DLL.ZkZoneMusic_setDayEntranceDone(self._handle, c_bool(value))

    @night_entrance_done.setter
    def night_entrance_done(self, value: bool) -> None:
        DLL.ZkZoneMusic_setNightEntranceDone(self._handle, c_bool(value))


DLL.ZkZoneFarPlane_getVobFarPlaneZ.restype = c_float
DLL.ZkZoneFarPlane_getInnerRangePercentage.restype = c_float


class ZoneFarPlane(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def vob_far_plane_z(self) -> float:
        return DLL.ZkZoneFarPlane_getVobFarPlaneZ(self._handle)

    @vob_far_plane_z.setter
    def vob_far_plane_z(self, value: float) -> None:
        DLL.ZkZoneFarPlane_setVobFarPlaneZ(self._handle, c_float(value))

    @property
    def inner_range_percentage(self) -> float:
        return DLL.ZkZoneFarPlane_getInnerRangePercentage(self._handle)

    @inner_range_percentage.setter
    def inner_range_percentage(self, value: float) -> None:
        DLL.ZkZoneFarPlane_setInnerRangePercentage(self._handle, c_float(value))


DLL.ZkZoneFog_getRangeCenter.restype = c_float
DLL.ZkZoneFog_getInnerRangePercentage.restype = c_float
DLL.ZkZoneFog_getColor.restype = Color
DLL.ZkZoneFog_getFadeOutSky.restype = c_bool
DLL.ZkZoneFog_getOverrideColor.restype = c_bool


class ZoneFog(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def range_center(self) -> float:
        return DLL.ZkZoneFog_getRangeCenter(self._handle)

    @range_center.setter
    def range_center(self, value: float) -> None:
        DLL.ZkZoneFog_setRangeCenter(self._handle, c_float(value))

    @property
    def inner_range_percentage(self) -> float:
        return DLL.ZkZoneFog_getInnerRangePercentage(self._handle)

    @inner_range_percentage.setter
    def inner_range_percentage(self, value: float) -> None:
        DLL.ZkZoneFog_setInnerRangePercentage(self._handle, c_float(value))

    @property
    def color(self) -> Color:
        return DLL.ZkZoneFog_getColor(self._handle)

    @color.setter
    def color(self, value: Color) -> None:
        DLL.ZkZoneFog_setColor(self._handle, value)

    @property
    def fade_out_sky(self) -> bool:
        return DLL.ZkZoneFog_getFadeOutSky(self._handle)

    @fade_out_sky.setter
    def fade_out_sky(self, value: bool) -> None:
        DLL.ZkZoneFog_setFadeOutSky(self._handle, c_bool(value))

    @property
    def override_color(self) -> bool:
        return DLL.ZkZoneFog_getOverrideColor(self._handle)

    @override_color.setter
    def override_color(self, value: bool) -> None:
        DLL.ZkZoneFog_setOverrideColor(self._handle, c_bool(value))
