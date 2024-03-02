__all__ = ["SpellInstance"]

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit.daedalus.base import DaedalusInstance


class SpellInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def time_per_mana(self) -> float:
        DLL.ZkSpellInstance_getTimePerMana.restype = c_float
        return DLL.ZkSpellInstance_getTimePerMana(self._handle)

    @time_per_mana.setter
    def time_per_mana(self, value: float) -> None:
        DLL.ZkSpellInstance_setTimePerMana(self._handle, c_float(value))

    @property
    def damage_per_level(self) -> int:
        DLL.ZkSpellInstance_getDamagePerLevel.restype = c_int32
        return DLL.ZkSpellInstance_getDamagePerLevel(self._handle)

    @damage_per_level.setter
    def damage_per_level(self, value: int) -> None:
        DLL.ZkSpellInstance_setDamagePerLevel(self._handle, c_int32(value))

    @property
    def damage_type(self) -> int:
        DLL.ZkSpellInstance_getDamageType.restype = c_int32
        return DLL.ZkSpellInstance_getDamageType(self._handle)

    @damage_type.setter
    def damage_type(self, value: int) -> None:
        DLL.ZkSpellInstance_setDamageType(self._handle, c_int32(value))

    @property
    def spell_type(self) -> int:
        DLL.ZkSpellInstance_getSpellType.restype = c_int32
        return DLL.ZkSpellInstance_getSpellType(self._handle)

    @spell_type.setter
    def spell_type(self, value: int) -> None:
        DLL.ZkSpellInstance_setSpellType(self._handle, c_int32(value))

    @property
    def can_turn_during_invest(self) -> int:
        DLL.ZkSpellInstance_getCanTurnDuringInvest.restype = c_int32
        return DLL.ZkSpellInstance_getCanTurnDuringInvest(self._handle)

    @can_turn_during_invest.setter
    def can_turn_during_invest(self, value: int) -> None:
        DLL.ZkSpellInstance_setCanTurnDuringInvest(self._handle, c_int32(value))

    @property
    def can_change_target_during_invest(self) -> int:
        DLL.ZkSpellInstance_getCanChangeTargetDuringInvest.restype = c_int32
        return DLL.ZkSpellInstance_getCanChangeTargetDuringInvest(self._handle)

    @can_change_target_during_invest.setter
    def can_change_target_during_invest(self, value: int) -> None:
        DLL.ZkSpellInstance_setCanChangeTargetDuringInvest(self._handle, c_int32(value))

    @property
    def is_multi_effect(self) -> int:
        DLL.ZkSpellInstance_getIsMultiEffect.restype = c_int32
        return DLL.ZkSpellInstance_getIsMultiEffect(self._handle)

    @is_multi_effect.setter
    def is_multi_effect(self, value: int) -> None:
        DLL.ZkSpellInstance_setIsMultiEffect(self._handle, c_int32(value))

    @property
    def target_collect_algo(self) -> int:
        DLL.ZkSpellInstance_getTargetCollectAlgo.restype = c_int32
        return DLL.ZkSpellInstance_getTargetCollectAlgo(self._handle)

    @target_collect_algo.setter
    def target_collect_algo(self, value: int) -> None:
        DLL.ZkSpellInstance_setTargetCollectAlgo(self._handle, c_int32(value))

    @property
    def target_collect_type(self) -> int:
        DLL.ZkSpellInstance_getTargetCollectType.restype = c_int32
        return DLL.ZkSpellInstance_getTargetCollectType(self._handle)

    @target_collect_type.setter
    def target_collect_type(self, value: int) -> None:
        DLL.ZkSpellInstance_setTargetCollectType(self._handle, c_int32(value))

    @property
    def target_collect_range(self) -> int:
        DLL.ZkSpellInstance_getTargetCollectRange.restype = c_int32
        return DLL.ZkSpellInstance_getTargetCollectRange(self._handle)

    @target_collect_range.setter
    def target_collect_range(self, value: int) -> None:
        DLL.ZkSpellInstance_setTargetCollectRange(self._handle, c_int32(value))

    @property
    def target_collect_azi(self) -> int:
        DLL.ZkSpellInstance_getTargetCollectAzi.restype = c_int32
        return DLL.ZkSpellInstance_getTargetCollectAzi(self._handle)

    @target_collect_azi.setter
    def target_collect_azi(self, value: int) -> None:
        DLL.ZkSpellInstance_setTargetCollectAzi(self._handle, c_int32(value))

    @property
    def target_collect_elevation(self) -> int:
        DLL.ZkSpellInstance_getTargetCollectElevation.restype = c_int32
        return DLL.ZkSpellInstance_getTargetCollectElevation(self._handle)

    @target_collect_elevation.setter
    def target_collect_elevation(self, value: int) -> None:
        DLL.ZkSpellInstance_setTargetCollectElevation(self._handle, c_int32(value))
