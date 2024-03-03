__all__ = [
    "DaedalusVm",
    "DaedalusType",
]

from collections.abc import Callable
from ctypes import CFUNCTYPE
from ctypes import c_float
from ctypes import c_int32
from ctypes import c_void_p
from typing import Any
from typing import TypeVar
from typing import Union

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._native import ZkPointer
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance
from zenkit.daedalus.base import DaedalusInstanceType
from zenkit.daedalus_script import DaedalusScript
from zenkit.daedalus_script import DaedalusSymbol

DaedalusType = Union[int, float, str, bool, DaedalusInstance, None]
DaedalusTypeGeneric = TypeVar("DaedalusTypeGeneric", bound=DaedalusType)

DaedalusVmExternalCallback = CFUNCTYPE(None, c_void_p, c_void_p)
DaedalusVmExternalDefaultCallback = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)


class DaedalusVm(DaedalusScript):
    __slots__ = ("_handle", "_delete", "_keepalive", "_externals")

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

        self._externals = []

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "DaedalusVm":
        handle = _native.load("ZkDaedalusVm_load", path_or_file_like)
        return DaedalusVm(_handle=handle, _delete=True)

    @property
    def global_self(self) -> DaedalusInstance:
        DLL.ZkDaedalusVm_getGlobalSelf.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_getGlobalSelf(self._handle).value
        return DaedalusInstance.from_native(handle)

    @property
    def global_other(self) -> DaedalusInstance:
        DLL.ZkDaedalusVm_getGlobalOther.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_getGlobalOther(self._handle).value
        return DaedalusInstance.from_native(handle)

    @property
    def global_victim(self) -> DaedalusInstance:
        DLL.ZkDaedalusVm_getGlobalVictim.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_getGlobalVictim(self._handle).value
        return DaedalusInstance.from_native(handle)

    @property
    def global_hero(self) -> DaedalusInstance:
        DLL.ZkDaedalusVm_getGlobalHero.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_getGlobalHero(self._handle).value
        return DaedalusInstance.from_native(handle)

    @property
    def global_item(self) -> DaedalusInstance:
        DLL.ZkDaedalusVm_getGlobalItem.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_getGlobalItem(self._handle).value
        return DaedalusInstance.from_native(handle)

    @global_self.setter
    def global_self(self, val: DaedalusInstance) -> None:
        DLL.ZkDaedalusVm_setGlobalSelf(self._handle, val.handle)

    @global_other.setter
    def global_other(self, val: DaedalusInstance) -> None:
        DLL.ZkDaedalusVm_setGlobalOther(self._handle, val.handle)

    @global_victim.setter
    def global_victim(self, val: DaedalusInstance) -> None:
        DLL.ZkDaedalusVm_setGlobalVictim(self._handle, val.handle)

    @global_hero.setter
    def global_hero(self, val: DaedalusInstance) -> None:
        DLL.ZkDaedalusVm_setGlobalHero(self._handle, val.handle)

    @global_item.setter
    def global_item(self, val: DaedalusInstance) -> None:
        DLL.ZkDaedalusVm_setGlobalItem(self._handle, val.handle)

    def push(self, val: DaedalusType) -> None:
        if isinstance(val, DaedalusInstance):
            DLL.ZkDaedalusVm_pushInstance(self._handle, val.handle)
        elif isinstance(val, bool | int):
            DLL.ZkDaedalusVm_pushInt(self._handle, c_int32(val))
        elif isinstance(val, float):
            DLL.ZkDaedalusVm_pushFloat(self._handle, c_float(val))
        elif isinstance(val, str):
            DLL.ZkDaedalusVm_pushString(self._handle, val.encode("utf-8"))
        else:
            raise ValueError("Unsupported type: " + type(val))

    def pop(self, typ: type[DaedalusTypeGeneric]) -> DaedalusTypeGeneric:
        if typ == DaedalusInstance:
            return self.pop_instance()
        elif typ == int or typ == bool:
            return self.pop_int()
        elif typ == float:
            return self.pop_float()
        elif typ == str:
            return self.pop_string()
        else:
            raise ValueError("Unsupported type: " + typ)

    def pop_int(self) -> int:
        DLL.ZkDaedalusVm_popInt.restype = c_int32
        return DLL.ZkDaedalusVm_popInt(self._handle)

    def pop_float(self) -> float:
        DLL.ZkDaedalusVm_popFloat.restype = c_float
        return DLL.ZkDaedalusVm_popFloat(self._handle)

    def pop_string(self) -> str:
        DLL.ZkDaedalusVm_popString.restype = ZkString
        return DLL.ZkDaedalusVm_popString(self._handle).value

    def pop_instance(self) -> DaedalusInstance:
        DLL.ZkDaedalusVm_popInstance.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_popInstance(self._handle).value
        return DaedalusInstance.from_native(handle)

    def alloc_instance(self, sym: DaedalusSymbol, type: DaedalusInstanceType) -> DaedalusInstance:
        DLL.ZkDaedalusVm_allocInstance.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_allocInstance(self._handle, sym.handle, type.value).value
        return DaedalusInstance.from_native(handle)

    def init_instance(self, sym: DaedalusSymbol, type: DaedalusInstanceType) -> DaedalusInstance:
        DLL.ZkDaedalusVm_initInstance.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_initInstance(self._handle, sym.handle, type.value).value
        return DaedalusInstance.from_native(handle)

    def init_instance_direct(self, sym: DaedalusInstance) -> DaedalusInstance:
        DLL.ZkDaedalusVm_initInstanceDirect.restype = ZkPointer
        handle = DLL.ZkDaedalusVm_initInstanceDirect(self._handle, sym.handle).value
        return DaedalusInstance.from_native(handle)

    def print_stack_trace(self) -> None:
        DLL.ZkDaedalusVm_printStackTrace(self._handle)

    def call(
        self, sym: DaedalusSymbol, *args: DaedalusType, rtype: type[DaedalusTypeGeneric] = None
    ) -> DaedalusTypeGeneric:
        for arg in args:
            self.push(arg)
        self._call_function(sym)

        if rtype is not None:
            return self.pop(rtype)
        return None

    def register_external(
        self, sym: DaedalusSymbol, cb: Callable[..., DaedalusType | None], *args: type[DaedalusType]
    ) -> None:
        def _fn():
            vals = [self.pop(arg) for arg in reversed(args)][::-1]
            res = cb(*vals)
            if res is not None:
                self.push(res)

        self._register_external(sym, _fn)

    def register_external_default(self, cb: Callable[[DaedalusSymbol], None]) -> None:
        def _handle(_, __, p):
            cb(DaedalusSymbol(_handle=c_void_p(p)))

        fptr = DaedalusVmExternalDefaultCallback(_handle)
        self._externals.append(fptr)
        DLL.ZkDaedalusVm_registerExternalDefault(self._handle, fptr, c_void_p(None))

    def _call_function(self, sym: DaedalusSymbol) -> None:
        DLL.ZkDaedalusVm_callFunction(self._handle, sym.handle)

    def _register_external(self, sym: DaedalusSymbol, cb: Callable[[], None]) -> None:
        fptr = DaedalusVmExternalCallback(lambda _, __: cb())
        self._externals.append(fptr)
        DLL.ZkDaedalusVm_registerExternal(self._handle, sym.handle, fptr, c_void_p(None))

    def _deleter(self) -> None:
        DLL.ZkDaedalusVm_del(self._handle)
