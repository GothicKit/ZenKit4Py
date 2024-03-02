__all__ = ["MissionInstance"]

from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class MissionInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def name(self) -> str:
        DLL.ZkMissionInstance_getName.restype = ZkString
        return DLL.ZkMissionInstance_getName(self._handle).value

    @name.setter
    def name(self, value: str) -> None:
        DLL.ZkMissionInstance_setName(self._handle, value.encode("utf-8"))

    @property
    def description(self) -> str:
        DLL.ZkMissionInstance_getDescription.restype = ZkString
        return DLL.ZkMissionInstance_getDescription(self._handle).value

    @description.setter
    def description(self, value: str) -> None:
        DLL.ZkMissionInstance_setDescription(self._handle, value.encode("utf-8"))

    @property
    def duration(self) -> int:
        DLL.ZkMissionInstance_getDuration.restype = c_int32
        return DLL.ZkMissionInstance_getDuration(self._handle)

    @duration.setter
    def duration(self, value: int) -> None:
        DLL.ZkMissionInstance_setDuration(self._handle, c_int32(value))

    @property
    def important(self) -> int:
        DLL.ZkMissionInstance_getImportant.restype = c_int32
        return DLL.ZkMissionInstance_getImportant(self._handle)

    @important.setter
    def important(self, value: int) -> None:
        DLL.ZkMissionInstance_setImportant(self._handle, c_int32(value))

    @property
    def offer_conditions(self) -> int:
        DLL.ZkMissionInstance_getOfferConditions.restype = c_int32
        return DLL.ZkMissionInstance_getOfferConditions(self._handle)

    @offer_conditions.setter
    def offer_conditions(self, value: int) -> None:
        DLL.ZkMissionInstance_setOfferConditions(self._handle, c_int32(value))

    @property
    def offer(self) -> int:
        DLL.ZkMissionInstance_getOffer.restype = c_int32
        return DLL.ZkMissionInstance_getOffer(self._handle)

    @offer.setter
    def offer(self, value: int) -> None:
        DLL.ZkMissionInstance_setOffer(self._handle, c_int32(value))

    @property
    def success_conditions(self) -> int:
        DLL.ZkMissionInstance_getSuccessConditions.restype = c_int32
        return DLL.ZkMissionInstance_getSuccessConditions(self._handle)

    @success_conditions.setter
    def success_conditions(self, value: int) -> None:
        DLL.ZkMissionInstance_setSuccessConditions(self._handle, c_int32(value))

    @property
    def success(self) -> int:
        DLL.ZkMissionInstance_getSuccess.restype = c_int32
        return DLL.ZkMissionInstance_getSuccess(self._handle)

    @success.setter
    def success(self, value: int) -> None:
        DLL.ZkMissionInstance_setSuccess(self._handle, c_int32(value))

    @property
    def failure_conditions(self) -> int:
        DLL.ZkMissionInstance_getFailureConditions.restype = c_int32
        return DLL.ZkMissionInstance_getFailureConditions(self._handle)

    @failure_conditions.setter
    def failure_conditions(self, value: int) -> None:
        DLL.ZkMissionInstance_setFailureConditions(self._handle, c_int32(value))

    @property
    def failure(self) -> int:
        DLL.ZkMissionInstance_getFailure.restype = c_int32
        return DLL.ZkMissionInstance_getFailure(self._handle)

    @failure.setter
    def failure(self, value: int) -> None:
        DLL.ZkMissionInstance_setFailure(self._handle, c_int32(value))

    @property
    def obsolete_conditions(self) -> int:
        DLL.ZkMissionInstance_getObsoleteConditions.restype = c_int32
        return DLL.ZkMissionInstance_getObsoleteConditions(self._handle)

    @obsolete_conditions.setter
    def obsolete_conditions(self, value: int) -> None:
        DLL.ZkMissionInstance_setObsoleteConditions(self._handle, c_int32(value))

    @property
    def obsolete(self) -> int:
        DLL.ZkMissionInstance_getObsolete.restype = c_int32
        return DLL.ZkMissionInstance_getObsolete(self._handle)

    @obsolete.setter
    def obsolete(self, value: int) -> None:
        DLL.ZkMissionInstance_setObsolete(self._handle, c_int32(value))

    @property
    def running(self) -> int:
        DLL.ZkMissionInstance_getRunning.restype = c_int32
        return DLL.ZkMissionInstance_getRunning(self._handle)

    @running.setter
    def running(self, value: int) -> None:
        DLL.ZkMissionInstance_setRunning(self._handle, c_int32(value))
