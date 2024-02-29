__all__ = [
    "VirtualObject",
    "Visual",
    "VobType",
    "EventManager",
    "Ai",
    "AnimationType",
    "ShadowType",
    "SpriteAlignment",
    "VisualDecal",
    "VisualType",
    "AiType",
    "AiMove",
    "AiHuman",
]

from collections.abc import Iterator
from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from ctypes import c_uint8
from ctypes import c_uint32
from ctypes import c_void_p
from enum import IntEnum
from typing import Any
from typing import Final
from typing import cast

from zenkit import AlphaFunction
from zenkit._core import DLL
from zenkit._core import AxisAlignedBoundingBox
from zenkit._core import Mat3x3
from zenkit._core import Vec2f
from zenkit._core import Vec3f
from zenkit._native import ZkPointer
from zenkit._native import ZkString


class VobType(IntEnum):
    zCVob = 0
    zCVobLevelCompo = 1
    oCItem = 2
    oCNpc = 3
    zCMoverController = 4
    zCVobScreenFX = 5
    zCVobStair = 6
    zCPFXController = 7
    zCVobAnimate = 8
    zCVobLensFlare = 9
    zCVobLight = 10
    zCVobSpot = 11
    zCVobStartpoint = 12
    zCMessageFilter = 13
    zCCodeMaster = 14
    zCTriggerWorldStart = 15
    zCCSCamera = 16
    zCCamTrj_KeyFrame = 17
    oCTouchDamage = 18
    zCTriggerUntouch = 19
    zCEarthquake = 20
    oCMOB = 21
    oCMobInter = 22
    oCMobBed = 23
    oCMobFire = 24
    oCMobLadder = 25
    oCMobSwitch = 26
    oCMobWheel = 27
    oCMobContainer = 28
    oCMobDoor = 29
    zCTrigger = 30
    zCTriggerList = 31
    oCTriggerScript = 32
    oCTriggerChangeLevel = 33
    oCCSTrigger = 34
    zCMover = 35
    zCVobSound = 36
    zCVobSoundDaytime = 37
    oCZoneMusic = 38
    oCZoneMusicDefault = 39
    zCZoneZFog = 40
    zCZoneZFogDefault = 41
    zCZoneVobFarPlane = 42
    zCZoneVobFarPlaneDefault = 43
    ignored = 44
    unknown = 45


class SpriteAlignment(IntEnum):
    NONE = 0
    YAW = 1
    FULL = 2


class ShadowType(IntEnum):
    NONE = 0
    BLOB = 1


class AnimationType(IntEnum):
    NONE = 0
    WIND = 1
    WIND_ALT = 2


class VisualType(IntEnum):
    DECAL = 0
    MESH = 1
    MULTI_RESOLUTION_MESH = 2
    PARTICLE_EFFECT = 3
    CAMERA = 4
    MODEL = 5
    MORPH_MESH = 6
    UNKNOWN = 7


class AiType(IntEnum):
    HUMAN = 0
    MOVE = 1


DLL.ZkVisual_getName.restype = ZkString
DLL.ZkVisual_getType.restype = c_int
DLL.ZkVisual_new.restype = ZkPointer


class Visual:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def new(fmt: VisualType) -> "Visual":
        return Visual.from_native(
            DLL.ZkVisual_new(fmt.value).value,
            _delete=True,
            _keepalive=DLL,
        )

    @staticmethod
    def from_native(handle: c_void_p, *, _delete: bool = False, _keepalive: Any = None) -> "Visual | None":
        if handle.value is None:
            return None
        visual = VisualType(DLL.ZkVisual_getType(handle))
        return _VISUALS.get(visual, Visual)(_handle=handle, _delete=_delete, _keepalive=_keepalive)

    @property
    def handle(self) -> c_void_p:
        return self._handle

    @property
    def name(self) -> str:
        return DLL.ZkVisual_getName(self._handle).value

    @name.setter
    def name(self, value: str) -> None:
        DLL.ZkVisual_setName(self._handle, value.encode("utf-8"))

    @property
    def type(self) -> VisualType:
        return VisualType(DLL.ZkVisual_getType(self._handle))

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkVisual_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<{self.__class__} handle={self.handle} name={self.name} type={self.type.name}>"


DLL.ZkVisualDecal_getName.restype = ZkString
DLL.ZkVisualDecal_getDimension.restype = Vec2f
DLL.ZkVisualDecal_getOffset.restype = Vec2f
DLL.ZkVisualDecal_getTwoSided.restype = c_bool
DLL.ZkVisualDecal_getAlphaFunc.restype = c_int
DLL.ZkVisualDecal_getTextureAnimFps.restype = c_float
DLL.ZkVisualDecal_getAlphaWeight.restype = c_uint8
DLL.ZkVisualDecal_getIgnoreDaylight.restype = c_bool


class VisualDecal(Visual):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def new(*args: Any) -> "VisualDecal":
        return cast(VisualDecal, Visual.new(VisualType.DECAL))

    @property
    def name(self) -> str:
        return DLL.ZkVisualDecal_getName(self._handle).value

    @name.setter
    def name(self, value: str) -> None:
        DLL.ZkVisualDecal_setName(self._handle, value.encode("utf-8"))

    @property
    def dimension(self) -> Vec2f:
        return DLL.ZkVisualDecal_getDimension(self._handle)

    @dimension.setter
    def dimension(self, value: Vec2f) -> None:
        DLL.ZkVisualDecal_setDimension(self._handle, value)

    @property
    def offset(self) -> Vec2f:
        return DLL.ZkVisualDecal_getOffset(self._handle)

    @offset.setter
    def offset(self, value: Vec2f) -> None:
        DLL.ZkVisualDecal_setOffset(self._handle, value)

    @property
    def two_sided(self) -> bool:
        return DLL.ZkVisualDecal_getTwoSided(self._handle)

    @two_sided.setter
    def two_sided(self, value: bool) -> None:
        DLL.ZkVisualDecal_setTwoSided(self._handle, c_bool(value))

    @property
    def alpha_func(self) -> AlphaFunction:
        return AlphaFunction(DLL.ZkVisualDecal_getAlphaFunc(self._handle))

    @alpha_func.setter
    def alpha_func(self, value: AlphaFunction) -> None:
        DLL.ZkVisualDecal_setAlphaFunc(self._handle, value.value)

    @property
    def texture_anim_fps(self) -> float:
        return DLL.ZkVisualDecal_getTextureAnimFps(self._handle)

    @texture_anim_fps.setter
    def texture_anim_fps(self, value: float) -> None:
        DLL.ZkVisualDecal_setTextureAnimFps(self._handle, c_float(value))

    @property
    def alpha_weight(self) -> int:
        return DLL.ZkVisualDecal_getAlphaWeight(self._handle)

    @alpha_weight.setter
    def alpha_weight(self, value: int) -> None:
        DLL.ZkVisualDecal_setAlphaWeight(self._handle, c_uint8(value))

    @property
    def ignore_daylight(self) -> bool:
        return DLL.ZkVisualDecal_getIgnoreDaylight(self._handle)

    @ignore_daylight.setter
    def ignore_daylight(self, value: bool) -> None:
        DLL.ZkVisualDecal_setIgnoreDaylight(self._handle, c_bool(value))


_VISUALS: Final[dict[VisualType, type[Visual]]] = {
    VisualType.DECAL: VisualDecal,
    VisualType.MESH: Visual,
    VisualType.MULTI_RESOLUTION_MESH: Visual,
    VisualType.PARTICLE_EFFECT: Visual,
    VisualType.CAMERA: Visual,
    VisualType.MODEL: Visual,
    VisualType.MORPH_MESH: Visual,
    VisualType.UNKNOWN: Visual,
}

DLL.ZkAi_new.restype = ZkPointer
DLL.ZkAi_getType.restype = c_int


class Ai:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def new(fmt: AiType) -> "Ai":
        return Ai.from_native(
            DLL.ZkAi_new(fmt.value).value,
            _delete=True,
            _keepalive=DLL,
        )

    @staticmethod
    def from_native(handle: c_void_p, *, _delete: bool = False, _keepalive: Any = None) -> "Ai | None":
        if handle.value is None:
            return None
        ai = AiType(DLL.ZkAi_getType(handle))
        return _AIS.get(ai, Ai)(_handle=handle, _delete=_delete, _keepalive=_keepalive)

    @property
    def handle(self) -> c_void_p:
        return self._handle

    @property
    def type(self) -> AiType:
        return AiType(DLL.ZkAi_getType(self._handle))

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkAi_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} handle={self._handle} type={self.type.name}>"


DLL.ZkAiHuman_getWaterLevel.restype = int
DLL.ZkAiHuman_getFloorY.restype = c_float
DLL.ZkAiHuman_getWaterY.restype = c_float
DLL.ZkAiHuman_getCeilY.restype = c_float
DLL.ZkAiHuman_getFeetY.restype = c_float
DLL.ZkAiHuman_getHeadY.restype = c_float
DLL.ZkAiHuman_getFallDistY.restype = c_float
DLL.ZkAiHuman_getFallStartY.restype = c_float
DLL.ZkAiHuman_getNpc.restype = ZkPointer
DLL.ZkAiHuman_getWalkMode.restype = int
DLL.ZkAiHuman_getWeaponMode.restype = int
DLL.ZkAiHuman_getWmodeAst.restype = int
DLL.ZkAiHuman_getWmodeSelect.restype = int
DLL.ZkAiHuman_getChangeWeapon.restype = c_bool
DLL.ZkAiHuman_getActionMode.restype = int


class AiHuman(Ai):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def new(*args) -> "AiHuman":
        return cast(AiHuman, Ai.new(AiType.HUMAN))

    @property
    def water_level(self) -> int:
        return DLL.ZkAiHuman_getWaterLevel(self._handle)

    @property
    def floor_y(self) -> float:
        return DLL.ZkAiHuman_getFloorY(self._handle)

    @property
    def water_y(self) -> float:
        return DLL.ZkAiHuman_getWaterY(self._handle)

    @property
    def ceil_y(self) -> float:
        return DLL.ZkAiHuman_getCeilY(self._handle)

    @property
    def feet_y(self) -> float:
        return DLL.ZkAiHuman_getFeetY(self._handle)

    @property
    def head_y(self) -> float:
        return DLL.ZkAiHuman_getHeadY(self._handle)

    @property
    def fall_dist_y(self) -> float:
        return DLL.ZkAiHuman_getFallDistY(self._handle)

    @property
    def fall_start_y(self) -> float:
        return DLL.ZkAiHuman_getFallStartY(self._handle)

    @property
    def npc(self) -> "VirtualObject":
        # FIXME(lmichaelis): Should return an `Npc` instance
        return VirtualObject.from_native(DLL.ZkAiHuman_getNpc(self._handle).value, takeref=True)

    @property
    def walk_mode(self) -> int:
        return DLL.ZkAiHuman_getWalkMode(self._handle)

    @property
    def weapon_mode(self) -> int:
        return DLL.ZkAiHuman_getWeaponMode(self._handle)

    @property
    def wmode_ast(self) -> int:
        return DLL.ZkAiHuman_getWmodeAst(self._handle)

    @property
    def wmode_select(self) -> int:
        return DLL.ZkAiHuman_getWmodeSelect(self._handle)

    @property
    def change_weapon(self) -> bool:
        return DLL.ZkAiHuman_getChangeWeapon(self._handle)

    @property
    def action_mode(self) -> int:
        return DLL.ZkAiHuman_getActionMode(self._handle)

    @water_level.setter
    def water_level(self, value: int) -> None:
        DLL.ZkAiHuman_setWaterLevel(self._handle, int(value))

    @floor_y.setter
    def floor_y(self, value: float) -> None:
        DLL.ZkAiHuman_setFloorY(self._handle, c_float(value))

    @water_y.setter
    def water_y(self, value: float) -> None:
        DLL.ZkAiHuman_setWaterY(self._handle, c_float(value))

    @ceil_y.setter
    def ceil_y(self, value: float) -> None:
        DLL.ZkAiHuman_setCeilY(self._handle, c_float(value))

    @feet_y.setter
    def feet_y(self, value: float) -> None:
        DLL.ZkAiHuman_setFeetY(self._handle, c_float(value))

    @head_y.setter
    def head_y(self, value: float) -> None:
        DLL.ZkAiHuman_setHeadY(self._handle, c_float(value))

    @fall_dist_y.setter
    def fall_dist_y(self, value: float) -> None:
        DLL.ZkAiHuman_setFallDistY(self._handle, c_float(value))

    @fall_start_y.setter
    def fall_start_y(self, value: float) -> None:
        DLL.ZkAiHuman_setFallStartY(self._handle, c_float(value))

    # FIXME(lmichaelis): Implement this setter
    """
    @npc.setter
    def npc(self, value: Npc) -> None:
        DLL.ZkAiHuman_setNpc(self._handle, value.handle)
    """

    @walk_mode.setter
    def walk_mode(self, value: int) -> None:
        DLL.ZkAiHuman_setWalkMode(self._handle, int(value))

    @weapon_mode.setter
    def weapon_mode(self, value: int) -> None:
        DLL.ZkAiHuman_setWeaponMode(self._handle, int(value))

    @wmode_ast.setter
    def wmode_ast(self, value: int) -> None:
        DLL.ZkAiHuman_setWmodeAst(self._handle, int(value))

    @wmode_select.setter
    def wmode_select(self, value: int) -> None:
        DLL.ZkAiHuman_setWmodeSelect(self._handle, int(value))

    @change_weapon.setter
    def change_weapon(self, value: bool) -> None:
        DLL.ZkAiHuman_setChangeWeapon(self._handle, c_bool(value))

    @action_mode.setter
    def action_mode(self, value: int) -> None:
        DLL.ZkAiHuman_setActionMode(self._handle, int(value))


DLL.ZkAiMove_getVob.restype = ZkPointer
DLL.ZkAiMove_getOwner.restype = ZkPointer


class AiMove(Ai):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def new(*args: Any) -> "AiMove":
        return cast(AiMove, Ai.new(AiType.MOVE))

    @property
    def vob(self) -> "VirtualObject":
        return VirtualObject.from_native(DLL.ZkAiMove_getVob(self._handle).value, takeref=True)

    @vob.setter
    def vob(self, value: "VirtualObject") -> None:
        DLL.ZkAiMove_setVob(self._handle, value.handle)

    @property
    def owner(self) -> "VirtualObject":
        # FIXME(lmichaelis): Should return an `Npc` instance
        return VirtualObject.from_native(DLL.ZkAiMove_getOwner(self._handle).value, takeref=True)

    # FIXME(lmichaelis): Implement this setter
    """
    @owner.setter
    def owner(self, value: Npc) -> None:
        DLL.ZkAiMove_setOwner(self._handle, value.handle)
    """


_AIS: Final[dict[AiType, type[Ai]]] = {AiType.HUMAN: AiHuman, AiType.MOVE: AiMove}


DLL.ZkEventManager_getCleared.restype = c_bool
DLL.ZkEventManager_getActive.restype = c_bool


class EventManager:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def new() -> "EventManager":
        return EventManager(
            _handle=DLL.ZkEventManager_new().value,
            _delete=True,
            _keepalive=DLL,
        )

    @property
    def handle(self) -> c_void_p:
        return self._handle

    @property
    def cleared(self) -> bool:
        return DLL.ZkEventManager_getCleared(self._handle)

    @cleared.setter
    def cleared(self, value: bool) -> None:
        DLL.ZkEventManager_setCleared(self._handle, c_bool(value))

    @property
    def active(self) -> bool:
        return DLL.ZkEventManager_getActive(self._handle)

    @active.setter
    def active(self, value: bool) -> None:
        DLL.ZkEventManager_setActive(self._handle, c_bool(value))

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkEventManager_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} handle={self._handle}>"


DLL.ZkVirtualObject_getType.restype = c_int
DLL.ZkVirtualObject_getId.restype = c_uint32
DLL.ZkVirtualObject_getBbox.restype = AxisAlignedBoundingBox
DLL.ZkVirtualObject_getPosition.restype = Vec3f
DLL.ZkVirtualObject_getRotation.restype = Mat3x3
DLL.ZkVirtualObject_getShowVisual.restype = c_bool
DLL.ZkVirtualObject_getSpriteCameraFacingMode.restype = c_int
DLL.ZkVirtualObject_getCdStatic.restype = c_bool
DLL.ZkVirtualObject_getCdDynamic.restype = c_bool
DLL.ZkVirtualObject_getVobStatic.restype = c_bool
DLL.ZkVirtualObject_getDynamicShadows.restype = c_int
DLL.ZkVirtualObject_getPhysicsEnabled.restype = c_bool
DLL.ZkVirtualObject_getAnimMode.restype = c_int
DLL.ZkVirtualObject_getBias.restype = c_int32
DLL.ZkVirtualObject_getAmbient.restype = c_bool
DLL.ZkVirtualObject_getAnimStrength.restype = c_float
DLL.ZkVirtualObject_getFarClipScale.restype = c_float
DLL.ZkVirtualObject_getPresetName.restype = ZkString
DLL.ZkVirtualObject_getName.restype = ZkString
DLL.ZkVirtualObject_getVisual.restype = ZkPointer
DLL.ZkVirtualObject_getSleepMode.restype = c_uint8
DLL.ZkVirtualObject_getNextOnTimer.restype = c_float
DLL.ZkVirtualObject_getAi.restype = ZkPointer
DLL.ZkVirtualObject_getEventManager.restype = ZkPointer
DLL.ZkVirtualObject_getChildCount.restype = c_size_t
DLL.ZkVirtualObject_getChild.restype = ZkPointer
DLL.ZkVirtualObject_new.restype = ZkPointer
DLL.ZkObject_takeRef.restype = ZkPointer


class VirtualObject:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def new(typ: VobType) -> "VirtualObject":
        return VirtualObject.from_native(DLL.ZkVirtualObject_new(typ.value).value, takeref=False)

    @staticmethod
    def from_native(handle: c_void_p, *, delete: bool = False, keepalive: Any = DLL, takeref: bool) -> "VirtualObject":
        from zenkit.vob import _VOBS

        if handle is None or handle.value is None:
            return None

        if takeref:
            handle = DLL.ZkObject_takeRef(handle).value
            delete = True
            keepalive = None

        typ = VobType(DLL.ZkVirtualObject_getType(handle))
        ctor = _VOBS.get(typ, VirtualObject)

        return ctor(_handle=handle, _delete=delete, _keepalive=keepalive)

    @property
    def handle(self) -> c_void_p:
        return self._handle

    @property
    def type(self) -> VobType:
        return VobType(DLL.ZkVirtualObject_getType(self._handle))

    @property
    def id(self) -> int:
        return DLL.ZkVirtualObject_getId(self._handle)

    @property
    def bbox(self) -> AxisAlignedBoundingBox:
        return DLL.ZkVirtualObject_getBbox(self._handle)

    @bbox.setter
    def bbox(self, value: AxisAlignedBoundingBox) -> None:
        DLL.ZkVirtualObject_setBbox(self._handle, AxisAlignedBoundingBox(value))

    @property
    def position(self) -> Vec3f:
        return DLL.ZkVirtualObject_getPosition(self._handle)

    @position.setter
    def position(self, value: Vec3f) -> None:
        DLL.ZkVirtualObject_setPosition(self._handle, Vec3f(value))

    @property
    def rotation(self) -> Mat3x3:
        return DLL.ZkVirtualObject_getRotation(self._handle)

    @rotation.setter
    def rotation(self, value: Mat3x3) -> None:
        DLL.ZkVirtualObject_setRotation(self._handle, Mat3x3(value))

    @property
    def show_visual(self) -> bool:
        return DLL.ZkVirtualObject_getShowVisual(self._handle)

    @show_visual.setter
    def show_visual(self, value: bool) -> None:
        DLL.ZkVirtualObject_setShowVisual(self._handle, c_bool(value))

    @property
    def sprite_camera_facing_mode(self) -> SpriteAlignment:
        return SpriteAlignment(DLL.ZkVirtualObject_getSpriteCameraFacingMode(self._handle))

    @sprite_camera_facing_mode.setter
    def sprite_camera_facing_mode(self, value: SpriteAlignment) -> None:
        DLL.ZkVirtualObject_setSpriteCameraFacingMode(self._handle, c_int(value.value))

    @property
    def cd_static(self) -> bool:
        return DLL.ZkVirtualObject_getCdStatic(self._handle)

    @cd_static.setter
    def cd_static(self, value: bool) -> None:
        DLL.ZkVirtualObject_setCdStatic(self._handle, c_bool(value))

    @property
    def cd_dynamic(self) -> bool:
        return DLL.ZkVirtualObject_getCdDynamic(self._handle)

    @cd_dynamic.setter
    def cd_dynamic(self, value: bool) -> None:
        DLL.ZkVirtualObject_setCdDynamic(self._handle, c_bool(value))

    @property
    def vob_static(self) -> bool:
        return DLL.ZkVirtualObject_getVobStatic(self._handle)

    @vob_static.setter
    def vob_static(self, value: bool) -> None:
        DLL.ZkVirtualObject_setVobStatic(self._handle, c_bool(value))

    @property
    def dynamic_shadows(self) -> ShadowType:
        return ShadowType(DLL.ZkVirtualObject_getDynamicShadows(self._handle))

    @dynamic_shadows.setter
    def dynamic_shadows(self, value: ShadowType) -> None:
        DLL.ZkVirtualObject_setDynamicShadows(self._handle, value.value)

    @property
    def physics_enabled(self) -> bool:
        return DLL.ZkVirtualObject_getPhysicsEnabled(self._handle)

    @physics_enabled.setter
    def physics_enabled(self, value: bool) -> None:
        DLL.ZkVirtualObject_setPhysicsEnabled(self._handle, c_bool(value))

    @property
    def anim_mode(self) -> AnimationType:
        return AnimationType(DLL.ZkVirtualObject_getAnimMode(self._handle))

    @anim_mode.setter
    def anim_mode(self, value: AnimationType) -> None:
        DLL.ZkVirtualObject_setAnimMode(self._handle, value.value)

    @property
    def bias(self) -> int:
        return DLL.ZkVirtualObject_getBias(self._handle)

    @bias.setter
    def bias(self, value: int) -> None:
        DLL.ZkVirtualObject_setBias(self._handle, c_int32(value))

    @property
    def ambient(self) -> bool:
        return DLL.ZkVirtualObject_getAmbient(self._handle)

    @ambient.setter
    def ambient(self, value: bool) -> None:
        DLL.ZkVirtualObject_setAmbient(self._handle, c_bool(value))

    @property
    def anim_strength(self) -> float:
        return DLL.ZkVirtualObject_getAnimStrength(self._handle)

    @anim_strength.setter
    def anim_strength(self, value: float) -> None:
        DLL.ZkVirtualObject_setAnimStrength(self._handle, c_float(value))

    @property
    def far_clip_scale(self) -> float:
        return DLL.ZkVirtualObject_getFarClipScale(self._handle)

    @far_clip_scale.setter
    def far_clip_scale(self, value: float) -> None:
        DLL.ZkVirtualObject_setFarClipScale(self._handle, c_float(value))

    @property
    def preset_name(self) -> str:
        return DLL.ZkVirtualObject_getPresetName(self._handle).value

    @preset_name.setter
    def preset_name(self, value: str) -> None:
        DLL.ZkVirtualObject_setPresetName(self._handle, value.encode("utf-8"))

    @property
    def name(self) -> str:
        return DLL.ZkVirtualObject_getName(self._handle).value

    @name.setter
    def name(self, value: str) -> None:
        DLL.ZkVirtualObject_setName(self._handle, value.encode("utf-8"))

    @property
    def visual(self) -> Visual | None:
        handle = DLL.ZkVirtualObject_getVisual(self._handle).value
        return Visual.from_native(handle, _keepalive=self)

    @visual.setter
    def visual(self, value: Visual) -> None:
        DLL.ZkVirtualObject_setVisual(self._handle, value.handle)

    @property
    def sleep_mode(self) -> int:
        return DLL.ZkVirtualObject_getSleepMode(self._handle)

    @sleep_mode.setter
    def sleep_mode(self, value: int) -> None:
        DLL.ZkVirtualObject_setSleepMode(self._handle, c_uint8(value))

    @property
    def next_on_timer(self) -> float:
        return DLL.ZkVirtualObject_getNextOnTimer(self._handle)

    @next_on_timer.setter
    def next_on_timer(self, value: float) -> None:
        DLL.ZkVirtualObject_setNextOnTimer(self._handle, c_float(value))

    @property
    def ai(self) -> Ai | None:
        handle = DLL.ZkVirtualObject_getAi(self._handle).value
        if handle.value is None:
            return None
        return Ai(_handle=handle, _keepalive=self)

    @ai.setter
    def ai(self, value: Ai) -> None:
        DLL.ZkVirtualObject_setAi(self._handle, value.handle)

    @property
    def event_manager(self) -> EventManager | None:
        handle = DLL.ZkVirtualObject_getEventManager(self._handle).value
        if handle.value is None:
            return None
        return EventManager(_handle=handle, _keepalive=self)

    @event_manager.setter
    def event_manager(self, value: EventManager | None) -> None:
        DLL.ZkVirtualObject_setEventManager(self._handle, value.handle)

    @property
    def children(self) -> list["VirtualObject"]:
        count = DLL.ZkVirtualObject_getChildCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkVirtualObject_getChild(self._handle, i)
            items.append(VirtualObject.from_native(handle, takeref=True))

        return items

    def get_child(self, i: int) -> "VirtualObject":
        handle = DLL.ZkVirtualObject_getChild(self._handle, i)
        return VirtualObject.from_native(handle, takeref=True)

    def add_child(self, child: "VirtualObject") -> None:
        DLL.ZkVirtualObject_addChild(self._handle, child._handle)

    def remove_child(self, i: int) -> None:
        DLL.ZkVirtualObject_removeChild(self._handle, c_size_t(i))

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkVirtualObject_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} handle={self._handle} name={self.name!r} type={self.type.name}>"

    def __iter__(self) -> Iterator["VirtualObject"]:
        return iter(self.children)

    def __getitem__(self, item: int) -> "VirtualObject":
        return self.get_child(item)

    def __delitem__(self, item: int) -> None:
        self.remove_child(item)
