from zenkit.vob.cutscene_camera import CameraTrajectoryFrame
from zenkit.vob.cutscene_camera import CutsceneCamera
from zenkit.vob.light import Light
from zenkit.vob.virtual_object import VirtualObject
from zenkit.vob.virtual_object import VobType

_VOBS: dict[VobType, type[VirtualObject]] = {
    VobType.zCCSCamera: CutsceneCamera,
    VobType.zCCamTrj_KeyFrame: CameraTrajectoryFrame,
    VobType.zCVobLight: Light,
}
