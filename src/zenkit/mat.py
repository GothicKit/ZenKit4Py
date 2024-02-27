__all__ = [
    "Material",
    "MaterialGroup",
    "AnimationMapping",
    "WaveSpeed",
    "AlphaFunction",
    "WaveMode",
]

from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_void_p
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._core import Vec2f
from zenkit._native import ZkString


class MaterialGroup(IntEnum):
    UNDEFINED = 0
    METAL = 1
    STONE = 2
    WOOD = 3
    EARTH = 4
    WATER = 5
    SNOW = 6


class AnimationMapping(IntEnum):
    NONE = 0
    LINEAR = 1


class WaveMode(IntEnum):
    NONE = 0
    GROUND_AMBIENT = 1
    GROUND = 2
    WALL_AMBIENT = 3
    WALL = 4
    ENVIRONMENT = 5
    WIND_AMBIENT = 6
    WIND = 7


class WaveSpeed(IntEnum):
    NONE = 0
    SLOW = 1
    NORMAL = 2
    FAST = 3


class AlphaFunction(IntEnum):
    DEFAULT = 0
    NONE = 1
    BLEND = 2
    ADD = 3
    SUBTRACT = 4
    MULTIPLY = 5
    MULTIPLY_ALT = 6


DLL.ZkMaterial_getName.restype = ZkString
DLL.ZkMaterial_getGroup.restype = c_int
DLL.ZkMaterial_getColor.restype = c_uint
DLL.ZkMaterial_getSmoothAngle.restype = c_float
DLL.ZkMaterial_getTexture.restype = ZkString
DLL.ZkMaterial_getTextureScale.restype = Vec2f
DLL.ZkMaterial_getTextureAnimationFps.restype = c_float
DLL.ZkMaterial_getTextureAnimationMapping.restype = c_int
DLL.ZkMaterial_getTextureAnimationMappingDirection.restype = Vec2f
DLL.ZkMaterial_getDisableCollision.restype = c_bool
DLL.ZkMaterial_getDisableLightmap.restype = c_bool
DLL.ZkMaterial_getDontCollapse.restype = c_bool
DLL.ZkMaterial_getDetailObject.restype = ZkString
DLL.ZkMaterial_getForceOccluder.restype = c_bool
DLL.ZkMaterial_getEnvironmentMapping.restype = c_bool
DLL.ZkMaterial_getEnvironmentMappingStrength.restype = c_float
DLL.ZkMaterial_getWaveMode.restype = c_int
DLL.ZkMaterial_getWaveSpeed.restype = c_int
DLL.ZkMaterial_getWaveAmplitude.restype = c_float
DLL.ZkMaterial_getWaveGridSize.restype = c_float
DLL.ZkMaterial_getIgnoreSun.restype = c_bool
DLL.ZkMaterial_getAlphaFunction.restype = c_int
DLL.ZkMaterial_getDefaultMapping.restype = Vec2f


class Material:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def name(self) -> str:
        return DLL.ZkMaterial_getName(self._handle).value

    @property
    def group(self) -> MaterialGroup:
        return MaterialGroup(DLL.ZkMaterial_getGroup(self._handle))

    @property
    def color(self) -> int:
        return DLL.ZkMaterial_getColor(self._handle)

    @property
    def smooth_angle(self) -> float:
        return DLL.ZkMaterial_getSmoothAngle(self._handle)

    @property
    def texture(self) -> str:
        return DLL.ZkMaterial_getTexture(self._handle).value

    @property
    def texture_scale(self) -> Vec2f:
        return DLL.ZkMaterial_getTextureScale(self._handle)

    @property
    def texture_animation_fps(self) -> float:
        return DLL.ZkMaterial_getTextureAnimationFps(self._handle)

    @property
    def texture_animation_mapping(self) -> AnimationMapping:
        return AnimationMapping(DLL.ZkMaterial_getTextureAnimationMapping(self._handle))

    @property
    def texture_animation_mapping_direction(self) -> Vec2f:
        return DLL.ZkMaterial_getTextureAnimationMappingDirection(self._handle)

    @property
    def disable_collision(self) -> bool:
        return DLL.ZkMaterial_getDisableCollision(self._handle)

    @property
    def disable_lightmap(self) -> bool:
        return DLL.ZkMaterial_getDisableLightmap(self._handle)

    @property
    def dont_collapse(self) -> bool:
        return DLL.ZkMaterial_getDontCollapse(self._handle)

    @property
    def detail_object(self) -> str:
        return DLL.ZkMaterial_getDetailObject(self._handle).value

    @property
    def force_occluder(self) -> bool:
        return DLL.ZkMaterial_getForceOccluder(self._handle)

    @property
    def environment_mapping(self) -> bool:
        return DLL.ZkMaterial_getEnvironmentMapping(self._handle)

    @property
    def environment_mapping_strength(self) -> float:
        return DLL.ZkMaterial_getEnvironmentMappingStrength(self._handle)

    @property
    def wave_mode(self) -> WaveMode:
        return WaveMode(DLL.ZkMaterial_getWaveMode(self._handle))

    @property
    def wave_speed(self) -> WaveSpeed:
        return WaveSpeed(DLL.ZkMaterial_getWaveSpeed(self._handle))

    @property
    def wave_amplitude(self) -> float:
        return DLL.ZkMaterial_getWaveAmplitude(self._handle)

    @property
    def wave_grid_size(self) -> float:
        return DLL.ZkMaterial_getWaveGridSize(self._handle)

    @property
    def ignore_sun(self) -> bool:
        return DLL.ZkMaterial_getIgnoreSun(self._handle)

    @property
    def alpha_function(self) -> AlphaFunction:
        return AlphaFunction(DLL.ZkMaterial_getAlphaFunction(self._handle))

    @property
    def default_mapping(self) -> Vec2f:
        return DLL.ZkMaterial_getDefaultMapping(self._handle)

    def __del__(self) -> None:
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<Material handle={self._handle} name={self.name!r}>"
