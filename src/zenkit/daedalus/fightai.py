__all__ = ["FightAiInstance"]

from enum import IntEnum
from typing import Any

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

    """TODO(lmichaelis):
    ZKC_API ZkFightAiMove ZkFightAiInstance_getMove(ZkFightAiInstance const* slf, ZkSize i);
    ZKC_API void ZkFightAiInstance_setMove(ZkFightAiInstance* slf, ZkSize i, ZkFightAiMove move);
    """
