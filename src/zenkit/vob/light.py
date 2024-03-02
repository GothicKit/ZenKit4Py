__all__ = [
    "Light",
    "LightQuality",
    "LightType",
]

from ctypes import POINTER
from ctypes import byref
from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int
from ctypes import c_size_t
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._core import Color
from zenkit._native import ZkString
from zenkit.vob.virtual_object import VirtualObject


class LightType(IntEnum):
    POINT = 0
    SPOT = 1
    RESERVED0 = 2
    RESERVED1 = 3


class LightQuality(IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2


DLL.ZkLight_getPreset.restype = ZkString
DLL.ZkLight_getLightType.restype = c_int
DLL.ZkLight_getRange.restype = c_float
DLL.ZkLight_getColor.restype = Color
DLL.ZkLight_getConeAngle.restype = c_float
DLL.ZkLight_getIsStatic.restype = c_bool
DLL.ZkLight_getQuality.restype = c_int
DLL.ZkLight_getLensflareFx.restype = ZkString
DLL.ZkLight_getOn.restype = c_bool
DLL.ZkLight_getRangeAnimationScale.restype = POINTER(c_float)
DLL.ZkLight_getRangeAnimationFps.restype = c_float
DLL.ZkLight_getRangeAnimationSmooth.restype = c_bool
DLL.ZkLight_getColorAnimationFps.restype = c_float
DLL.ZkLight_getColorAnimationSmooth.restype = c_bool
DLL.ZkLight_getCanMove.restype = c_bool
DLL.ZkLight_getColorAnimationCount.restype = c_int
DLL.ZkLight_getColorAnimationItem.restype = Color


class Light(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def preset(self) -> str:
        return DLL.ZkLight_getPreset(self._handle).value

    @preset.setter
    def preset(self, value: str) -> None:
        DLL.ZkLight_setPreset(self._handle, value.encode("utf-8"))

    @property
    def light_type(self) -> LightType:
        return LightType(DLL.ZkLight_getLightType(self._handle))

    @light_type.setter
    def light_type(self, value: LightType) -> None:
        DLL.ZkLight_setLightType(self._handle, value.value)

    @property
    def range(self) -> float:
        return DLL.ZkLight_getRange(self._handle)

    @range.setter
    def range(self, value: float) -> None:
        DLL.ZkLight_setRange(self._handle, c_float(value))

    @property
    def color(self) -> Color:
        return DLL.ZkLight_getColor(self._handle)

    @color.setter
    def color(self, value: Color) -> None:
        DLL.ZkLight_setColor(self._handle, value)

    @property
    def cone_angle(self) -> float:
        return DLL.ZkLight_getConeAngle(self._handle)

    @cone_angle.setter
    def cone_angle(self, value: float) -> None:
        DLL.ZkLight_setConeAngle(self._handle, c_float(value))

    @property
    def is_static(self) -> bool:
        return DLL.ZkLight_getIsStatic(self._handle)

    @is_static.setter
    def is_static(self, value: bool) -> None:
        DLL.ZkLight_setIsStatic(self._handle, c_bool(value))

    @property
    def quality(self) -> LightQuality:
        return LightQuality(DLL.ZkLight_getQuality(self._handle))

    @quality.setter
    def quality(self, value: LightQuality) -> None:
        DLL.ZkLight_setQuality(self._handle, value.value)

    @property
    def lensflare_fx(self) -> str:
        return DLL.ZkLight_getLensflareFx(self._handle).value

    @lensflare_fx.setter
    def lensflare_fx(self, value: str) -> None:
        DLL.ZkLight_setLensflareFx(self._handle, value.encode("utf-8"))

    @property
    def on(self) -> bool:
        return DLL.ZkLight_getOn(self._handle)

    @on.setter
    def on(self, value: bool) -> None:
        DLL.ZkLight_setOn(self._handle, c_bool(value))

    @property
    def range_animation_scale(self) -> list[float]:
        count = c_size_t(0)
        handle = DLL.ZkLight_getRangeAnimationScale(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @range_animation_scale.setter
    def range_animation_scale(self, value: list[float]) -> None:
        DLL.ZkLight_setRangeAnimationScale(self._handle, POINTER(value))

    @property
    def range_animation_fps(self) -> float:
        return DLL.ZkLight_getRangeAnimationFps(self._handle)

    @range_animation_fps.setter
    def range_animation_fps(self, value: float) -> None:
        DLL.ZkLight_setRangeAnimationFps(self._handle, c_float(value))

    @property
    def range_animation_smooth(self) -> bool:
        return DLL.ZkLight_getRangeAnimationSmooth(self._handle)

    @range_animation_smooth.setter
    def range_animation_smooth(self, value: bool) -> None:
        DLL.ZkLight_setRangeAnimationSmooth(self._handle, c_bool(value))

    @property
    def color_animation(self) -> list[Color]:
        count = DLL.ZkLight_getColorAnimationCount(self._handle)
        return [DLL.ZkLight_getColorAnimationItem(self._handle, i) for i in range(count)]

    @property
    def color_animation_fps(self) -> float:
        return DLL.ZkLight_getColorAnimationFps(self._handle)

    @color_animation_fps.setter
    def color_animation_fps(self, value: float) -> None:
        DLL.ZkLight_setColorAnimationFps(self._handle, c_float(value))

    @property
    def color_animation_smooth(self) -> bool:
        return DLL.ZkLight_getColorAnimationSmooth(self._handle)

    @color_animation_smooth.setter
    def color_animation_smooth(self, value: bool) -> None:
        DLL.ZkLight_setColorAnimationSmooth(self._handle, c_bool(value))

    @property
    def can_move(self) -> bool:
        return DLL.ZkLight_getCanMove(self._handle)

    @can_move.setter
    def can_move(self, value: bool) -> None:
        DLL.ZkLight_setCanMove(self._handle, c_bool(value))
