__all__ = ["ItemReactInstance"]

from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit.daedalus.base import DaedalusInstance


class ItemReactInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def npc(self) -> int:
        DLL.ZkItemReactInstance_getNpc.restype = c_int32
        return DLL.ZkItemReactInstance_getNpc(self._handle)

    @npc.setter
    def npc(self, value: int) -> None:
        DLL.ZkItemReactInstance_setNpc(self._handle, c_int32(value))

    @property
    def trade_item(self) -> int:
        DLL.ZkItemReactInstance_getTradeItem.restype = c_int32
        return DLL.ZkItemReactInstance_getTradeItem(self._handle)

    @trade_item.setter
    def trade_item(self, value: int) -> None:
        DLL.ZkItemReactInstance_setTradeItem(self._handle, c_int32(value))

    @property
    def trade_amount(self) -> int:
        DLL.ZkItemReactInstance_getTradeAmount.restype = c_int32
        return DLL.ZkItemReactInstance_getTradeAmount(self._handle)

    @trade_amount.setter
    def trade_amount(self, value: int) -> None:
        DLL.ZkItemReactInstance_setTradeAmount(self._handle, c_int32(value))

    @property
    def requested_category(self) -> int:
        DLL.ZkItemReactInstance_getRequestedCategory.restype = c_int32
        return DLL.ZkItemReactInstance_getRequestedCategory(self._handle)

    @requested_category.setter
    def requested_category(self, value: int) -> None:
        DLL.ZkItemReactInstance_setRequestedCategory(self._handle, c_int32(value))

    @property
    def requested_item(self) -> int:
        DLL.ZkItemReactInstance_getRequestedItem.restype = c_int32
        return DLL.ZkItemReactInstance_getRequestedItem(self._handle)

    @requested_item.setter
    def requested_item(self, value: int) -> None:
        DLL.ZkItemReactInstance_setRequestedItem(self._handle, c_int32(value))

    @property
    def requested_amount(self) -> int:
        DLL.ZkItemReactInstance_getRequestedAmount.restype = c_int32
        return DLL.ZkItemReactInstance_getRequestedAmount(self._handle)

    @requested_amount.setter
    def requested_amount(self, value: int) -> None:
        DLL.ZkItemReactInstance_setRequestedAmount(self._handle, c_int32(value))

    @property
    def reaction(self) -> int:
        DLL.ZkItemReactInstance_getReaction.restype = c_int32
        return DLL.ZkItemReactInstance_getReaction(self._handle)

    @reaction.setter
    def reaction(self, value: int) -> None:
        DLL.ZkItemReactInstance_setReaction(self._handle, c_int32(value))
