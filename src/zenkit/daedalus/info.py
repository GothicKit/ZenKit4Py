__all__ = [
    "InfoInstance",
]

from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class InfoInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def npc(self) -> int:
        DLL.ZkInfoInstance_getNpc.restype = c_int32
        return DLL.ZkInfoInstance_getNpc(self._handle)

    @npc.setter
    def npc(self, value: int) -> None:
        DLL.ZkInfoInstance_setNpc(self._handle, c_int32(value))

    @property
    def nr(self) -> int:
        DLL.ZkInfoInstance_getNr.restype = c_int32
        return DLL.ZkInfoInstance_getNr(self._handle)

    @nr.setter
    def nr(self, value: int) -> None:
        DLL.ZkInfoInstance_setNr(self._handle, c_int32(value))

    @property
    def important(self) -> int:
        DLL.ZkInfoInstance_getImportant.restype = c_int32
        return DLL.ZkInfoInstance_getImportant(self._handle)

    @important.setter
    def important(self, value: int) -> None:
        DLL.ZkInfoInstance_setImportant(self._handle, c_int32(value))

    @property
    def condition(self) -> int:
        DLL.ZkInfoInstance_getCondition.restype = c_int32
        return DLL.ZkInfoInstance_getCondition(self._handle)

    @condition.setter
    def condition(self, value: int) -> None:
        DLL.ZkInfoInstance_setCondition(self._handle, c_int32(value))

    @property
    def information(self) -> int:
        DLL.ZkInfoInstance_getInformation.restype = c_int32
        return DLL.ZkInfoInstance_getInformation(self._handle)

    @information.setter
    def information(self, value: int) -> None:
        DLL.ZkInfoInstance_setInformation(self._handle, c_int32(value))

    @property
    def description(self) -> str:
        DLL.ZkInfoInstance_getDescription.restype = ZkString
        return DLL.ZkInfoInstance_getDescription(self._handle).value

    @description.setter
    def description(self, value: str) -> None:
        DLL.ZkInfoInstance_setDescription(self._handle, value.encode("utf-8"))

    @property
    def trade(self) -> int:
        DLL.ZkInfoInstance_getTrade.restype = c_int32
        return DLL.ZkInfoInstance_getTrade(self._handle)

    @trade.setter
    def trade(self, value: int) -> None:
        DLL.ZkInfoInstance_setTrade(self._handle, c_int32(value))

    @property
    def permanent(self) -> int:
        DLL.ZkInfoInstance_getPermanent.restype = c_int32
        return DLL.ZkInfoInstance_getPermanent(self._handle)

    @permanent.setter
    def permanent(self, value: int) -> None:
        DLL.ZkInfoInstance_setPermanent(self._handle, c_int32(value))
