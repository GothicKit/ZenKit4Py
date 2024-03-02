__all__ = [
    "DaedalusInstance",
    "DaedalusInstanceType",
]

from enum import IntEnum
from typing import Any


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

    def __init__(self, **kwargs: Any):
        self._handle = None

        if "_handle" in kwargs:
            self._handle = kwargs.pop("_handle")
