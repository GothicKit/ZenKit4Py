__all__ = ["FightAiInstance"]

from ctypes import c_int
from ctypes import c_size_t
from enum import IntEnum
from typing import Any

from zenkit._core import DLL
from zenkit.daedalus.base import DaedalusInstance


class FightAiMove(IntEnum):
    NOP = (0,)
    RUN = (1,)
    RUN_BACK = (2,)
    JUMP_BACK = (3,)
    TURN = (4,)
    STRAFE = (5,)
    ATTACK = (6,)
    ATTACK_SIDE = (7,)
    ATTACK_FRONT = (8,)
    ATTACK_TRIPLE = (9,)
    ATTACK_WHIRL = (10,)
    ATTACK_MASTER = (11,)
    TURN_TO_HIT = (15,)
    PARRY = (17,)
    STAND_UP = (18,)
    WAIT = (19,)
    WAIT_LONGER = (23,)
    WAIT_EXT = (24,)


class FightAiInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def get_move(self, i: int) -> FightAiMove:
        if i < 0 or i >= 5:
            raise IndexError(i)

        DLL.ZkFightAiInstance_getMove.restype = c_int
        return FightAiMove(DLL.ZkFightAiInstance_getMove(self._handle, c_size_t(i)))

    def set_user_string(self, i: int, val: FightAiMove) -> None:
        if i < 0 or i >= 5:
            raise IndexError(i)
        return DLL.ZkFightAiInstance_setMove(self._handle, c_size_t(i), val.value)
