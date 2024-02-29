__all__ = [
    "CutsceneCamera",
    "CameraMotion",
    "CameraLerpType",
    "CameraLoopType",
    "CameraTrajectory",
    "CameraTrajectoryFrame",
]

from ctypes import c_bool
from ctypes import c_float
from ctypes import c_int
from ctypes import c_int32
from ctypes import c_size_t
from enum import IntEnum

from zenkit._core import DLL
from zenkit._core import Mat4x4
from zenkit._native import ZkPointer
from zenkit._native import ZkString
from zenkit.vob.virtual_object import VirtualObject


class CameraTrajectory(IntEnum):
    WORLD = 0
    OBJECT = 1


class CameraLoopType(IntEnum):
    NONE = 0
    RESTART = 1
    PINGPONG = 2


class CameraLerpType(IntEnum):
    UNDEFINED = 0
    PATH = 1
    PATH_IGNORE_ROLL = 2
    PATH_ROTATION_SAMPLES = 3


class CameraMotion(IntEnum):
    UNDEFINED = 0
    SMOOTH = 1
    LINEAR = 2
    STEP = 3
    SLOW = 4
    FAST = 5
    CUSTOM = 6


DLL.ZkCameraTrajectoryFrame_getTime.restype = c_float
DLL.ZkCameraTrajectoryFrame_getRollAngle.restype = c_float
DLL.ZkCameraTrajectoryFrame_getFovScale.restype = c_float
DLL.ZkCameraTrajectoryFrame_getMotionType.restype = c_int
DLL.ZkCameraTrajectoryFrame_getMotionTypeFov.restype = c_int
DLL.ZkCameraTrajectoryFrame_getMotionTypeRoll.restype = c_int
DLL.ZkCameraTrajectoryFrame_getMotionTypeTimeScale.restype = c_int
DLL.ZkCameraTrajectoryFrame_getTension.restype = c_float
DLL.ZkCameraTrajectoryFrame_getCamBias.restype = c_float
DLL.ZkCameraTrajectoryFrame_getContinuity.restype = c_float
DLL.ZkCameraTrajectoryFrame_getTimeScale.restype = c_float
DLL.ZkCameraTrajectoryFrame_getTimeFixed.restype = c_bool
DLL.ZkCameraTrajectoryFrame_getOriginalPose.restype = Mat4x4


class CameraTrajectoryFrame(VirtualObject):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def time(self) -> float:
        return DLL.ZkCameraTrajectoryFrame_getTime(self._handle)

    @time.setter
    def time(self, value: float) -> None:
        DLL.ZkCameraTrajectoryFrame_setTime(self._handle, c_float(value))

    @property
    def roll_angle(self) -> float:
        return DLL.ZkCameraTrajectoryFrame_getRollAngle(self._handle)

    @roll_angle.setter
    def roll_angle(self, value: float) -> None:
        DLL.ZkCameraTrajectoryFrame_setRollAngle(self._handle, c_float(value))

    @property
    def fov_scale(self) -> float:
        return DLL.ZkCameraTrajectoryFrame_getFovScale(self._handle)

    @fov_scale.setter
    def fov_scale(self, value: float) -> None:
        DLL.ZkCameraTrajectoryFrame_setFovScale(self._handle, c_float(value))

    @property
    def motion_type(self) -> CameraMotion:
        return CameraMotion(DLL.ZkCameraTrajectoryFrame_getMotionType(self._handle))

    @motion_type.setter
    def motion_type(self, value: CameraMotion) -> None:
        DLL.ZkCameraTrajectoryFrame_setMotionType(self._handle, value.value)

    @property
    def motion_type_fov(self) -> CameraMotion:
        return CameraMotion(DLL.ZkCameraTrajectoryFrame_getMotionTypeFov(self._handle))

    @motion_type_fov.setter
    def motion_type_fov(self, value: CameraMotion) -> None:
        DLL.ZkCameraTrajectoryFrame_setMotionTypeFov(self._handle, value.value)

    @property
    def motion_type_roll(self) -> CameraMotion:
        return CameraMotion(DLL.ZkCameraTrajectoryFrame_getMotionTypeRoll(self._handle))

    @motion_type_roll.setter
    def motion_type_roll(self, value: CameraMotion) -> None:
        DLL.ZkCameraTrajectoryFrame_setMotionTypeRoll(self._handle, value.value)

    @property
    def motion_type_time_scale(self) -> CameraMotion:
        return CameraMotion(DLL.ZkCameraTrajectoryFrame_getMotionTypeTimeScale(self._handle))

    @motion_type_time_scale.setter
    def motion_type_time_scale(self, value: CameraMotion) -> None:
        DLL.ZkCameraTrajectoryFrame_setMotionTypeTimeScale(self._handle, value.value)

    @property
    def tension(self) -> float:
        return DLL.ZkCameraTrajectoryFrame_getTension(self._handle)

    @tension.setter
    def tension(self, value: float) -> None:
        DLL.ZkCameraTrajectoryFrame_setTension(self._handle, c_float(value))

    @property
    def cam_bias(self) -> float:
        return DLL.ZkCameraTrajectoryFrame_getCamBias(self._handle)

    @cam_bias.setter
    def cam_bias(self, value: float) -> None:
        DLL.ZkCameraTrajectoryFrame_setCamBias(self._handle, c_float(value))

    @property
    def continuity(self) -> float:
        return DLL.ZkCameraTrajectoryFrame_getContinuity(self._handle)

    @continuity.setter
    def continuity(self, value: float) -> None:
        DLL.ZkCameraTrajectoryFrame_setContinuity(self._handle, c_float(value))

    @property
    def time_scale(self) -> float:
        return DLL.ZkCameraTrajectoryFrame_getTimeScale(self._handle)

    @time_scale.setter
    def time_scale(self, value: float) -> None:
        DLL.ZkCameraTrajectoryFrame_setTimeScale(self._handle, c_float(value))

    @property
    def time_fixed(self) -> bool:
        return DLL.ZkCameraTrajectoryFrame_getTimeFixed(self._handle)

    @time_fixed.setter
    def time_fixed(self, value: bool) -> None:
        DLL.ZkCameraTrajectoryFrame_setTimeFixed(self._handle, c_bool(value))

    @property
    def original_pose(self) -> Mat4x4:
        return DLL.ZkCameraTrajectoryFrame_getOriginalPose(self._handle)

    @original_pose.setter
    def original_pose(self, value: Mat4x4) -> None:
        DLL.ZkCameraTrajectoryFrame_setOriginalPose(self._handle, Mat4x4(value))


DLL.ZkCutsceneCamera_getTrajectoryFOR.restype = c_int
DLL.ZkCutsceneCamera_getTargetTrajectoryFOR.restype = c_int
DLL.ZkCutsceneCamera_getLoopMode.restype = c_int
DLL.ZkCutsceneCamera_getLerpMode.restype = c_int
DLL.ZkCutsceneCamera_getIgnoreFORVobRotation.restype = c_bool
DLL.ZkCutsceneCamera_getIgnoreFORVobRotationTarget.restype = c_bool
DLL.ZkCutsceneCamera_getAdapt.restype = c_bool
DLL.ZkCutsceneCamera_getEaseFirst.restype = c_bool
DLL.ZkCutsceneCamera_getEaseLast.restype = c_bool
DLL.ZkCutsceneCamera_getTotalDuration.restype = c_float
DLL.ZkCutsceneCamera_getAutoFocusVob.restype = ZkString
DLL.ZkCutsceneCamera_getAutoPlayerMovable.restype = c_bool
DLL.ZkCutsceneCamera_getAutoUntriggerLast.restype = c_bool
DLL.ZkCutsceneCamera_getAutoUntriggerLastDelay.restype = c_float
DLL.ZkCutsceneCamera_getPositionCount.restype = c_int32
DLL.ZkCutsceneCamera_getTargetCount.restype = c_int32
DLL.ZkCutsceneCamera_getIsPaused.restype = c_bool
DLL.ZkCutsceneCamera_getIsStarted.restype = c_bool
DLL.ZkCutsceneCamera_getGotoTimeMode.restype = c_bool
DLL.ZkCutsceneCamera_getTime.restype = c_float
DLL.ZkCutsceneCamera_getFrameCount.restype = c_size_t
DLL.ZkCutsceneCamera_getFrame.restype = ZkPointer


class CutsceneCamera(VirtualObject):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def trajectory_for(self) -> CameraTrajectory:
        return CameraTrajectory(DLL.ZkCutsceneCamera_getTrajectoryFOR(self._handle))

    @trajectory_for.setter
    def trajectory_for(self, value: CameraTrajectory) -> None:
        DLL.ZkCutsceneCamera_setTrajectoryFOR(self._handle, value.value)

    @property
    def target_trajectory_for(self) -> CameraTrajectory:
        return CameraTrajectory(DLL.ZkCutsceneCamera_getTargetTrajectoryFOR(self._handle))

    @target_trajectory_for.setter
    def target_trajectory_for(self, value: CameraTrajectory) -> None:
        DLL.ZkCutsceneCamera_setTargetTrajectoryFOR(self._handle, value.value)

    @property
    def loop_mode(self) -> CameraLoopType:
        return CameraLoopType(DLL.ZkCutsceneCamera_getLoopMode(self._handle))

    @loop_mode.setter
    def loop_mode(self, value: CameraLoopType) -> None:
        DLL.ZkCutsceneCamera_setLoopMode(self._handle, value.value)

    @property
    def lerp_mode(self) -> CameraLerpType:
        return CameraLerpType(DLL.ZkCutsceneCamera_getLerpMode(self._handle))

    @lerp_mode.setter
    def lerp_mode(self, value: CameraLerpType) -> None:
        DLL.ZkCutsceneCamera_setLerpMode(self._handle, value.value)

    @property
    def ignore_for_vob_rotation(self) -> bool:
        return DLL.ZkCutsceneCamera_getIgnoreFORVobRotation(self._handle)

    @ignore_for_vob_rotation.setter
    def ignore_for_vob_rotation(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setIgnoreFORVobRotation(self._handle, c_bool(value))

    @property
    def ignore_for_vob_rotation_target(self) -> bool:
        return DLL.ZkCutsceneCamera_getIgnoreFORVobRotationTarget(self._handle)

    @ignore_for_vob_rotation_target.setter
    def ignore_for_vob_rotation_target(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setIgnoreFORVobRotationTarget(self._handle, c_bool(value))

    @property
    def adapt(self) -> bool:
        return DLL.ZkCutsceneCamera_getAdapt(self._handle)

    @adapt.setter
    def adapt(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setAdapt(self._handle, c_bool(value))

    @property
    def ease_first(self) -> bool:
        return DLL.ZkCutsceneCamera_getEaseFirst(self._handle)

    @ease_first.setter
    def ease_first(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setEaseFirst(self._handle, c_bool(value))

    @property
    def ease_last(self) -> bool:
        return DLL.ZkCutsceneCamera_getEaseLast(self._handle)

    @ease_last.setter
    def ease_last(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setEaseLast(self._handle, c_bool(value))

    @property
    def total_duration(self) -> float:
        return DLL.ZkCutsceneCamera_getTotalDuration(self._handle)

    @total_duration.setter
    def total_duration(self, value: float) -> None:
        DLL.ZkCutsceneCamera_setTotalDuration(self._handle, c_float(value))

    @property
    def auto_focus_vob(self) -> str:
        return DLL.ZkCutsceneCamera_getAutoFocusVob(self._handle).value

    @auto_focus_vob.setter
    def auto_focus_vob(self, value: str) -> None:
        DLL.ZkCutsceneCamera_setAutoFocusVob(self._handle, value.encode("utf-8"))

    @property
    def auto_player_movable(self) -> bool:
        return DLL.ZkCutsceneCamera_getAutoPlayerMovable(self._handle)

    @auto_player_movable.setter
    def auto_player_movable(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setAutoPlayerMovable(self._handle, c_bool(value))

    @property
    def auto_untrigger_last(self) -> bool:
        return DLL.ZkCutsceneCamera_getAutoUntriggerLast(self._handle)

    @auto_untrigger_last.setter
    def auto_untrigger_last(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setAutoUntriggerLast(self._handle, c_bool(value))

    @property
    def auto_untrigger_last_delay(self) -> float:
        return DLL.ZkCutsceneCamera_getAutoUntriggerLastDelay(self._handle)

    @auto_untrigger_last_delay.setter
    def auto_untrigger_last_delay(self, value: float) -> None:
        DLL.ZkCutsceneCamera_setAutoUntriggerLastDelay(self._handle, c_float(value))

    @property
    def position_count(self) -> int:
        return DLL.ZkCutsceneCamera_getPositionCount(self._handle)

    @property
    def target_count(self) -> int:
        return DLL.ZkCutsceneCamera_getTargetCount(self._handle)

    @property
    def is_paused(self) -> bool:
        return DLL.ZkCutsceneCamera_getIsPaused(self._handle)

    @is_paused.setter
    def is_paused(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setIsPaused(self._handle, c_bool(value))

    @property
    def is_started(self) -> bool:
        return DLL.ZkCutsceneCamera_getIsStarted(self._handle)

    @is_started.setter
    def is_started(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setIsStarted(self._handle, c_bool(value))

    @property
    def goto_time_mode(self) -> bool:
        return DLL.ZkCutsceneCamera_getGotoTimeMode(self._handle)

    @goto_time_mode.setter
    def goto_time_mode(self, value: bool) -> None:
        DLL.ZkCutsceneCamera_setGotoTimeMode(self._handle, c_bool(value))

    @property
    def time(self) -> float:
        return DLL.ZkCutsceneCamera_getTime(self._handle)

    @time.setter
    def time(self, value: float) -> None:
        DLL.ZkCutsceneCamera_setTime(self._handle, c_float(value))

    @property
    def frames(self) -> list[CameraTrajectoryFrame]:
        count = DLL.ZkCutsceneCamera_getFrameCount(self._handle)
        items = []

        for i in range(count):
            handle = DLL.ZkCutsceneCamera_getFrame(self._handle, i).value
            items.append(CameraTrajectoryFrame(_handle=DLL.ZkObject_takeRef(handle), delete=True))

        return items
