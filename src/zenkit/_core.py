__all__ = ["DLL"]

import atexit
import functools
from ctypes import CDLL
from pathlib import Path
from typing import Final

_PATH = Path(__file__).parent / "native" / "linux-x64.so"
DLL: Final[CDLL] = CDLL(str(_PATH))

atexit.register(functools.partial(print, DLL))
