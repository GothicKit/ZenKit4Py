__all__ = [
    "AnimationCombine",
    "AnimationBlend",
    "AnimationAlias",
    "Animation",
    "AnimationFlags",
    "AnimationDirection",
    "EventCameraTremor",
    "EventMorphAnimation",
    "EventParticleEffect",
    "EventParticleEffectStop",
    "EventSoundEffect",
    "EventSoundEffectGround",
    "EventTag",
    "EventType",
    "FightMode",
    "ModelScript",
]

from ctypes import POINTER
from ctypes import byref
from ctypes import c_float
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from ctypes import c_uint32
from ctypes import c_void_p
from enum import IntEnum
from enum import IntFlag
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._native import ZkPointer
from zenkit._native import ZkString


class AnimationFlags(IntFlag):
    NONE = 0
    MOVE = 1
    ROTATE = 2
    QUEUE = 4
    FLY = 8
    IDLE = 16
    INPLACE = 32


class AnimationDirection(IntEnum):
    FORWARD = (0,)
    BACKWARD = (1,)


class EventType(IntEnum):
    UNKNOWN = 0
    ITEM_CREATE = 1
    ITEM_INSERT = 2
    ITEM_REMOVE = 3
    ITEM_DESTROY = 4
    ITEM_PLACE = 5
    ITEM_EXCHANGE = 6
    SET_FIGHT_MODE = 7
    MUNITION_PLACE = 8
    MUNITION_REMOVE = 9
    SOUND_DRAW = 10
    SOUND_UNDRAW = 11
    MESH_SWAP = 12
    TORCH_DRAW = 13
    TORCH_INVENTORY = 14
    TORCH_DROP = 15
    HIT_LIMB = 16
    HIT_DIRECTION = 17
    DAMAGE_MULTIPLIER = 18
    PARRY_FRAME = 19
    OPTIMAL_FRAME = 20
    HIT_END = 21
    COMBO_WINDOW = 22


class FightMode(IntEnum):
    FIST = (0,)
    SINGLE_HANDED = (1,)
    DUAL_HANDED = (2,)
    BOW = (3,)
    CROSSBOW = (4,)
    MAGIC = (5,)
    NONE = (6,)
    INVALID = (0xFF,)


DLL.ZkModelScript_getSkeletonName.restype = ZkString
DLL.ZkModelScript_getSkeletonMeshDisabled.restype = c_int
DLL.ZkModelScript_getDisabledAnimationsCount.restype = c_size_t
DLL.ZkModelScript_getDisabledAnimation.restype = ZkString
DLL.ZkModelScript_getMeshCount.restype = c_size_t
DLL.ZkModelScript_getMesh.restype = ZkString
DLL.ZkModelScript_getModelTagCount.restype = c_size_t
DLL.ZkModelScript_getModelTag.restype = ZkString
DLL.ZkModelScript_getAnimationCombineCount.restype = c_size_t
DLL.ZkModelScript_getAnimationCombine.restype = ZkPointer
DLL.ZkModelScript_getAnimationBlendCount.restype = c_size_t
DLL.ZkModelScript_getAnimationBlend.restype = ZkPointer
DLL.ZkModelScript_getAnimationAliasCount.restype = c_size_t
DLL.ZkModelScript_getAnimationAlias.restype = ZkPointer
DLL.ZkModelScript_getAnimationCount.restype = c_size_t
DLL.ZkModelScript_getAnimation.restype = ZkPointer
DLL.ZkAnimation_getName.restype = ZkString
DLL.ZkAnimation_getLayer.restype = c_uint32
DLL.ZkAnimation_getNext.restype = ZkString
DLL.ZkAnimation_getBlendIn.restype = c_float
DLL.ZkAnimation_getBlendOut.restype = c_float
DLL.ZkAnimation_getFlags.restype = c_int
DLL.ZkAnimation_getModel.restype = ZkString
DLL.ZkAnimation_getDirection.restype = c_int
DLL.ZkAnimation_getFirstFrame.restype = c_int32
DLL.ZkAnimation_getLastFrame.restype = c_int32
DLL.ZkAnimation_getFps.restype = c_float
DLL.ZkAnimation_getSpeed.restype = c_float
DLL.ZkAnimation_getCollisionVolumeScale.restype = c_float
DLL.ZkAnimation_getEventTagCount.restype = c_size_t
DLL.ZkAnimation_getParticleEffectCount.restype = c_size_t
DLL.ZkAnimation_getParticleEffectStopCount.restype = c_size_t
DLL.ZkAnimation_getSoundEffectCount.restype = c_size_t
DLL.ZkAnimation_getSoundEffectGroundCount.restype = c_size_t
DLL.ZkAnimation_getMorphAnimationCount.restype = c_size_t
DLL.ZkAnimation_getCameraTremorCount.restype = c_size_t
DLL.ZkAnimation_getEventTag.restype = ZkPointer
DLL.ZkAnimation_getParticleEffect.restype = ZkPointer
DLL.ZkAnimation_getParticleEffectStop.restype = ZkPointer
DLL.ZkAnimation_getSoundEffect.restype = ZkPointer
DLL.ZkAnimation_getSoundEffectGround.restype = ZkPointer
DLL.ZkAnimation_getMorphAnimation.restype = ZkPointer
DLL.ZkAnimation_getCameraTremor.restype = ZkPointer
DLL.ZkEventTag_getFrame.restype = c_int32
DLL.ZkEventTag_getType.restype = c_int
DLL.ZkEventTag_getSlot.restype = ZkString
DLL.ZkEventTag_getItem.restype = ZkString
DLL.ZkEventTag_getFrames.restype = POINTER(c_int32)
DLL.ZkEventTag_getFightMode.restype = c_int
DLL.ZkEventTag_getIsAttached.restype = c_int
DLL.ZkEventParticleEffect_getFrame.restype = c_int32
DLL.ZkEventParticleEffect_getIndex.restype = c_int32
DLL.ZkEventParticleEffect_getName.restype = ZkString
DLL.ZkEventParticleEffect_getPosition.restype = ZkString
DLL.ZkEventParticleEffect_getIsAttached.restype = c_int
DLL.ZkEventParticleEffectStop_getFrame.restype = c_int32
DLL.ZkEventParticleEffectStop_getIndex.restype = c_int32
DLL.ZkEventSoundEffect_getFrame.restype = c_int32
DLL.ZkEventSoundEffect_getName.restype = ZkString
DLL.ZkEventSoundEffect_getRange.restype = c_float
DLL.ZkEventSoundEffect_getEmptySlot.restype = c_int
DLL.ZkEventSoundEffectGround_getFrame.restype = c_int32
DLL.ZkEventSoundEffectGround_getName.restype = ZkString
DLL.ZkEventSoundEffectGround_getRange.restype = c_float
DLL.ZkEventSoundEffectGround_getEmptySlot.restype = c_int
DLL.ZkMorphAnimation_getFrame.restype = c_int32
DLL.ZkMorphAnimation_getAnimation.restype = ZkString
DLL.ZkMorphAnimation_getNode.restype = ZkString
DLL.ZkEventCameraTremor_getFrame.restype = c_int32
DLL.ZkEventCameraTremor_getField1.restype = c_int32
DLL.ZkEventCameraTremor_getField2.restype = c_int32
DLL.ZkEventCameraTremor_getField3.restype = c_int32
DLL.ZkEventCameraTremor_getField4.restype = c_int32
DLL.ZkAnimationCombine_getName.restype = ZkString
DLL.ZkAnimationCombine_getLayer.restype = c_uint32
DLL.ZkAnimationCombine_getNext.restype = ZkString
DLL.ZkAnimationCombine_getBlendIn.restype = c_float
DLL.ZkAnimationCombine_getBlendOut.restype = c_float
DLL.ZkAnimationCombine_getFlags.restype = c_int
DLL.ZkAnimationCombine_getModel.restype = ZkString
DLL.ZkAnimationCombine_getLastFrame.restype = c_int32
DLL.ZkAnimationBlend_getName.restype = ZkString
DLL.ZkAnimationBlend_getNext.restype = ZkString
DLL.ZkAnimationBlend_getBlendIn.restype = c_float
DLL.ZkAnimationBlend_getBlendOut.restype = c_float
DLL.ZkAnimationAlias_getName.restype = ZkString
DLL.ZkAnimationAlias_getLayer.restype = c_uint32
DLL.ZkAnimationAlias_getNext.restype = ZkString
DLL.ZkAnimationAlias_getBlendIn.restype = c_float
DLL.ZkAnimationAlias_getBlendOut.restype = c_float
DLL.ZkAnimationAlias_getFlags.restype = c_int
DLL.ZkAnimationAlias_getAlias.restype = ZkString
DLL.ZkAnimationAlias_getDirection.restype = c_int


class ModelScript:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "ModelScript":
        handle = _native.load("ZkModelScript_load", path_or_file_like)
        return ModelScript(_handle=handle, _delete=True)

    @property
    def skeleton_name(self) -> str:
        return DLL.ZkModelScript_getSkeletonName(self._handle).value

    @property
    def skeleton_mesh_disabled(self) -> bool:
        return DLL.ZkModelScript_getSkeletonMeshDisabled(self._handle) != 0

    @property
    def disabled_animations(self) -> list[str]:
        count = DLL.ZkModelScript_getDisabledAnimationsCount(self._handle)
        return [DLL.ZkModelScript_getDisabledAnimation(self._handle, i).value for i in range(count)]

    @property
    def meshes(self) -> list[str]:
        count = DLL.ZkModelScript_getMeshCount(self._handle)
        return [DLL.ZkModelScript_getMesh(self._handle, i).value for i in range(count)]

    @property
    def animation_combines(self) -> list["AnimationCombine"]:
        count = DLL.ZkModelScript_getAnimationCombineCount(self._handle)
        return [
            AnimationCombine(_handle=DLL.ZkModelScript_getAnimationCombine(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]

    @property
    def animation_blends(self) -> list["AnimationBlend"]:
        count = DLL.ZkModelScript_getAnimationBlendCount(self._handle)
        return [
            AnimationBlend(_handle=DLL.ZkModelScript_getAnimationBlend(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]

    @property
    def animation_aliases(self) -> list["AnimationAlias"]:
        count = DLL.ZkModelScript_getAnimationAliasCount(self._handle)
        return [
            AnimationAlias(_handle=DLL.ZkModelScript_getAnimationAlias(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]

    @property
    def model_tags(self) -> list[str]:
        count = DLL.ZkModelScript_getModelTagCount(self._handle)
        return [DLL.ZkModelScript_getModelTag(self._handle, i).value for i in range(count)]

    @property
    def animations(self) -> list["Animation"]:
        count = DLL.ZkModelScript_getAnimationCount(self._handle)
        return [
            Animation(_handle=DLL.ZkModelScript_getAnimation(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkModelScript_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<ModelScript handle={self._handle} name={self.skeleton_name!r}>"


class Animation:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)
        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<Animation handle={self._handle} name={self.name!r} next={self.next!r} layer={self.layer}>"

    @property
    def name(self) -> str:
        return DLL.ZkAnimation_getName(self._handle).value

    @property
    def layer(self) -> int:
        return DLL.ZkAnimation_getLayer(self._handle)

    @property
    def next(self) -> str:
        return DLL.ZkAnimation_getNext(self._handle).value

    @property
    def blend_in(self) -> float:
        return DLL.ZkAnimation_getBlendIn(self._handle)

    @property
    def blend_out(self) -> float:
        return DLL.ZkAnimation_getBlendOut(self._handle)

    @property
    def flags(self) -> AnimationFlags:
        return AnimationFlags(DLL.ZkAnimation_getFlags(self._handle))

    @property
    def model(self) -> str:
        return DLL.ZkAnimation_getModel(self._handle).value

    @property
    def direction(self) -> AnimationDirection:
        return AnimationDirection(DLL.ZkAnimation_getDirection(self._handle))

    @property
    def first_frame(self) -> int:
        return DLL.ZkAnimation_getFirstFrame(self._handle)

    @property
    def last_frame(self) -> int:
        return DLL.ZkAnimation_getLastFrame(self._handle)

    @property
    def fps(self) -> float:
        return DLL.ZkAnimation_getFps(self._handle)

    @property
    def speed(self) -> float:
        return DLL.ZkAnimation_getSpeed(self._handle)

    @property
    def collision_volume_scale(self) -> float:
        return DLL.ZkAnimation_getCollisionVolumeScale(self._handle)

    @property
    def event_tags(self) -> list["EventTag"]:
        count = DLL.ZkAnimation_getEventTagCount(self._handle)
        return [
            EventTag(_handle=DLL.ZkAnimation_getEventTag(self._handle, i).value, _keepalive=self) for i in range(count)
        ]

    @property
    def particle_effects(self) -> list["EventParticleEffect"]:
        count = DLL.ZkAnimation_getParticleEffectCount(self._handle)
        return [
            EventParticleEffect(_handle=DLL.ZkAnimation_getParticleEffect(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]

    @property
    def particle_effects_stop(self) -> list["EventParticleEffectStop"]:
        count = DLL.ZkAnimation_getParticleEffectStopCount(self._handle)
        return [
            EventParticleEffectStop(
                _handle=DLL.ZkAnimation_getParticleEffectStop(self._handle, i).value, _keepalive=self
            )
            for i in range(count)
        ]

    @property
    def sound_effects(self) -> list["EventSoundEffect"]:
        count = DLL.ZkAnimation_getSoundEffectCount(self._handle)
        return [
            EventSoundEffect(_handle=DLL.ZkAnimation_getSoundEffect(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]

    @property
    def sound_effects_ground(self) -> list["EventSoundEffectGround"]:
        count = DLL.ZkAnimation_getSoundEffectGroundCount(self._handle)
        return [
            EventSoundEffectGround(_handle=DLL.ZkAnimation_getSoundEffectGround(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]

    @property
    def morph_animations(self) -> list["EventMorphAnimation"]:
        count = DLL.ZkAnimation_getMorphAnimationCount(self._handle)
        return [
            EventMorphAnimation(_handle=DLL.ZkAnimation_getMorphAnimation(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]

    @property
    def camera_tremors(self) -> list["EventCameraTremor"]:
        count = DLL.ZkAnimation_getCameraTremorCount(self._handle)
        return [
            EventCameraTremor(_handle=DLL.ZkAnimation_getCameraTremor(self._handle, i).value, _keepalive=self)
            for i in range(count)
        ]


class AnimationCombine:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<AnimationCombine handle={self._handle} name={self.name!r} next={self.next!r} layer={self.layer}>"

    @property
    def name(self) -> str:
        return DLL.ZkAnimationCombine_getName(self._handle).value

    @property
    def layer(self) -> int:
        return DLL.ZkAnimationCombine_getLayer(self._handle)

    @property
    def next(self) -> str:
        return DLL.ZkAnimationCombine_getNext(self._handle).value

    @property
    def blend_in(self) -> float:
        return DLL.ZkAnimationCombine_getBlendIn(self._handle)

    @property
    def blend_out(self) -> float:
        return DLL.ZkAnimationCombine_getBlendOut(self._handle)

    @property
    def flags(self) -> AnimationFlags:
        return AnimationFlags(DLL.ZkAnimationCombine_getFlags(self._handle))

    @property
    def model(self) -> str:
        return DLL.ZkAnimationCombine_getModel(self._handle).value

    @property
    def last_frame(self) -> int:
        return DLL.ZkAnimationCombine_getLastFrame(self._handle)


class AnimationBlend:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<AnimationCombine handle={self._handle} name={self.name!r} next={self.next!r}>"

    @property
    def name(self) -> str:
        return DLL.ZkAnimationBlend_getName(self._handle).value

    @property
    def next(self) -> str:
        return DLL.ZkAnimationBlend_getNext(self._handle).value

    @property
    def blend_in(self) -> float:
        return DLL.ZkAnimationBlend_getBlendIn(self._handle)

    @property
    def blend_out(self) -> float:
        return DLL.ZkAnimationBlend_getBlendOut(self._handle)


class AnimationAlias:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<AnimationAlias handle={self._handle} name={self.name!r} next={self.next!r} layer={self.layer}>"

    @property
    def name(self) -> str:
        return DLL.ZkAnimationAlias_getName(self._handle).value

    @property
    def layer(self) -> int:
        return DLL.ZkAnimationAlias_getLayer(self._handle)

    @property
    def next(self) -> str:
        return DLL.ZkAnimationAlias_getNext(self._handle).value

    @property
    def blend_in(self) -> float:
        return DLL.ZkAnimationAlias_getBlendIn(self._handle)

    @property
    def blend_out(self) -> float:
        return DLL.ZkAnimationAlias_getBlendOut(self._handle)

    @property
    def flags(self) -> AnimationFlags:
        return AnimationFlags(DLL.ZkAnimationAlias_getFlags(self._handle))

    @property
    def alias(self) -> str:
        return DLL.ZkAnimationAlias_getAlias(self._handle).value

    @property
    def direction(self) -> AnimationDirection:
        return AnimationDirection(DLL.ZkAnimationAlias_getDirection(self._handle))


class EventTag:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<EventTag handle={self._handle} frame={self.frame}>"

    @property
    def frame(self) -> int:
        return DLL.ZkEventTag_getFrame(self._handle)

    @property
    def type(self) -> EventType:
        return EventType(DLL.ZkEventTag_getType(self._handle))

    @property
    def slot(self) -> str:
        return DLL.ZkEventTag_getSlot(self._handle).value

    @property
    def item(self) -> str:
        return DLL.ZkEventTag_getItem(self._handle).value

    @property
    def frames(self) -> list[int]:
        count = c_size_t(0)
        handle = DLL.ZkEventTag_getFrames(self._handle, byref(count))
        return [handle[i] for i in range(count.value)]

    @property
    def fight_mode(self) -> FightMode:
        return FightMode(DLL.ZkEventTag_getFightMode(self._handle))

    @property
    def is_attached(self) -> bool:
        return DLL.ZkEventTag_getIsAttached(self._handle) != 0


class EventParticleEffect:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<EventParticleEffect handle={self._handle} frame={self.frame} name={self.name!r} index={self.index}>"

    @property
    def frame(self) -> int:
        return DLL.ZkEventParticleEffect_getFrame(self._handle)

    @property
    def index(self) -> int:
        return DLL.ZkEventParticleEffect_getIndex(self._handle)

    @property
    def name(self) -> str:
        return DLL.ZkEventParticleEffect_getName(self._handle).value

    @property
    def position(self) -> str:
        return DLL.ZkEventParticleEffect_getPosition(self._handle).value

    @property
    def is_attached(self) -> bool:
        return DLL.ZkEventParticleEffect_getIsAttached(self._handle) != 0


class EventParticleEffectStop:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<EventParticleEffectStop handle={self._handle} frame={self.frame} index={self.index}>"

    @property
    def frame(self) -> int:
        return DLL.ZkEventParticleEffectStop_getFrame(self._handle)

    @property
    def index(self) -> int:
        return DLL.ZkEventParticleEffectStop_getIndex(self._handle)


class EventSoundEffect:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<EventSoundEffect handle={self._handle} frame={self.frame} name={self.name!r}>"

    @property
    def frame(self) -> int:
        return DLL.ZkEventSoundEffect_getFrame(self._handle)

    @property
    def name(self) -> str:
        return DLL.ZkEventSoundEffect_getName(self._handle).value

    @property
    def range(self) -> float:
        return DLL.ZkEventSoundEffect_getRange(self._handle)

    @property
    def empty_slot(self) -> bool:
        return DLL.ZkEventSoundEffect_getEmptySlot(self._handle) != 0


class EventSoundEffectGround:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<EventSoundEffectGround handle={self._handle} frame={self.frame} name={self.name!r}>"

    @property
    def frame(self) -> int:
        return DLL.ZkEventSoundEffectGround_getFrame(self._handle)

    @property
    def name(self) -> str:
        return DLL.ZkEventSoundEffectGround_getName(self._handle).value

    @property
    def range(self) -> float:
        return DLL.ZkEventSoundEffectGround_getRange(self._handle)

    @property
    def empty_slot(self) -> bool:
        return DLL.ZkEventSoundEffectGround_getEmptySlot(self._handle) != 0


class EventMorphAnimation:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return (f"<EventMorphAnimation handle={self._handle} frame={self.frame} "
                f"animation={self.animation!r} node={self.node!r}>")

    @property
    def frame(self) -> int:
        return DLL.ZkMorphAnimation_getFrame(self._handle)

    @property
    def animation(self) -> str:
        return DLL.ZkMorphAnimation_getAnimation(self._handle).value

    @property
    def node(self) -> str:
        return DLL.ZkMorphAnimation_getNode(self._handle).value


class EventCameraTremor:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    def __repr__(self) -> str:
        return f"<EventCameraTremor handle={self._handle} frame={self.frame}>"

    @property
    def frame(self) -> int:
        return DLL.ZkEventCameraTremor_getFrame(self._handle)

    @property
    def field1(self) -> int:
        return DLL.ZkEventCameraTremor_getField1(self._handle)

    @property
    def field2(self) -> int:
        return DLL.ZkEventCameraTremor_getField2(self._handle)

    @property
    def field3(self) -> int:
        return DLL.ZkEventCameraTremor_getField3(self._handle)

    @property
    def field4(self) -> int:
        return DLL.ZkEventCameraTremor_getField4(self._handle)
