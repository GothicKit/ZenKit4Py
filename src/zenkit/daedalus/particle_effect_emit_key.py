__all__ = [
    "ParticleEffectEmitKeyInstance",
]

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class ParticleEffectEmitKeyInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def vis_name_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getVisNameS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getVisNameS(self._handle).value

    @vis_name_s.setter
    def vis_name_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setVisNameS(self._handle, value.encode("utf-8"))

    @property
    def vis_size_scale(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getVisSizeScale.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getVisSizeScale(self._handle)

    @vis_size_scale.setter
    def vis_size_scale(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setVisSizeScale(self._handle, c_float(value))

    @property
    def scale_duration(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getScaleDuration.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getScaleDuration(self._handle)

    @scale_duration.setter
    def scale_duration(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setScaleDuration(self._handle, c_float(value))

    @property
    def pfx_pps_value(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxPpsValue.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxPpsValue(self._handle)

    @pfx_pps_value.setter
    def pfx_pps_value(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxPpsValue(self._handle, c_float(value))

    @property
    def pfx_pps_is_smooth_chg(self) -> int:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxPpsIsSmoothChg.restype = c_int32
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxPpsIsSmoothChg(self._handle)

    @pfx_pps_is_smooth_chg.setter
    def pfx_pps_is_smooth_chg(self, value: int) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxPpsIsSmoothChg(self._handle, c_int32(value))

    @property
    def pfx_pps_is_looping_chg(self) -> int:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxPpsIsLoopingChg.restype = c_int32
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxPpsIsLoopingChg(self._handle)

    @pfx_pps_is_looping_chg.setter
    def pfx_pps_is_looping_chg(self, value: int) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxPpsIsLoopingChg(self._handle, c_int32(value))

    @property
    def pfx_sc_time(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxScTime.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxScTime(self._handle)

    @pfx_sc_time.setter
    def pfx_sc_time(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxScTime(self._handle, c_float(value))

    @property
    def pfx_fly_gravity_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxFlyGravityS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxFlyGravityS(self._handle).value

    @pfx_fly_gravity_s.setter
    def pfx_fly_gravity_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxFlyGravityS(self._handle, value.encode("utf-8"))

    @property
    def pfx_shp_dim_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxShpDimS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxShpDimS(self._handle).value

    @pfx_shp_dim_s.setter
    def pfx_shp_dim_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxShpDimS(self._handle, value.encode("utf-8"))

    @property
    def pfx_shp_is_volume_chg(self) -> int:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxShpIsVolumeChg.restype = c_int32
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxShpIsVolumeChg(self._handle)

    @pfx_shp_is_volume_chg.setter
    def pfx_shp_is_volume_chg(self, value: int) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxShpIsVolumeChg(self._handle, c_int32(value))

    @property
    def pfx_shp_scale_fps(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxShpScaleFps.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxShpScaleFps(self._handle)

    @pfx_shp_scale_fps.setter
    def pfx_shp_scale_fps(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxShpScaleFps(self._handle, c_float(value))

    @property
    def pfx_shp_distrib_walks_peed(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxShpDistribWalksPeed.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxShpDistribWalksPeed(self._handle)

    @pfx_shp_distrib_walks_peed.setter
    def pfx_shp_distrib_walks_peed(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxShpDistribWalksPeed(self._handle, c_float(value))

    @property
    def pfx_shp_offset_vec_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxShpOffsetVecS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxShpOffsetVecS(self._handle).value

    @pfx_shp_offset_vec_s.setter
    def pfx_shp_offset_vec_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxShpOffsetVecS(self._handle, value.encode("utf-8"))

    @property
    def pfx_shp_distrib_type_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxShpDistribTypeS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxShpDistribTypeS(self._handle).value

    @pfx_shp_distrib_type_s.setter
    def pfx_shp_distrib_type_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxShpDistribTypeS(self._handle, value.encode("utf-8"))

    @property
    def pfx_dir_mode_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxDirModeS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxDirModeS(self._handle).value

    @pfx_dir_mode_s.setter
    def pfx_dir_mode_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxDirModeS(self._handle, value.encode("utf-8"))

    @property
    def pfx_dir_for_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxDirForS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxDirForS(self._handle).value

    @pfx_dir_for_s.setter
    def pfx_dir_for_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxDirForS(self._handle, value.encode("utf-8"))

    @property
    def pfx_dir_mode_target_for_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxDirModeTargetForS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxDirModeTargetForS(self._handle).value

    @pfx_dir_mode_target_for_s.setter
    def pfx_dir_mode_target_for_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxDirModeTargetForS(self._handle, value.encode("utf-8"))

    @property
    def pfx_dir_mode_target_pos_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxDirModeTargetPosS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxDirModeTargetPosS(self._handle).value

    @pfx_dir_mode_target_pos_s.setter
    def pfx_dir_mode_target_pos_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxDirModeTargetPosS(self._handle, value.encode("utf-8"))

    @property
    def pfx_vel_avg(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxVelAvg.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxVelAvg(self._handle)

    @pfx_vel_avg.setter
    def pfx_vel_avg(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxVelAvg(self._handle, c_float(value))

    @property
    def pfx_lsp_part_avg(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxLspPartAvg.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxLspPartAvg(self._handle)

    @pfx_lsp_part_avg.setter
    def pfx_lsp_part_avg(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxLspPartAvg(self._handle, c_float(value))

    @property
    def pfx_vis_alpha_start(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getPfxVisAlphaStart.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getPfxVisAlphaStart(self._handle)

    @pfx_vis_alpha_start.setter
    def pfx_vis_alpha_start(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setPfxVisAlphaStart(self._handle, c_float(value))

    @property
    def light_preset_name(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getLightPresetName.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getLightPresetName(self._handle).value

    @light_preset_name.setter
    def light_preset_name(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setLightPresetName(self._handle, value.encode("utf-8"))

    @property
    def light_range(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getLightRange.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getLightRange(self._handle)

    @light_range.setter
    def light_range(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setLightRange(self._handle, c_float(value))

    @property
    def sfx_id(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getSfxId.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getSfxId(self._handle).value

    @sfx_id.setter
    def sfx_id(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setSfxId(self._handle, value.encode("utf-8"))

    @property
    def sfx_is_ambient(self) -> int:
        DLL.ZkParticleEffectEmitKeyInstance_getSfxIsAmbient.restype = c_int32
        return DLL.ZkParticleEffectEmitKeyInstance_getSfxIsAmbient(self._handle)

    @sfx_is_ambient.setter
    def sfx_is_ambient(self, value: int) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setSfxIsAmbient(self._handle, c_int32(value))

    @property
    def em_create_fx_id(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getEmCreateFxId.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getEmCreateFxId(self._handle).value

    @em_create_fx_id.setter
    def em_create_fx_id(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setEmCreateFxId(self._handle, value.encode("utf-8"))

    @property
    def em_fly_gravity(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getEmFlyGravity.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getEmFlyGravity(self._handle)

    @em_fly_gravity.setter
    def em_fly_gravity(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setEmFlyGravity(self._handle, c_float(value))

    @property
    def em_self_rot_vel_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getEmSelfRotVelS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getEmSelfRotVelS(self._handle).value

    @em_self_rot_vel_s.setter
    def em_self_rot_vel_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setEmSelfRotVelS(self._handle, value.encode("utf-8"))

    @property
    def em_trj_mode_s(self) -> str:
        DLL.ZkParticleEffectEmitKeyInstance_getEmTrjModeS.restype = ZkString
        return DLL.ZkParticleEffectEmitKeyInstance_getEmTrjModeS(self._handle).value

    @em_trj_mode_s.setter
    def em_trj_mode_s(self, value: str) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setEmTrjModeS(self._handle, value.encode("utf-8"))

    @property
    def em_trj_ease_vel(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getEmTrjEaseVel.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getEmTrjEaseVel(self._handle)

    @em_trj_ease_vel.setter
    def em_trj_ease_vel(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setEmTrjEaseVel(self._handle, c_float(value))

    @property
    def em_check_collision(self) -> int:
        DLL.ZkParticleEffectEmitKeyInstance_getEmCheckCollision.restype = c_int32
        return DLL.ZkParticleEffectEmitKeyInstance_getEmCheckCollision(self._handle)

    @em_check_collision.setter
    def em_check_collision(self, value: int) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setEmCheckCollision(self._handle, c_int32(value))

    @property
    def em_fx_lifespan(self) -> float:
        DLL.ZkParticleEffectEmitKeyInstance_getEmFxLifespan.restype = c_float
        return DLL.ZkParticleEffectEmitKeyInstance_getEmFxLifespan(self._handle)

    @em_fx_lifespan.setter
    def em_fx_lifespan(self, value: float) -> None:
        DLL.ZkParticleEffectEmitKeyInstance_setEmFxLifespan(self._handle, c_float(value))
