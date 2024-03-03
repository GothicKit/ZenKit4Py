from zenkit.daedalus.base import DaedalusInstanceType
from zenkit.daedalus.camera import CameraInstance
from zenkit.daedalus.effect_base import EffectBaseInstance
from zenkit.daedalus.fightai import FightAiInstance
from zenkit.daedalus.focus import FocusInstance
from zenkit.daedalus.guildvalues import GuildValuesInstance
from zenkit.daedalus.info import InfoInstance
from zenkit.daedalus.item import ItemInstance
from zenkit.daedalus.item_react import ItemReactInstance
from zenkit.daedalus.menu import MenuInstance
from zenkit.daedalus.menu_item import MenuItemInstance
from zenkit.daedalus.mission import MissionInstance
from zenkit.daedalus.music_jingle import MusicJingleInstance
from zenkit.daedalus.music_system import MusicSystemInstance
from zenkit.daedalus.music_theme import MusicThemeInstance
from zenkit.daedalus.npc import NpcInstance
from zenkit.daedalus.particle_effect import ParticleEffectInstance
from zenkit.daedalus.particle_effect_emit_key import ParticleEffectEmitKeyInstance
from zenkit.daedalus.sound_effect import SoundEffectInstance
from zenkit.daedalus.sound_system import SoundSystemInstance
from zenkit.daedalus.spell_instance import SpellInstance
from zenkit.daedalus.svm import SvmInstance

_INSTANCES = {
    DaedalusInstanceType.GUILD_VALUES: GuildValuesInstance,
    DaedalusInstanceType.NPC: NpcInstance,
    DaedalusInstanceType.MISSION: MissionInstance,
    DaedalusInstanceType.ITEM: ItemInstance,
    DaedalusInstanceType.FOCUS: FocusInstance,
    DaedalusInstanceType.INFO: InfoInstance,
    DaedalusInstanceType.ITEM_REACT: ItemReactInstance,
    DaedalusInstanceType.SPELL: SpellInstance,
    DaedalusInstanceType.SVM: SvmInstance,
    DaedalusInstanceType.MENU: MenuInstance,
    DaedalusInstanceType.MENU_ITEM: MenuItemInstance,
    DaedalusInstanceType.CAMERA: CameraInstance,
    DaedalusInstanceType.MUSIC_SYSTEM: MusicSystemInstance,
    DaedalusInstanceType.MUSIC_THEME: MusicThemeInstance,
    DaedalusInstanceType.MUSIC_JINGLE: MusicJingleInstance,
    DaedalusInstanceType.PARTICLE_EFFECT: ParticleEffectInstance,
    DaedalusInstanceType.EFFECT_BASE: EffectBaseInstance,
    DaedalusInstanceType.PARTICLE_EFFECT_EMIT_KEY: ParticleEffectEmitKeyInstance,
    DaedalusInstanceType.FIGHT_AI: FightAiInstance,
    DaedalusInstanceType.SOUND_EFFECT: SoundEffectInstance,
    DaedalusInstanceType.SOUND_SYSTEM: SoundSystemInstance,
}
