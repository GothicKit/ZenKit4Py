__all__ = ["GuildValuesInstance"]

from typing import Any

from zenkit.daedalus.base import DaedalusInstance


class GuildValuesInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    """TODO(lmichaelis):
    ZKC_API int32_t ZkGuildValuesInstance_getWaterDepthKnee(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setWaterDepthKnee(ZkGuildValuesInstance* slf, ZkSize i, int32_t waterDepthKnee);
    ZKC_API int32_t ZkGuildValuesInstance_getWaterDepthChest(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setWaterDepthChest(ZkGuildValuesInstance* slf, ZkSize i, int32_t waterDepthChest);
    ZKC_API int32_t ZkGuildValuesInstance_getJumpUpHeight(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setJumpUpHeight(ZkGuildValuesInstance* slf, ZkSize i, int32_t jumpUpHeight);
    ZKC_API int32_t ZkGuildValuesInstance_getSwimTime(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setSwimTime(ZkGuildValuesInstance* slf, ZkSize i, int32_t swimTime);
    ZKC_API int32_t ZkGuildValuesInstance_getDiveTime(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setDiveTime(ZkGuildValuesInstance* slf, ZkSize i, int32_t diveTime);
    ZKC_API int32_t ZkGuildValuesInstance_getStepHeight(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setStepHeight(ZkGuildValuesInstance* slf, ZkSize i, int32_t stepHeight);
    ZKC_API int32_t ZkGuildValuesInstance_getJumpLowHeight(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setJumpLowHeight(ZkGuildValuesInstance* slf, ZkSize i, int32_t jumpLowHeight);
    ZKC_API int32_t ZkGuildValuesInstance_getJumpMidHeight(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setJumpMidHeight(ZkGuildValuesInstance* slf, ZkSize i, int32_t jumpMidHeight);
    ZKC_API int32_t ZkGuildValuesInstance_getSlideAngle(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setSlideAngle(ZkGuildValuesInstance* slf, ZkSize i, int32_t slideAngle);
    ZKC_API int32_t ZkGuildValuesInstance_getSlideAngle2(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setSlideAngle2(ZkGuildValuesInstance* slf, ZkSize i, int32_t slideAngle2);
    ZKC_API int32_t ZkGuildValuesInstance_getDisableAutoRoll(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setDisableAutoRoll(ZkGuildValuesInstance* slf, ZkSize i, int32_t disableAutoRoll);
    ZKC_API int32_t ZkGuildValuesInstance_getSurfaceAlign(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setSurfaceAlign(ZkGuildValuesInstance* slf, ZkSize i, int32_t surfaceAlign);
    ZKC_API int32_t ZkGuildValuesInstance_getClimbHeadingAngle(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setClimbHeadingAngle(ZkGuildValuesInstance* slf, ZkSize i, int32_t climbHeadingAngle);
    ZKC_API int32_t ZkGuildValuesInstance_getClimbHorizAngle(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setClimbHorizAngle(ZkGuildValuesInstance* slf, ZkSize i, int32_t climbHorizAngle);
    ZKC_API int32_t ZkGuildValuesInstance_getClimbGroundAngle(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setClimbGroundAngle(ZkGuildValuesInstance* slf, ZkSize i, int32_t climbGroundAngle);
    ZKC_API int32_t ZkGuildValuesInstance_getFightRangeBase(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFightRangeBase(ZkGuildValuesInstance* slf, ZkSize i, int32_t fightRangeBase);
    ZKC_API int32_t ZkGuildValuesInstance_getFightRangeFist(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFightRangeFist(ZkGuildValuesInstance* slf, ZkSize i, int32_t fightRangeFist);
    ZKC_API int32_t ZkGuildValuesInstance_getFightRangeG(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFightRangeG(ZkGuildValuesInstance* slf, ZkSize i, int32_t fightRangeG);
    ZKC_API int32_t ZkGuildValuesInstance_getFightRange1Hs(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFightRange1Hs(ZkGuildValuesInstance* slf, ZkSize i, int32_t fightRange1Hs);
    ZKC_API int32_t ZkGuildValuesInstance_getFightRange1Ha(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFightRange1Ha(ZkGuildValuesInstance* slf, ZkSize i, int32_t fightRange1Ha);
    ZKC_API int32_t ZkGuildValuesInstance_getFightRange2Hs(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFightRange2Hs(ZkGuildValuesInstance* slf, ZkSize i, int32_t fightRange2Hs);
    ZKC_API int32_t ZkGuildValuesInstance_getFightRange2Ha(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFightRange2Ha(ZkGuildValuesInstance* slf, ZkSize i, int32_t fightRange2Ha);
    ZKC_API int32_t ZkGuildValuesInstance_getFallDownHeight(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFallDownHeight(ZkGuildValuesInstance* slf, ZkSize i, int32_t fallDownHeight);
    ZKC_API int32_t ZkGuildValuesInstance_getFallDownDamage(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setFallDownDamage(ZkGuildValuesInstance* slf, ZkSize i, int32_t fallDownDamage);
    ZKC_API int32_t ZkGuildValuesInstance_getBloodDisabled(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setBloodDisabled(ZkGuildValuesInstance* slf, ZkSize i, int32_t bloodDisabled);
    ZKC_API int32_t ZkGuildValuesInstance_getBloodMaxDistance(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setBloodMaxDistance(ZkGuildValuesInstance* slf, ZkSize i, int32_t bloodMaxDistance);
    ZKC_API int32_t ZkGuildValuesInstance_getBloodAmount(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setBloodAmount(ZkGuildValuesInstance* slf, ZkSize i, int32_t bloodAmount);
    ZKC_API int32_t ZkGuildValuesInstance_getBloodFlow(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setBloodFlow(ZkGuildValuesInstance* slf, ZkSize i, int32_t bloodFlow);
    ZKC_API int32_t ZkGuildValuesInstance_getTurnSpeed(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setTurnSpeed(ZkGuildValuesInstance* slf, ZkSize i, int32_t turnSpeed);
    ZKC_API ZkString ZkGuildValuesInstance_getBloodEmitter(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setBloodEmitter(ZkGuildValuesInstance* slf, ZkSize i, ZkString bloodEmitter);
    ZKC_API ZkString ZkGuildValuesInstance_getBloodTexture(ZkGuildValuesInstance const* slf, ZkSize i);
    ZKC_API void ZkGuildValuesInstance_setBloodTexture(ZkGuildValuesInstance* slf, ZkSize i, ZkString bloodTexture);
    """
