__all__ = ["ModelMesh"]

from ctypes import CFUNCTYPE
from ctypes import c_bool
from ctypes import c_size_t
from ctypes import c_uint
from ctypes import c_void_p
from typing import Any

from zenkit import _native
from zenkit._core import DLL
from zenkit._core import PathOrFileLike
from zenkit._native import ZkPointer
from zenkit._native import ZkString
from zenkit.multi_resolution_mesh import MultiResolutionMesh
from zenkit.soft_skin_mesh import SoftSkinMesh

_ModelMeshAttachmentEnumerator = CFUNCTYPE(c_bool, c_void_p, ZkString, ZkPointer)

DLL.ZkModelMesh_getChecksum.restype = c_uint
DLL.ZkModelMesh_getMeshCount.restype = c_size_t
DLL.ZkModelMesh_getMesh.restype = ZkPointer


class ModelMesh:
    __slots__ = ("_handle", "_delete", "_keepalive")

    def __init__(self, **kwargs: Any) -> None:
        self._handle = c_void_p(None)

        if "_handle" in kwargs:
            self._handle: c_void_p = kwargs.pop("_handle")
            self._delete: bool = kwargs.pop("_delete", False)
            self._keepalive = kwargs.pop("_keepalive", DLL)

    @staticmethod
    def load(path_or_file_like: PathOrFileLike) -> "ModelMesh":
        handle = _native.load("ZkModelMesh_load", path_or_file_like)
        return ModelMesh(_handle=handle, _delete=True)

    @property
    def checksum(self) -> int:
        return DLL.ZkModelMesh_getChecksum(self._handle)

    @property
    def meshes(self) -> list[SoftSkinMesh]:
        count = DLL.ZkModelMesh_getMeshCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkModelMesh_getMesh(self._handle, i).value
            items.append(SoftSkinMesh(_handle=handle, _keepalive=self))

        return items

    @property
    def attachments(self) -> dict[str, MultiResolutionMesh]:
        def _enumerate(_ctx: int, name: ZkString, ptr: ZkPointer) -> bool:
            attachments[name.value] = MultiResolutionMesh(_handle=ptr.value, _keepalive=self)
            return False

        attachments = {}
        enumerator = _ModelMeshAttachmentEnumerator(_enumerate)

        DLL.ZkModelMesh_enumerateAttachments(self._handle, enumerator, c_void_p(None))
        return attachments

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkModelMesh_del(self._handle)
        self._handle = None
        self._keepalive = None

    def __repr__(self) -> str:
        return f"<ModelMesh handle={self._handle}>"
