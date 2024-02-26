__all__ = ["ModelMesh"]

from ctypes import c_void_p, c_size_t, CFUNCTYPE, c_bool, c_char_p, c_uint
from os import PathLike
from typing import Any

from zenkit import Read, VfsNode, MultiResolutionMesh
from zenkit._core import DLL
from zenkit.softskin import SoftSkinMesh

_ModelMeshAttachmentEnumerator = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)


class ModelMesh:
    __slots__ = ("_handle", "_delete")

    def __init__(
        self, src: str | PathLike | Read | bytes | bytearray | VfsNode = None,
        **kwargs: Any
    ) -> None:
        if "_handle" in kwargs:
            self._handle = kwargs.pop("_handle")
            self._delete = False
            return

        if src is None:
            raise ValueError("No source provided")

        rd: Read
        if isinstance(src, VfsNode):
            rd = src.open()
        elif isinstance(src, Read):
            rd = src
        else:
            rd = Read(src)

        DLL.ZkModelMesh_load.restype = c_void_p
        self._handle = c_void_p(DLL.ZkModelMesh_load(rd.handle))
        self._delete = True

    @property
    def checksum(self) -> int:
        DLL.ZkModelMesh_getChecksum.restype = c_uint
        return DLL.ZkModelMesh_getChecksum(self._handle)

    @property
    def meshes(self) -> list[SoftSkinMesh]:
        DLL.ZkModelMesh_getMeshCount.restype = c_size_t
        count = DLL.ZkModelMesh_getMeshCount(self._handle)

        DLL.ZkModelMesh_getMesh.restype = c_void_p
        return [
            SoftSkinMesh(_handle=c_void_p(DLL.ZkModelMesh_getMesh(self._handle, i)))
            for i in range(count)
        ]

    @property
    def attachments(self) -> dict[str, MultiResolutionMesh]:
        attachments = {}

        def _enumerate(_, name, ptr):
            attachments[name.decode("utf-8")] = MultiResolutionMesh(_handle=c_void_p(ptr))
            return False
        enum = _ModelMeshAttachmentEnumerator(_enumerate)

        DLL.ZkModelMesh_enumerateAttachments.restype = None
        DLL.ZkModelMesh_enumerateAttachments(self._handle, enum, c_void_p(None))

        return attachments

    def __del__(self) -> None:
        if self._delete:
            DLL.ZkModelMesh_del(self._handle)
            self._handle = None
