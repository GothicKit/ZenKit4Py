__all__ = [
    "Animate",
    "Item",
    "LensFlare",
    "ParticleEffectController",
    "MessageFilterAction",
    "MessageFilter",
    "MoverController",
    "TouchDamage",
    "TouchCollisionType",
    "CodeMaster",
    "Earthquake",
    "MoverMessageType",
]

from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._core import Vec3f
from zenkit._native import ZkString
from zenkit.vob.virtual_object import VirtualObject


class MessageFilterAction(IntEnum):
    NONE = 0
    TRIGGER = 1
    UNTRIGGER = 2
    ENABLE = 3
    DISABLE = 4
    TOGGLE = 5


class MoverMessageType(IntEnum):
    FIXED_DIRECT = 0
    FIXED_ORDER = 1
    NEXT = 2
    PREVIOUS = 3


class TouchCollisionType(IntEnum):
    NONE = 0
    BOX = 1
    POINT = 2


DLL.ZkAnimate_getStartOn.restype = c_bool
DLL.ZkAnimate_getIsRunning.restype = c_bool


class Animate(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def start_on(self) -> bool:
        return DLL.ZkAnimate_getStartOn(self._handle)

    @start_on.setter
    def start_on(self, value: bool) -> None:
        DLL.ZkAnimate_setStartOn(self._handle, c_bool(value))

    @property
    def is_running(self) -> bool:
        return DLL.ZkAnimate_getIsRunning(self._handle)

    @is_running.setter
    def is_running(self, value: bool) -> None:
        DLL.ZkAnimate_setIsRunning(self._handle, c_bool(value))


DLL.ZkItem_getInstance.restype = ZkString
DLL.ZkItem_getAmount.restype = int
DLL.ZkItem_getFlags.restype = int


class Item(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def instance(self) -> str:
        return DLL.ZkItem_getInstance(self._handle).value

    @instance.setter
    def instance(self, value: str) -> None:
        DLL.ZkItem_setInstance(self._handle, value.encode("utf-8"))

    @property
    def amount(self) -> int:
        return DLL.ZkItem_getAmount(self._handle)

    @amount.setter
    def amount(self, value: int) -> None:
        DLL.ZkItem_setAmount(self._handle, int(value))

    @property
    def flags(self) -> int:
        return DLL.ZkItem_getFlags(self._handle)

    @flags.setter
    def flags(self, value: int) -> None:
        DLL.ZkItem_setFlags(self._handle, int(value))


DLL.ZkLensFlare_getEffect.restype = ZkString


class LensFlare(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def effect(self) -> str:
        return DLL.ZkLensFlare_getEffect(self._handle).value

    @effect.setter
    def effect(self, value: str) -> None:
        DLL.ZkLensFlare_setEffect(self._handle, value.encode("utf-8"))


DLL.ZkParticleEffectController_getEffectName.restype = ZkString
DLL.ZkParticleEffectController_getKillWhenDone.restype = c_bool
DLL.ZkParticleEffectController_getInitiallyRunning.restype = c_bool


class ParticleEffectController(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def effect_name(self) -> str:
        return DLL.ZkParticleEffectController_getEffectName(self._handle).value

    @effect_name.setter
    def effect_name(self, value: str) -> None:
        DLL.ZkParticleEffectController_setEffectName(self._handle, value.encode("utf-8"))

    @property
    def kill_when_done(self) -> bool:
        return DLL.ZkParticleEffectController_getKillWhenDone(self._handle)

    @kill_when_done.setter
    def kill_when_done(self, value: bool) -> None:
        DLL.ZkParticleEffectController_setKillWhenDone(self._handle, c_bool(value))

    @property
    def initially_running(self) -> bool:
        return DLL.ZkParticleEffectController_getInitiallyRunning(self._handle)

    @initially_running.setter
    def initially_running(self, value: bool) -> None:
        DLL.ZkParticleEffectController_setInitiallyRunning(self._handle, c_bool(value))


DLL.ZkMessageFilter_getTarget.restype = ZkString
DLL.ZkMessageFilter_getOnTrigger.restype = c_int
DLL.ZkMessageFilter_getOnUntrigger.restype = c_int


class MessageFilter(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def target(self) -> str:
        return DLL.ZkMessageFilter_getTarget(self._handle).value

    @target.setter
    def target(self, value: str) -> None:
        DLL.ZkMessageFilter_setTarget(self._handle, value.encode("utf-8"))

    @property
    def on_trigger(self) -> MessageFilterAction:
        return MessageFilterAction(DLL.ZkMessageFilter_getOnTrigger(self._handle))

    @on_trigger.setter
    def on_trigger(self, value: MessageFilterAction) -> None:
        DLL.ZkMessageFilter_setOnTrigger(self._handle, value.value)

    @property
    def on_untrigger(self) -> MessageFilterAction:
        return MessageFilterAction(DLL.ZkMessageFilter_getOnUntrigger(self._handle))

    @on_untrigger.setter
    def on_untrigger(self, value: MessageFilterAction) -> None:
        DLL.ZkMessageFilter_setOnUntrigger(self._handle, value.value)


DLL.ZkCodeMaster_getTarget.restype = ZkString
DLL.ZkCodeMaster_getOrdered.restype = c_bool
DLL.ZkCodeMaster_getFirstFalseIsFailure.restype = c_bool
DLL.ZkCodeMaster_getFailureTarget.restype = ZkString
DLL.ZkCodeMaster_getUntriggeredCancels.restype = c_bool
DLL.ZkCodeMaster_getSlaveCount.restype = c_size_t
DLL.ZkCodeMaster_getSlave.restype = ZkString


class CodeMaster(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def target(self) -> str:
        return DLL.ZkCodeMaster_getTarget(self._handle).value

    @target.setter
    def target(self, value: str) -> None:
        DLL.ZkCodeMaster_setTarget(self._handle, value.encode("utf-8"))

    @property
    def ordered(self) -> bool:
        return DLL.ZkCodeMaster_getOrdered(self._handle)

    @ordered.setter
    def ordered(self, value: bool) -> None:
        DLL.ZkCodeMaster_setOrdered(self._handle, c_bool(value))

    @property
    def first_false_is_failure(self) -> bool:
        return DLL.ZkCodeMaster_getFirstFalseIsFailure(self._handle)

    @first_false_is_failure.setter
    def first_false_is_failure(self, value: bool) -> None:
        DLL.ZkCodeMaster_setFirstFalseIsFailure(self._handle, c_bool(value))

    @property
    def failure_target(self) -> str:
        return DLL.ZkCodeMaster_getFailureTarget(self._handle).value

    @failure_target.setter
    def failure_target(self, value: str) -> None:
        DLL.ZkCodeMaster_setFailureTarget(self._handle, value.encode("utf-8"))

    @property
    def untriggered_cancels(self) -> bool:
        return DLL.ZkCodeMaster_getUntriggeredCancels(self._handle)

    @untriggered_cancels.setter
    def untriggered_cancels(self, value: bool) -> None:
        DLL.ZkCodeMaster_setUntriggeredCancels(self._handle, c_bool(value))

    @property
    def slaves(self) -> list[str]:
        count = DLL.ZkCodeMaster_getSlaveCount(self._handle)
        return [DLL.ZkCodeMaster_getSlave(self._handle, i) for i in range(count)]

    @slaves.setter
    def slaves(self, value: list[str]) -> None:
        count = DLL.ZkCodeMaster_getSlaveCount(self._handle)
        for _ in range(count):
            DLL.ZkCodeMaster_removeSlave(self._handle, 0)

        for v in value:
            DLL.ZkCodeMaster_addSlave(self._handle, v.encode("utf-8"))


DLL.ZkMoverController_getTarget.restype = ZkString
DLL.ZkMoverController_getMessage.restype = c_int
DLL.ZkMoverController_getKey.restype = c_int32


class MoverController(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def target(self) -> str:
        return DLL.ZkMoverController_getTarget(self._handle).value

    @target.setter
    def target(self, value: str) -> None:
        DLL.ZkMoverController_setTarget(self._handle, value.encode("utf-8"))

    @property
    def message(self) -> MoverMessageType:
        return MoverMessageType(DLL.ZkMoverController_getMessage(self._handle))

    @message.setter
    def message(self, value: MoverMessageType) -> None:
        DLL.ZkMoverController_setMessage(self._handle, value.value)

    @property
    def key(self) -> int:
        return DLL.ZkMoverController_getKey(self._handle)

    @key.setter
    def key(self, value: int) -> None:
        DLL.ZkMoverController_setKey(self._handle, c_int32(value))


DLL.ZkTouchDamage_getDamage.restype = c_float
DLL.ZkTouchDamage_getIsBarrier.restype = c_bool
DLL.ZkTouchDamage_getIsBlunt.restype = c_bool
DLL.ZkTouchDamage_getIsEdge.restype = c_bool
DLL.ZkTouchDamage_getIsFire.restype = c_bool
DLL.ZkTouchDamage_getIsFly.restype = c_bool
DLL.ZkTouchDamage_getIsMagic.restype = c_bool
DLL.ZkTouchDamage_getIsPoint.restype = c_bool
DLL.ZkTouchDamage_getIsFall.restype = c_bool
DLL.ZkTouchDamage_getRepeatDelaySeconds.restype = c_float
DLL.ZkTouchDamage_getVolumeScale.restype = c_float
DLL.ZkTouchDamage_getCollisionType.restype = c_int


class TouchDamage(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def damage(self) -> float:
        return DLL.ZkTouchDamage_getDamage(self._handle)

    @damage.setter
    def damage(self, value: float) -> None:
        DLL.ZkTouchDamage_setDamage(self._handle, c_float(value))

    @property
    def is_barrier(self) -> bool:
        return DLL.ZkTouchDamage_getIsBarrier(self._handle)

    @is_barrier.setter
    def is_barrier(self, value: bool) -> None:
        DLL.ZkTouchDamage_setIsBarrier(self._handle, c_bool(value))

    @property
    def is_blunt(self) -> bool:
        return DLL.ZkTouchDamage_getIsBlunt(self._handle)

    @is_blunt.setter
    def is_blunt(self, value: bool) -> None:
        DLL.ZkTouchDamage_setIsBlunt(self._handle, c_bool(value))

    @property
    def is_edge(self) -> bool:
        return DLL.ZkTouchDamage_getIsEdge(self._handle)

    @is_edge.setter
    def is_edge(self, value: bool) -> None:
        DLL.ZkTouchDamage_setIsEdge(self._handle, c_bool(value))

    @property
    def is_fire(self) -> bool:
        return DLL.ZkTouchDamage_getIsFire(self._handle)

    @is_fire.setter
    def is_fire(self, value: bool) -> None:
        DLL.ZkTouchDamage_setIsFire(self._handle, c_bool(value))

    @property
    def is_fly(self) -> bool:
        return DLL.ZkTouchDamage_getIsFly(self._handle)

    @is_fly.setter
    def is_fly(self, value: bool) -> None:
        DLL.ZkTouchDamage_setIsFly(self._handle, c_bool(value))

    @property
    def is_magic(self) -> bool:
        return DLL.ZkTouchDamage_getIsMagic(self._handle)

    @is_magic.setter
    def is_magic(self, value: bool) -> None:
        DLL.ZkTouchDamage_setIsMagic(self._handle, c_bool(value))

    @property
    def is_point(self) -> bool:
        return DLL.ZkTouchDamage_getIsPoint(self._handle)

    @is_point.setter
    def is_point(self, value: bool) -> None:
        DLL.ZkTouchDamage_setIsPoint(self._handle, c_bool(value))

    @property
    def is_fall(self) -> bool:
        return DLL.ZkTouchDamage_getIsFall(self._handle)

    @is_fall.setter
    def is_fall(self, value: bool) -> None:
        DLL.ZkTouchDamage_setIsFall(self._handle, c_bool(value))

    @property
    def repeat_delay_seconds(self) -> float:
        return DLL.ZkTouchDamage_getRepeatDelaySeconds(self._handle)

    @repeat_delay_seconds.setter
    def repeat_delay_seconds(self, value: float) -> None:
        DLL.ZkTouchDamage_setRepeatDelaySeconds(self._handle, c_float(value))

    @property
    def volume_scale(self) -> float:
        return DLL.ZkTouchDamage_getVolumeScale(self._handle)

    @volume_scale.setter
    def volume_scale(self, value: float) -> None:
        DLL.ZkTouchDamage_setVolumeScale(self._handle, c_float(value))

    @property
    def collision_type(self) -> TouchCollisionType:
        return TouchCollisionType(DLL.ZkTouchDamage_getCollisionType(self._handle))

    @collision_type.setter
    def collision_type(self, value: TouchCollisionType) -> None:
        DLL.ZkTouchDamage_setCollisionType(self._handle, value.value)


DLL.ZkEarthquake_getRadius.restype = c_float
DLL.ZkEarthquake_getDuration.restype = c_float
DLL.ZkEarthquake_getAmplitude.restype = Vec3f


class Earthquake(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def radius(self) -> float:
        return DLL.ZkEarthquake_getRadius(self._handle)

    @radius.setter
    def radius(self, value: float) -> None:
        DLL.ZkEarthquake_setRadius(self._handle, c_float(value))

    @property
    def duration(self) -> float:
        return DLL.ZkEarthquake_getDuration(self._handle)

    @duration.setter
    def duration(self, value: float) -> None:
        DLL.ZkEarthquake_setDuration(self._handle, c_float(value))

    @property
    def amplitude(self) -> Vec3f:
        return DLL.ZkEarthquake_getAmplitude(self._handle)

    @amplitude.setter
    def amplitude(self, value: Vec3f) -> None:
        DLL.ZkEarthquake_setAmplitude(self._handle, Vec3f(value))
