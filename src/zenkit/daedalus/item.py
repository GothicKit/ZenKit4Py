__all__ = [
    "ItemInstance",
    "ItemInstanceConditionSlot",
    "ItemInstanceFlag",
    "ItemInstanceStateSlot",
    "ItemInstanceTextSlot",
]

from ctypes import c_int32
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance
from zenkit.daedalus.npc import DamageType


class ItemInstanceFlag(IntEnum):
    DAGGER = 1 << 13
    SWORD = 1 << 14
    AXE = 1 << 15
    TWO_HANDED_SWORD = 1 << 16
    TWO_HANDED_AXE = 1 << 17
    BOW = 1 << 19
    CROSSBOW = 1 << 20
    AMULET = 1 << 22
    RING = 1 << 11
    BELT = 1 << 24
    MISSION = 1 << 12


class ItemInstanceConditionSlot(IntEnum):
    SLOT0 = 0
    SLOT1 = 1
    SLOT2 = 2


class ItemInstanceStateSlot(IntEnum):
    SLOT0 = 0
    SLOT1 = 1
    SLOT2 = 2
    SLOT3 = 3


class ItemInstanceTextSlot(IntEnum):
    SLOT0 = 0
    SLOT1 = 1
    SLOT2 = 2
    SLOT3 = 3
    SLOT4 = 4
    SLOT5 = 5


class ItemInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def id(self) -> int:
        DLL.ZkItemInstance_getId.restype = c_int32
        return DLL.ZkItemInstance_getId(self._handle)

    @id.setter
    def id(self, value: int) -> None:
        DLL.ZkItemInstance_setId(self._handle, c_int32(value))

    @property
    def name(self) -> str:
        DLL.ZkItemInstance_getName.restype = ZkString
        return DLL.ZkItemInstance_getName(self._handle).value

    @name.setter
    def name(self, value: str) -> None:
        DLL.ZkItemInstance_setName(self._handle, value.encode("utf-8"))

    @property
    def name_id(self) -> str:
        DLL.ZkItemInstance_getNameId.restype = ZkString
        return DLL.ZkItemInstance_getNameId(self._handle).value

    @name_id.setter
    def name_id(self, value: str) -> None:
        DLL.ZkItemInstance_setNameId(self._handle, value.encode("utf-8"))

    @property
    def hp(self) -> int:
        DLL.ZkItemInstance_getHp.restype = c_int32
        return DLL.ZkItemInstance_getHp(self._handle)

    @hp.setter
    def hp(self, value: int) -> None:
        DLL.ZkItemInstance_setHp(self._handle, c_int32(value))

    @property
    def hp_max(self) -> int:
        DLL.ZkItemInstance_getHpMax.restype = c_int32
        return DLL.ZkItemInstance_getHpMax(self._handle)

    @hp_max.setter
    def hp_max(self, value: int) -> None:
        DLL.ZkItemInstance_setHpMax(self._handle, c_int32(value))

    @property
    def main_flag(self) -> int:
        DLL.ZkItemInstance_getMainFlag.restype = c_int32
        return DLL.ZkItemInstance_getMainFlag(self._handle)

    @main_flag.setter
    def main_flag(self, value: int) -> None:
        DLL.ZkItemInstance_setMainFlag(self._handle, c_int32(value))

    @property
    def flags(self) -> int:
        DLL.ZkItemInstance_getFlags.restype = c_int32
        return DLL.ZkItemInstance_getFlags(self._handle)

    @flags.setter
    def flags(self, value: int) -> None:
        DLL.ZkItemInstance_setFlags(self._handle, c_int32(value))

    @property
    def weight(self) -> int:
        DLL.ZkItemInstance_getWeight.restype = c_int32
        return DLL.ZkItemInstance_getWeight(self._handle)

    @weight.setter
    def weight(self, value: int) -> None:
        DLL.ZkItemInstance_setWeight(self._handle, c_int32(value))

    @property
    def value(self) -> int:
        DLL.ZkItemInstance_getValue.restype = c_int32
        return DLL.ZkItemInstance_getValue(self._handle)

    @value.setter
    def value(self, value: int) -> None:
        DLL.ZkItemInstance_setValue(self._handle, c_int32(value))

    @property
    def damage_type(self) -> int:
        DLL.ZkItemInstance_getDamageType.restype = c_int32
        return DLL.ZkItemInstance_getDamageType(self._handle)

    @damage_type.setter
    def damage_type(self, value: int) -> None:
        DLL.ZkItemInstance_setDamageType(self._handle, c_int32(value))

    @property
    def damage_total(self) -> int:
        DLL.ZkItemInstance_getDamageTotal.restype = c_int32
        return DLL.ZkItemInstance_getDamageTotal(self._handle)

    @damage_total.setter
    def damage_total(self, value: int) -> None:
        DLL.ZkItemInstance_setDamageTotal(self._handle, c_int32(value))

    @property
    def wear(self) -> int:
        DLL.ZkItemInstance_getWear.restype = c_int32
        return DLL.ZkItemInstance_getWear(self._handle)

    @wear.setter
    def wear(self, value: int) -> None:
        DLL.ZkItemInstance_setWear(self._handle, c_int32(value))

    @property
    def nutrition(self) -> int:
        DLL.ZkItemInstance_getNutrition.restype = c_int32
        return DLL.ZkItemInstance_getNutrition(self._handle)

    @nutrition.setter
    def nutrition(self, value: int) -> None:
        DLL.ZkItemInstance_setNutrition(self._handle, c_int32(value))

    @property
    def magic(self) -> int:
        DLL.ZkItemInstance_getMagic.restype = c_int32
        return DLL.ZkItemInstance_getMagic(self._handle)

    @magic.setter
    def magic(self, value: int) -> None:
        DLL.ZkItemInstance_setMagic(self._handle, c_int32(value))

    @property
    def on_equip(self) -> int:
        DLL.ZkItemInstance_getOnEquip.restype = c_int32
        return DLL.ZkItemInstance_getOnEquip(self._handle)

    @on_equip.setter
    def on_equip(self, value: int) -> None:
        DLL.ZkItemInstance_setOnEquip(self._handle, c_int32(value))

    @property
    def on_unequip(self) -> int:
        DLL.ZkItemInstance_getOnUnequip.restype = c_int32
        return DLL.ZkItemInstance_getOnUnequip(self._handle)

    @on_unequip.setter
    def on_unequip(self, value: int) -> None:
        DLL.ZkItemInstance_setOnUnequip(self._handle, c_int32(value))

    @property
    def owner(self) -> int:
        DLL.ZkItemInstance_getOwner.restype = c_int32
        return DLL.ZkItemInstance_getOwner(self._handle)

    @owner.setter
    def owner(self, value: int) -> None:
        DLL.ZkItemInstance_setOwner(self._handle, c_int32(value))

    @property
    def owner_guild(self) -> int:
        DLL.ZkItemInstance_getOwnerGuild.restype = c_int32
        return DLL.ZkItemInstance_getOwnerGuild(self._handle)

    @owner_guild.setter
    def owner_guild(self, value: int) -> None:
        DLL.ZkItemInstance_setOwnerGuild(self._handle, c_int32(value))

    @property
    def disguise_guild(self) -> int:
        DLL.ZkItemInstance_getDisguiseGuild.restype = c_int32
        return DLL.ZkItemInstance_getDisguiseGuild(self._handle)

    @disguise_guild.setter
    def disguise_guild(self, value: int) -> None:
        DLL.ZkItemInstance_setDisguiseGuild(self._handle, c_int32(value))

    @property
    def visual(self) -> str:
        DLL.ZkItemInstance_getVisual.restype = ZkString
        return DLL.ZkItemInstance_getVisual(self._handle).value

    @visual.setter
    def visual(self, value: str) -> None:
        DLL.ZkItemInstance_setVisual(self._handle, value.encode("utf-8"))

    @property
    def visual_change(self) -> str:
        DLL.ZkItemInstance_getVisualChange.restype = ZkString
        return DLL.ZkItemInstance_getVisualChange(self._handle).value

    @visual_change.setter
    def visual_change(self, value: str) -> None:
        DLL.ZkItemInstance_setVisualChange(self._handle, value.encode("utf-8"))

    @property
    def effect(self) -> str:
        DLL.ZkItemInstance_getEffect.restype = ZkString
        return DLL.ZkItemInstance_getEffect(self._handle).value

    @effect.setter
    def effect(self, value: str) -> None:
        DLL.ZkItemInstance_setEffect(self._handle, value.encode("utf-8"))

    @property
    def visual_skin(self) -> int:
        DLL.ZkItemInstance_getVisualSkin.restype = c_int32
        return DLL.ZkItemInstance_getVisualSkin(self._handle)

    @visual_skin.setter
    def visual_skin(self, value: int) -> None:
        DLL.ZkItemInstance_setVisualSkin(self._handle, c_int32(value))

    @property
    def scheme_name(self) -> str:
        DLL.ZkItemInstance_getSchemeName.restype = ZkString
        return DLL.ZkItemInstance_getSchemeName(self._handle).value

    @scheme_name.setter
    def scheme_name(self, value: str) -> None:
        DLL.ZkItemInstance_setSchemeName(self._handle, value.encode("utf-8"))

    @property
    def material(self) -> int:
        DLL.ZkItemInstance_getMaterial.restype = c_int32
        return DLL.ZkItemInstance_getMaterial(self._handle)

    @material.setter
    def material(self, value: int) -> None:
        DLL.ZkItemInstance_setMaterial(self._handle, c_int32(value))

    @property
    def munition(self) -> int:
        DLL.ZkItemInstance_getMunition.restype = c_int32
        return DLL.ZkItemInstance_getMunition(self._handle)

    @munition.setter
    def munition(self, value: int) -> None:
        DLL.ZkItemInstance_setMunition(self._handle, c_int32(value))

    @property
    def spell(self) -> int:
        DLL.ZkItemInstance_getSpell.restype = c_int32
        return DLL.ZkItemInstance_getSpell(self._handle)

    @spell.setter
    def spell(self, value: int) -> None:
        DLL.ZkItemInstance_setSpell(self._handle, c_int32(value))

    @property
    def range(self) -> int:
        DLL.ZkItemInstance_getRange.restype = c_int32
        return DLL.ZkItemInstance_getRange(self._handle)

    @range.setter
    def range(self, value: int) -> None:
        DLL.ZkItemInstance_setRange(self._handle, c_int32(value))

    @property
    def mag_circle(self) -> int:
        DLL.ZkItemInstance_getMagCircle.restype = c_int32
        return DLL.ZkItemInstance_getMagCircle(self._handle)

    @mag_circle.setter
    def mag_circle(self, value: int) -> None:
        DLL.ZkItemInstance_setMagCircle(self._handle, c_int32(value))

    @property
    def description(self) -> str:
        DLL.ZkItemInstance_getDescription.restype = ZkString
        return DLL.ZkItemInstance_getDescription(self._handle).value

    @description.setter
    def description(self, value: str) -> None:
        DLL.ZkItemInstance_setDescription(self._handle, value.encode("utf-8"))

    @property
    def inv_z_bias(self) -> int:
        DLL.ZkItemInstance_getInvZBias.restype = c_int32
        return DLL.ZkItemInstance_getInvZBias(self._handle)

    @inv_z_bias.setter
    def inv_z_bias(self, value: int) -> None:
        DLL.ZkItemInstance_setInvZBias(self._handle, c_int32(value))

    @property
    def inv_rot_x(self) -> int:
        DLL.ZkItemInstance_getInvRotX.restype = c_int32
        return DLL.ZkItemInstance_getInvRotX(self._handle)

    @inv_rot_x.setter
    def inv_rot_x(self, value: int) -> None:
        DLL.ZkItemInstance_setInvRotX(self._handle, c_int32(value))

    @property
    def inv_rot_y(self) -> int:
        DLL.ZkItemInstance_getInvRotY.restype = c_int32
        return DLL.ZkItemInstance_getInvRotY(self._handle)

    @inv_rot_y.setter
    def inv_rot_y(self, value: int) -> None:
        DLL.ZkItemInstance_setInvRotY(self._handle, c_int32(value))

    @property
    def inv_rot_z(self) -> int:
        DLL.ZkItemInstance_getInvRotZ.restype = c_int32
        return DLL.ZkItemInstance_getInvRotZ(self._handle)

    @inv_rot_z.setter
    def inv_rot_z(self, value: int) -> None:
        DLL.ZkItemInstance_setInvRotZ(self._handle, c_int32(value))

    @property
    def inv_animate(self) -> int:
        DLL.ZkItemInstance_getInvAnimate.restype = c_int32
        return DLL.ZkItemInstance_getInvAnimate(self._handle)

    @inv_animate.setter
    def inv_animate(self, value: int) -> None:
        DLL.ZkItemInstance_setInvAnimate(self._handle, c_int32(value))

    def get_damage(self, type: DamageType) -> int:
        DLL.ZkItemInstance_getDamage.restype = c_int32
        return DLL.ZkItemInstance_getDamage(self._handle, type.value)

    def get_protection(self, type: DamageType) -> int:
        DLL.ZkItemInstance_getProtection.restype = c_int32
        return DLL.ZkItemInstance_getProtection(self._handle, type.value)

    def get_cond_atr(self, slot: ItemInstanceConditionSlot) -> int:
        DLL.ZkItemInstance_getCondAtr.restype = c_int32
        return DLL.ZkItemInstance_getCondAtr(self._handle, slot.value)

    def get_cond_value(self, slot: ItemInstanceConditionSlot) -> int:
        DLL.ZkItemInstance_getCondValue.restype = c_int32
        return DLL.ZkItemInstance_getCondValue(self._handle, slot.value)

    def get_change_atr(self, slot: ItemInstanceConditionSlot) -> int:
        DLL.ZkItemInstance_getChangeAtr.restype = c_int32
        return DLL.ZkItemInstance_getChangeAtr(self._handle, slot.value)

    def get_change_value(self, slot: ItemInstanceConditionSlot) -> int:
        DLL.ZkItemInstance_getChangeValue.restype = c_int32
        return DLL.ZkItemInstance_getChangeValue(self._handle, slot.value)

    def get_on_state(self, slot: ItemInstanceStateSlot) -> int:
        DLL.ZkItemInstance_getOnState.restype = c_int32
        return DLL.ZkItemInstance_getOnState(self._handle, slot.value)

    def get_count(self, slot: ItemInstanceTextSlot) -> int:
        DLL.ZkItemInstance_getCount.restype = c_int32
        return DLL.ZkItemInstance_getCount(self._handle, slot.value)

    def get_text(self, slot: ItemInstanceTextSlot) -> str:
        DLL.ZkItemInstance_getText.restype = ZkString
        return DLL.ZkItemInstance_getText(self._handle, slot.value)

    def set_damage(self, type: DamageType, val: int) -> None:
        DLL.ZkItemInstance_setDamage(self._handle, type.value, c_int32(val))

    def set_protection(self, type: DamageType, val: int) -> None:
        DLL.ZkItemInstance_setProtection(self._handle, type.value, c_int32(val))

    def set_cond_atr(self, slot: ItemInstanceConditionSlot, val: int) -> None:
        DLL.ZkItemInstance_setCondAtr(self._handle, slot.value, c_int32(val))

    def set_cond_value(self, slot: ItemInstanceConditionSlot, val: int) -> None:
        DLL.ZkItemInstance_setCondValue(self._handle, slot.value, c_int32(val))

    def set_change_atr(self, slot: ItemInstanceConditionSlot, val: int) -> None:
        DLL.ZkItemInstance_setChangeAtr(self._handle, slot.value, c_int32(val))

    def set_change_value(self, slot: ItemInstanceConditionSlot, val: int) -> None:
        DLL.ZkItemInstance_setChangeValue(self._handle, slot.value, c_int32(val))

    def set_on_state(self, slot: ItemInstanceStateSlot, val: int) -> None:
        DLL.ZkItemInstance_setOnState(self._handle, slot.value, c_int32(val))

    def set_count(self, slot: ItemInstanceTextSlot, val: int) -> None:
        DLL.ZkItemInstance_setCount(self._handle, slot.value, c_int32(val))

    def set_text(self, slot: ItemInstanceTextSlot, val: str) -> None:
        DLL.ZkItemInstance_setText(self._handle, slot.value, val.encode("utf-8"))
