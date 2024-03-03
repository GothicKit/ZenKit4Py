__all__ = [
    "DamageType",
    "NpcInstance",
    "NpcInstanceAttribute",
    "NpcInstanceFlag",
    "NpcInstanceMissionSlot",
    "NpcInstanceType",
    "NpcInstanceTalent",
    "NpcInstanceNameSlot",
]

from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from ctypes import c_uint32
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance

_NPC_AIVAR_COUNT = 100


class DamageType(IntEnum):
    BARRIER = 0
    BLUNT = 1
    EDGE = 2
    FIRE = 3
    FLY = 4
    MAGIC = 5
    POINT = 6
    FALL = 7


class NpcInstanceAttribute(IntEnum):
    HITPOINTS = 0
    HITPOINTS_MAX = 1
    MANA = 2
    MANA_MAX = 3
    STRENGTH = 4
    DEXTERITY = 5
    REGENERATE_HP = 6
    REGENERATE_MANA = 7


class NpcInstanceTalent(IntEnum):
    UNKNOWN = 0
    ONE_HANDED = 1
    TWO_HANDED = 2
    BOW = 3
    CROSSBOW = 4


class NpcInstanceType(IntEnum):
    G1_AMBIENT = 0
    G1_MAIN = 1
    G1_GUARD = 2
    G1_FRIEND = 3
    G1_MINE_AMBIENT = 4
    G1_MINE_GUARD = 5
    G1_OW_AMBIENT = 6
    G1_OW_GUARD = 7
    G1_ROGUE = 8
    G2_AMBIENT = 0
    G2_MAIN = 1
    G2_FRIEND = 2
    G2_OC_AMBIENT = 3
    G2_OC_MAIN = 4
    G2_BL_AMBIENT = 5
    G2_TAL_AMBIENT = 6
    G2_BL_MAIN = 7


class NpcInstanceFlag(IntEnum):
    NONE = 0
    FRIENDS = 1 << 0
    IMMORTAL = 1 << 1
    GHOST = 1 << 2
    PROTECTED = 1 << 3


class NpcInstanceNameSlot(IntEnum):
    SLOT0 = 0
    SLOT1 = 1
    SLOT2 = 2
    SLOT3 = 3
    SLOT4 = 4


class NpcInstanceMissionSlot(IntEnum):
    SLOT0 = 0
    SLOT1 = 1
    SLOT2 = 2
    SLOT3 = 3
    SLOT4 = 4


class NpcInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def id(self) -> int:
        DLL.ZkNpcInstance_getId.restype = c_int32
        return DLL.ZkNpcInstance_getId(self._handle)

    @id.setter
    def id(self, value: int) -> None:
        DLL.ZkNpcInstance_setId(self._handle, c_int32(value))

    @property
    def slot(self) -> str:
        DLL.ZkNpcInstance_getSlot.restype = ZkString
        return DLL.ZkNpcInstance_getSlot(self._handle).value

    @slot.setter
    def slot(self, value: str) -> None:
        DLL.ZkNpcInstance_setSlot(self._handle, value.encode("utf-8"))

    @property
    def effect(self) -> str:
        DLL.ZkNpcInstance_getEffect.restype = ZkString
        return DLL.ZkNpcInstance_getEffect(self._handle).value

    @effect.setter
    def effect(self, value: str) -> None:
        DLL.ZkNpcInstance_setEffect(self._handle, value.encode("utf-8"))

    @property
    def type(self) -> NpcInstanceType:
        DLL.ZkNpcInstance_getType.restype = c_int
        return NpcInstanceType(DLL.ZkNpcInstance_getType(self._handle))

    @type.setter
    def type(self, value: NpcInstanceType) -> None:
        DLL.ZkNpcInstance_setType(self._handle, value.value)

    @property
    def flags(self) -> int:
        DLL.ZkNpcInstance_getFlags.restype = c_uint32
        return DLL.ZkNpcInstance_getFlags(self._handle)

    @flags.setter
    def flags(self, value: int) -> None:
        DLL.ZkNpcInstance_setFlags(self._handle, c_uint32(value))

    @property
    def damage_type(self) -> int:
        DLL.ZkNpcInstance_getDamageType.restype = c_int32
        return DLL.ZkNpcInstance_getDamageType(self._handle)

    @damage_type.setter
    def damage_type(self, value: int) -> None:
        DLL.ZkNpcInstance_setDamageType(self._handle, c_int32(value))

    @property
    def guild(self) -> int:
        DLL.ZkNpcInstance_getGuild.restype = c_int32
        return DLL.ZkNpcInstance_getGuild(self._handle)

    @guild.setter
    def guild(self, value: int) -> None:
        DLL.ZkNpcInstance_setGuild(self._handle, c_int32(value))

    @property
    def level(self) -> int:
        DLL.ZkNpcInstance_getLevel.restype = c_int32
        return DLL.ZkNpcInstance_getLevel(self._handle)

    @level.setter
    def level(self, value: int) -> None:
        DLL.ZkNpcInstance_setLevel(self._handle, c_int32(value))

    @property
    def fight_tactic(self) -> int:
        DLL.ZkNpcInstance_getFightTactic.restype = c_int32
        return DLL.ZkNpcInstance_getFightTactic(self._handle)

    @fight_tactic.setter
    def fight_tactic(self, value: int) -> None:
        DLL.ZkNpcInstance_setFightTactic(self._handle, c_int32(value))

    @property
    def weapon(self) -> int:
        DLL.ZkNpcInstance_getWeapon.restype = c_int32
        return DLL.ZkNpcInstance_getWeapon(self._handle)

    @weapon.setter
    def weapon(self, value: int) -> None:
        DLL.ZkNpcInstance_setWeapon(self._handle, c_int32(value))

    @property
    def voice(self) -> int:
        DLL.ZkNpcInstance_getVoice.restype = c_int32
        return DLL.ZkNpcInstance_getVoice(self._handle)

    @voice.setter
    def voice(self, value: int) -> None:
        DLL.ZkNpcInstance_setVoice(self._handle, c_int32(value))

    @property
    def voice_pitch(self) -> int:
        DLL.ZkNpcInstance_getVoicePitch.restype = c_int32
        return DLL.ZkNpcInstance_getVoicePitch(self._handle)

    @voice_pitch.setter
    def voice_pitch(self, value: int) -> None:
        DLL.ZkNpcInstance_setVoicePitch(self._handle, c_int32(value))

    @property
    def body_mass(self) -> int:
        DLL.ZkNpcInstance_getBodyMass.restype = c_int32
        return DLL.ZkNpcInstance_getBodyMass(self._handle)

    @body_mass.setter
    def body_mass(self, value: int) -> None:
        DLL.ZkNpcInstance_setBodyMass(self._handle, c_int32(value))

    @property
    def daily_routine(self) -> int:
        DLL.ZkNpcInstance_getDailyRoutine.restype = c_int32
        return DLL.ZkNpcInstance_getDailyRoutine(self._handle)

    @daily_routine.setter
    def daily_routine(self, value: int) -> None:
        DLL.ZkNpcInstance_setDailyRoutine(self._handle, c_int32(value))

    @property
    def start_ai_state(self) -> int:
        DLL.ZkNpcInstance_getStartAiState.restype = c_int32
        return DLL.ZkNpcInstance_getStartAiState(self._handle)

    @start_ai_state.setter
    def start_ai_state(self, value: int) -> None:
        DLL.ZkNpcInstance_setStartAiState(self._handle, c_int32(value))

    @property
    def spawn_point(self) -> str:
        DLL.ZkNpcInstance_getSpawnPoint.restype = ZkString
        return DLL.ZkNpcInstance_getSpawnPoint(self._handle).value

    @spawn_point.setter
    def spawn_point(self, value: str) -> None:
        DLL.ZkNpcInstance_setSpawnPoint(self._handle, value.encode("utf-8"))

    @property
    def spawn_delay(self) -> int:
        DLL.ZkNpcInstance_getSpawnDelay.restype = c_int32
        return DLL.ZkNpcInstance_getSpawnDelay(self._handle)

    @spawn_delay.setter
    def spawn_delay(self, value: int) -> None:
        DLL.ZkNpcInstance_setSpawnDelay(self._handle, c_int32(value))

    @property
    def senses(self) -> int:
        DLL.ZkNpcInstance_getSenses.restype = c_int32
        return DLL.ZkNpcInstance_getSenses(self._handle)

    @senses.setter
    def senses(self, value: int) -> None:
        DLL.ZkNpcInstance_setSenses(self._handle, c_int32(value))

    @property
    def senses_range(self) -> int:
        DLL.ZkNpcInstance_getSensesRange.restype = c_int32
        return DLL.ZkNpcInstance_getSensesRange(self._handle)

    @senses_range.setter
    def senses_range(self, value: int) -> None:
        DLL.ZkNpcInstance_setSensesRange(self._handle, c_int32(value))

    @property
    def wp(self) -> str:
        DLL.ZkNpcInstance_getWp.restype = ZkString
        return DLL.ZkNpcInstance_getWp(self._handle).value

    @wp.setter
    def wp(self, value: str) -> None:
        DLL.ZkNpcInstance_setWp(self._handle, value.encode("utf-8"))

    @property
    def exp(self) -> int:
        DLL.ZkNpcInstance_getExp.restype = c_int32
        return DLL.ZkNpcInstance_getExp(self._handle)

    @exp.setter
    def exp(self, value: int) -> None:
        DLL.ZkNpcInstance_setExp(self._handle, c_int32(value))

    @property
    def exp_next(self) -> int:
        DLL.ZkNpcInstance_getExpNext.restype = c_int32
        return DLL.ZkNpcInstance_getExpNext(self._handle)

    @exp_next.setter
    def exp_next(self, value: int) -> None:
        DLL.ZkNpcInstance_setExpNext(self._handle, c_int32(value))

    @property
    def lp(self) -> int:
        DLL.ZkNpcInstance_getLp.restype = c_int32
        return DLL.ZkNpcInstance_getLp(self._handle)

    @lp.setter
    def lp(self, value: int) -> None:
        DLL.ZkNpcInstance_setLp(self._handle, c_int32(value))

    @property
    def body_state_interruptable_override(self) -> int:
        DLL.ZkNpcInstance_getBodyStateInterruptableOverride.restype = c_int32
        return DLL.ZkNpcInstance_getBodyStateInterruptableOverride(self._handle)

    @body_state_interruptable_override.setter
    def body_state_interruptable_override(self, value: int) -> None:
        DLL.ZkNpcInstance_setBodyStateInterruptableOverride(self._handle, c_int32(value))

    @property
    def no_focus(self) -> int:
        DLL.ZkNpcInstance_getNoFocus.restype = c_int32
        return DLL.ZkNpcInstance_getNoFocus(self._handle)

    @no_focus.setter
    def no_focus(self, value: int) -> None:
        DLL.ZkNpcInstance_setNoFocus(self._handle, c_int32(value))

    def get_name(self, slot: NpcInstanceNameSlot) -> str:
        DLL.ZkNpcInstance_getName.restype = ZkString
        return DLL.ZkNpcInstance_getName(self._handle, slot.value).value

    def get_mission(self, slot: NpcInstanceMissionSlot) -> int:
        DLL.ZkNpcInstance_getMission.restype = c_int32
        return DLL.ZkNpcInstance_getMission(self._handle, slot.value)

    def get_attribute(self, attribute: NpcInstanceAttribute) -> int:
        DLL.ZkNpcInstance_getAttribute.restype = c_int32
        return DLL.ZkNpcInstance_getAttribute(self._handle, attribute.value)

    def get_hit_chance(self, talent: NpcInstanceTalent) -> int:
        DLL.ZkNpcInstance_getHitChance.restype = c_int32
        return DLL.ZkNpcInstance_getHitChance(self._handle, talent.value)

    def get_protection(self, typ: DamageType) -> int:
        DLL.ZkNpcInstance_getProtection.restype = c_int32
        return DLL.ZkNpcInstance_getProtection(self._handle, typ.value)

    def get_damage(self, typ: DamageType) -> int:
        DLL.ZkNpcInstance_getDamage.restype = c_int32
        return DLL.ZkNpcInstance_getDamage(self._handle, typ.value)

    def get_ai_var(self, i: int) -> int:
        if i < 0 or i >= _NPC_AIVAR_COUNT:
            raise IndexError(i)
        DLL.ZkNpcInstance_getAiVar.restype = c_int32
        return DLL.ZkNpcInstance_getAiVar(self._handle, c_size_t(i))

    def set_name(self, slot: NpcInstanceNameSlot, val: str) -> None:
        DLL.ZkNpcInstance_setName(self._handle, slot.value, val.encode("utf-8"))

    def set_mission(self, slot: NpcInstanceMissionSlot, val: int) -> None:
        DLL.ZkNpcInstance_setMission(self._handle, slot.value, val)

    def set_attribute(self, attribute: NpcInstanceAttribute, val: int) -> None:
        DLL.ZkNpcInstance_setAttribute(self._handle, attribute.value, val)

    def set_hit_chance(self, talent: NpcInstanceTalent, val: int) -> None:
        DLL.ZkNpcInstance_setHitChance(self._handle, talent.value, val)

    def set_protection(self, typ: DamageType, val: int) -> None:
        DLL.ZkNpcInstance_setProtection(self._handle, typ.value, val)

    def set_damage(self, typ: DamageType, val: int) -> None:
        DLL.ZkNpcInstance_setDamage(self._handle, typ.value, val)

    def set_ai_var(self, i: int, val: int) -> None:
        if i < 0 or i >= _NPC_AIVAR_COUNT:
            raise IndexError(i)
        DLL.ZkNpcInstance_setAiVar(self._handle, c_size_t(i), val)
