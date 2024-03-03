__all__ = ["GuildValuesInstance"]

from ctypes import c_int32
from ctypes import c_size_t
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class GuildValuesInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def get_water_depth_knee(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getWaterDepthKnee.restype = c_int32
        return DLL.ZkGuildValuesInstance_getWaterDepthKnee(self._handle, c_size_t(i))

    def get_water_depth_chest(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getWaterDepthChest.restype = c_int32
        return DLL.ZkGuildValuesInstance_getWaterDepthChest(self._handle, c_size_t(i))

    def get_jump_up_height(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getJumpUpHeight.restype = c_int32
        return DLL.ZkGuildValuesInstance_getJumpUpHeight(self._handle, c_size_t(i))

    def get_swim_time(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getSwimTime.restype = c_int32
        return DLL.ZkGuildValuesInstance_getSwimTime(self._handle, c_size_t(i))

    def get_dive_time(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getDiveTime.restype = c_int32
        return DLL.ZkGuildValuesInstance_getDiveTime(self._handle, c_size_t(i))

    def get_step_height(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getStepHeight.restype = c_int32
        return DLL.ZkGuildValuesInstance_getStepHeight(self._handle, c_size_t(i))

    def get_jump_low_height(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getJumpLowHeight.restype = c_int32
        return DLL.ZkGuildValuesInstance_getJumpLowHeight(self._handle, c_size_t(i))

    def get_jump_mid_height(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getJumpMidHeight.restype = c_int32
        return DLL.ZkGuildValuesInstance_getJumpMidHeight(self._handle, c_size_t(i))

    def get_slide_angle(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getSlideAngle.restype = c_int32
        return DLL.ZkGuildValuesInstance_getSlideAngle(self._handle, c_size_t(i))

    def get_slide_angle_2(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getSlideAngle2.restype = c_int32
        return DLL.ZkGuildValuesInstance_getSlideAngle2(self._handle, c_size_t(i))

    def get_disable_auto_roll(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getDisableAutoRoll.restype = c_int32
        return DLL.ZkGuildValuesInstance_getDisableAutoRoll(self._handle, c_size_t(i))

    def get_surface_align(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getSurfaceAlign.restype = c_int32
        return DLL.ZkGuildValuesInstance_getSurfaceAlign(self._handle, c_size_t(i))

    def get_climb_heading_angle(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getClimbHeadingAngle.restype = c_int32
        return DLL.ZkGuildValuesInstance_getClimbHeadingAngle(self._handle, c_size_t(i))

    def get_climb_horiz_angle(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getClimbHorizAngle.restype = c_int32
        return DLL.ZkGuildValuesInstance_getClimbHorizAngle(self._handle, c_size_t(i))

    def get_climb_ground_angle(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getClimbGroundAngle.restype = c_int32
        return DLL.ZkGuildValuesInstance_getClimbGroundAngle(self._handle, c_size_t(i))

    def get_fight_range_base(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFightRangeBase.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFightRangeBase(self._handle, c_size_t(i))

    def get_fight_range_fist(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFightRangeFist.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFightRangeFist(self._handle, c_size_t(i))

    def get_fight_range_g(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFightRangeG.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFightRangeG(self._handle, c_size_t(i))

    def get_fight_range_1_hs(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFightRange1Hs.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFightRange1Hs(self._handle, c_size_t(i))

    def get_fight_range_1_ha(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFightRange1Ha.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFightRange1Ha(self._handle, c_size_t(i))

    def get_fight_range_2_hs(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFightRange2Hs.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFightRange2Hs(self._handle, c_size_t(i))

    def get_fight_range_2_ha(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFightRange2Ha.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFightRange2Ha(self._handle, c_size_t(i))

    def get_fall_down_height(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFallDownHeight.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFallDownHeight(self._handle, c_size_t(i))

    def get_fall_down_damage(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getFallDownDamage.restype = c_int32
        return DLL.ZkGuildValuesInstance_getFallDownDamage(self._handle, c_size_t(i))

    def get_blood_disabled(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getBloodDisabled.restype = c_int32
        return DLL.ZkGuildValuesInstance_getBloodDisabled(self._handle, c_size_t(i))

    def get_blood_max_distance(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getBloodMaxDistance.restype = c_int32
        return DLL.ZkGuildValuesInstance_getBloodMaxDistance(self._handle, c_size_t(i))

    def get_blood_amount(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getBloodAmount.restype = c_int32
        return DLL.ZkGuildValuesInstance_getBloodAmount(self._handle, c_size_t(i))

    def get_blood_flow(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getBloodFlow.restype = c_int32
        return DLL.ZkGuildValuesInstance_getBloodFlow(self._handle, c_size_t(i))

    def get_turn_speed(self, i: int) -> int:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getTurnSpeed.restype = c_int32
        return DLL.ZkGuildValuesInstance_getTurnSpeed(self._handle, c_size_t(i))

    def get_blood_emitter(self, i: int) -> str:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getBloodEmitter.restype = ZkString
        return DLL.ZkGuildValuesInstance_getBloodEmitter(self._handle, i).value

    def get_blood_texture(self, i: int) -> str:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_getBloodTexture.restype = ZkString
        return DLL.ZkGuildValuesInstance_getBloodTexture(self._handle, i).value

    def set_water_depth_knee(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setWaterDepthKnee(self._handle, i, c_int32(val))

    def set_water_depth_chest(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setWaterDepthChest(self._handle, i, c_int32(val))

    def set_jump_up_height(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setJumpUpHeight(self._handle, i, c_int32(val))

    def set_swim_time(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setSwimTime(self._handle, i, c_int32(val))

    def set_dive_time(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setDiveTime(self._handle, i, c_int32(val))

    def set_step_height(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setStepHeight(self._handle, i, c_int32(val))

    def set_jump_low_height(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setJumpLowHeight(self._handle, i, c_int32(val))

    def set_jump_mid_height(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setJumpMidHeight(self._handle, i, c_int32(val))

    def set_slide_angle(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setSlideAngle(self._handle, i, c_int32(val))

    def set_slide_angle_2(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setSlideAngle2(self._handle, i, c_int32(val))

    def set_disable_auto_roll(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setDisableAutoRoll(self._handle, i, c_int32(val))

    def set_surface_align(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setSurfaceAlign(self._handle, i, c_int32(val))

    def set_climb_heading_angle(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setClimbHeadingAngle(self._handle, i, c_int32(val))

    def set_climb_horiz_angle(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setClimbHorizAngle(self._handle, i, c_int32(val))

    def set_climb_ground_angle(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setClimbGroundAngle(self._handle, i, c_int32(val))

    def set_fight_range_base(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFightRangeBase(self._handle, i, c_int32(val))

    def set_fight_range_fist(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFightRangeFist(self._handle, i, c_int32(val))

    def set_fight_range_g(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFightRangeG(self._handle, i, c_int32(val))

    def set_fight_range_1_hs(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFightRange1Hs(self._handle, i, c_int32(val))

    def set_fight_range_1_ha(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFightRange1Ha(self._handle, i, c_int32(val))

    def set_fight_range_2_hs(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFightRange2Hs(self._handle, i, c_int32(val))

    def set_fight_range_2_ha(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFightRange2Ha(self._handle, i, c_int32(val))

    def set_fall_down_height(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFallDownHeight(self._handle, i, c_int32(val))

    def set_fall_down_damage(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setFallDownDamage(self._handle, i, c_int32(val))

    def set_blood_disabled(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setBloodDisabled(self._handle, i, c_int32(val))

    def set_blood_max_distance(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setBloodMaxDistance(self._handle, i, c_int32(val))

    def set_blood_amount(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setBloodAmount(self._handle, i, c_int32(val))

    def set_blood_flow(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setBloodFlow(self._handle, i, c_int32(val))

    def set_turn_speed(self, i: int, val: int) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setTurnSpeed(self._handle, i, c_int32(val))

    def set_blood_emitter(self, i: int, val: str) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setBloodEmitter(self._handle, i, val.encode("utf-8"))

    def set_blood_texture(self, i: int, val: str) -> None:
        if i < 0 or i >= 66:
            raise IndexError(i)
        DLL.ZkGuildValuesInstance_setBloodTexture(self._handle, i, val.encode("utf-8"))
