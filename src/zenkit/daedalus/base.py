__all__ = [
    "DaedalusInstance",
    "DaedalusInstanceType",
]

from ctypes import c_int
from ctypes import c_uint32
from ctypes import c_void_p
from enum import IntEnum
from typing import Any

from zenkit._core import DLL


class DaedalusInstanceType(IntEnum):
    GUILD_VALUES = 0
    NPC = 1
    MISSION = 2
    ITEM = 3
    FOCUS = 4
    INFO = 5
    ITEM_REACT = 6
    SPELL = 7
    SVM = 8
    MENU = 9
    MENU_ITEM = 10
    CAMERA = 11
    MUSIC_SYSTEM = 12
    MUSIC_THEME = 13
    MUSIC_JINGLE = 14
    PARTICLE_EFFECT = 15
    EFFECT_BASE = 16
    PARTICLE_EFFECT_EMIT_KEY = 17
    FIGHT_AI = 18
    SOUND_EFFECT = 19
    SOUND_SYSTEM = 20
    INVALID = 21


class DaedalusInstance:
    __slots__ = ("_handle",)

    def __init__(self, **kwargs: Any) -> None:
        self._handle = None

        if "_handle" in kwargs:
            self._handle = kwargs.pop("_handle")

    @staticmethod
    def from_native(handle: c_void_p | None) -> "DaedalusInstance | None":
        from zenkit.daedalus import _INSTANCES

        if handle is None or handle.value is None or handle.value == 0:
            return None

        DLL.ZkDaedalusInstance_getType.restype = c_int
        typ = DaedalusInstanceType(DLL.ZkDaedalusInstance_getType(handle))

        return _INSTANCES.get(typ, DaedalusInstance)(_handle=handle)

    @property
    def handle(self) -> c_void_p:
        return self._handle

    @property
    def type(self) -> DaedalusInstanceType:
        DLL.ZkDaedalusInstance_getType.restype = c_int
        return DaedalusInstanceType(DLL.ZkDaedalusInstance_getType(self._handle))

    @property
    def index(self) -> int:
        DLL.ZkDaedalusInstance_getIndex.restype = c_uint32
        return DLL.ZkDaedalusInstance_getIndex(self._handle)
