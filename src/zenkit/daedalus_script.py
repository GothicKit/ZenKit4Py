__all__ = [
    "DaedalusScript",
    "DaedalusSymbol",
    "DaedalusInstruction",
    "DaedalusDataType",
    "DaedalusOpcode",
]

from abc import abstractmethod
from ctypes import Structure
from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from ctypes import c_uint16
from ctypes import c_uint32
from ctypes import c_void_p
from enum import IntEnum
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._native import ZkPointer
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class DaedalusOpcode(IntEnum):
    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3
    MOD = 4
    OR = 5
    ANDB = 6
    LT = 7
    GT = 8
    MOVI = 9
    ORR = 11
    AND = 12
    LSL = 13
    LSR = 14
    LTE = 15
    EQ = 16
    NEQ = 17
    GTE = 18
    ADDMOVI = 19
    SUBMOVI = 20
    MULMOVI = 21
    DIVMOVI = 22
    PLUS = 30
    NEGATE = 31
    NOT = 32
    CMPL = 33
    NOP = 45
    RSR = 60
    BL = 61
    BE = 62
    PUSHI = 64
    PUSHV = 65
    PUSHVI = 67
    MOVS = 70
    MOVSS = 71
    MOVVF = 72
    MOVF = 73
    MOVVI = 74
    B = 75
    BZ = 76
    GMOVI = 80
    PUSHVV = 245


class DaedalusDataType(IntEnum):
    VOID = 0
    FLOAT = 1
    INT = 2
    STRING = 3
    CLASS = 4
    FUNCTION = 5
    PROTOTYPE = 6
    INSTANCE = 7


class DaedalusSymbol:
    __slots__ = ("_handle", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @property
    def handle(self) -> c_void_p:
        return self._handle

    def get_string(self, i: int = 0, ctx: DaedalusInstance | None = None) -> str:
        DLL.ZkDaedalusSymbol_getString.restype = ZkString
        return DLL.ZkDaedalusSymbol_getString(self._handle, c_uint16(i), ctx.handle if ctx else None).value

    def set_string(self, val: str, i: int = 0, ctx: DaedalusInstance | None = None) -> None:
        DLL.ZkDaedalusSymbol_setString(self._handle, val.encode("utf-8"), c_uint16(i), ctx.handle if ctx else None)

    def get_int(self, i: int = 0, ctx: DaedalusInstance | None = None) -> int:
        DLL.ZkDaedalusSymbol_getInt.restype = c_int32
        return DLL.ZkDaedalusSymbol_getInt(self._handle, c_uint16(i), ctx.handle if ctx else None).value

    def set_int(self, val: int, i: int = 0, ctx: DaedalusInstance | None = None) -> None:
        DLL.ZkDaedalusSymbol_setInt(self._handle, c_int32(val), c_uint16(i), ctx.handle if ctx else None)

    def get_float(self, i: int = 0, ctx: DaedalusInstance | None = None) -> float:
        DLL.ZkDaedalusSymbol_getFloat.restype = c_float
        return DLL.ZkDaedalusSymbol_getFloat(self._handle, c_uint16(i), ctx.handle if ctx else None).value

    def set_float(self, val: float, i: int = 0, ctx: DaedalusInstance | None = None) -> None:
        DLL.ZkDaedalusSymbol_setFloat(self._handle, c_float(val), c_uint16(i), ctx.handle if ctx else None)

    @property
    def is_const(self) -> bool:
        DLL.ZkDaedalusSymbol_getIsConst.restype = c_bool
        return DLL.ZkDaedalusSymbol_getIsConst(self._handle)

    @property
    def is_member(self) -> bool:
        DLL.ZkDaedalusSymbol_getIsMember.restype = c_bool
        return DLL.ZkDaedalusSymbol_getIsMember(self._handle)

    @property
    def is_external(self) -> bool:
        DLL.ZkDaedalusSymbol_getIsExternal.restype = c_bool
        return DLL.ZkDaedalusSymbol_getIsExternal(self._handle)

    @property
    def is_merged(self) -> bool:
        DLL.ZkDaedalusSymbol_getIsMerged.restype = c_bool
        return DLL.ZkDaedalusSymbol_getIsMerged(self._handle)

    @property
    def is_generated(self) -> bool:
        DLL.ZkDaedalusSymbol_getIsGenerated.restype = c_bool
        return DLL.ZkDaedalusSymbol_getIsGenerated(self._handle)

    @property
    def has_return(self) -> bool:
        DLL.ZkDaedalusSymbol_getHasReturn.restype = c_bool
        return DLL.ZkDaedalusSymbol_getHasReturn(self._handle)

    @property
    def name(self) -> str:
        DLL.ZkDaedalusSymbol_getName.restype = ZkString
        return DLL.ZkDaedalusSymbol_getName(self._handle).value

    @property
    def address(self) -> int:
        DLL.ZkDaedalusSymbol_getAddress.restype = c_int32
        return DLL.ZkDaedalusSymbol_getAddress(self._handle)

    @property
    def parent(self) -> int:
        DLL.ZkDaedalusSymbol_getParent.restype = c_int32
        return DLL.ZkDaedalusSymbol_getParent(self._handle)

    @property
    def size(self) -> int:
        DLL.ZkDaedalusSymbol_getSize.restype = c_int32
        return DLL.ZkDaedalusSymbol_getSize(self._handle)

    @property
    def type(self) -> DaedalusDataType:
        DLL.ZkDaedalusSymbol_getType.restype = c_int
        return DaedalusDataType(DLL.ZkDaedalusSymbol_getType(self._handle))

    @property
    def index(self) -> int:
        DLL.ZkDaedalusSymbol_getIndex.restype = c_uint32
        return DLL.ZkDaedalusSymbol_getIndex(self._handle)

    @property
    def return_type(self) -> DaedalusDataType:
        DLL.ZkDaedalusSymbol_getReturnType.restype = c_int
        return DaedalusDataType(DLL.ZkDaedalusSymbol_getReturnType(self._handle))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} handle={self._handle} name={self.name!r} type={self.type.name}>"


class DaedalusInstruction(Structure):
    _fields_ = [
        ("_op", c_int),
        ("_size", c_int32),
        ("_addr_sym_imm", c_int32),
        ("_index", c_int32),
    ]

    @property
    def op(self) -> DaedalusOpcode:
        return DaedalusOpcode(self._op)

    @property
    def size(self) -> int:
        return self._size

    @property
    def address(self) -> int:
        return c_uint32(self._addr_sym_imm).value

    @property
    def symbol(self) -> int:
        return c_uint32(self._addr_sym_imm).value

    @property
    def immediate(self) -> int:
        return self._addr_sym_imm

    @property
    def index(self) -> int:
        return self._index


class DaedalusScript:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "DaedalusScript":
        handle = _native.load("ZkDaedalusScript_load", path_or_file_like)
        return DaedalusScript(_handle=handle, _delete=True)

    @property
    def symbols(self) -> list[DaedalusSymbol]:
        DLL.ZkDaedalusScript_getSymbolCount.restype = c_uint32
        count = DLL.ZkDaedalusScript_getSymbolCount(self._handle)
        items = []

        for i in range(count):
            items.append(self.get_symbol_by_index(i))

        return items

    def get_instruction(self, address: int) -> DaedalusInstruction:
        DLL.ZkDaedalusScript_getInstruction.restype = DaedalusInstruction
        return DLL.ZkDaedalusScript_getInstruction(self._handle, c_size_t(address))

    def get_symbol_by_index(self, i: int) -> DaedalusSymbol | None:
        DLL.ZkDaedalusScript_getSymbolByIndex.restype = ZkPointer
        handle = DLL.ZkDaedalusScript_getSymbolByIndex(self._handle, c_uint32(i)).value
        if handle is None or handle.value is None:
            return None
        return DaedalusSymbol(_handle=handle, _keepalive=self)

    def get_symbol_by_address(self, i: int) -> DaedalusSymbol | None:
        DLL.ZkDaedalusScript_getSymbolByAddress.restype = ZkPointer
        handle = DLL.ZkDaedalusScript_getSymbolByAddress(self._handle, c_size_t(i)).value
        if handle is None or handle.value is None:
            return None
        return DaedalusSymbol(_handle=handle, _keepalive=self)

    def get_symbol_by_name(self, name: str) -> DaedalusSymbol | None:
        DLL.ZkDaedalusScript_getSymbolByName.restype = ZkPointer
        handle = DLL.ZkDaedalusScript_getSymbolByName(self._handle, name.encode("utf-8")).value
        if handle is None or handle.value is None:
            return None
        return DaedalusSymbol(_handle=handle, _keepalive=self)

    def __del__(self) -> None:
        self._deleter()

    @abstractmethod
    def _deleter(self) -> None:
        DLL.ZkDaedalusScript_del(self._handle)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} handle={self._handle}>"
