__all__ = ["MenuInstance"]

from ctypes import c_int32
from ctypes import c_size_t
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance

_MENU_ITEM_COUNT = 150


class MenuInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def back_pic(self) -> str:
        DLL.ZkMenuInstance_getBackPic.restype = ZkString
        return DLL.ZkMenuInstance_getBackPic(self._handle).value

    @back_pic.setter
    def back_pic(self, value: str) -> None:
        DLL.ZkMenuInstance_setBackPic(self._handle, value.encode("utf-8"))

    @property
    def back_world(self) -> str:
        DLL.ZkMenuInstance_getBackWorld.restype = ZkString
        return DLL.ZkMenuInstance_getBackWorld(self._handle).value

    @back_world.setter
    def back_world(self, value: str) -> None:
        DLL.ZkMenuInstance_setBackWorld(self._handle, value.encode("utf-8"))

    @property
    def pos_x(self) -> int:
        DLL.ZkMenuInstance_getPosX.restype = c_int32
        return DLL.ZkMenuInstance_getPosX(self._handle)

    @pos_x.setter
    def pos_x(self, value: int) -> None:
        DLL.ZkMenuInstance_setPosX(self._handle, c_int32(value))

    @property
    def pos_y(self) -> int:
        DLL.ZkMenuInstance_getPosY.restype = c_int32
        return DLL.ZkMenuInstance_getPosY(self._handle)

    @pos_y.setter
    def pos_y(self, value: int) -> None:
        DLL.ZkMenuInstance_setPosY(self._handle, c_int32(value))

    @property
    def dim_x(self) -> int:
        DLL.ZkMenuInstance_getDimX.restype = c_int32
        return DLL.ZkMenuInstance_getDimX(self._handle)

    @dim_x.setter
    def dim_x(self, value: int) -> None:
        DLL.ZkMenuInstance_setDimX(self._handle, c_int32(value))

    @property
    def dim_y(self) -> int:
        DLL.ZkMenuInstance_getDimY.restype = c_int32
        return DLL.ZkMenuInstance_getDimY(self._handle)

    @dim_y.setter
    def dim_y(self, value: int) -> None:
        DLL.ZkMenuInstance_setDimY(self._handle, c_int32(value))

    @property
    def alpha(self) -> int:
        DLL.ZkMenuInstance_getAlpha.restype = c_int32
        return DLL.ZkMenuInstance_getAlpha(self._handle)

    @alpha.setter
    def alpha(self, value: int) -> None:
        DLL.ZkMenuInstance_setAlpha(self._handle, c_int32(value))

    @property
    def music_theme(self) -> str:
        DLL.ZkMenuInstance_getMusicTheme.restype = ZkString
        return DLL.ZkMenuInstance_getMusicTheme(self._handle).value

    @music_theme.setter
    def music_theme(self, value: str) -> None:
        DLL.ZkMenuInstance_setMusicTheme(self._handle, value.encode("utf-8"))

    @property
    def event_timer_msec(self) -> int:
        DLL.ZkMenuInstance_getEventTimerMsec.restype = c_int32
        return DLL.ZkMenuInstance_getEventTimerMsec(self._handle)

    @event_timer_msec.setter
    def event_timer_msec(self, value: int) -> None:
        DLL.ZkMenuInstance_setEventTimerMsec(self._handle, c_int32(value))

    @property
    def flags(self) -> int:
        DLL.ZkMenuInstance_getFlags.restype = c_int32
        return DLL.ZkMenuInstance_getFlags(self._handle)

    @flags.setter
    def flags(self, value: int) -> None:
        DLL.ZkMenuInstance_setFlags(self._handle, c_int32(value))

    @property
    def default_outgame(self) -> int:
        DLL.ZkMenuInstance_getDefaultOutgame.restype = c_int32
        return DLL.ZkMenuInstance_getDefaultOutgame(self._handle)

    @default_outgame.setter
    def default_outgame(self, value: int) -> None:
        DLL.ZkMenuInstance_setDefaultOutgame(self._handle, c_int32(value))

    @property
    def default_ingame(self) -> int:
        DLL.ZkMenuInstance_getDefaultIngame.restype = c_int32
        return DLL.ZkMenuInstance_getDefaultIngame(self._handle)

    @default_ingame.setter
    def default_ingame(self, value: int) -> None:
        DLL.ZkMenuInstance_setDefaultIngame(self._handle, c_int32(value))

    def get_item(self, i: int) -> str:
        if i < 0 or i >= _MENU_ITEM_COUNT:
            raise IndexError(i)
        DLL.ZkMenuInstance_getItem.restype = ZkString
        return DLL.ZkMenuInstance_getItem(self._handle, c_size_t(i))

    def set_item(self, i: int, val: str) -> None:
        if i < 0 or i >= _MENU_ITEM_COUNT:
            raise IndexError(i)
        DLL.ZkMenuInstance_setItem(self._handle, c_size_t(i), val.encode("utf-8"))
