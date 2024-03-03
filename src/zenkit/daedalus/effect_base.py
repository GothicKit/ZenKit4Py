__all__ = ["EffectBaseInstance"]

from ctypes import c_float
from ctypes import c_int32
from ctypes import c_size_t
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class EffectBaseInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def vis_name_s(self) -> str:
        DLL.ZkEffectBaseInstance_getVisNameS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getVisNameS(self._handle).value

    @vis_name_s.setter
    def vis_name_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setVisNameS(self._handle, value.encode("utf-8"))

    @property
    def vis_size_s(self) -> str:
        DLL.ZkEffectBaseInstance_getVisSizeS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getVisSizeS(self._handle).value

    @vis_size_s.setter
    def vis_size_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setVisSizeS(self._handle, value.encode("utf-8"))

    @property
    def vis_alpha(self) -> float:
        DLL.ZkEffectBaseInstance_getVisAlpha.restype = c_float
        return DLL.ZkEffectBaseInstance_getVisAlpha(self._handle)

    @vis_alpha.setter
    def vis_alpha(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setVisAlpha(self._handle, c_float(value))

    @property
    def vis_alpha_blend_func_s(self) -> str:
        DLL.ZkEffectBaseInstance_getVisAlphaBlendFuncS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getVisAlphaBlendFuncS(self._handle).value

    @vis_alpha_blend_func_s.setter
    def vis_alpha_blend_func_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setVisAlphaBlendFuncS(self._handle, value.encode("utf-8"))

    @property
    def vis_tex_ani_fps(self) -> float:
        DLL.ZkEffectBaseInstance_getVisTexAniFps.restype = c_float
        return DLL.ZkEffectBaseInstance_getVisTexAniFps(self._handle)

    @vis_tex_ani_fps.setter
    def vis_tex_ani_fps(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setVisTexAniFps(self._handle, c_float(value))

    @property
    def vis_tex_ani_is_looping(self) -> int:
        DLL.ZkEffectBaseInstance_getVisTexAniIsLooping.restype = c_int32
        return DLL.ZkEffectBaseInstance_getVisTexAniIsLooping(self._handle)

    @vis_tex_ani_is_looping.setter
    def vis_tex_ani_is_looping(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setVisTexAniIsLooping(self._handle, c_int32(value))

    @property
    def em_trj_mode_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmTrjModeS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmTrjModeS(self._handle).value

    @em_trj_mode_s.setter
    def em_trj_mode_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjModeS(self._handle, value.encode("utf-8"))

    @property
    def em_trj_origin_node(self) -> str:
        DLL.ZkEffectBaseInstance_getEmTrjOriginNode.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmTrjOriginNode(self._handle).value

    @em_trj_origin_node.setter
    def em_trj_origin_node(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjOriginNode(self._handle, value.encode("utf-8"))

    @property
    def em_trj_target_node(self) -> str:
        DLL.ZkEffectBaseInstance_getEmTrjTargetNode.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmTrjTargetNode(self._handle).value

    @em_trj_target_node.setter
    def em_trj_target_node(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjTargetNode(self._handle, value.encode("utf-8"))

    @property
    def em_trj_target_range(self) -> float:
        DLL.ZkEffectBaseInstance_getEmTrjTargetRange.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmTrjTargetRange(self._handle)

    @em_trj_target_range.setter
    def em_trj_target_range(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjTargetRange(self._handle, c_float(value))

    @property
    def em_trj_target_azi(self) -> float:
        DLL.ZkEffectBaseInstance_getEmTrjTargetAzi.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmTrjTargetAzi(self._handle)

    @em_trj_target_azi.setter
    def em_trj_target_azi(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjTargetAzi(self._handle, c_float(value))

    @property
    def em_trj_target_elev(self) -> float:
        DLL.ZkEffectBaseInstance_getEmTrjTargetElev.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmTrjTargetElev(self._handle)

    @em_trj_target_elev.setter
    def em_trj_target_elev(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjTargetElev(self._handle, c_float(value))

    @property
    def em_trj_num_keys(self) -> int:
        DLL.ZkEffectBaseInstance_getEmTrjNumKeys.restype = c_int32
        return DLL.ZkEffectBaseInstance_getEmTrjNumKeys(self._handle)

    @em_trj_num_keys.setter
    def em_trj_num_keys(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjNumKeys(self._handle, c_int32(value))

    @property
    def em_trj_num_keys_var(self) -> int:
        DLL.ZkEffectBaseInstance_getEmTrjNumKeysVar.restype = c_int32
        return DLL.ZkEffectBaseInstance_getEmTrjNumKeysVar(self._handle)

    @em_trj_num_keys_var.setter
    def em_trj_num_keys_var(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjNumKeysVar(self._handle, c_int32(value))

    @property
    def em_trj_angle_elev_var(self) -> float:
        DLL.ZkEffectBaseInstance_getEmTrjAngleElevVar.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmTrjAngleElevVar(self._handle)

    @em_trj_angle_elev_var.setter
    def em_trj_angle_elev_var(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjAngleElevVar(self._handle, c_float(value))

    @property
    def em_trj_angle_head_var(self) -> float:
        DLL.ZkEffectBaseInstance_getEmTrjAngleHeadVar.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmTrjAngleHeadVar(self._handle)

    @em_trj_angle_head_var.setter
    def em_trj_angle_head_var(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjAngleHeadVar(self._handle, c_float(value))

    @property
    def em_trj_key_dist_var(self) -> float:
        DLL.ZkEffectBaseInstance_getEmTrjKeyDistVar.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmTrjKeyDistVar(self._handle)

    @em_trj_key_dist_var.setter
    def em_trj_key_dist_var(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjKeyDistVar(self._handle, c_float(value))

    @property
    def em_trj_loop_mode_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmTrjLoopModeS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmTrjLoopModeS(self._handle).value

    @em_trj_loop_mode_s.setter
    def em_trj_loop_mode_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjLoopModeS(self._handle, value.encode("utf-8"))

    @property
    def em_trj_ease_func_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmTrjEaseFuncS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmTrjEaseFuncS(self._handle).value

    @em_trj_ease_func_s.setter
    def em_trj_ease_func_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjEaseFuncS(self._handle, value.encode("utf-8"))

    @property
    def em_trj_ease_vel(self) -> float:
        DLL.ZkEffectBaseInstance_getEmTrjEaseVel.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmTrjEaseVel(self._handle)

    @em_trj_ease_vel.setter
    def em_trj_ease_vel(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjEaseVel(self._handle, c_float(value))

    @property
    def em_trj_dyn_update_delay(self) -> float:
        DLL.ZkEffectBaseInstance_getEmTrjDynUpdateDelay.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmTrjDynUpdateDelay(self._handle)

    @em_trj_dyn_update_delay.setter
    def em_trj_dyn_update_delay(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjDynUpdateDelay(self._handle, c_float(value))

    @property
    def em_trj_dyn_update_target_only(self) -> int:
        DLL.ZkEffectBaseInstance_getEmTrjDynUpdateTargetOnly.restype = c_int32
        return DLL.ZkEffectBaseInstance_getEmTrjDynUpdateTargetOnly(self._handle)

    @em_trj_dyn_update_target_only.setter
    def em_trj_dyn_update_target_only(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setEmTrjDynUpdateTargetOnly(self._handle, c_int32(value))

    @property
    def em_fx_create_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmFxCreateS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmFxCreateS(self._handle).value

    @em_fx_create_s.setter
    def em_fx_create_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmFxCreateS(self._handle, value.encode("utf-8"))

    @property
    def em_fx_invest_origin_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmFxInvestOriginS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmFxInvestOriginS(self._handle).value

    @em_fx_invest_origin_s.setter
    def em_fx_invest_origin_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmFxInvestOriginS(self._handle, value.encode("utf-8"))

    @property
    def em_fx_invest_target_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmFxInvestTargetS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmFxInvestTargetS(self._handle).value

    @em_fx_invest_target_s.setter
    def em_fx_invest_target_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmFxInvestTargetS(self._handle, value.encode("utf-8"))

    @property
    def em_fx_trigger_delay(self) -> float:
        DLL.ZkEffectBaseInstance_getEmFxTriggerDelay.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmFxTriggerDelay(self._handle)

    @em_fx_trigger_delay.setter
    def em_fx_trigger_delay(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmFxTriggerDelay(self._handle, c_float(value))

    @property
    def em_fx_create_down_trj(self) -> int:
        DLL.ZkEffectBaseInstance_getEmFxCreateDownTrj.restype = c_int32
        return DLL.ZkEffectBaseInstance_getEmFxCreateDownTrj(self._handle)

    @em_fx_create_down_trj.setter
    def em_fx_create_down_trj(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setEmFxCreateDownTrj(self._handle, c_int32(value))

    @property
    def em_action_coll_dyn_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmActionCollDynS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmActionCollDynS(self._handle).value

    @em_action_coll_dyn_s.setter
    def em_action_coll_dyn_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmActionCollDynS(self._handle, value.encode("utf-8"))

    @property
    def em_action_coll_stat_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmActionCollStatS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmActionCollStatS(self._handle).value

    @em_action_coll_stat_s.setter
    def em_action_coll_stat_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmActionCollStatS(self._handle, value.encode("utf-8"))

    @property
    def em_fx_coll_stat_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmFxCollStatS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmFxCollStatS(self._handle).value

    @em_fx_coll_stat_s.setter
    def em_fx_coll_stat_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmFxCollStatS(self._handle, value.encode("utf-8"))

    @property
    def em_fx_coll_dyn_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmFxCollDynS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmFxCollDynS(self._handle).value

    @em_fx_coll_dyn_s.setter
    def em_fx_coll_dyn_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmFxCollDynS(self._handle, value.encode("utf-8"))

    @property
    def em_fx_coll_stat_align_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmFxCollStatAlignS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmFxCollStatAlignS(self._handle).value

    @em_fx_coll_stat_align_s.setter
    def em_fx_coll_stat_align_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmFxCollStatAlignS(self._handle, value.encode("utf-8"))

    @property
    def em_fx_coll_dyn_align_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmFxCollDynAlignS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmFxCollDynAlignS(self._handle).value

    @em_fx_coll_dyn_align_s.setter
    def em_fx_coll_dyn_align_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmFxCollDynAlignS(self._handle, value.encode("utf-8"))

    @property
    def em_fx_lifespan(self) -> float:
        DLL.ZkEffectBaseInstance_getEmFxLifespan.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmFxLifespan(self._handle)

    @em_fx_lifespan.setter
    def em_fx_lifespan(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmFxLifespan(self._handle, c_float(value))

    @property
    def em_check_collision(self) -> int:
        DLL.ZkEffectBaseInstance_getEmCheckCollision.restype = c_int32
        return DLL.ZkEffectBaseInstance_getEmCheckCollision(self._handle)

    @em_check_collision.setter
    def em_check_collision(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setEmCheckCollision(self._handle, c_int32(value))

    @property
    def em_adjust_shp_to_origin(self) -> int:
        DLL.ZkEffectBaseInstance_getEmAdjustShpToOrigin.restype = c_int32
        return DLL.ZkEffectBaseInstance_getEmAdjustShpToOrigin(self._handle)

    @em_adjust_shp_to_origin.setter
    def em_adjust_shp_to_origin(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setEmAdjustShpToOrigin(self._handle, c_int32(value))

    @property
    def em_invest_next_key_duration(self) -> float:
        DLL.ZkEffectBaseInstance_getEmInvestNextKeyDuration.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmInvestNextKeyDuration(self._handle)

    @em_invest_next_key_duration.setter
    def em_invest_next_key_duration(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmInvestNextKeyDuration(self._handle, c_float(value))

    @property
    def em_fly_gravity(self) -> float:
        DLL.ZkEffectBaseInstance_getEmFlyGravity.restype = c_float
        return DLL.ZkEffectBaseInstance_getEmFlyGravity(self._handle)

    @em_fly_gravity.setter
    def em_fly_gravity(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setEmFlyGravity(self._handle, c_float(value))

    @property
    def em_self_rot_vel_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmSelfRotVelS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmSelfRotVelS(self._handle).value

    @em_self_rot_vel_s.setter
    def em_self_rot_vel_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmSelfRotVelS(self._handle, value.encode("utf-8"))

    @property
    def light_preset_name(self) -> str:
        DLL.ZkEffectBaseInstance_getLightPresetName.restype = ZkString
        return DLL.ZkEffectBaseInstance_getLightPresetName(self._handle).value

    @light_preset_name.setter
    def light_preset_name(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setLightPresetName(self._handle, value.encode("utf-8"))

    @property
    def sfx_id(self) -> str:
        DLL.ZkEffectBaseInstance_getSfxId.restype = ZkString
        return DLL.ZkEffectBaseInstance_getSfxId(self._handle).value

    @sfx_id.setter
    def sfx_id(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setSfxId(self._handle, value.encode("utf-8"))

    @property
    def sfx_is_ambient(self) -> int:
        DLL.ZkEffectBaseInstance_getSfxIsAmbient.restype = c_int32
        return DLL.ZkEffectBaseInstance_getSfxIsAmbient(self._handle)

    @sfx_is_ambient.setter
    def sfx_is_ambient(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setSfxIsAmbient(self._handle, c_int32(value))

    @property
    def send_assess_magic(self) -> int:
        DLL.ZkEffectBaseInstance_getSendAssessMagic.restype = c_int32
        return DLL.ZkEffectBaseInstance_getSendAssessMagic(self._handle)

    @send_assess_magic.setter
    def send_assess_magic(self, value: int) -> None:
        DLL.ZkEffectBaseInstance_setSendAssessMagic(self._handle, c_int32(value))

    @property
    def secs_per_damage(self) -> float:
        DLL.ZkEffectBaseInstance_getSecsPerDamage.restype = c_float
        return DLL.ZkEffectBaseInstance_getSecsPerDamage(self._handle)

    @secs_per_damage.setter
    def secs_per_damage(self, value: float) -> None:
        DLL.ZkEffectBaseInstance_setSecsPerDamage(self._handle, c_float(value))

    @property
    def em_fx_coll_dyn_perc_s(self) -> str:
        DLL.ZkEffectBaseInstance_getEmFxCollDynPercS.restype = ZkString
        return DLL.ZkEffectBaseInstance_getEmFxCollDynPercS(self._handle).value

    @em_fx_coll_dyn_perc_s.setter
    def em_fx_coll_dyn_perc_s(self, value: str) -> None:
        DLL.ZkEffectBaseInstance_setEmFxCollDynPercS(self._handle, value.encode("utf-8"))

    def get_user_string(self, i: int) -> str:
        if i < 0 or i >= 5:
            raise IndexError(i)

        DLL.ZkEffectBaseInstance_getUserString.restype = ZkString
        return DLL.ZkEffectBaseInstance_getUserString(self._handle, c_size_t(i)).value

    def set_user_string(self, i: int, val: str) -> None:
        if i < 0 or i >= 5:
            raise IndexError(i)
        return DLL.ZkEffectBaseInstance_setUserString(self._handle, c_size_t(i), val.encode("utf-8"))
