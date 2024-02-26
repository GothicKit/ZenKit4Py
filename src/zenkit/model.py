__all__ = [
    "Model",
]

from ctypes import c_void_p
from os import PathLike

from zenkit import Read, VfsNode, ModelMesh, ModelHierarchy
from zenkit._core import DLL


class Model:
    __slots__ = ("_handle",)


    def __init__(
            self, src: str | PathLike | Read | bytes | bytearray | VfsNode
    ) -> None:
        if src is None:
            raise ValueError("No source provided")

        rd: Read
        if isinstance(src, VfsNode):
            rd = src.open()
        elif isinstance(src, Read):
            rd = src
        else:
            rd = Read(src)

        DLL.ZkModel_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkModel_load(rd.handle))

    @property
    def mesh(self) -> ModelMesh:
        DLL.ZkModel_getMesh.restype = c_void_p
        return ModelMesh(_handle=c_void_p(DLL.ZkModel_getMesh(self._handle)))

    @property
    def hierarchy(self) -> ModelHierarchy:
        DLL.ZkModel_getHierarchy.restype = c_void_p
        return ModelHierarchy(_handle=c_void_p(DLL.ZkModel_getHierarchy(self._handle)))

    def __del__(self) -> None:
        DLL.ZkModel_del(self._handle)
        self._handle = None
