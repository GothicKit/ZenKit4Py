__all__ = [
    "MenuItemType",
    "MenuItemFlag",
    "MenuItemInstance",
]

from ctypes import c_float
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance

_MENU_ITEM_TEXT_COUNT = 10
_MENU_ITEM_USER_COUNT = 4
_MENU_ITEM_EVENT_ACTION_COUNT = 10
_MENU_ITEM_SELECT_ACTION_COUNT = 5


class MenuItemType(IntEnum):
    UNKNOWN = 0
    TEXT = 1
    SLIDER = 2
    INPUT = 3
    CURSOR = 4
    CHOICEBOX = 5
    BUTTON = 6
    LISTBOX = 7


class MenuItemFlag(IntEnum):
    CHROMAKEYED = 1 << 0
    TRANSPARENT = 1 << 1
    SELECTABLE = 1 << 2
    MOVABLE = 1 << 3
    CENTERED = 1 << 4
    DISABLED = 1 << 5
    FADE = 1 << 6
    EFFECTS = 1 << 7
    ONLY_OUTGAME = 1 << 8
    ONLY_INGAME = 1 << 9
    PERF_OPTION = 1 << 10
    MULTILINE = 1 << 11
    NEEDS_APPLY = 1 << 12
    NEEDS_RESTART = 1 << 13
    EXTENDED_MENU = 1 << 14
    HOR_SELECTABLE = 1 << 15


class MenuItemInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def font_name(self) -> str:
        DLL.ZkMenuItemInstance_getFontName.restype = ZkString
        return DLL.ZkMenuItemInstance_getFontName(self._handle).value

    @font_name.setter
    def font_name(self, value: str) -> None:
        DLL.ZkMenuItemInstance_setFontName(self._handle, value.encode("utf-8"))

    @property
    def backpic(self) -> str:
        DLL.ZkMenuItemInstance_getBackpic.restype = ZkString
        return DLL.ZkMenuItemInstance_getBackpic(self._handle).value

    @backpic.setter
    def backpic(self, value: str) -> None:
        DLL.ZkMenuItemInstance_setBackpic(self._handle, value.encode("utf-8"))

    @property
    def alpha_mode(self) -> str:
        DLL.ZkMenuItemInstance_getAlphaMode.restype = ZkString
        return DLL.ZkMenuItemInstance_getAlphaMode(self._handle).value

    @alpha_mode.setter
    def alpha_mode(self, value: str) -> None:
        DLL.ZkMenuItemInstance_setAlphaMode(self._handle, value.encode("utf-8"))

    @property
    def alpha(self) -> int:
        DLL.ZkMenuItemInstance_getAlpha.restype = c_int32
        return DLL.ZkMenuItemInstance_getAlpha(self._handle)

    @alpha.setter
    def alpha(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setAlpha(self._handle, c_int32(value))

    @property
    def type(self) -> MenuItemType:
        DLL.ZkMenuItemInstance_getType.restype = c_int
        return MenuItemType(DLL.ZkMenuItemInstance_getType(self._handle))

    @type.setter
    def type(self, value: MenuItemType) -> None:
        DLL.ZkMenuItemInstance_setType(self._handle, value.value)

    @property
    def on_chg_set_option(self) -> str:
        DLL.ZkMenuItemInstance_getOnChgSetOption.restype = ZkString
        return DLL.ZkMenuItemInstance_getOnChgSetOption(self._handle).value

    @on_chg_set_option.setter
    def on_chg_set_option(self, value: str) -> None:
        DLL.ZkMenuItemInstance_setOnChgSetOption(self._handle, value.encode("utf-8"))

    @property
    def on_chg_set_option_section(self) -> str:
        DLL.ZkMenuItemInstance_getOnChgSetOptionSection.restype = ZkString
        return DLL.ZkMenuItemInstance_getOnChgSetOptionSection(self._handle).value

    @on_chg_set_option_section.setter
    def on_chg_set_option_section(self, value: str) -> None:
        DLL.ZkMenuItemInstance_setOnChgSetOptionSection(self._handle, value.encode("utf-8"))

    @property
    def pos_x(self) -> int:
        DLL.ZkMenuItemInstance_getPosX.restype = c_int32
        return DLL.ZkMenuItemInstance_getPosX(self._handle)

    @pos_x.setter
    def pos_x(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setPosX(self._handle, c_int32(value))

    @property
    def pos_y(self) -> int:
        DLL.ZkMenuItemInstance_getPosY.restype = c_int32
        return DLL.ZkMenuItemInstance_getPosY(self._handle)

    @pos_y.setter
    def pos_y(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setPosY(self._handle, c_int32(value))

    @property
    def dim_x(self) -> int:
        DLL.ZkMenuItemInstance_getDimX.restype = c_int32
        return DLL.ZkMenuItemInstance_getDimX(self._handle)

    @dim_x.setter
    def dim_x(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setDimX(self._handle, c_int32(value))

    @property
    def dim_y(self) -> int:
        DLL.ZkMenuItemInstance_getDimY.restype = c_int32
        return DLL.ZkMenuItemInstance_getDimY(self._handle)

    @dim_y.setter
    def dim_y(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setDimY(self._handle, c_int32(value))

    @property
    def size_start_scale(self) -> float:
        DLL.ZkMenuItemInstance_getSizeStartScale.restype = c_float
        return DLL.ZkMenuItemInstance_getSizeStartScale(self._handle)

    @size_start_scale.setter
    def size_start_scale(self, value: float) -> None:
        DLL.ZkMenuItemInstance_setSizeStartScale(self._handle, c_float(value))

    @property
    def flags(self) -> int:
        DLL.ZkMenuItemInstance_getFlags.restype = c_int32
        return DLL.ZkMenuItemInstance_getFlags(self._handle)

    @flags.setter
    def flags(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setFlags(self._handle, c_int32(value))

    @property
    def open_delay_time(self) -> float:
        DLL.ZkMenuItemInstance_getOpenDelayTime.restype = c_float
        return DLL.ZkMenuItemInstance_getOpenDelayTime(self._handle)

    @open_delay_time.setter
    def open_delay_time(self, value: float) -> None:
        DLL.ZkMenuItemInstance_setOpenDelayTime(self._handle, c_float(value))

    @property
    def open_duration(self) -> float:
        DLL.ZkMenuItemInstance_getOpenDuration.restype = c_float
        return DLL.ZkMenuItemInstance_getOpenDuration(self._handle)

    @open_duration.setter
    def open_duration(self, value: float) -> None:
        DLL.ZkMenuItemInstance_setOpenDuration(self._handle, c_float(value))

    @property
    def frame_pos_x(self) -> int:
        DLL.ZkMenuItemInstance_getFramePosX.restype = c_int32
        return DLL.ZkMenuItemInstance_getFramePosX(self._handle)

    @frame_pos_x.setter
    def frame_pos_x(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setFramePosX(self._handle, c_int32(value))

    @property
    def frame_pos_y(self) -> int:
        DLL.ZkMenuItemInstance_getFramePosY.restype = c_int32
        return DLL.ZkMenuItemInstance_getFramePosY(self._handle)

    @frame_pos_y.setter
    def frame_pos_y(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setFramePosY(self._handle, c_int32(value))

    @property
    def frame_size_x(self) -> int:
        DLL.ZkMenuItemInstance_getFrameSizeX.restype = c_int32
        return DLL.ZkMenuItemInstance_getFrameSizeX(self._handle)

    @frame_size_x.setter
    def frame_size_x(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setFrameSizeX(self._handle, c_int32(value))

    @property
    def frame_size_y(self) -> int:
        DLL.ZkMenuItemInstance_getFrameSizeY.restype = c_int32
        return DLL.ZkMenuItemInstance_getFrameSizeY(self._handle)

    @frame_size_y.setter
    def frame_size_y(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setFrameSizeY(self._handle, c_int32(value))

    @property
    def hide_if_option_section_set(self) -> str:
        DLL.ZkMenuItemInstance_getHideIfOptionSectionSet.restype = ZkString
        return DLL.ZkMenuItemInstance_getHideIfOptionSectionSet(self._handle).value

    @hide_if_option_section_set.setter
    def hide_if_option_section_set(self, value: str) -> None:
        DLL.ZkMenuItemInstance_setHideIfOptionSectionSet(self._handle, value.encode("utf-8"))

    @property
    def hide_if_option_set(self) -> str:
        DLL.ZkMenuItemInstance_getHideIfOptionSet.restype = ZkString
        return DLL.ZkMenuItemInstance_getHideIfOptionSet(self._handle).value

    @hide_if_option_set.setter
    def hide_if_option_set(self, value: str) -> None:
        DLL.ZkMenuItemInstance_setHideIfOptionSet(self._handle, value.encode("utf-8"))

    @property
    def hide_on_value(self) -> int:
        DLL.ZkMenuItemInstance_getHideOnValue.restype = c_int32
        return DLL.ZkMenuItemInstance_getHideOnValue(self._handle)

    @hide_on_value.setter
    def hide_on_value(self, value: int) -> None:
        DLL.ZkMenuItemInstance_setHideOnValue(self._handle, c_int32(value))

    def get_on_sel_action(self, i: int) -> int:
        if i < 0 or i >= _MENU_ITEM_SELECT_ACTION_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_getOnSelAction.restype = c_int32
        return DLL.ZkMenuItemInstance_getOnSelAction(self._handle, c_size_t(i))

    def get_on_event_action(self, i: int) -> int:
        if i < 0 or i >= _MENU_ITEM_EVENT_ACTION_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_getOnEventAction.restype = c_int32
        return DLL.ZkMenuItemInstance_getOnEventAction(self._handle, c_size_t(i))

    def get_user_float(self, i: int) -> float:
        if i < 0 or i >= _MENU_ITEM_USER_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_getUserFloat.restype = float
        return DLL.ZkMenuItemInstance_getUserFloat(self._handle, c_size_t(i))

    def get_text(self, i: int) -> str:
        if i < 0 or i >= _MENU_ITEM_TEXT_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_getText.restype = ZkString
        return DLL.ZkMenuItemInstance_getText(self._handle, c_size_t(i)).value

    def get_on_sel_action_s(self, i: int) -> str:
        if i < 0 or i >= _MENU_ITEM_SELECT_ACTION_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_getOnSelActionS.restype = ZkString
        return DLL.ZkMenuItemInstance_getOnSelActionS(self._handle, c_size_t(i)).value

    def get_user_string(self, i: int) -> str:
        if i < 0 or i >= _MENU_ITEM_USER_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_getUserString.restype = ZkString
        return DLL.ZkMenuItemInstance_getUserString(self._handle, c_size_t(i)).value

    def set_on_sel_action(self, i: int, val: int) -> None:
        if i < 0 or i >= _MENU_ITEM_SELECT_ACTION_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_setOnSelAction(self._handle, c_size_t(i), val)

    def set_on_event_action(self, i: int, val: int) -> None:
        if i < 0 or i >= _MENU_ITEM_EVENT_ACTION_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_setOnEventAction(self._handle, c_size_t(i), val)

    def set_user_float(self, i: int, val: float) -> None:
        if i < 0 or i >= _MENU_ITEM_USER_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_setUserFloat(self._handle, c_size_t(i), c_float(val))

    def set_text(self, i: int, val: str) -> None:
        if i < 0 or i >= _MENU_ITEM_TEXT_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_setText(self._handle, c_size_t(i), val.encode("utf-8"))

    def set_on_sel_action_s(self, i: int, val: str) -> None:
        if i < 0 or i >= _MENU_ITEM_SELECT_ACTION_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_setOnSelActionS(self._handle, c_size_t(i), val.encode("utf-8"))

    def set_user_string(self, i: int, val: str) -> None:
        if i < 0 or i >= _MENU_ITEM_USER_COUNT:
            raise IndexError(i)
        DLL.ZkMenuItemInstance_setUserString(self._handle, c_size_t(i), val.encode("utf-8"))
