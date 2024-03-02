__all__ = ["ParticleEffectInstance"]

from ctypes import c_float
from ctypes import c_int32
from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class ParticleEffectInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def pps_value(self) -> float:
        DLL.ZkParticleEffectInstance_getPpsValue.restype = c_float
        return DLL.ZkParticleEffectInstance_getPpsValue(self._handle)

    @pps_value.setter
    def pps_value(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setPpsValue(self._handle, c_float(value))

    @property
    def pps_scale_keys_s(self) -> str:
        DLL.ZkParticleEffectInstance_getPpsScaleKeysS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getPpsScaleKeysS(self._handle).value

    @pps_scale_keys_s.setter
    def pps_scale_keys_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setPpsScaleKeysS(self._handle, value.encode("utf-8"))

    @property
    def pps_is_looping(self) -> int:
        DLL.ZkParticleEffectInstance_getPpsIsLooping.restype = c_int32
        return DLL.ZkParticleEffectInstance_getPpsIsLooping(self._handle)

    @pps_is_looping.setter
    def pps_is_looping(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setPpsIsLooping(self._handle, c_int32(value))

    @property
    def pps_is_smooth(self) -> int:
        DLL.ZkParticleEffectInstance_getPpsIsSmooth.restype = c_int32
        return DLL.ZkParticleEffectInstance_getPpsIsSmooth(self._handle)

    @pps_is_smooth.setter
    def pps_is_smooth(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setPpsIsSmooth(self._handle, c_int32(value))

    @property
    def pps_fps(self) -> float:
        DLL.ZkParticleEffectInstance_getPpsFps.restype = c_float
        return DLL.ZkParticleEffectInstance_getPpsFps(self._handle)

    @pps_fps.setter
    def pps_fps(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setPpsFps(self._handle, c_float(value))

    @property
    def pps_create_em_s(self) -> str:
        DLL.ZkParticleEffectInstance_getPpsCreateEmS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getPpsCreateEmS(self._handle).value

    @pps_create_em_s.setter
    def pps_create_em_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setPpsCreateEmS(self._handle, value.encode("utf-8"))

    @property
    def pps_create_em_delay(self) -> float:
        DLL.ZkParticleEffectInstance_getPpsCreateEmDelay.restype = c_float
        return DLL.ZkParticleEffectInstance_getPpsCreateEmDelay(self._handle)

    @pps_create_em_delay.setter
    def pps_create_em_delay(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setPpsCreateEmDelay(self._handle, c_float(value))

    @property
    def shp_type_s(self) -> str:
        DLL.ZkParticleEffectInstance_getShpTypeS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getShpTypeS(self._handle).value

    @shp_type_s.setter
    def shp_type_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setShpTypeS(self._handle, value.encode("utf-8"))

    @property
    def shp_for_s(self) -> str:
        DLL.ZkParticleEffectInstance_getShpForS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getShpForS(self._handle).value

    @shp_for_s.setter
    def shp_for_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setShpForS(self._handle, value.encode("utf-8"))

    @property
    def shp_offset_vec_s(self) -> str:
        DLL.ZkParticleEffectInstance_getShpOffsetVecS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getShpOffsetVecS(self._handle).value

    @shp_offset_vec_s.setter
    def shp_offset_vec_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setShpOffsetVecS(self._handle, value.encode("utf-8"))

    @property
    def shp_distrib_type_s(self) -> str:
        DLL.ZkParticleEffectInstance_getShpDistribTypeS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getShpDistribTypeS(self._handle).value

    @shp_distrib_type_s.setter
    def shp_distrib_type_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setShpDistribTypeS(self._handle, value.encode("utf-8"))

    @property
    def shp_distrib_walk_speed(self) -> float:
        DLL.ZkParticleEffectInstance_getShpDistribWalkSpeed.restype = c_float
        return DLL.ZkParticleEffectInstance_getShpDistribWalkSpeed(self._handle)

    @shp_distrib_walk_speed.setter
    def shp_distrib_walk_speed(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setShpDistribWalkSpeed(self._handle, c_float(value))

    @property
    def shp_is_volume(self) -> int:
        DLL.ZkParticleEffectInstance_getShpIsVolume.restype = c_int32
        return DLL.ZkParticleEffectInstance_getShpIsVolume(self._handle)

    @shp_is_volume.setter
    def shp_is_volume(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setShpIsVolume(self._handle, c_int32(value))

    @property
    def shp_dim_s(self) -> str:
        DLL.ZkParticleEffectInstance_getShpDimS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getShpDimS(self._handle).value

    @shp_dim_s.setter
    def shp_dim_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setShpDimS(self._handle, value.encode("utf-8"))

    @property
    def shp_mesh_s(self) -> str:
        DLL.ZkParticleEffectInstance_getShpMeshS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getShpMeshS(self._handle).value

    @shp_mesh_s.setter
    def shp_mesh_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setShpMeshS(self._handle, value.encode("utf-8"))

    @property
    def shp_mesh_render_b(self) -> int:
        DLL.ZkParticleEffectInstance_getShpMeshRenderB.restype = c_int32
        return DLL.ZkParticleEffectInstance_getShpMeshRenderB(self._handle)

    @shp_mesh_render_b.setter
    def shp_mesh_render_b(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setShpMeshRenderB(self._handle, c_int32(value))

    @property
    def shp_scale_keys_s(self) -> str:
        DLL.ZkParticleEffectInstance_getShpScaleKeysS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getShpScaleKeysS(self._handle).value

    @shp_scale_keys_s.setter
    def shp_scale_keys_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setShpScaleKeysS(self._handle, value.encode("utf-8"))

    @property
    def shp_scale_is_looping(self) -> int:
        DLL.ZkParticleEffectInstance_getShpScaleIsLooping.restype = c_int32
        return DLL.ZkParticleEffectInstance_getShpScaleIsLooping(self._handle)

    @shp_scale_is_looping.setter
    def shp_scale_is_looping(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setShpScaleIsLooping(self._handle, c_int32(value))

    @property
    def shp_scale_is_smooth(self) -> int:
        DLL.ZkParticleEffectInstance_getShpScaleIsSmooth.restype = c_int32
        return DLL.ZkParticleEffectInstance_getShpScaleIsSmooth(self._handle)

    @shp_scale_is_smooth.setter
    def shp_scale_is_smooth(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setShpScaleIsSmooth(self._handle, c_int32(value))

    @property
    def shp_scale_fps(self) -> float:
        DLL.ZkParticleEffectInstance_getShpScaleFps.restype = c_float
        return DLL.ZkParticleEffectInstance_getShpScaleFps(self._handle)

    @shp_scale_fps.setter
    def shp_scale_fps(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setShpScaleFps(self._handle, c_float(value))

    @property
    def dir_mode_s(self) -> str:
        DLL.ZkParticleEffectInstance_getDirModeS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getDirModeS(self._handle).value

    @dir_mode_s.setter
    def dir_mode_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setDirModeS(self._handle, value.encode("utf-8"))

    @property
    def dir_for_s(self) -> str:
        DLL.ZkParticleEffectInstance_getDirForS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getDirForS(self._handle).value

    @dir_for_s.setter
    def dir_for_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setDirForS(self._handle, value.encode("utf-8"))

    @property
    def dir_mode_target_for_s(self) -> str:
        DLL.ZkParticleEffectInstance_getDirModeTargetForS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getDirModeTargetForS(self._handle).value

    @dir_mode_target_for_s.setter
    def dir_mode_target_for_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setDirModeTargetForS(self._handle, value.encode("utf-8"))

    @property
    def dir_mode_target_pos_s(self) -> str:
        DLL.ZkParticleEffectInstance_getDirModeTargetPosS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getDirModeTargetPosS(self._handle).value

    @dir_mode_target_pos_s.setter
    def dir_mode_target_pos_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setDirModeTargetPosS(self._handle, value.encode("utf-8"))

    @property
    def dir_angle_head(self) -> float:
        DLL.ZkParticleEffectInstance_getDirAngleHead.restype = c_float
        return DLL.ZkParticleEffectInstance_getDirAngleHead(self._handle)

    @dir_angle_head.setter
    def dir_angle_head(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setDirAngleHead(self._handle, c_float(value))

    @property
    def dir_angle_head_var(self) -> float:
        DLL.ZkParticleEffectInstance_getDirAngleHeadVar.restype = c_float
        return DLL.ZkParticleEffectInstance_getDirAngleHeadVar(self._handle)

    @dir_angle_head_var.setter
    def dir_angle_head_var(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setDirAngleHeadVar(self._handle, c_float(value))

    @property
    def dir_angle_elev(self) -> float:
        DLL.ZkParticleEffectInstance_getDirAngleElev.restype = c_float
        return DLL.ZkParticleEffectInstance_getDirAngleElev(self._handle)

    @dir_angle_elev.setter
    def dir_angle_elev(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setDirAngleElev(self._handle, c_float(value))

    @property
    def dir_angle_elev_var(self) -> float:
        DLL.ZkParticleEffectInstance_getDirAngleElevVar.restype = c_float
        return DLL.ZkParticleEffectInstance_getDirAngleElevVar(self._handle)

    @dir_angle_elev_var.setter
    def dir_angle_elev_var(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setDirAngleElevVar(self._handle, c_float(value))

    @property
    def vel_avg(self) -> float:
        DLL.ZkParticleEffectInstance_getVelAvg.restype = c_float
        return DLL.ZkParticleEffectInstance_getVelAvg(self._handle)

    @vel_avg.setter
    def vel_avg(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setVelAvg(self._handle, c_float(value))

    @property
    def vel_var(self) -> float:
        DLL.ZkParticleEffectInstance_getVelVar.restype = c_float
        return DLL.ZkParticleEffectInstance_getVelVar(self._handle)

    @vel_var.setter
    def vel_var(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setVelVar(self._handle, c_float(value))

    @property
    def lsp_part_avg(self) -> float:
        DLL.ZkParticleEffectInstance_getLspPartAvg.restype = c_float
        return DLL.ZkParticleEffectInstance_getLspPartAvg(self._handle)

    @lsp_part_avg.setter
    def lsp_part_avg(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setLspPartAvg(self._handle, c_float(value))

    @property
    def lsp_part_var(self) -> float:
        DLL.ZkParticleEffectInstance_getLspPartVar.restype = c_float
        return DLL.ZkParticleEffectInstance_getLspPartVar(self._handle)

    @lsp_part_var.setter
    def lsp_part_var(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setLspPartVar(self._handle, c_float(value))

    @property
    def fly_gravity_s(self) -> str:
        DLL.ZkParticleEffectInstance_getFlyGravityS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getFlyGravityS(self._handle).value

    @fly_gravity_s.setter
    def fly_gravity_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setFlyGravityS(self._handle, value.encode("utf-8"))

    @property
    def fly_colldet_b(self) -> int:
        DLL.ZkParticleEffectInstance_getFlyColldetB.restype = c_int32
        return DLL.ZkParticleEffectInstance_getFlyColldetB(self._handle)

    @fly_colldet_b.setter
    def fly_colldet_b(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setFlyColldetB(self._handle, c_int32(value))

    @property
    def vis_name_s(self) -> str:
        DLL.ZkParticleEffectInstance_getVisNameS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getVisNameS(self._handle).value

    @vis_name_s.setter
    def vis_name_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setVisNameS(self._handle, value.encode("utf-8"))

    @property
    def vis_orientation_s(self) -> str:
        DLL.ZkParticleEffectInstance_getVisOrientationS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getVisOrientationS(self._handle).value

    @vis_orientation_s.setter
    def vis_orientation_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setVisOrientationS(self._handle, value.encode("utf-8"))

    @property
    def vis_tex_is_quadpoly(self) -> int:
        DLL.ZkParticleEffectInstance_getVisTexIsQuadpoly.restype = c_int32
        return DLL.ZkParticleEffectInstance_getVisTexIsQuadpoly(self._handle)

    @vis_tex_is_quadpoly.setter
    def vis_tex_is_quadpoly(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setVisTexIsQuadpoly(self._handle, c_int32(value))

    @property
    def vis_tex_ani_fps(self) -> float:
        DLL.ZkParticleEffectInstance_getVisTexAniFps.restype = c_float
        return DLL.ZkParticleEffectInstance_getVisTexAniFps(self._handle)

    @vis_tex_ani_fps.setter
    def vis_tex_ani_fps(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setVisTexAniFps(self._handle, c_float(value))

    @property
    def vis_tex_ani_is_looping(self) -> int:
        DLL.ZkParticleEffectInstance_getVisTexAniIsLooping.restype = c_int32
        return DLL.ZkParticleEffectInstance_getVisTexAniIsLooping(self._handle)

    @vis_tex_ani_is_looping.setter
    def vis_tex_ani_is_looping(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setVisTexAniIsLooping(self._handle, c_int32(value))

    @property
    def vis_tex_color_start_s(self) -> str:
        DLL.ZkParticleEffectInstance_getVisTexColorStartS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getVisTexColorStartS(self._handle).value

    @vis_tex_color_start_s.setter
    def vis_tex_color_start_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setVisTexColorStartS(self._handle, value.encode("utf-8"))

    @property
    def vis_tex_color_end_s(self) -> str:
        DLL.ZkParticleEffectInstance_getVisTexColorEndS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getVisTexColorEndS(self._handle).value

    @vis_tex_color_end_s.setter
    def vis_tex_color_end_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setVisTexColorEndS(self._handle, value.encode("utf-8"))

    @property
    def vis_size_start_s(self) -> str:
        DLL.ZkParticleEffectInstance_getVisSizeStartS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getVisSizeStartS(self._handle).value

    @vis_size_start_s.setter
    def vis_size_start_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setVisSizeStartS(self._handle, value.encode("utf-8"))

    @property
    def vis_size_end_scale(self) -> float:
        DLL.ZkParticleEffectInstance_getVisSizeEndScale.restype = c_float
        return DLL.ZkParticleEffectInstance_getVisSizeEndScale(self._handle)

    @vis_size_end_scale.setter
    def vis_size_end_scale(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setVisSizeEndScale(self._handle, c_float(value))

    @property
    def vis_alpha_func_s(self) -> str:
        DLL.ZkParticleEffectInstance_getVisAlphaFuncS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getVisAlphaFuncS(self._handle).value

    @vis_alpha_func_s.setter
    def vis_alpha_func_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setVisAlphaFuncS(self._handle, value.encode("utf-8"))

    @property
    def vis_alpha_start(self) -> float:
        DLL.ZkParticleEffectInstance_getVisAlphaStart.restype = c_float
        return DLL.ZkParticleEffectInstance_getVisAlphaStart(self._handle)

    @vis_alpha_start.setter
    def vis_alpha_start(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setVisAlphaStart(self._handle, c_float(value))

    @property
    def vis_alpha_end(self) -> float:
        DLL.ZkParticleEffectInstance_getVisAlphaEnd.restype = c_float
        return DLL.ZkParticleEffectInstance_getVisAlphaEnd(self._handle)

    @vis_alpha_end.setter
    def vis_alpha_end(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setVisAlphaEnd(self._handle, c_float(value))

    @property
    def trl_fade_speed(self) -> float:
        DLL.ZkParticleEffectInstance_getTrlFadeSpeed.restype = c_float
        return DLL.ZkParticleEffectInstance_getTrlFadeSpeed(self._handle)

    @trl_fade_speed.setter
    def trl_fade_speed(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setTrlFadeSpeed(self._handle, c_float(value))

    @property
    def trl_texture_s(self) -> str:
        DLL.ZkParticleEffectInstance_getTrlTextureS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getTrlTextureS(self._handle).value

    @trl_texture_s.setter
    def trl_texture_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setTrlTextureS(self._handle, value.encode("utf-8"))

    @property
    def trl_width(self) -> float:
        DLL.ZkParticleEffectInstance_getTrlWidth.restype = c_float
        return DLL.ZkParticleEffectInstance_getTrlWidth(self._handle)

    @trl_width.setter
    def trl_width(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setTrlWidth(self._handle, c_float(value))

    @property
    def mrk_fades_peed(self) -> float:
        DLL.ZkParticleEffectInstance_getMrkFadesPeed.restype = c_float
        return DLL.ZkParticleEffectInstance_getMrkFadesPeed(self._handle)

    @mrk_fades_peed.setter
    def mrk_fades_peed(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setMrkFadesPeed(self._handle, c_float(value))

    @property
    def mrkt_exture_s(self) -> str:
        DLL.ZkParticleEffectInstance_getMrktExtureS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getMrktExtureS(self._handle).value

    @mrkt_exture_s.setter
    def mrkt_exture_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setMrktExtureS(self._handle, value.encode("utf-8"))

    @property
    def mrk_size(self) -> float:
        DLL.ZkParticleEffectInstance_getMrkSize.restype = c_float
        return DLL.ZkParticleEffectInstance_getMrkSize(self._handle)

    @mrk_size.setter
    def mrk_size(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setMrkSize(self._handle, c_float(value))

    @property
    def flock_mode(self) -> str:
        DLL.ZkParticleEffectInstance_getFlockMode.restype = ZkString
        return DLL.ZkParticleEffectInstance_getFlockMode(self._handle).value

    @flock_mode.setter
    def flock_mode(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setFlockMode(self._handle, value.encode("utf-8"))

    @property
    def flock_strength(self) -> float:
        DLL.ZkParticleEffectInstance_getFlockStrength.restype = c_float
        return DLL.ZkParticleEffectInstance_getFlockStrength(self._handle)

    @flock_strength.setter
    def flock_strength(self, value: float) -> None:
        DLL.ZkParticleEffectInstance_setFlockStrength(self._handle, c_float(value))

    @property
    def use_emitters_for(self) -> int:
        DLL.ZkParticleEffectInstance_getUseEmittersFor.restype = c_int32
        return DLL.ZkParticleEffectInstance_getUseEmittersFor(self._handle)

    @use_emitters_for.setter
    def use_emitters_for(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setUseEmittersFor(self._handle, c_int32(value))

    @property
    def time_start_end_s(self) -> str:
        DLL.ZkParticleEffectInstance_getTimeStartEndS.restype = ZkString
        return DLL.ZkParticleEffectInstance_getTimeStartEndS(self._handle).value

    @time_start_end_s.setter
    def time_start_end_s(self, value: str) -> None:
        DLL.ZkParticleEffectInstance_setTimeStartEndS(self._handle, value.encode("utf-8"))

    @property
    def m_bias_ambient_pfx(self) -> int:
        DLL.ZkParticleEffectInstance_getMBiasAmbientPfx.restype = c_int32
        return DLL.ZkParticleEffectInstance_getMBiasAmbientPfx(self._handle)

    @m_bias_ambient_pfx.setter
    def m_bias_ambient_pfx(self, value: int) -> None:
        DLL.ZkParticleEffectInstance_setMBiasAmbientPfx(self._handle, c_int32(value))
