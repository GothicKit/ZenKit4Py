__all__ = [
    "MovableObject",
    "InteractiveObject",
    "Container",
    "Door",
    "Fire",
    "SoundMaterialType",
]

from ctypes import c_bool
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkPointer
from zenkit._native import ZkString
from zenkit.vob.misc import Item
from zenkit.vob.virtual_object import VirtualObject


class SoundMaterialType(IntEnum):
    WOOD = 0
    STONE = 1
    METAL = 2
    LEATHER = 3
    CLAY = 4
    GLASS = 5


DLL.ZkMovableObject_getName.restype = ZkString
DLL.ZkMovableObject_getHp.restype = c_int32
DLL.ZkMovableObject_getDamage.restype = c_int32
DLL.ZkMovableObject_getMovable.restype = c_bool
DLL.ZkMovableObject_getTakable.restype = c_bool
DLL.ZkMovableObject_getFocusOverride.restype = c_bool
DLL.ZkMovableObject_getMaterial.restype = c_int
DLL.ZkMovableObject_getVisualDestroyed.restype = ZkString
DLL.ZkMovableObject_getOwner.restype = ZkString
DLL.ZkMovableObject_getOwnerGuild.restype = ZkString
DLL.ZkMovableObject_getDestroyed.restype = c_bool


class MovableObject(VirtualObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def name(self) -> str:
        return DLL.ZkMovableObject_getName(self._handle).value

    @name.setter
    def name(self, value: str) -> None:
        DLL.ZkMovableObject_setName(self._handle, value.encode("utf-8"))

    @property
    def hp(self) -> int:
        return DLL.ZkMovableObject_getHp(self._handle)

    @hp.setter
    def hp(self, value: int) -> None:
        DLL.ZkMovableObject_setHp(self._handle, c_int32(value))

    @property
    def damage(self) -> int:
        return DLL.ZkMovableObject_getDamage(self._handle)

    @damage.setter
    def damage(self, value: int) -> None:
        DLL.ZkMovableObject_setDamage(self._handle, c_int32(value))

    @property
    def movable(self) -> bool:
        return DLL.ZkMovableObject_getMovable(self._handle)

    @movable.setter
    def movable(self, value: bool) -> None:
        DLL.ZkMovableObject_setMovable(self._handle, c_bool(value))

    @property
    def takable(self) -> bool:
        return DLL.ZkMovableObject_getTakable(self._handle)

    @takable.setter
    def takable(self, value: bool) -> None:
        DLL.ZkMovableObject_setTakable(self._handle, c_bool(value))

    @property
    def focus_override(self) -> bool:
        return DLL.ZkMovableObject_getFocusOverride(self._handle)

    @focus_override.setter
    def focus_override(self, value: bool) -> None:
        DLL.ZkMovableObject_setFocusOverride(self._handle, c_bool(value))

    @property
    def material(self) -> SoundMaterialType:
        return SoundMaterialType(DLL.ZkMovableObject_getMaterial(self._handle))

    @material.setter
    def material(self, value: SoundMaterialType) -> None:
        DLL.ZkMovableObject_setMaterial(self._handle, value.value)

    @property
    def visual_destroyed(self) -> str:
        return DLL.ZkMovableObject_getVisualDestroyed(self._handle).value

    @visual_destroyed.setter
    def visual_destroyed(self, value: str) -> None:
        DLL.ZkMovableObject_setVisualDestroyed(self._handle, value.encode("utf-8"))

    @property
    def owner(self) -> str:
        return DLL.ZkMovableObject_getOwner(self._handle).value

    @owner.setter
    def owner(self, value: str) -> None:
        DLL.ZkMovableObject_setOwner(self._handle, value.encode("utf-8"))

    @property
    def owner_guild(self) -> str:
        return DLL.ZkMovableObject_getOwnerGuild(self._handle).value

    @owner_guild.setter
    def owner_guild(self, value: str) -> None:
        DLL.ZkMovableObject_setOwnerGuild(self._handle, value.encode("utf-8"))

    @property
    def destroyed(self) -> bool:
        return DLL.ZkMovableObject_getDestroyed(self._handle)

    @destroyed.setter
    def destroyed(self, value: bool) -> None:
        DLL.ZkMovableObject_setDestroyed(self._handle, c_bool(value))


DLL.ZkInteractiveObject_getState.restype = c_int32
DLL.ZkInteractiveObject_getTarget.restype = ZkString
DLL.ZkInteractiveObject_getItem.restype = ZkString
DLL.ZkInteractiveObject_getConditionFunction.restype = ZkString
DLL.ZkInteractiveObject_getOnStateChangeFunction.restype = ZkString
DLL.ZkInteractiveObject_getRewind.restype = c_bool


class InteractiveObject(MovableObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def state(self) -> int:
        return DLL.ZkInteractiveObject_getState(self._handle)

    @state.setter
    def state(self, value: int) -> None:
        DLL.ZkInteractiveObject_setState(self._handle, c_int32(value))

    @property
    def target(self) -> str:
        return DLL.ZkInteractiveObject_getTarget(self._handle).value

    @target.setter
    def target(self, value: str) -> None:
        DLL.ZkInteractiveObject_setTarget(self._handle, value.encode("utf-8"))

    @property
    def item(self) -> str:
        return DLL.ZkInteractiveObject_getItem(self._handle).value

    @item.setter
    def item(self, value: str) -> None:
        DLL.ZkInteractiveObject_setItem(self._handle, value.encode("utf-8"))

    @property
    def condition_function(self) -> str:
        return DLL.ZkInteractiveObject_getConditionFunction(self._handle).value

    @condition_function.setter
    def condition_function(self, value: str) -> None:
        DLL.ZkInteractiveObject_setConditionFunction(self._handle, value.encode("utf-8"))

    @property
    def on_state_change_function(self) -> str:
        return DLL.ZkInteractiveObject_getOnStateChangeFunction(self._handle).value

    @on_state_change_function.setter
    def on_state_change_function(self, value: str) -> None:
        DLL.ZkInteractiveObject_setOnStateChangeFunction(self._handle, value.encode("utf-8"))

    @property
    def rewind(self) -> bool:
        return DLL.ZkInteractiveObject_getRewind(self._handle)

    @rewind.setter
    def rewind(self, value: bool) -> None:
        DLL.ZkInteractiveObject_setRewind(self._handle, c_bool(value))


DLL.ZkFire_getSlot.restype = ZkString
DLL.ZkFire_getVobTree.restype = ZkString


class Fire(InteractiveObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def slot(self) -> str:
        return DLL.ZkFire_getSlot(self._handle).value

    @slot.setter
    def slot(self, value: str) -> None:
        DLL.ZkFire_setSlot(self._handle, value.encode("utf-8"))

    @property
    def vob_tree(self) -> str:
        return DLL.ZkFire_getVobTree(self._handle).value

    @vob_tree.setter
    def vob_tree(self, value: str) -> None:
        DLL.ZkFire_setVobTree(self._handle, value.encode("utf-8"))


DLL.ZkContainer_getIsLocked.restype = c_bool
DLL.ZkContainer_getKey.restype = ZkString
DLL.ZkContainer_getPickString.restype = ZkString
DLL.ZkContainer_getContents.restype = ZkString
DLL.ZkContainer_getItemCount.restype = c_size_t
DLL.ZkContainer_getItem.restype = ZkPointer


class Container(InteractiveObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def is_locked(self) -> bool:
        return DLL.ZkContainer_getIsLocked(self._handle)

    @is_locked.setter
    def is_locked(self, value: bool) -> None:
        DLL.ZkContainer_setIsLocked(self._handle, c_bool(value))

    @property
    def key(self) -> str:
        return DLL.ZkContainer_getKey(self._handle).value

    @key.setter
    def key(self, value: str) -> None:
        DLL.ZkContainer_setKey(self._handle, value.encode("utf-8"))

    @property
    def pick_string(self) -> str:
        return DLL.ZkContainer_getPickString(self._handle).value

    @pick_string.setter
    def pick_string(self, value: str) -> None:
        DLL.ZkContainer_setPickString(self._handle, value.encode("utf-8"))

    @property
    def contents(self) -> str:
        return DLL.ZkContainer_getContents(self._handle).value

    @contents.setter
    def contents(self, value: str) -> None:
        DLL.ZkContainer_setContents(self._handle, value.encode("utf-8"))

    @property
    def items(self) -> list[Item]:
        count = DLL.ZkContainer_getItemCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkContainer_getItem(self._handle, i).value
            items.append(Item(_handle=DLL.ZkObject_takeRef(handle).value, _delete=True))

        return items

    @items.setter
    def items(self, value: list[Item]) -> None:
        count = DLL.ZkContainer_getItemCount(self._handle)
        for _ in range(count):
            DLL.ZkContainer_removeItem(self._handle, 0)

        for v in value:
            DLL.ZkContainer_addItem(self._handle, v.handle)


DLL.ZkDoor_getIsLocked.restype = c_bool
DLL.ZkDoor_getKey.restype = ZkString
DLL.ZkDoor_getPickString.restype = ZkString


class Door(InteractiveObject):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def is_locked(self) -> bool:
        return DLL.ZkDoor_getIsLocked(self._handle)

    @is_locked.setter
    def is_locked(self, value: bool) -> None:
        DLL.ZkDoor_setIsLocked(self._handle, c_bool(value))

    @property
    def key(self) -> str:
        return DLL.ZkDoor_getKey(self._handle).value

    @key.setter
    def key(self, value: str) -> None:
        DLL.ZkDoor_setKey(self._handle, value.encode("utf-8"))

    @property
    def pick_string(self) -> str:
        return DLL.ZkDoor_getPickString(self._handle).value

    @pick_string.setter
    def pick_string(self, value: str) -> None:
        DLL.ZkDoor_setPickString(self._handle, value.encode("utf-8"))
