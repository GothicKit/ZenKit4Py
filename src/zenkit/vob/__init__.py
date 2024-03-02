from zenkit.vob.cutscene_camera import CameraTrajectoryFrame
from zenkit.vob.cutscene_camera import CutsceneCamera
from zenkit.vob.light import Light
from zenkit.vob.misc import Animate
from zenkit.vob.misc import CodeMaster
from zenkit.vob.misc import Earthquake
from zenkit.vob.misc import Item
from zenkit.vob.misc import MessageFilter
from zenkit.vob.misc import MoverController
from zenkit.vob.misc import ParticleEffectController
from zenkit.vob.misc import TouchDamage
from zenkit.vob.movable_object import Container
from zenkit.vob.movable_object import Door
from zenkit.vob.movable_object import Fire
from zenkit.vob.movable_object import InteractiveObject
from zenkit.vob.movable_object import MovableObject
from zenkit.vob.sound import Sound
from zenkit.vob.sound import SoundDaytime
from zenkit.vob.trigger import Mover
from zenkit.vob.trigger import Trigger
from zenkit.vob.trigger import TriggerChangeLevel
from zenkit.vob.trigger import TriggerList
from zenkit.vob.trigger import TriggerScript
from zenkit.vob.trigger import TriggerUntouch
from zenkit.vob.trigger import TriggerWorldStart
from zenkit.vob.virtual_object import VirtualObject
from zenkit.vob.virtual_object import VobType
from zenkit.vob.zone import ZoneFarPlane
from zenkit.vob.zone import ZoneFog
from zenkit.vob.zone import ZoneMusic

_VOBS: dict[VobType, type[VirtualObject]] = {
    VobType.zCVob: VirtualObject,
    VobType.zCVobScreenFX: VirtualObject,
    VobType.zCVobStair: VirtualObject,
    VobType.zCVobStartpoint: VirtualObject,
    VobType.zCVobSpot: VirtualObject,
    VobType.zCVobLevelCompo: VirtualObject,
    VobType.zCCSCamera: CutsceneCamera,
    VobType.zCCamTrj_KeyFrame: CameraTrajectoryFrame,
    VobType.zCVobLight: Light,
    VobType.zCVobAnimate: Animate,
    VobType.oCItem: Item,
    VobType.zCPFXController: ParticleEffectController,
    VobType.zCMessageFilter: MessageFilter,
    VobType.zCMoverController: MoverController,
    VobType.oCTouchDamage: TouchDamage,
    VobType.zCCodeMaster: CodeMaster,
    VobType.zCEarthquake: Earthquake,
    VobType.oCMOB: MovableObject,
    VobType.oCMobInter: InteractiveObject,
    VobType.oCMobBed: InteractiveObject,
    VobType.oCMobWheel: InteractiveObject,
    VobType.oCMobLadder: InteractiveObject,
    VobType.oCMobSwitch: InteractiveObject,
    VobType.oCMobContainer: Container,
    VobType.oCMobDoor: Door,
    VobType.oCMobFire: Fire,
    VobType.zCVobSound: Sound,
    VobType.zCVobSoundDaytime: SoundDaytime,
    VobType.zCTrigger: Trigger,
    VobType.zCTriggerList: TriggerList,
    VobType.oCTriggerScript: TriggerScript,
    VobType.oCTriggerChangeLevel: TriggerChangeLevel,
    VobType.zCTriggerWorldStart: TriggerWorldStart,
    VobType.zCTriggerUntouch: TriggerUntouch,
    VobType.zCMover: Mover,
    VobType.oCZoneMusic: ZoneMusic,
    VobType.oCZoneMusicDefault: ZoneMusic,
    VobType.zCZoneZFog: ZoneFog,
    VobType.zCZoneZFogDefault: ZoneFog,
    VobType.zCZoneVobFarPlane: ZoneFarPlane,
    VobType.zCZoneVobFarPlaneDefault: ZoneFarPlane,
}
