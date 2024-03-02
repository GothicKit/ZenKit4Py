__all__ = [
    "Trigger",
    "TriggerList",
    "TriggerScript",
    "TriggerChangeLevel",
    "TriggerWorldStart",
    "TriggerUntouch",
    "Mover",
    "MoverBehavior",
    "MoverLerpType",
    "MoverSpeedType",
    "TriggerBatchMode",
    "TriggerListTarget",
]

from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from ctypes import c_uint8
from ctypes import c_uint32
from dataclasses import dataclass
from enum import IntEnum
from typing import Any

from zenkit import AnimationSample
from zenkit._core import DLL
from zenkit._core import Vec3f
from zenkit._native import ZkPointer
from zenkit._native import ZkString
from zenkit.vob.virtual_object import VirtualObject


class MoverBehavior(IntEnum):
    TOGGLE = 0
    TRIGGER_CONTROL = 1
    OPEN_TIME = 2
    LOOP = 3
    SINGLE_KEYS = 4


class MoverLerpType(IntEnum):
    CURVE = 0
    LINEAR = 1


class MoverSpeedType(IntEnum):
    CONSTANT = 0
    SLOW_START_END = 1
    SLOW_START = 2
    SLOW_END = 3
    SEGMENT_SLOW_START_END = 4
    SEGMENT_SLOW_START = 5
    SEGMENT_SLOW_END = 6


class TriggerBatchMode(IntEnum):
    ALL = 0
    NEXT = 1
    RANDOM = 2


DLL.ZkTrigger_getTarget.restype = ZkString
DLL.ZkTrigger_getStartEnabled.restype = c_bool
DLL.ZkTrigger_getSendUntrigger.restype = c_bool
DLL.ZkTrigger_getReactToOnTrigger.restype = c_bool
DLL.ZkTrigger_getReactToOnTouch.restype = c_bool
DLL.ZkTrigger_getReactToOnDamage.restype = c_bool
DLL.ZkTrigger_getRespondToObject.restype = c_bool
DLL.ZkTrigger_getRespondToPC.restype = c_bool
DLL.ZkTrigger_getRespondToNPC.restype = c_bool
DLL.ZkTrigger_getVobTarget.restype = ZkString
DLL.ZkTrigger_getMaxActivationCount.restype = c_int32
DLL.ZkTrigger_getRetriggerDelaySeconds.restype = c_float
DLL.ZkTrigger_getDamageThreshold.restype = c_float
DLL.ZkTrigger_getFireDelaySeconds.restype = c_float
DLL.ZkTrigger_getNextTimeTriggerable.restype = c_float
DLL.ZkTrigger_getOtherVob.restype = ZkPointer
DLL.ZkTrigger_getCountCanBeActivated.restype = c_int
DLL.ZkTrigger_getIsEnabled.restype = c_bool


class Trigger(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def target(self) -> str:
        return DLL.ZkTrigger_getTarget(self._handle).value

    @target.setter
    def target(self, value: str) -> None:
        DLL.ZkTrigger_setTarget(self._handle, value.encode("utf-8"))

    @property
    def start_enabled(self) -> bool:
        return DLL.ZkTrigger_getStartEnabled(self._handle)

    @property
    def send_untrigger(self) -> bool:
        return DLL.ZkTrigger_getSendUntrigger(self._handle)

    @property
    def react_to_on_trigger(self) -> bool:
        return DLL.ZkTrigger_getReactToOnTrigger(self._handle)

    @property
    def react_to_on_touch(self) -> bool:
        return DLL.ZkTrigger_getReactToOnTouch(self._handle)

    @property
    def react_to_on_damage(self) -> bool:
        return DLL.ZkTrigger_getReactToOnDamage(self._handle)

    @property
    def respond_to_object(self) -> bool:
        return DLL.ZkTrigger_getRespondToObject(self._handle)

    @property
    def respond_to_pc(self) -> bool:
        return DLL.ZkTrigger_getRespondToPC(self._handle)

    @property
    def respond_to_npc(self) -> bool:
        return DLL.ZkTrigger_getRespondToNPC(self._handle)

    @start_enabled.setter
    def start_enabled(self, value: bool) -> None:
        DLL.ZkTrigger_setStartEnabled(self._handle, c_bool(value))

    @send_untrigger.setter
    def send_untrigger(self, value: bool) -> None:
        DLL.ZkTrigger_setSendUntrigger(self._handle, c_bool(value))

    @react_to_on_trigger.setter
    def react_to_on_trigger(self, value: bool) -> None:
        DLL.ZkTrigger_setReactToOnTrigger(self._handle, c_bool(value))

    @react_to_on_touch.setter
    def react_to_on_touch(self, value: bool) -> None:
        DLL.ZkTrigger_setReactToOnTouch(self._handle, c_bool(value))

    @react_to_on_damage.setter
    def react_to_on_damage(self, value: bool) -> None:
        DLL.ZkTrigger_setReactToOnDamage(self._handle, c_bool(value))

    @respond_to_object.setter
    def respond_to_object(self, value: bool) -> None:
        DLL.ZkTrigger_setRespondToObject(self._handle, c_bool(value))

    @respond_to_pc.setter
    def respond_to_pc(self, value: bool) -> None:
        DLL.ZkTrigger_setRespondToPC(self._handle, c_bool(value))

    @respond_to_npc.setter
    def respond_to_npc(self, value: bool) -> None:
        DLL.ZkTrigger_setRespondToNPC(self._handle, c_bool(value))

    @property
    def vob_target(self) -> str:
        return DLL.ZkTrigger_getVobTarget(self._handle).value

    @vob_target.setter
    def vob_target(self, value: str) -> None:
        DLL.ZkTrigger_setVobTarget(self._handle, value.encode("utf-8"))

    @property
    def max_activation_count(self) -> int:
        return DLL.ZkTrigger_getMaxActivationCount(self._handle)

    @max_activation_count.setter
    def max_activation_count(self, value: int) -> None:
        DLL.ZkTrigger_setMaxActivationCount(self._handle, c_int32(value))

    @property
    def retrigger_delay_seconds(self) -> float:
        return DLL.ZkTrigger_getRetriggerDelaySeconds(self._handle)

    @retrigger_delay_seconds.setter
    def retrigger_delay_seconds(self, value: float) -> None:
        DLL.ZkTrigger_setRetriggerDelaySeconds(self._handle, c_float(value))

    @property
    def damage_threshold(self) -> float:
        return DLL.ZkTrigger_getDamageThreshold(self._handle)

    @damage_threshold.setter
    def damage_threshold(self, value: float) -> None:
        DLL.ZkTrigger_setDamageThreshold(self._handle, c_float(value))

    @property
    def fire_delay_seconds(self) -> float:
        return DLL.ZkTrigger_getFireDelaySeconds(self._handle)

    @fire_delay_seconds.setter
    def fire_delay_seconds(self, value: float) -> None:
        DLL.ZkTrigger_setFireDelaySeconds(self._handle, c_float(value))

    @property
    def next_time_triggerable(self) -> float:
        return DLL.ZkTrigger_getNextTimeTriggerable(self._handle)

    @property
    def other_vob(self) -> VirtualObject:
        return VirtualObject.from_native(DLL.ZkTrigger_getOtherVob(self._handle).value, takeref=True)

    @property
    def count_can_be_activated(self) -> int:
        return DLL.ZkTrigger_getCountCanBeActivated(self._handle)

    @property
    def is_enabled(self) -> bool:
        return DLL.ZkTrigger_getIsEnabled(self._handle)

    @next_time_triggerable.setter
    def next_time_triggerable(self, value: float) -> None:
        DLL.ZkTrigger_setNextTimeTriggerable(self._handle, c_float(value))

    @other_vob.setter
    def other_vob(self, value: VirtualObject) -> None:
        DLL.ZkTrigger_setOtherVob(self._handle, value.handle)

    @count_can_be_activated.setter
    def count_can_be_activated(self, value: int) -> None:
        DLL.ZkTrigger_setCountCanBeActivated(self._handle, c_int(value))

    @is_enabled.setter
    def is_enabled(self, value: bool) -> None:
        DLL.ZkTrigger_setIsEnabled(self._handle, c_bool(value))


DLL.ZkMover_getBehavior.restype = c_int
DLL.ZkMover_getTouchBlockerDamage.restype = c_float
DLL.ZkMover_getStayOpenTimeSeconds.restype = c_float
DLL.ZkMover_getIsLocked.restype = c_bool
DLL.ZkMover_getAutoLink.restype = c_bool
DLL.ZkMover_getAutoRotate.restype = c_bool
DLL.ZkMover_getSpeed.restype = c_float
DLL.ZkMover_getLerpType.restype = c_int
DLL.ZkMover_getSpeedType.restype = c_int
DLL.ZkMover_getActKeyPosDelta.restype = Vec3f
DLL.ZkMover_getActKeyframeF.restype = c_float
DLL.ZkMover_getActKeyframe.restype = c_int
DLL.ZkMover_getNextKeyframe.restype = c_int
DLL.ZkMover_getMoveSpeedUnit.restype = c_float
DLL.ZkMover_getAdvanceDir.restype = c_float
DLL.ZkMover_getMoverState.restype = c_uint32
DLL.ZkMover_getTriggerEventCount.restype = c_int
DLL.ZkMover_getStayOpenTimeDest.restype = c_float
DLL.ZkMover_getSfxOpenStart.restype = ZkString
DLL.ZkMover_getSfxOpenEnd.restype = ZkString
DLL.ZkMover_getSfxTransitioning.restype = ZkString
DLL.ZkMover_getSfxCloseStart.restype = ZkString
DLL.ZkMover_getSfxCloseEnd.restype = ZkString
DLL.ZkMover_getSfxLock.restype = ZkString
DLL.ZkMover_getSfxUnlock.restype = ZkString
DLL.ZkMover_getSfxUseLocked.restype = ZkString
DLL.ZkMover_getKeyframeCount.restype = c_size_t
DLL.ZkMover_getKeyframe.restype = AnimationSample


class Mover(Trigger):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def behavior(self) -> MoverBehavior:
        return MoverBehavior(DLL.ZkMover_getBehavior(self._handle))

    @behavior.setter
    def behavior(self, value: MoverBehavior) -> None:
        DLL.ZkMover_setBehavior(self._handle, value.value)

    @property
    def touch_blocker_damage(self) -> float:
        return DLL.ZkMover_getTouchBlockerDamage(self._handle)

    @touch_blocker_damage.setter
    def touch_blocker_damage(self, value: float) -> None:
        DLL.ZkMover_setTouchBlockerDamage(self._handle, c_float(value))

    @property
    def stay_open_time_seconds(self) -> float:
        return DLL.ZkMover_getStayOpenTimeSeconds(self._handle)

    @stay_open_time_seconds.setter
    def stay_open_time_seconds(self, value: float) -> None:
        DLL.ZkMover_setStayOpenTimeSeconds(self._handle, c_float(value))

    @property
    def is_locked(self) -> bool:
        return DLL.ZkMover_getIsLocked(self._handle)

    @is_locked.setter
    def is_locked(self, value: bool) -> None:
        DLL.ZkMover_setIsLocked(self._handle, c_bool(value))

    @property
    def auto_link(self) -> bool:
        return DLL.ZkMover_getAutoLink(self._handle)

    @auto_link.setter
    def auto_link(self, value: bool) -> None:
        DLL.ZkMover_setAutoLink(self._handle, c_bool(value))

    @property
    def auto_rotate(self) -> bool:
        return DLL.ZkMover_getAutoRotate(self._handle)

    @auto_rotate.setter
    def auto_rotate(self, value: bool) -> None:
        DLL.ZkMover_setAutoRotate(self._handle, c_bool(value))

    @property
    def speed(self) -> float:
        return DLL.ZkMover_getSpeed(self._handle)

    @speed.setter
    def speed(self, value: float) -> None:
        DLL.ZkMover_setSpeed(self._handle, c_float(value))

    @property
    def lerp_type(self) -> MoverLerpType:
        return MoverLerpType(DLL.ZkMover_getLerpType(self._handle))

    @lerp_type.setter
    def lerp_type(self, value: MoverLerpType) -> None:
        DLL.ZkMover_setLerpType(self._handle, value.value)

    @property
    def speed_type(self) -> MoverSpeedType:
        return MoverSpeedType(DLL.ZkMover_getSpeedType(self._handle))

    @speed_type.setter
    def speed_type(self, value: MoverSpeedType) -> None:
        DLL.ZkMover_setSpeedType(self._handle, value.value)

    @property
    def act_key_pos_delta(self) -> Vec3f:
        return DLL.ZkMover_getActKeyPosDelta(self._handle)

    @property
    def act_keyframe_f(self) -> float:
        return DLL.ZkMover_getActKeyframeF(self._handle)

    @property
    def act_keyframe(self) -> int:
        return DLL.ZkMover_getActKeyframe(self._handle)

    @property
    def next_keyframe(self) -> int:
        return DLL.ZkMover_getNextKeyframe(self._handle)

    @property
    def move_speed_unit(self) -> float:
        return DLL.ZkMover_getMoveSpeedUnit(self._handle)

    @property
    def advance_dir(self) -> float:
        return DLL.ZkMover_getAdvanceDir(self._handle)

    @property
    def mover_state(self) -> int:
        return DLL.ZkMover_getMoverState(self._handle)

    @property
    def trigger_event_count(self) -> int:
        return DLL.ZkMover_getTriggerEventCount(self._handle)

    @property
    def stay_open_time_dest(self) -> float:
        return DLL.ZkMover_getStayOpenTimeDest(self._handle)

    @act_key_pos_delta.setter
    def act_key_pos_delta(self, value: Vec3f) -> None:
        DLL.ZkMover_setActKeyPosDelta(self._handle, Vec3f(value))

    @act_keyframe_f.setter
    def act_keyframe_f(self, value: float) -> None:
        DLL.ZkMover_setActKeyframeF(self._handle, c_float(value))

    @act_keyframe.setter
    def act_keyframe(self, value: int) -> None:
        DLL.ZkMover_setActKeyframe(self._handle, c_int(value))

    @next_keyframe.setter
    def next_keyframe(self, value: int) -> None:
        DLL.ZkMover_setNextKeyframe(self._handle, c_int(value))

    @move_speed_unit.setter
    def move_speed_unit(self, value: float) -> None:
        DLL.ZkMover_setMoveSpeedUnit(self._handle, c_float(value))

    @advance_dir.setter
    def advance_dir(self, value: float) -> None:
        DLL.ZkMover_setAdvanceDir(self._handle, c_float(value))

    @mover_state.setter
    def mover_state(self, value: int) -> None:
        DLL.ZkMover_setMoverState(self._handle, c_uint32(value))

    @trigger_event_count.setter
    def trigger_event_count(self, value: int) -> None:
        DLL.ZkMover_setTriggerEventCount(self._handle, c_int(value))

    @stay_open_time_dest.setter
    def stay_open_time_dest(self, value: float) -> None:
        DLL.ZkMover_setStayOpenTimeDest(self._handle, c_float(value))

    @property
    def sfx_open_start(self) -> str:
        return DLL.ZkMover_getSfxOpenStart(self._handle).value

    @sfx_open_start.setter
    def sfx_open_start(self, value: str) -> None:
        DLL.ZkMover_setSfxOpenStart(self._handle, value.encode("utf-8"))

    @property
    def sfx_open_end(self) -> str:
        return DLL.ZkMover_getSfxOpenEnd(self._handle).value

    @sfx_open_end.setter
    def sfx_open_end(self, value: str) -> None:
        DLL.ZkMover_setSfxOpenEnd(self._handle, value.encode("utf-8"))

    @property
    def sfx_transitioning(self) -> str:
        return DLL.ZkMover_getSfxTransitioning(self._handle).value

    @sfx_transitioning.setter
    def sfx_transitioning(self, value: str) -> None:
        DLL.ZkMover_setSfxTransitioning(self._handle, value.encode("utf-8"))

    @property
    def sfx_close_start(self) -> str:
        return DLL.ZkMover_getSfxCloseStart(self._handle).value

    @sfx_close_start.setter
    def sfx_close_start(self, value: str) -> None:
        DLL.ZkMover_setSfxCloseStart(self._handle, value.encode("utf-8"))

    @property
    def sfx_close_end(self) -> str:
        return DLL.ZkMover_getSfxCloseEnd(self._handle).value

    @sfx_close_end.setter
    def sfx_close_end(self, value: str) -> None:
        DLL.ZkMover_setSfxCloseEnd(self._handle, value.encode("utf-8"))

    @property
    def sfx_lock(self) -> str:
        return DLL.ZkMover_getSfxLock(self._handle).value

    @sfx_lock.setter
    def sfx_lock(self, value: str) -> None:
        DLL.ZkMover_setSfxLock(self._handle, value.encode("utf-8"))

    @property
    def sfx_unlock(self) -> str:
        return DLL.ZkMover_getSfxUnlock(self._handle).value

    @sfx_unlock.setter
    def sfx_unlock(self, value: str) -> None:
        DLL.ZkMover_setSfxUnlock(self._handle, value.encode("utf-8"))

    @property
    def sfx_use_locked(self) -> str:
        return DLL.ZkMover_getSfxUseLocked(self._handle).value

    @sfx_use_locked.setter
    def sfx_use_locked(self, value: str) -> None:
        DLL.ZkMover_setSfxUseLocked(self._handle, value.encode("utf-8"))

    @property
    def keyframes(self) -> list[AnimationSample]:
        count = DLL.ZkMover_getKeyframeCount(self._handle)
        return [DLL.ZkMover_getKeyframe(self._handle, i) for i in range(count)]


@dataclass
class TriggerListTarget:
    name: str
    delay_seconds: float


DLL.ZkTriggerList_getMode.restype = c_int
DLL.ZkTriggerList_getActTarget.restype = c_uint8
DLL.ZkTriggerList_getSendOnTrigger.restype = c_bool
DLL.ZkTriggerList_getTargetCount.restype = c_size_t
DLL.ZkTriggerList_getTarget.restype = ZkPointer
DLL.ZkTriggerListTarget_getName.restype = ZkString
DLL.ZkTriggerListTarget_getDelaySeconds.restype = c_float


class TriggerList(Trigger):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def mode(self) -> TriggerBatchMode:
        return TriggerBatchMode(DLL.ZkTriggerList_getMode(self._handle))

    @mode.setter
    def mode(self, value: TriggerBatchMode) -> None:
        DLL.ZkTriggerList_setMode(self._handle, value.value)

    @property
    def act_target(self) -> int:
        return DLL.ZkTriggerList_getActTarget(self._handle)

    @property
    def send_on_trigger(self) -> bool:
        return DLL.ZkTriggerList_getSendOnTrigger(self._handle)

    @act_target.setter
    def act_target(self, value: int) -> None:
        DLL.ZkTriggerList_setActTarget(self._handle, c_uint8(value))

    @send_on_trigger.setter
    def send_on_trigger(self, value: bool) -> None:
        DLL.ZkTriggerList_setSendOnTrigger(self._handle, c_bool(value))

    @property
    def targets(self) -> list[TriggerListTarget]:
        count = DLL.ZkTriggerList_getTargetCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkTriggerList_getTarget(self._handle, i).value
            items.append(
                TriggerListTarget(
                    name=DLL.ZkTriggerListTarget_getName(handle).value,
                    delay_seconds=DLL.ZkTriggerListTarget_getDelaySeconds(handle),
                )
            )

        return items


DLL.ZkTriggerScript_getFunction.restype = ZkString


class TriggerScript(Trigger):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def function(self) -> str:
        return DLL.ZkTriggerScript_getFunction(self._handle).value

    @function.setter
    def function(self, value: str) -> None:
        DLL.ZkTriggerScript_setFunction(self._handle, value.encode("utf-8"))


DLL.ZkTriggerChangeLevel_getLevelName.restype = ZkString
DLL.ZkTriggerChangeLevel_getStartVob.restype = ZkString


class TriggerChangeLevel(Trigger):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def level_name(self) -> str:
        return DLL.ZkTriggerChangeLevel_getLevelName(self._handle).value

    @level_name.setter
    def level_name(self, value: str) -> None:
        DLL.ZkTriggerChangeLevel_setLevelName(self._handle, value.encode("utf-8"))

    @property
    def start_vob(self) -> str:
        return DLL.ZkTriggerChangeLevel_getStartVob(self._handle).value

    @start_vob.setter
    def start_vob(self, value: str) -> None:
        DLL.ZkTriggerChangeLevel_setStartVob(self._handle, value.encode("utf-8"))


DLL.ZkTriggerWorldStart_getTarget.restype = ZkString
DLL.ZkTriggerWorldStart_getFireOnce.restype = c_bool
DLL.ZkTriggerWorldStart_getHasFired.restype = c_bool


class TriggerWorldStart(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def target(self) -> str:
        return DLL.ZkTriggerWorldStart_getTarget(self._handle).value

    @target.setter
    def target(self, value: str) -> None:
        DLL.ZkTriggerWorldStart_setTarget(self._handle, value.encode("utf-8"))

    @property
    def fire_once(self) -> bool:
        return DLL.ZkTriggerWorldStart_getFireOnce(self._handle)

    @fire_once.setter
    def fire_once(self, value: bool) -> None:
        DLL.ZkTriggerWorldStart_setFireOnce(self._handle, c_bool(value))

    @property
    def has_fired(self) -> bool:
        return DLL.ZkTriggerWorldStart_getHasFired(self._handle)

    @has_fired.setter
    def has_fired(self, value: bool) -> None:
        DLL.ZkTriggerWorldStart_setHasFired(self._handle, c_bool(value))


DLL.ZkTriggerUntouch_getTarget.restype = ZkString


class TriggerUntouch(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def target(self) -> str:
        return DLL.ZkTriggerUntouch_getTarget(self._handle).value

    @target.setter
    def target(self, value: str) -> None:
        DLL.ZkTriggerUntouch_setTarget(self._handle, value.encode("utf-8"))
