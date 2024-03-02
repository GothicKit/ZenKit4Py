__all__ = [
    "CameraInstance",
]

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit.daedalus.base import DaedalusInstance


class CameraInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def best_range(self) -> float:
        DLL.ZkCameraInstance_getBestRange.restype = c_float
        return DLL.ZkCameraInstance_getBestRange(self._handle)

    @best_range.setter
    def best_range(self, value: float) -> None:
        DLL.ZkCameraInstance_setBestRange(self._handle, c_float(value))

    @property
    def min_range(self) -> float:
        DLL.ZkCameraInstance_getMinRange.restype = c_float
        return DLL.ZkCameraInstance_getMinRange(self._handle)

    @min_range.setter
    def min_range(self, value: float) -> None:
        DLL.ZkCameraInstance_setMinRange(self._handle, c_float(value))

    @property
    def max_range(self) -> float:
        DLL.ZkCameraInstance_getMaxRange.restype = c_float
        return DLL.ZkCameraInstance_getMaxRange(self._handle)

    @max_range.setter
    def max_range(self, value: float) -> None:
        DLL.ZkCameraInstance_setMaxRange(self._handle, c_float(value))

    @property
    def best_elevation(self) -> float:
        DLL.ZkCameraInstance_getBestElevation.restype = c_float
        return DLL.ZkCameraInstance_getBestElevation(self._handle)

    @best_elevation.setter
    def best_elevation(self, value: float) -> None:
        DLL.ZkCameraInstance_setBestElevation(self._handle, c_float(value))

    @property
    def min_elevation(self) -> float:
        DLL.ZkCameraInstance_getMinElevation.restype = c_float
        return DLL.ZkCameraInstance_getMinElevation(self._handle)

    @min_elevation.setter
    def min_elevation(self, value: float) -> None:
        DLL.ZkCameraInstance_setMinElevation(self._handle, c_float(value))

    @property
    def max_elevation(self) -> float:
        DLL.ZkCameraInstance_getMaxElevation.restype = c_float
        return DLL.ZkCameraInstance_getMaxElevation(self._handle)

    @max_elevation.setter
    def max_elevation(self, value: float) -> None:
        DLL.ZkCameraInstance_setMaxElevation(self._handle, c_float(value))

    @property
    def best_azimuth(self) -> float:
        DLL.ZkCameraInstance_getBestAzimuth.restype = c_float
        return DLL.ZkCameraInstance_getBestAzimuth(self._handle)

    @best_azimuth.setter
    def best_azimuth(self, value: float) -> None:
        DLL.ZkCameraInstance_setBestAzimuth(self._handle, c_float(value))

    @property
    def min_azimuth(self) -> float:
        DLL.ZkCameraInstance_getMinAzimuth.restype = c_float
        return DLL.ZkCameraInstance_getMinAzimuth(self._handle)

    @min_azimuth.setter
    def min_azimuth(self, value: float) -> None:
        DLL.ZkCameraInstance_setMinAzimuth(self._handle, c_float(value))

    @property
    def max_azimuth(self) -> float:
        DLL.ZkCameraInstance_getMaxAzimuth.restype = c_float
        return DLL.ZkCameraInstance_getMaxAzimuth(self._handle)

    @max_azimuth.setter
    def max_azimuth(self, value: float) -> None:
        DLL.ZkCameraInstance_setMaxAzimuth(self._handle, c_float(value))

    @property
    def best_rot_z(self) -> float:
        DLL.ZkCameraInstance_getBestRotZ.restype = c_float
        return DLL.ZkCameraInstance_getBestRotZ(self._handle)

    @best_rot_z.setter
    def best_rot_z(self, value: float) -> None:
        DLL.ZkCameraInstance_setBestRotZ(self._handle, c_float(value))

    @property
    def min_rot_z(self) -> float:
        DLL.ZkCameraInstance_getMinRotZ.restype = c_float
        return DLL.ZkCameraInstance_getMinRotZ(self._handle)

    @min_rot_z.setter
    def min_rot_z(self, value: float) -> None:
        DLL.ZkCameraInstance_setMinRotZ(self._handle, c_float(value))

    @property
    def max_rot_z(self) -> float:
        DLL.ZkCameraInstance_getMaxRotZ.restype = c_float
        return DLL.ZkCameraInstance_getMaxRotZ(self._handle)

    @max_rot_z.setter
    def max_rot_z(self, value: float) -> None:
        DLL.ZkCameraInstance_setMaxRotZ(self._handle, c_float(value))

    @property
    def rot_offset_x(self) -> float:
        DLL.ZkCameraInstance_getRotOffsetX.restype = c_float
        return DLL.ZkCameraInstance_getRotOffsetX(self._handle)

    @rot_offset_x.setter
    def rot_offset_x(self, value: float) -> None:
        DLL.ZkCameraInstance_setRotOffsetX(self._handle, c_float(value))

    @property
    def rot_offset_y(self) -> float:
        DLL.ZkCameraInstance_getRotOffsetY.restype = c_float
        return DLL.ZkCameraInstance_getRotOffsetY(self._handle)

    @rot_offset_y.setter
    def rot_offset_y(self, value: float) -> None:
        DLL.ZkCameraInstance_setRotOffsetY(self._handle, c_float(value))

    @property
    def rot_offset_z(self) -> float:
        DLL.ZkCameraInstance_getRotOffsetZ.restype = c_float
        return DLL.ZkCameraInstance_getRotOffsetZ(self._handle)

    @rot_offset_z.setter
    def rot_offset_z(self, value: float) -> None:
        DLL.ZkCameraInstance_setRotOffsetZ(self._handle, c_float(value))

    @property
    def target_offset_x(self) -> float:
        DLL.ZkCameraInstance_getTargetOffsetX.restype = c_float
        return DLL.ZkCameraInstance_getTargetOffsetX(self._handle)

    @target_offset_x.setter
    def target_offset_x(self, value: float) -> None:
        DLL.ZkCameraInstance_setTargetOffsetX(self._handle, c_float(value))

    @property
    def target_offset_y(self) -> float:
        DLL.ZkCameraInstance_getTargetOffsetY.restype = c_float
        return DLL.ZkCameraInstance_getTargetOffsetY(self._handle)

    @target_offset_y.setter
    def target_offset_y(self, value: float) -> None:
        DLL.ZkCameraInstance_setTargetOffsetY(self._handle, c_float(value))

    @property
    def target_offset_z(self) -> float:
        DLL.ZkCameraInstance_getTargetOffsetZ.restype = c_float
        return DLL.ZkCameraInstance_getTargetOffsetZ(self._handle)

    @target_offset_z.setter
    def target_offset_z(self, value: float) -> None:
        DLL.ZkCameraInstance_setTargetOffsetZ(self._handle, c_float(value))

    @property
    def velo_trans(self) -> float:
        DLL.ZkCameraInstance_getVeloTrans.restype = c_float
        return DLL.ZkCameraInstance_getVeloTrans(self._handle)

    @velo_trans.setter
    def velo_trans(self, value: float) -> None:
        DLL.ZkCameraInstance_setVeloTrans(self._handle, c_float(value))

    @property
    def velo_rot(self) -> float:
        DLL.ZkCameraInstance_getVeloRot.restype = c_float
        return DLL.ZkCameraInstance_getVeloRot(self._handle)

    @velo_rot.setter
    def velo_rot(self, value: float) -> None:
        DLL.ZkCameraInstance_setVeloRot(self._handle, c_float(value))

    @property
    def translate(self) -> int:
        DLL.ZkCameraInstance_getTranslate.restype = c_int32
        return DLL.ZkCameraInstance_getTranslate(self._handle)

    @translate.setter
    def translate(self, value: int) -> None:
        DLL.ZkCameraInstance_setTranslate(self._handle, c_int32(value))

    @property
    def rotate(self) -> int:
        DLL.ZkCameraInstance_getRotate.restype = c_int32
        return DLL.ZkCameraInstance_getRotate(self._handle)

    @rotate.setter
    def rotate(self, value: int) -> None:
        DLL.ZkCameraInstance_setRotate(self._handle, c_int32(value))

    @property
    def collision(self) -> int:
        DLL.ZkCameraInstance_getCollision.restype = c_int32
        return DLL.ZkCameraInstance_getCollision(self._handle)

    @collision.setter
    def collision(self, value: int) -> None:
        DLL.ZkCameraInstance_setCollision(self._handle, c_int32(value))
