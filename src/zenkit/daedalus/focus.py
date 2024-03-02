__all__ = ["FocusInstance"]

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit.daedalus.base import DaedalusInstance


class FocusInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def npc_longrange(self) -> float:
        DLL.ZkFocusInstance_getNpcLongrange.restype = c_float
        return DLL.ZkFocusInstance_getNpcLongrange(self._handle)

    @npc_longrange.setter
    def npc_longrange(self, value: float) -> None:
        DLL.ZkFocusInstance_setNpcLongrange(self._handle, c_float(value))

    @property
    def npc_range1(self) -> float:
        DLL.ZkFocusInstance_getNpcRange1.restype = c_float
        return DLL.ZkFocusInstance_getNpcRange1(self._handle)

    @npc_range1.setter
    def npc_range1(self, value: float) -> None:
        DLL.ZkFocusInstance_setNpcRange1(self._handle, c_float(value))

    @property
    def npc_range2(self) -> float:
        DLL.ZkFocusInstance_getNpcRange2.restype = c_float
        return DLL.ZkFocusInstance_getNpcRange2(self._handle)

    @npc_range2.setter
    def npc_range2(self, value: float) -> None:
        DLL.ZkFocusInstance_setNpcRange2(self._handle, c_float(value))

    @property
    def npc_azi(self) -> float:
        DLL.ZkFocusInstance_getNpcAzi.restype = c_float
        return DLL.ZkFocusInstance_getNpcAzi(self._handle)

    @npc_azi.setter
    def npc_azi(self, value: float) -> None:
        DLL.ZkFocusInstance_setNpcAzi(self._handle, c_float(value))

    @property
    def npc_elevdo(self) -> float:
        DLL.ZkFocusInstance_getNpcElevdo.restype = c_float
        return DLL.ZkFocusInstance_getNpcElevdo(self._handle)

    @npc_elevdo.setter
    def npc_elevdo(self, value: float) -> None:
        DLL.ZkFocusInstance_setNpcElevdo(self._handle, c_float(value))

    @property
    def npc_elevup(self) -> float:
        DLL.ZkFocusInstance_getNpcElevup.restype = c_float
        return DLL.ZkFocusInstance_getNpcElevup(self._handle)

    @npc_elevup.setter
    def npc_elevup(self, value: float) -> None:
        DLL.ZkFocusInstance_setNpcElevup(self._handle, c_float(value))

    @property
    def npc_prio(self) -> int:
        DLL.ZkFocusInstance_getNpcPrio.restype = c_int32
        return DLL.ZkFocusInstance_getNpcPrio(self._handle)

    @npc_prio.setter
    def npc_prio(self, value: int) -> None:
        DLL.ZkFocusInstance_setNpcPrio(self._handle, c_int32(value))

    @property
    def item_range1(self) -> float:
        DLL.ZkFocusInstance_getItemRange1.restype = c_float
        return DLL.ZkFocusInstance_getItemRange1(self._handle)

    @item_range1.setter
    def item_range1(self, value: float) -> None:
        DLL.ZkFocusInstance_setItemRange1(self._handle, c_float(value))

    @property
    def item_range2(self) -> float:
        DLL.ZkFocusInstance_getItemRange2.restype = c_float
        return DLL.ZkFocusInstance_getItemRange2(self._handle)

    @item_range2.setter
    def item_range2(self, value: float) -> None:
        DLL.ZkFocusInstance_setItemRange2(self._handle, c_float(value))

    @property
    def item_azi(self) -> float:
        DLL.ZkFocusInstance_getItemAzi.restype = c_float
        return DLL.ZkFocusInstance_getItemAzi(self._handle)

    @item_azi.setter
    def item_azi(self, value: float) -> None:
        DLL.ZkFocusInstance_setItemAzi(self._handle, c_float(value))

    @property
    def item_elevdo(self) -> float:
        DLL.ZkFocusInstance_getItemElevdo.restype = c_float
        return DLL.ZkFocusInstance_getItemElevdo(self._handle)

    @item_elevdo.setter
    def item_elevdo(self, value: float) -> None:
        DLL.ZkFocusInstance_setItemElevdo(self._handle, c_float(value))

    @property
    def item_elevup(self) -> float:
        DLL.ZkFocusInstance_getItemElevup.restype = c_float
        return DLL.ZkFocusInstance_getItemElevup(self._handle)

    @item_elevup.setter
    def item_elevup(self, value: float) -> None:
        DLL.ZkFocusInstance_setItemElevup(self._handle, c_float(value))

    @property
    def item_prio(self) -> int:
        DLL.ZkFocusInstance_getItemPrio.restype = c_int32
        return DLL.ZkFocusInstance_getItemPrio(self._handle)

    @item_prio.setter
    def item_prio(self, value: int) -> None:
        DLL.ZkFocusInstance_setItemPrio(self._handle, c_int32(value))

    @property
    def mob_range1(self) -> float:
        DLL.ZkFocusInstance_getMobRange1.restype = c_float
        return DLL.ZkFocusInstance_getMobRange1(self._handle)

    @mob_range1.setter
    def mob_range1(self, value: float) -> None:
        DLL.ZkFocusInstance_setMobRange1(self._handle, c_float(value))

    @property
    def mob_range2(self) -> float:
        DLL.ZkFocusInstance_getMobRange2.restype = c_float
        return DLL.ZkFocusInstance_getMobRange2(self._handle)

    @mob_range2.setter
    def mob_range2(self, value: float) -> None:
        DLL.ZkFocusInstance_setMobRange2(self._handle, c_float(value))

    @property
    def mob_azi(self) -> float:
        DLL.ZkFocusInstance_getMobAzi.restype = c_float
        return DLL.ZkFocusInstance_getMobAzi(self._handle)

    @mob_azi.setter
    def mob_azi(self, value: float) -> None:
        DLL.ZkFocusInstance_setMobAzi(self._handle, c_float(value))

    @property
    def mob_elevdo(self) -> float:
        DLL.ZkFocusInstance_getMobElevdo.restype = c_float
        return DLL.ZkFocusInstance_getMobElevdo(self._handle)

    @mob_elevdo.setter
    def mob_elevdo(self, value: float) -> None:
        DLL.ZkFocusInstance_setMobElevdo(self._handle, c_float(value))

    @property
    def mob_elevup(self) -> float:
        DLL.ZkFocusInstance_getMobElevup.restype = c_float
        return DLL.ZkFocusInstance_getMobElevup(self._handle)

    @mob_elevup.setter
    def mob_elevup(self, value: float) -> None:
        DLL.ZkFocusInstance_setMobElevup(self._handle, c_float(value))

    @property
    def mob_prio(self) -> int:
        DLL.ZkFocusInstance_getMobPrio.restype = c_int32
        return DLL.ZkFocusInstance_getMobPrio(self._handle)

    @mob_prio.setter
    def mob_prio(self, value: int) -> None:
        DLL.ZkFocusInstance_setMobPrio(self._handle, c_int32(value))
