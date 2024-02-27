__all__ = [
    "Model",
]

from ctypes import c_void_p
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._native import ZkPointer
from zenkit.mdh import ModelHierarchy
from zenkit.mdm import ModelMesh

DLL.ZkModel_getMesh.restype = ZkPointer
DLL.ZkModel_getHierarchy.restype = ZkPointer


class Model:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "Model":
        handle = _native.load("ZkModel_load", path_or_file_like)
        return Model(_handle=handle, _delete=True)

    @property
    def mesh(self) -> ModelMesh:
        return ModelMesh(_handle=DLL.ZkModel_getMesh(self._handle).value, _keepalive=self)

    @property
    def hierarchy(self) -> ModelHierarchy:
        return ModelHierarchy(_handle=DLL.ZkModel_getHierarchy(self._handle).value, _keepalive=self)

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkModel_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<Model handle={self._handle}>"
