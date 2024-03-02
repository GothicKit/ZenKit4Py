__all__ = ["SvmInstance"]

from typing import Any

from zenkit._core import DLL
from zenkit._native import ZkString
from zenkit.daedalus.base import DaedalusInstance


class SvmInstance(DaedalusInstance):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def mil_greetings(self) -> str:
        DLL.ZkSvmInstance_getMilGreetings.restype = ZkString
        return DLL.ZkSvmInstance_getMilGreetings(self._handle).value

    @property
    def pal_greetings(self) -> str:
        DLL.ZkSvmInstance_getPalGreetings.restype = ZkString
        return DLL.ZkSvmInstance_getPalGreetings(self._handle).value

    @property
    def weather(self) -> str:
        DLL.ZkSvmInstance_getWeather.restype = ZkString
        return DLL.ZkSvmInstance_getWeather(self._handle).value

    @property
    def i_get_you_still(self) -> str:
        DLL.ZkSvmInstance_getIGetYouStill.restype = ZkString
        return DLL.ZkSvmInstance_getIGetYouStill(self._handle).value

    @property
    def die_enemy(self) -> str:
        DLL.ZkSvmInstance_getDieEnemy.restype = ZkString
        return DLL.ZkSvmInstance_getDieEnemy(self._handle).value

    @property
    def die_monster(self) -> str:
        DLL.ZkSvmInstance_getDieMonster.restype = ZkString
        return DLL.ZkSvmInstance_getDieMonster(self._handle).value

    @property
    def addon_die_monster(self) -> str:
        DLL.ZkSvmInstance_getAddonDieMonster.restype = ZkString
        return DLL.ZkSvmInstance_getAddonDieMonster(self._handle).value

    @property
    def addon_die_monster2(self) -> str:
        DLL.ZkSvmInstance_getAddonDieMonster2.restype = ZkString
        return DLL.ZkSvmInstance_getAddonDieMonster2(self._handle).value

    @property
    def dirty_thief(self) -> str:
        DLL.ZkSvmInstance_getDirtyThief.restype = ZkString
        return DLL.ZkSvmInstance_getDirtyThief(self._handle).value

    @property
    def hands_off(self) -> str:
        DLL.ZkSvmInstance_getHandsOff.restype = ZkString
        return DLL.ZkSvmInstance_getHandsOff(self._handle).value

    @property
    def sheep_killer(self) -> str:
        DLL.ZkSvmInstance_getSheepKiller.restype = ZkString
        return DLL.ZkSvmInstance_getSheepKiller(self._handle).value

    @property
    def sheep_killer_monster(self) -> str:
        DLL.ZkSvmInstance_getSheepKillerMonster.restype = ZkString
        return DLL.ZkSvmInstance_getSheepKillerMonster(self._handle).value

    @property
    def you_murderer(self) -> str:
        DLL.ZkSvmInstance_getYouMurderer.restype = ZkString
        return DLL.ZkSvmInstance_getYouMurderer(self._handle).value

    @property
    def die_stupid_beast(self) -> str:
        DLL.ZkSvmInstance_getDieStupidBeast.restype = ZkString
        return DLL.ZkSvmInstance_getDieStupidBeast(self._handle).value

    @property
    def you_dare_hit_me(self) -> str:
        DLL.ZkSvmInstance_getYouDareHitMe.restype = ZkString
        return DLL.ZkSvmInstance_getYouDareHitMe(self._handle).value

    @property
    def you_asked_for_it(self) -> str:
        DLL.ZkSvmInstance_getYouAskedForIt.restype = ZkString
        return DLL.ZkSvmInstance_getYouAskedForIt(self._handle).value

    @property
    def then_i_beat_you_out_of_here(self) -> str:
        DLL.ZkSvmInstance_getThenIBeatYouOutOfHere.restype = ZkString
        return DLL.ZkSvmInstance_getThenIBeatYouOutOfHere(self._handle).value

    @property
    def what_did_you_do_in_there(self) -> str:
        DLL.ZkSvmInstance_getWhatDidYouDoInThere.restype = ZkString
        return DLL.ZkSvmInstance_getWhatDidYouDoInThere(self._handle).value

    @property
    def will_you_stop_fighting(self) -> str:
        DLL.ZkSvmInstance_getWillYouStopFighting.restype = ZkString
        return DLL.ZkSvmInstance_getWillYouStopFighting(self._handle).value

    @property
    def kill_enemy(self) -> str:
        DLL.ZkSvmInstance_getKillEnemy.restype = ZkString
        return DLL.ZkSvmInstance_getKillEnemy(self._handle).value

    @property
    def enemy_killed(self) -> str:
        DLL.ZkSvmInstance_getEnemyKilled.restype = ZkString
        return DLL.ZkSvmInstance_getEnemyKilled(self._handle).value

    @property
    def monster_killed(self) -> str:
        DLL.ZkSvmInstance_getMonsterKilled.restype = ZkString
        return DLL.ZkSvmInstance_getMonsterKilled(self._handle).value

    @property
    def addon_monster_killed(self) -> str:
        DLL.ZkSvmInstance_getAddonMonsterKilled.restype = ZkString
        return DLL.ZkSvmInstance_getAddonMonsterKilled(self._handle).value

    @property
    def addon_monster_killed2(self) -> str:
        DLL.ZkSvmInstance_getAddonMonsterKilled2.restype = ZkString
        return DLL.ZkSvmInstance_getAddonMonsterKilled2(self._handle).value

    @property
    def thief_down(self) -> str:
        DLL.ZkSvmInstance_getThiefDown.restype = ZkString
        return DLL.ZkSvmInstance_getThiefDown(self._handle).value

    @property
    def rumfummler_down(self) -> str:
        DLL.ZkSvmInstance_getRumfummlerDown.restype = ZkString
        return DLL.ZkSvmInstance_getRumfummlerDown(self._handle).value

    @property
    def sheep_attacker_down(self) -> str:
        DLL.ZkSvmInstance_getSheepAttackerDown.restype = ZkString
        return DLL.ZkSvmInstance_getSheepAttackerDown(self._handle).value

    @property
    def kill_murderer(self) -> str:
        DLL.ZkSvmInstance_getKillMurderer.restype = ZkString
        return DLL.ZkSvmInstance_getKillMurderer(self._handle).value

    @property
    def stupid_beast_killed(self) -> str:
        DLL.ZkSvmInstance_getStupidBeastKilled.restype = ZkString
        return DLL.ZkSvmInstance_getStupidBeastKilled(self._handle).value

    @property
    def never_hit_me_again(self) -> str:
        DLL.ZkSvmInstance_getNeverHitMeAgain.restype = ZkString
        return DLL.ZkSvmInstance_getNeverHitMeAgain(self._handle).value

    @property
    def you_better_should_have_listened(self) -> str:
        DLL.ZkSvmInstance_getYouBetterShouldHaveListened.restype = ZkString
        return DLL.ZkSvmInstance_getYouBetterShouldHaveListened(self._handle).value

    @property
    def get_up_and_begone(self) -> str:
        DLL.ZkSvmInstance_getGetUpAndBegone.restype = ZkString
        return DLL.ZkSvmInstance_getGetUpAndBegone(self._handle).value

    @property
    def never_enter_room_again(self) -> str:
        DLL.ZkSvmInstance_getNeverEnterRoomAgain.restype = ZkString
        return DLL.ZkSvmInstance_getNeverEnterRoomAgain(self._handle).value

    @property
    def there_is_no_fighting_here(self) -> str:
        DLL.ZkSvmInstance_getThereIsNoFightingHere.restype = ZkString
        return DLL.ZkSvmInstance_getThereIsNoFightingHere(self._handle).value

    @property
    def spare_me(self) -> str:
        DLL.ZkSvmInstance_getSpareMe.restype = ZkString
        return DLL.ZkSvmInstance_getSpareMe(self._handle).value

    @property
    def run_away(self) -> str:
        DLL.ZkSvmInstance_getRunAway.restype = ZkString
        return DLL.ZkSvmInstance_getRunAway(self._handle).value

    @property
    def alarm(self) -> str:
        DLL.ZkSvmInstance_getAlarm.restype = ZkString
        return DLL.ZkSvmInstance_getAlarm(self._handle).value

    @property
    def guards(self) -> str:
        DLL.ZkSvmInstance_getGuards.restype = ZkString
        return DLL.ZkSvmInstance_getGuards(self._handle).value

    @property
    def help(self) -> str:
        DLL.ZkSvmInstance_getHelp.restype = ZkString
        return DLL.ZkSvmInstance_getHelp(self._handle).value

    @property
    def good_monster_kill(self) -> str:
        DLL.ZkSvmInstance_getGoodMonsterKill.restype = ZkString
        return DLL.ZkSvmInstance_getGoodMonsterKill(self._handle).value

    @property
    def good_kill(self) -> str:
        DLL.ZkSvmInstance_getGoodKill.restype = ZkString
        return DLL.ZkSvmInstance_getGoodKill(self._handle).value

    @property
    def not_now(self) -> str:
        DLL.ZkSvmInstance_getNotNow.restype = ZkString
        return DLL.ZkSvmInstance_getNotNow(self._handle).value

    @property
    def run_coward(self) -> str:
        DLL.ZkSvmInstance_getRunCoward.restype = ZkString
        return DLL.ZkSvmInstance_getRunCoward(self._handle).value

    @property
    def get_out_of_here(self) -> str:
        DLL.ZkSvmInstance_getGetOutOfHere.restype = ZkString
        return DLL.ZkSvmInstance_getGetOutOfHere(self._handle).value

    @property
    def why_are_you_in_here(self) -> str:
        DLL.ZkSvmInstance_getWhyAreYouInHere.restype = ZkString
        return DLL.ZkSvmInstance_getWhyAreYouInHere(self._handle).value

    @property
    def yes_go_out_of_here(self) -> str:
        DLL.ZkSvmInstance_getYesGoOutOfHere.restype = ZkString
        return DLL.ZkSvmInstance_getYesGoOutOfHere(self._handle).value

    @property
    def whats_this_supposed_to_be(self) -> str:
        DLL.ZkSvmInstance_getWhatsThisSupposedToBe.restype = ZkString
        return DLL.ZkSvmInstance_getWhatsThisSupposedToBe(self._handle).value

    @property
    def you_disturbed_my_slumber(self) -> str:
        DLL.ZkSvmInstance_getYouDisturbedMySlumber.restype = ZkString
        return DLL.ZkSvmInstance_getYouDisturbedMySlumber(self._handle).value

    @property
    def i_took_your_gold(self) -> str:
        DLL.ZkSvmInstance_getITookYourGold.restype = ZkString
        return DLL.ZkSvmInstance_getITookYourGold(self._handle).value

    @property
    def shit_no_gold(self) -> str:
        DLL.ZkSvmInstance_getShitNoGold.restype = ZkString
        return DLL.ZkSvmInstance_getShitNoGold(self._handle).value

    @property
    def i_take_your_weapon(self) -> str:
        DLL.ZkSvmInstance_getITakeYourWeapon.restype = ZkString
        return DLL.ZkSvmInstance_getITakeYourWeapon(self._handle).value

    @property
    def what_are_you_doing(self) -> str:
        DLL.ZkSvmInstance_getWhatAreYouDoing.restype = ZkString
        return DLL.ZkSvmInstance_getWhatAreYouDoing(self._handle).value

    @property
    def looking_for_trouble_again(self) -> str:
        DLL.ZkSvmInstance_getLookingForTroubleAgain.restype = ZkString
        return DLL.ZkSvmInstance_getLookingForTroubleAgain(self._handle).value

    @property
    def stop_magic(self) -> str:
        DLL.ZkSvmInstance_getStopMagic.restype = ZkString
        return DLL.ZkSvmInstance_getStopMagic(self._handle).value

    @property
    def i_said_stop_magic(self) -> str:
        DLL.ZkSvmInstance_getISaidStopMagic.restype = ZkString
        return DLL.ZkSvmInstance_getISaidStopMagic(self._handle).value

    @property
    def weapon_down(self) -> str:
        DLL.ZkSvmInstance_getWeaponDown.restype = ZkString
        return DLL.ZkSvmInstance_getWeaponDown(self._handle).value

    @property
    def i_said_weapon_down(self) -> str:
        DLL.ZkSvmInstance_getISaidWeaponDown.restype = ZkString
        return DLL.ZkSvmInstance_getISaidWeaponDown(self._handle).value

    @property
    def wise_move(self) -> str:
        DLL.ZkSvmInstance_getWiseMove.restype = ZkString
        return DLL.ZkSvmInstance_getWiseMove(self._handle).value

    @property
    def next_time_youre_in_for_it(self) -> str:
        DLL.ZkSvmInstance_getNextTimeYoureInForIt.restype = ZkString
        return DLL.ZkSvmInstance_getNextTimeYoureInForIt(self._handle).value

    @property
    def oh_my_head(self) -> str:
        DLL.ZkSvmInstance_getOhMyHead.restype = ZkString
        return DLL.ZkSvmInstance_getOhMyHead(self._handle).value

    @property
    def theres_a_fight(self) -> str:
        DLL.ZkSvmInstance_getTheresAFight.restype = ZkString
        return DLL.ZkSvmInstance_getTheresAFight(self._handle).value

    @property
    def oh_my_god_its_a_fight(self) -> str:
        DLL.ZkSvmInstance_getOhMyGodItsAFight.restype = ZkString
        return DLL.ZkSvmInstance_getOhMyGodItsAFight(self._handle).value

    @property
    def good_victory(self) -> str:
        DLL.ZkSvmInstance_getGoodVictory.restype = ZkString
        return DLL.ZkSvmInstance_getGoodVictory(self._handle).value

    @property
    def not_bad(self) -> str:
        DLL.ZkSvmInstance_getNotBad.restype = ZkString
        return DLL.ZkSvmInstance_getNotBad(self._handle).value

    @property
    def oh_my_god_hes_down(self) -> str:
        DLL.ZkSvmInstance_getOhMyGodHesDown.restype = ZkString
        return DLL.ZkSvmInstance_getOhMyGodHesDown(self._handle).value

    @property
    def cheer_friend01(self) -> str:
        DLL.ZkSvmInstance_getCheerFriend01.restype = ZkString
        return DLL.ZkSvmInstance_getCheerFriend01(self._handle).value

    @property
    def cheer_friend02(self) -> str:
        DLL.ZkSvmInstance_getCheerFriend02.restype = ZkString
        return DLL.ZkSvmInstance_getCheerFriend02(self._handle).value

    @property
    def cheer_friend03(self) -> str:
        DLL.ZkSvmInstance_getCheerFriend03.restype = ZkString
        return DLL.ZkSvmInstance_getCheerFriend03(self._handle).value

    @property
    def ooh01(self) -> str:
        DLL.ZkSvmInstance_getOoh01.restype = ZkString
        return DLL.ZkSvmInstance_getOoh01(self._handle).value

    @property
    def ooh02(self) -> str:
        DLL.ZkSvmInstance_getOoh02.restype = ZkString
        return DLL.ZkSvmInstance_getOoh02(self._handle).value

    @property
    def ooh03(self) -> str:
        DLL.ZkSvmInstance_getOoh03.restype = ZkString
        return DLL.ZkSvmInstance_getOoh03(self._handle).value

    @property
    def what_was_that(self) -> str:
        DLL.ZkSvmInstance_getWhatWasThat.restype = ZkString
        return DLL.ZkSvmInstance_getWhatWasThat(self._handle).value

    @property
    def get_out_of_my_bed(self) -> str:
        DLL.ZkSvmInstance_getGetOutOfMyBed.restype = ZkString
        return DLL.ZkSvmInstance_getGetOutOfMyBed(self._handle).value

    @property
    def awake(self) -> str:
        DLL.ZkSvmInstance_getAwake.restype = ZkString
        return DLL.ZkSvmInstance_getAwake(self._handle).value

    @property
    def abs_commander(self) -> str:
        DLL.ZkSvmInstance_getAbsCommander.restype = ZkString
        return DLL.ZkSvmInstance_getAbsCommander(self._handle).value

    @property
    def abs_monastery(self) -> str:
        DLL.ZkSvmInstance_getAbsMonastery.restype = ZkString
        return DLL.ZkSvmInstance_getAbsMonastery(self._handle).value

    @property
    def abs_farm(self) -> str:
        DLL.ZkSvmInstance_getAbsFarm.restype = ZkString
        return DLL.ZkSvmInstance_getAbsFarm(self._handle).value

    @property
    def abs_good(self) -> str:
        DLL.ZkSvmInstance_getAbsGood.restype = ZkString
        return DLL.ZkSvmInstance_getAbsGood(self._handle).value

    @property
    def sheep_killer_crime(self) -> str:
        DLL.ZkSvmInstance_getSheepKillerCrime.restype = ZkString
        return DLL.ZkSvmInstance_getSheepKillerCrime(self._handle).value

    @property
    def attack_crime(self) -> str:
        DLL.ZkSvmInstance_getAttackCrime.restype = ZkString
        return DLL.ZkSvmInstance_getAttackCrime(self._handle).value

    @property
    def theft_crime(self) -> str:
        DLL.ZkSvmInstance_getTheftCrime.restype = ZkString
        return DLL.ZkSvmInstance_getTheftCrime(self._handle).value

    @property
    def murder_crime(self) -> str:
        DLL.ZkSvmInstance_getMurderCrime.restype = ZkString
        return DLL.ZkSvmInstance_getMurderCrime(self._handle).value

    @property
    def pal_city_crime(self) -> str:
        DLL.ZkSvmInstance_getPalCityCrime.restype = ZkString
        return DLL.ZkSvmInstance_getPalCityCrime(self._handle).value

    @property
    def mil_city_crime(self) -> str:
        DLL.ZkSvmInstance_getMilCityCrime.restype = ZkString
        return DLL.ZkSvmInstance_getMilCityCrime(self._handle).value

    @property
    def city_crime(self) -> str:
        DLL.ZkSvmInstance_getCityCrime.restype = ZkString
        return DLL.ZkSvmInstance_getCityCrime(self._handle).value

    @property
    def mona_crime(self) -> str:
        DLL.ZkSvmInstance_getMonaCrime.restype = ZkString
        return DLL.ZkSvmInstance_getMonaCrime(self._handle).value

    @property
    def farm_crime(self) -> str:
        DLL.ZkSvmInstance_getFarmCrime.restype = ZkString
        return DLL.ZkSvmInstance_getFarmCrime(self._handle).value

    @property
    def oc_crime(self) -> str:
        DLL.ZkSvmInstance_getOcCrime.restype = ZkString
        return DLL.ZkSvmInstance_getOcCrime(self._handle).value

    @property
    def toughguy_attack_lost(self) -> str:
        DLL.ZkSvmInstance_getToughguyAttackLost.restype = ZkString
        return DLL.ZkSvmInstance_getToughguyAttackLost(self._handle).value

    @property
    def toughguy_attack_won(self) -> str:
        DLL.ZkSvmInstance_getToughguyAttackWon.restype = ZkString
        return DLL.ZkSvmInstance_getToughguyAttackWon(self._handle).value

    @property
    def toughguy_player_attack(self) -> str:
        DLL.ZkSvmInstance_getToughguyPlayerAttack.restype = ZkString
        return DLL.ZkSvmInstance_getToughguyPlayerAttack(self._handle).value

    @property
    def gold1000(self) -> str:
        DLL.ZkSvmInstance_getGold1000.restype = ZkString
        return DLL.ZkSvmInstance_getGold1000(self._handle).value

    @property
    def gold950(self) -> str:
        DLL.ZkSvmInstance_getGold950.restype = ZkString
        return DLL.ZkSvmInstance_getGold950(self._handle).value

    @property
    def gold900(self) -> str:
        DLL.ZkSvmInstance_getGold900.restype = ZkString
        return DLL.ZkSvmInstance_getGold900(self._handle).value

    @property
    def gold850(self) -> str:
        DLL.ZkSvmInstance_getGold850.restype = ZkString
        return DLL.ZkSvmInstance_getGold850(self._handle).value

    @property
    def gold800(self) -> str:
        DLL.ZkSvmInstance_getGold800.restype = ZkString
        return DLL.ZkSvmInstance_getGold800(self._handle).value

    @property
    def gold750(self) -> str:
        DLL.ZkSvmInstance_getGold750.restype = ZkString
        return DLL.ZkSvmInstance_getGold750(self._handle).value

    @property
    def gold700(self) -> str:
        DLL.ZkSvmInstance_getGold700.restype = ZkString
        return DLL.ZkSvmInstance_getGold700(self._handle).value

    @property
    def gold650(self) -> str:
        DLL.ZkSvmInstance_getGold650.restype = ZkString
        return DLL.ZkSvmInstance_getGold650(self._handle).value

    @property
    def gold600(self) -> str:
        DLL.ZkSvmInstance_getGold600.restype = ZkString
        return DLL.ZkSvmInstance_getGold600(self._handle).value

    @property
    def gold550(self) -> str:
        DLL.ZkSvmInstance_getGold550.restype = ZkString
        return DLL.ZkSvmInstance_getGold550(self._handle).value

    @property
    def gold500(self) -> str:
        DLL.ZkSvmInstance_getGold500.restype = ZkString
        return DLL.ZkSvmInstance_getGold500(self._handle).value

    @property
    def gold450(self) -> str:
        DLL.ZkSvmInstance_getGold450.restype = ZkString
        return DLL.ZkSvmInstance_getGold450(self._handle).value

    @property
    def gold400(self) -> str:
        DLL.ZkSvmInstance_getGold400.restype = ZkString
        return DLL.ZkSvmInstance_getGold400(self._handle).value

    @property
    def gold350(self) -> str:
        DLL.ZkSvmInstance_getGold350.restype = ZkString
        return DLL.ZkSvmInstance_getGold350(self._handle).value

    @property
    def gold300(self) -> str:
        DLL.ZkSvmInstance_getGold300.restype = ZkString
        return DLL.ZkSvmInstance_getGold300(self._handle).value

    @property
    def gold250(self) -> str:
        DLL.ZkSvmInstance_getGold250.restype = ZkString
        return DLL.ZkSvmInstance_getGold250(self._handle).value

    @property
    def gold200(self) -> str:
        DLL.ZkSvmInstance_getGold200.restype = ZkString
        return DLL.ZkSvmInstance_getGold200(self._handle).value

    @property
    def gold150(self) -> str:
        DLL.ZkSvmInstance_getGold150.restype = ZkString
        return DLL.ZkSvmInstance_getGold150(self._handle).value

    @property
    def gold100(self) -> str:
        DLL.ZkSvmInstance_getGold100.restype = ZkString
        return DLL.ZkSvmInstance_getGold100(self._handle).value

    @property
    def gold90(self) -> str:
        DLL.ZkSvmInstance_getGold90.restype = ZkString
        return DLL.ZkSvmInstance_getGold90(self._handle).value

    @property
    def gold80(self) -> str:
        DLL.ZkSvmInstance_getGold80.restype = ZkString
        return DLL.ZkSvmInstance_getGold80(self._handle).value

    @property
    def gold70(self) -> str:
        DLL.ZkSvmInstance_getGold70.restype = ZkString
        return DLL.ZkSvmInstance_getGold70(self._handle).value

    @property
    def gold60(self) -> str:
        DLL.ZkSvmInstance_getGold60.restype = ZkString
        return DLL.ZkSvmInstance_getGold60(self._handle).value

    @property
    def gold50(self) -> str:
        DLL.ZkSvmInstance_getGold50.restype = ZkString
        return DLL.ZkSvmInstance_getGold50(self._handle).value

    @property
    def gold40(self) -> str:
        DLL.ZkSvmInstance_getGold40.restype = ZkString
        return DLL.ZkSvmInstance_getGold40(self._handle).value

    @property
    def gold30(self) -> str:
        DLL.ZkSvmInstance_getGold30.restype = ZkString
        return DLL.ZkSvmInstance_getGold30(self._handle).value

    @property
    def gold20(self) -> str:
        DLL.ZkSvmInstance_getGold20.restype = ZkString
        return DLL.ZkSvmInstance_getGold20(self._handle).value

    @property
    def gold10(self) -> str:
        DLL.ZkSvmInstance_getGold10.restype = ZkString
        return DLL.ZkSvmInstance_getGold10(self._handle).value

    @property
    def smalltalk01(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk01.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk01(self._handle).value

    @property
    def smalltalk02(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk02.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk02(self._handle).value

    @property
    def smalltalk03(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk03.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk03(self._handle).value

    @property
    def smalltalk04(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk04.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk04(self._handle).value

    @property
    def smalltalk05(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk05.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk05(self._handle).value

    @property
    def smalltalk06(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk06.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk06(self._handle).value

    @property
    def smalltalk07(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk07.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk07(self._handle).value

    @property
    def smalltalk08(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk08.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk08(self._handle).value

    @property
    def smalltalk09(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk09.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk09(self._handle).value

    @property
    def smalltalk10(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk10.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk10(self._handle).value

    @property
    def smalltalk11(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk11.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk11(self._handle).value

    @property
    def smalltalk12(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk12.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk12(self._handle).value

    @property
    def smalltalk13(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk13.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk13(self._handle).value

    @property
    def smalltalk14(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk14.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk14(self._handle).value

    @property
    def smalltalk15(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk15.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk15(self._handle).value

    @property
    def smalltalk16(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk16.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk16(self._handle).value

    @property
    def smalltalk17(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk17.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk17(self._handle).value

    @property
    def smalltalk18(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk18.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk18(self._handle).value

    @property
    def smalltalk19(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk19.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk19(self._handle).value

    @property
    def smalltalk20(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk20.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk20(self._handle).value

    @property
    def smalltalk21(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk21.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk21(self._handle).value

    @property
    def smalltalk22(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk22.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk22(self._handle).value

    @property
    def smalltalk23(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk23.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk23(self._handle).value

    @property
    def smalltalk24(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk24.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk24(self._handle).value

    @property
    def smalltalk25(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk25.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk25(self._handle).value

    @property
    def smalltalk26(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk26.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk26(self._handle).value

    @property
    def smalltalk27(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk27.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk27(self._handle).value

    @property
    def smalltalk28(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk28.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk28(self._handle).value

    @property
    def smalltalk29(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk29.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk29(self._handle).value

    @property
    def smalltalk30(self) -> str:
        DLL.ZkSvmInstance_getSmalltalk30.restype = ZkString
        return DLL.ZkSvmInstance_getSmalltalk30(self._handle).value

    @property
    def no_learn_no_points(self) -> str:
        DLL.ZkSvmInstance_getNoLearnNoPoints.restype = ZkString
        return DLL.ZkSvmInstance_getNoLearnNoPoints(self._handle).value

    @property
    def no_learn_over_personal_max(self) -> str:
        DLL.ZkSvmInstance_getNoLearnOverPersonalMax.restype = ZkString
        return DLL.ZkSvmInstance_getNoLearnOverPersonalMax(self._handle).value

    @property
    def no_learn_youre_better(self) -> str:
        DLL.ZkSvmInstance_getNoLearnYoureBetter.restype = ZkString
        return DLL.ZkSvmInstance_getNoLearnYoureBetter(self._handle).value

    @property
    def you_learned_something(self) -> str:
        DLL.ZkSvmInstance_getYouLearnedSomething.restype = ZkString
        return DLL.ZkSvmInstance_getYouLearnedSomething(self._handle).value

    @property
    def unterstadt(self) -> str:
        DLL.ZkSvmInstance_getUnterstadt.restype = ZkString
        return DLL.ZkSvmInstance_getUnterstadt(self._handle).value

    @property
    def oberstadt(self) -> str:
        DLL.ZkSvmInstance_getOberstadt.restype = ZkString
        return DLL.ZkSvmInstance_getOberstadt(self._handle).value

    @property
    def tempel(self) -> str:
        DLL.ZkSvmInstance_getTempel.restype = ZkString
        return DLL.ZkSvmInstance_getTempel(self._handle).value

    @property
    def markt(self) -> str:
        DLL.ZkSvmInstance_getMarkt.restype = ZkString
        return DLL.ZkSvmInstance_getMarkt(self._handle).value

    @property
    def galgen(self) -> str:
        DLL.ZkSvmInstance_getGalgen.restype = ZkString
        return DLL.ZkSvmInstance_getGalgen(self._handle).value

    @property
    def kaserne(self) -> str:
        DLL.ZkSvmInstance_getKaserne.restype = ZkString
        return DLL.ZkSvmInstance_getKaserne(self._handle).value

    @property
    def hafen(self) -> str:
        DLL.ZkSvmInstance_getHafen.restype = ZkString
        return DLL.ZkSvmInstance_getHafen(self._handle).value

    @property
    def whereto(self) -> str:
        DLL.ZkSvmInstance_getWhereto.restype = ZkString
        return DLL.ZkSvmInstance_getWhereto(self._handle).value

    @property
    def oberstadt2_unterstadt(self) -> str:
        DLL.ZkSvmInstance_getOberstadt2Unterstadt.restype = ZkString
        return DLL.ZkSvmInstance_getOberstadt2Unterstadt(self._handle).value

    @property
    def unterstadt2_oberstadt(self) -> str:
        DLL.ZkSvmInstance_getUnterstadt2Oberstadt.restype = ZkString
        return DLL.ZkSvmInstance_getUnterstadt2Oberstadt(self._handle).value

    @property
    def unterstadt2_tempel(self) -> str:
        DLL.ZkSvmInstance_getUnterstadt2Tempel.restype = ZkString
        return DLL.ZkSvmInstance_getUnterstadt2Tempel(self._handle).value

    @property
    def unterstadt2_hafen(self) -> str:
        DLL.ZkSvmInstance_getUnterstadt2Hafen.restype = ZkString
        return DLL.ZkSvmInstance_getUnterstadt2Hafen(self._handle).value

    @property
    def tempel2_unterstadt(self) -> str:
        DLL.ZkSvmInstance_getTempel2Unterstadt.restype = ZkString
        return DLL.ZkSvmInstance_getTempel2Unterstadt(self._handle).value

    @property
    def tempel2_markt(self) -> str:
        DLL.ZkSvmInstance_getTempel2Markt.restype = ZkString
        return DLL.ZkSvmInstance_getTempel2Markt(self._handle).value

    @property
    def tempel2_galgen(self) -> str:
        DLL.ZkSvmInstance_getTempel2Galgen.restype = ZkString
        return DLL.ZkSvmInstance_getTempel2Galgen(self._handle).value

    @property
    def markt2_tempel(self) -> str:
        DLL.ZkSvmInstance_getMarkt2Tempel.restype = ZkString
        return DLL.ZkSvmInstance_getMarkt2Tempel(self._handle).value

    @property
    def markt2_kaserne(self) -> str:
        DLL.ZkSvmInstance_getMarkt2Kaserne.restype = ZkString
        return DLL.ZkSvmInstance_getMarkt2Kaserne(self._handle).value

    @property
    def markt2_galgen(self) -> str:
        DLL.ZkSvmInstance_getMarkt2Galgen.restype = ZkString
        return DLL.ZkSvmInstance_getMarkt2Galgen(self._handle).value

    @property
    def galgen2_tempel(self) -> str:
        DLL.ZkSvmInstance_getGalgen2Tempel.restype = ZkString
        return DLL.ZkSvmInstance_getGalgen2Tempel(self._handle).value

    @property
    def galgen2_markt(self) -> str:
        DLL.ZkSvmInstance_getGalgen2Markt.restype = ZkString
        return DLL.ZkSvmInstance_getGalgen2Markt(self._handle).value

    @property
    def galgen2_kaserne(self) -> str:
        DLL.ZkSvmInstance_getGalgen2Kaserne.restype = ZkString
        return DLL.ZkSvmInstance_getGalgen2Kaserne(self._handle).value

    @property
    def kaserne2_markt(self) -> str:
        DLL.ZkSvmInstance_getKaserne2Markt.restype = ZkString
        return DLL.ZkSvmInstance_getKaserne2Markt(self._handle).value

    @property
    def kaserne2_galgen(self) -> str:
        DLL.ZkSvmInstance_getKaserne2Galgen.restype = ZkString
        return DLL.ZkSvmInstance_getKaserne2Galgen(self._handle).value

    @property
    def hafen2_unterstadt(self) -> str:
        DLL.ZkSvmInstance_getHafen2Unterstadt.restype = ZkString
        return DLL.ZkSvmInstance_getHafen2Unterstadt(self._handle).value

    @property
    def dead(self) -> str:
        DLL.ZkSvmInstance_getDead.restype = ZkString
        return DLL.ZkSvmInstance_getDead(self._handle).value

    @property
    def aargh1(self) -> str:
        DLL.ZkSvmInstance_getAargh1.restype = ZkString
        return DLL.ZkSvmInstance_getAargh1(self._handle).value

    @property
    def aargh2(self) -> str:
        DLL.ZkSvmInstance_getAargh2.restype = ZkString
        return DLL.ZkSvmInstance_getAargh2(self._handle).value

    @property
    def aargh3(self) -> str:
        DLL.ZkSvmInstance_getAargh3.restype = ZkString
        return DLL.ZkSvmInstance_getAargh3(self._handle).value

    @property
    def addon_wrong_armor(self) -> str:
        DLL.ZkSvmInstance_getAddonWrongArmor.restype = ZkString
        return DLL.ZkSvmInstance_getAddonWrongArmor(self._handle).value

    @property
    def addon_wrong_armor_sld(self) -> str:
        DLL.ZkSvmInstance_getAddonWrongArmorSld.restype = ZkString
        return DLL.ZkSvmInstance_getAddonWrongArmorSld(self._handle).value

    @property
    def addon_wrong_armor_mil(self) -> str:
        DLL.ZkSvmInstance_getAddonWrongArmorMil.restype = ZkString
        return DLL.ZkSvmInstance_getAddonWrongArmorMil(self._handle).value

    @property
    def addon_wrong_armor_kdf(self) -> str:
        DLL.ZkSvmInstance_getAddonWrongArmorKdf.restype = ZkString
        return DLL.ZkSvmInstance_getAddonWrongArmorKdf(self._handle).value

    @property
    def addon_no_armor_bdt(self) -> str:
        DLL.ZkSvmInstance_getAddonNoArmorBdt.restype = ZkString
        return DLL.ZkSvmInstance_getAddonNoArmorBdt(self._handle).value

    @property
    def addon_die_bandit(self) -> str:
        DLL.ZkSvmInstance_getAddonDieBandit.restype = ZkString
        return DLL.ZkSvmInstance_getAddonDieBandit(self._handle).value

    @property
    def addon_dirty_pirate(self) -> str:
        DLL.ZkSvmInstance_getAddonDirtyPirate.restype = ZkString
        return DLL.ZkSvmInstance_getAddonDirtyPirate(self._handle).value

    @property
    def sc_hey_turn_around(self) -> str:
        DLL.ZkSvmInstance_getScHeyTurnAround.restype = ZkString
        return DLL.ZkSvmInstance_getScHeyTurnAround(self._handle).value

    @property
    def sc_hey_turn_around02(self) -> str:
        DLL.ZkSvmInstance_getScHeyTurnAround02.restype = ZkString
        return DLL.ZkSvmInstance_getScHeyTurnAround02(self._handle).value

    @property
    def sc_hey_turn_around03(self) -> str:
        DLL.ZkSvmInstance_getScHeyTurnAround03.restype = ZkString
        return DLL.ZkSvmInstance_getScHeyTurnAround03(self._handle).value

    @property
    def sc_hey_turn_around04(self) -> str:
        DLL.ZkSvmInstance_getScHeyTurnAround04.restype = ZkString
        return DLL.ZkSvmInstance_getScHeyTurnAround04(self._handle).value

    @property
    def sc_hey_wait_a_second(self) -> str:
        DLL.ZkSvmInstance_getScHeyWaitASecond.restype = ZkString
        return DLL.ZkSvmInstance_getScHeyWaitASecond(self._handle).value

    @property
    def doesnt_mork(self) -> str:
        DLL.ZkSvmInstance_getDoesntMork.restype = ZkString
        return DLL.ZkSvmInstance_getDoesntMork(self._handle).value

    @property
    def pick_broke(self) -> str:
        DLL.ZkSvmInstance_getPickBroke.restype = ZkString
        return DLL.ZkSvmInstance_getPickBroke(self._handle).value

    @property
    def need_key(self) -> str:
        DLL.ZkSvmInstance_getNeedKey.restype = ZkString
        return DLL.ZkSvmInstance_getNeedKey(self._handle).value

    @property
    def no_more_picks(self) -> str:
        DLL.ZkSvmInstance_getNoMorePicks.restype = ZkString
        return DLL.ZkSvmInstance_getNoMorePicks(self._handle).value

    @property
    def no_pick_lock_talent(self) -> str:
        DLL.ZkSvmInstance_getNoPickLockTalent.restype = ZkString
        return DLL.ZkSvmInstance_getNoPickLockTalent(self._handle).value

    @property
    def no_sweeping(self) -> str:
        DLL.ZkSvmInstance_getNoSweeping.restype = ZkString
        return DLL.ZkSvmInstance_getNoSweeping(self._handle).value

    @property
    def pick_lock_or_key_missing(self) -> str:
        DLL.ZkSvmInstance_getPickLockOrKeyMissing.restype = ZkString
        return DLL.ZkSvmInstance_getPickLockOrKeyMissing(self._handle).value

    @property
    def key_missing(self) -> str:
        DLL.ZkSvmInstance_getKeyMissing.restype = ZkString
        return DLL.ZkSvmInstance_getKeyMissing(self._handle).value

    @property
    def pick_lock_missing(self) -> str:
        DLL.ZkSvmInstance_getPickLockMissing.restype = ZkString
        return DLL.ZkSvmInstance_getPickLockMissing(self._handle).value

    @property
    def never_open(self) -> str:
        DLL.ZkSvmInstance_getNeverOpen.restype = ZkString
        return DLL.ZkSvmInstance_getNeverOpen(self._handle).value

    @property
    def missing_item(self) -> str:
        DLL.ZkSvmInstance_getMissingItem.restype = ZkString
        return DLL.ZkSvmInstance_getMissingItem(self._handle).value

    @property
    def dont_know(self) -> str:
        DLL.ZkSvmInstance_getDontKnow.restype = ZkString
        return DLL.ZkSvmInstance_getDontKnow(self._handle).value

    @property
    def nothing_to_get(self) -> str:
        DLL.ZkSvmInstance_getNothingToGet.restype = ZkString
        return DLL.ZkSvmInstance_getNothingToGet(self._handle).value

    @property
    def nothing_to_get02(self) -> str:
        DLL.ZkSvmInstance_getNothingToGet02.restype = ZkString
        return DLL.ZkSvmInstance_getNothingToGet02(self._handle).value

    @property
    def nothing_to_get03(self) -> str:
        DLL.ZkSvmInstance_getNothingToGet03.restype = ZkString
        return DLL.ZkSvmInstance_getNothingToGet03(self._handle).value

    @property
    def heal_shrine(self) -> str:
        DLL.ZkSvmInstance_getHealShrine.restype = ZkString
        return DLL.ZkSvmInstance_getHealShrine(self._handle).value

    @property
    def heal_last_shrine(self) -> str:
        DLL.ZkSvmInstance_getHealLastShrine.restype = ZkString
        return DLL.ZkSvmInstance_getHealLastShrine(self._handle).value

    @property
    def irdorath_there_you_are(self) -> str:
        DLL.ZkSvmInstance_getIrdorathThereYouAre.restype = ZkString
        return DLL.ZkSvmInstance_getIrdorathThereYouAre(self._handle).value

    @property
    def sc_opens_irdorath_book(self) -> str:
        DLL.ZkSvmInstance_getScOpensIrdorathBook.restype = ZkString
        return DLL.ZkSvmInstance_getScOpensIrdorathBook(self._handle).value

    @property
    def sc_opens_last_door(self) -> str:
        DLL.ZkSvmInstance_getScOpensLastDoor.restype = ZkString
        return DLL.ZkSvmInstance_getScOpensLastDoor(self._handle).value

    @property
    def trade1(self) -> str:
        DLL.ZkSvmInstance_getTrade1.restype = ZkString
        return DLL.ZkSvmInstance_getTrade1(self._handle).value

    @property
    def trade2(self) -> str:
        DLL.ZkSvmInstance_getTrade2.restype = ZkString
        return DLL.ZkSvmInstance_getTrade2(self._handle).value

    @property
    def trade3(self) -> str:
        DLL.ZkSvmInstance_getTrade3.restype = ZkString
        return DLL.ZkSvmInstance_getTrade3(self._handle).value

    @property
    def verstehe(self) -> str:
        DLL.ZkSvmInstance_getVerstehe.restype = ZkString
        return DLL.ZkSvmInstance_getVerstehe(self._handle).value

    @property
    def found_treasure(self) -> str:
        DLL.ZkSvmInstance_getFoundTreasure.restype = ZkString
        return DLL.ZkSvmInstance_getFoundTreasure(self._handle).value

    @property
    def cant_understand_this(self) -> str:
        DLL.ZkSvmInstance_getCantUnderstandThis.restype = ZkString
        return DLL.ZkSvmInstance_getCantUnderstandThis(self._handle).value

    @property
    def cant_read_this(self) -> str:
        DLL.ZkSvmInstance_getCantReadThis.restype = ZkString
        return DLL.ZkSvmInstance_getCantReadThis(self._handle).value

    @property
    def stoneplate1(self) -> str:
        DLL.ZkSvmInstance_getStoneplate1.restype = ZkString
        return DLL.ZkSvmInstance_getStoneplate1(self._handle).value

    @property
    def stoneplate2(self) -> str:
        DLL.ZkSvmInstance_getStoneplate2.restype = ZkString
        return DLL.ZkSvmInstance_getStoneplate2(self._handle).value

    @property
    def stoneplate3(self) -> str:
        DLL.ZkSvmInstance_getStoneplate3.restype = ZkString
        return DLL.ZkSvmInstance_getStoneplate3(self._handle).value

    @property
    def cough(self) -> str:
        DLL.ZkSvmInstance_getCough.restype = ZkString
        return DLL.ZkSvmInstance_getCough(self._handle).value

    @property
    def hui(self) -> str:
        DLL.ZkSvmInstance_getHui.restype = ZkString
        return DLL.ZkSvmInstance_getHui(self._handle).value

    @property
    def addon_this_little_bastard(self) -> str:
        DLL.ZkSvmInstance_getAddonThisLittleBastard.restype = ZkString
        return DLL.ZkSvmInstance_getAddonThisLittleBastard(self._handle).value

    @property
    def addon_open_adanos_temple(self) -> str:
        DLL.ZkSvmInstance_getAddonOpenAdanosTemple.restype = ZkString
        return DLL.ZkSvmInstance_getAddonOpenAdanosTemple(self._handle).value

    @property
    def attentat_addon_description(self) -> str:
        DLL.ZkSvmInstance_getAttentatAddonDescription.restype = ZkString
        return DLL.ZkSvmInstance_getAttentatAddonDescription(self._handle).value

    @property
    def attentat_addon_description2(self) -> str:
        DLL.ZkSvmInstance_getAttentatAddonDescription2.restype = ZkString
        return DLL.ZkSvmInstance_getAttentatAddonDescription2(self._handle).value

    @property
    def attentat_addon_pro(self) -> str:
        DLL.ZkSvmInstance_getAttentatAddonPro.restype = ZkString
        return DLL.ZkSvmInstance_getAttentatAddonPro(self._handle).value

    @property
    def attentat_addon_contra(self) -> str:
        DLL.ZkSvmInstance_getAttentatAddonContra.restype = ZkString
        return DLL.ZkSvmInstance_getAttentatAddonContra(self._handle).value

    @property
    def mine_addon_description(self) -> str:
        DLL.ZkSvmInstance_getMineAddonDescription.restype = ZkString
        return DLL.ZkSvmInstance_getMineAddonDescription(self._handle).value

    @property
    def addon_summon_ancient_ghost(self) -> str:
        DLL.ZkSvmInstance_getAddonSummonAncientGhost.restype = ZkString
        return DLL.ZkSvmInstance_getAddonSummonAncientGhost(self._handle).value

    @property
    def addon_ancient_ghost_not_near(self) -> str:
        DLL.ZkSvmInstance_getAddonAncientGhostNotNear.restype = ZkString
        return DLL.ZkSvmInstance_getAddonAncientGhostNotNear(self._handle).value

    @property
    def addon_gold_description(self) -> str:
        DLL.ZkSvmInstance_getAddonGoldDescription.restype = ZkString
        return DLL.ZkSvmInstance_getAddonGoldDescription(self._handle).value

    @property
    def watch_your_aim(self) -> str:
        DLL.ZkSvmInstance_getWatchYourAim.restype = ZkString
        return DLL.ZkSvmInstance_getWatchYourAim(self._handle).value

    @property
    def watch_your_aim_angry(self) -> str:
        DLL.ZkSvmInstance_getWatchYourAimAngry.restype = ZkString
        return DLL.ZkSvmInstance_getWatchYourAimAngry(self._handle).value

    @property
    def lets_forget_our_little_fight(self) -> str:
        DLL.ZkSvmInstance_getLetsForgetOurLittleFight.restype = ZkString
        return DLL.ZkSvmInstance_getLetsForgetOurLittleFight(self._handle).value

    @property
    def strange(self) -> str:
        DLL.ZkSvmInstance_getStrange.restype = ZkString
        return DLL.ZkSvmInstance_getStrange(self._handle).value

    @property
    def die_mortal_enemy(self) -> str:
        DLL.ZkSvmInstance_getDieMortalEnemy.restype = ZkString
        return DLL.ZkSvmInstance_getDieMortalEnemy(self._handle).value

    @property
    def now_wait(self) -> str:
        DLL.ZkSvmInstance_getNowWait.restype = ZkString
        return DLL.ZkSvmInstance_getNowWait(self._handle).value

    @property
    def now_wait_intruder(self) -> str:
        DLL.ZkSvmInstance_getNowWaitIntruder.restype = ZkString
        return DLL.ZkSvmInstance_getNowWaitIntruder(self._handle).value

    @property
    def you_still_not_have_enough(self) -> str:
        DLL.ZkSvmInstance_getYouStillNotHaveEnough.restype = ZkString
        return DLL.ZkSvmInstance_getYouStillNotHaveEnough(self._handle).value

    @property
    def you_attacked_my_charge(self) -> str:
        DLL.ZkSvmInstance_getYouAttackedMyCharge.restype = ZkString
        return DLL.ZkSvmInstance_getYouAttackedMyCharge(self._handle).value

    @property
    def i_will_teach_you_respect_for_foreign_property(self) -> str:
        DLL.ZkSvmInstance_getIWillTeachYouRespectForForeignProperty.restype = ZkString
        return DLL.ZkSvmInstance_getIWillTeachYouRespectForForeignProperty(self._handle).value

    @property
    def you_killed_one_of_us(self) -> str:
        DLL.ZkSvmInstance_getYouKilledOneOfUs.restype = ZkString
        return DLL.ZkSvmInstance_getYouKilledOneOfUs(self._handle).value

    @property
    def berzerk(self) -> str:
        DLL.ZkSvmInstance_getBerzerk.restype = ZkString
        return DLL.ZkSvmInstance_getBerzerk(self._handle).value

    @property
    def youll_be_sorry_for_this(self) -> str:
        DLL.ZkSvmInstance_getYoullBeSorryForThis.restype = ZkString
        return DLL.ZkSvmInstance_getYoullBeSorryForThis(self._handle).value

    @property
    def yes_yes(self) -> str:
        DLL.ZkSvmInstance_getYesYes.restype = ZkString
        return DLL.ZkSvmInstance_getYesYes(self._handle).value

    @property
    def shit_what_a_monster(self) -> str:
        DLL.ZkSvmInstance_getShitWhatAMonster.restype = ZkString
        return DLL.ZkSvmInstance_getShitWhatAMonster(self._handle).value

    @property
    def we_will_meet_again(self) -> str:
        DLL.ZkSvmInstance_getWeWillMeetAgain.restype = ZkString
        return DLL.ZkSvmInstance_getWeWillMeetAgain(self._handle).value

    @property
    def never_try_that_again(self) -> str:
        DLL.ZkSvmInstance_getNeverTryThatAgain.restype = ZkString
        return DLL.ZkSvmInstance_getNeverTryThatAgain(self._handle).value

    @property
    def i_took_your_ore(self) -> str:
        DLL.ZkSvmInstance_getITookYourOre.restype = ZkString
        return DLL.ZkSvmInstance_getITookYourOre(self._handle).value

    @property
    def shit_no_ore(self) -> str:
        DLL.ZkSvmInstance_getShitNoOre.restype = ZkString
        return DLL.ZkSvmInstance_getShitNoOre(self._handle).value

    @property
    def you_violated_forbidden_territory(self) -> str:
        DLL.ZkSvmInstance_getYouViolatedForbiddenTerritory.restype = ZkString
        return DLL.ZkSvmInstance_getYouViolatedForbiddenTerritory(self._handle).value

    @property
    def you_wanna_fool_me(self) -> str:
        DLL.ZkSvmInstance_getYouWannaFoolMe.restype = ZkString
        return DLL.ZkSvmInstance_getYouWannaFoolMe(self._handle).value

    @property
    def what_did_you_in_there(self) -> str:
        DLL.ZkSvmInstance_getWhatDidYouInThere.restype = ZkString
        return DLL.ZkSvmInstance_getWhatDidYouInThere(self._handle).value

    @property
    def intruder_alert(self) -> str:
        DLL.ZkSvmInstance_getIntruderAlert.restype = ZkString
        return DLL.ZkSvmInstance_getIntruderAlert(self._handle).value

    @property
    def behind_you(self) -> str:
        DLL.ZkSvmInstance_getBehindYou.restype = ZkString
        return DLL.ZkSvmInstance_getBehindYou(self._handle).value

    @property
    def hey_hey_hey(self) -> str:
        DLL.ZkSvmInstance_getHeyHeyHey.restype = ZkString
        return DLL.ZkSvmInstance_getHeyHeyHey(self._handle).value

    @property
    def cheer_fight(self) -> str:
        DLL.ZkSvmInstance_getCheerFight.restype = ZkString
        return DLL.ZkSvmInstance_getCheerFight(self._handle).value

    @property
    def cheer_friend(self) -> str:
        DLL.ZkSvmInstance_getCheerFriend.restype = ZkString
        return DLL.ZkSvmInstance_getCheerFriend(self._handle).value

    @property
    def ooh(self) -> str:
        DLL.ZkSvmInstance_getOoh.restype = ZkString
        return DLL.ZkSvmInstance_getOoh(self._handle).value

    @property
    def yeah_well_done(self) -> str:
        DLL.ZkSvmInstance_getYeahWellDone.restype = ZkString
        return DLL.ZkSvmInstance_getYeahWellDone(self._handle).value

    @property
    def he_defeatedhim(self) -> str:
        DLL.ZkSvmInstance_getHeDefeatedhim.restype = ZkString
        return DLL.ZkSvmInstance_getHeDefeatedhim(self._handle).value

    @property
    def he_deserv_edit(self) -> str:
        DLL.ZkSvmInstance_getHeDeservEdit.restype = ZkString
        return DLL.ZkSvmInstance_getHeDeservEdit(self._handle).value

    @property
    def he_killed_him(self) -> str:
        DLL.ZkSvmInstance_getHeKilledHim.restype = ZkString
        return DLL.ZkSvmInstance_getHeKilledHim(self._handle).value

    @property
    def it_was_a_good_fight(self) -> str:
        DLL.ZkSvmInstance_getItWasAGoodFight.restype = ZkString
        return DLL.ZkSvmInstance_getItWasAGoodFight(self._handle).value

    @property
    def friendly_greetings(self) -> str:
        DLL.ZkSvmInstance_getFriendlyGreetings.restype = ZkString
        return DLL.ZkSvmInstance_getFriendlyGreetings(self._handle).value

    @property
    def al_greetings(self) -> str:
        DLL.ZkSvmInstance_getAlGreetings.restype = ZkString
        return DLL.ZkSvmInstance_getAlGreetings(self._handle).value

    @property
    def mage_greetings(self) -> str:
        DLL.ZkSvmInstance_getMageGreetings.restype = ZkString
        return DLL.ZkSvmInstance_getMageGreetings(self._handle).value

    @property
    def sect_greetings(self) -> str:
        DLL.ZkSvmInstance_getSectGreetings.restype = ZkString
        return DLL.ZkSvmInstance_getSectGreetings(self._handle).value

    @property
    def there_he_is(self) -> str:
        DLL.ZkSvmInstance_getThereHeIs.restype = ZkString
        return DLL.ZkSvmInstance_getThereHeIs(self._handle).value

    @property
    def no_learn_over_max(self) -> str:
        DLL.ZkSvmInstance_getNoLearnOverMax.restype = ZkString
        return DLL.ZkSvmInstance_getNoLearnOverMax(self._handle).value

    @property
    def no_learn_you_already_know(self) -> str:
        DLL.ZkSvmInstance_getNoLearnYouAlreadyKnow.restype = ZkString
        return DLL.ZkSvmInstance_getNoLearnYouAlreadyKnow(self._handle).value

    @property
    def hey_you(self) -> str:
        DLL.ZkSvmInstance_getHeyYou.restype = ZkString
        return DLL.ZkSvmInstance_getHeyYou(self._handle).value

    @property
    def what_do_you_want(self) -> str:
        DLL.ZkSvmInstance_getWhatDoYouWant.restype = ZkString
        return DLL.ZkSvmInstance_getWhatDoYouWant(self._handle).value

    @property
    def i_said_what_do_you_want(self) -> str:
        DLL.ZkSvmInstance_getISaidWhatDoYouWant.restype = ZkString
        return DLL.ZkSvmInstance_getISaidWhatDoYouWant(self._handle).value

    @property
    def make_way(self) -> str:
        DLL.ZkSvmInstance_getMakeWay.restype = ZkString
        return DLL.ZkSvmInstance_getMakeWay(self._handle).value

    @property
    def out_of_my_way(self) -> str:
        DLL.ZkSvmInstance_getOutOfMyWay.restype = ZkString
        return DLL.ZkSvmInstance_getOutOfMyWay(self._handle).value

    @property
    def you_deaf_or_what(self) -> str:
        DLL.ZkSvmInstance_getYouDeafOrWhat.restype = ZkString
        return DLL.ZkSvmInstance_getYouDeafOrWhat(self._handle).value

    @property
    def look_away(self) -> str:
        DLL.ZkSvmInstance_getLookAway.restype = ZkString
        return DLL.ZkSvmInstance_getLookAway(self._handle).value

    @property
    def okay_keep_it(self) -> str:
        DLL.ZkSvmInstance_getOkayKeepIt.restype = ZkString
        return DLL.ZkSvmInstance_getOkayKeepIt(self._handle).value

    @property
    def whats_that(self) -> str:
        DLL.ZkSvmInstance_getWhatsThat.restype = ZkString
        return DLL.ZkSvmInstance_getWhatsThat(self._handle).value

    @property
    def thats_my_weapon(self) -> str:
        DLL.ZkSvmInstance_getThatsMyWeapon.restype = ZkString
        return DLL.ZkSvmInstance_getThatsMyWeapon(self._handle).value

    @property
    def give_it_tome(self) -> str:
        DLL.ZkSvmInstance_getGiveItTome.restype = ZkString
        return DLL.ZkSvmInstance_getGiveItTome(self._handle).value

    @property
    def you_can_keep_the_crap(self) -> str:
        DLL.ZkSvmInstance_getYouCanKeepTheCrap.restype = ZkString
        return DLL.ZkSvmInstance_getYouCanKeepTheCrap(self._handle).value

    @property
    def they_killed_my_friend(self) -> str:
        DLL.ZkSvmInstance_getTheyKilledMyFriend.restype = ZkString
        return DLL.ZkSvmInstance_getTheyKilledMyFriend(self._handle).value

    @property
    def sucker_got_some(self) -> str:
        DLL.ZkSvmInstance_getSuckerGotSome.restype = ZkString
        return DLL.ZkSvmInstance_getSuckerGotSome(self._handle).value

    @property
    def sucker_defeated_ebr(self) -> str:
        DLL.ZkSvmInstance_getSuckerDefeatedEbr.restype = ZkString
        return DLL.ZkSvmInstance_getSuckerDefeatedEbr(self._handle).value

    @property
    def sucker_defeated_gur(self) -> str:
        DLL.ZkSvmInstance_getSuckerDefeatedGur.restype = ZkString
        return DLL.ZkSvmInstance_getSuckerDefeatedGur(self._handle).value

    @property
    def sucker_defeated_mage(self) -> str:
        DLL.ZkSvmInstance_getSuckerDefeatedMage.restype = ZkString
        return DLL.ZkSvmInstance_getSuckerDefeatedMage(self._handle).value

    @property
    def sucker_defeated_nov_guard(self) -> str:
        DLL.ZkSvmInstance_getSuckerDefeatedNovGuard.restype = ZkString
        return DLL.ZkSvmInstance_getSuckerDefeatedNovGuard(self._handle).value

    @property
    def sucker_defeated_vlk_guard(self) -> str:
        DLL.ZkSvmInstance_getSuckerDefeatedVlkGuard.restype = ZkString
        return DLL.ZkSvmInstance_getSuckerDefeatedVlkGuard(self._handle).value

    @property
    def you_defeated_my_comrade(self) -> str:
        DLL.ZkSvmInstance_getYouDefeatedMyComrade.restype = ZkString
        return DLL.ZkSvmInstance_getYouDefeatedMyComrade(self._handle).value

    @property
    def you_defeated_nov_guard(self) -> str:
        DLL.ZkSvmInstance_getYouDefeatedNovGuard.restype = ZkString
        return DLL.ZkSvmInstance_getYouDefeatedNovGuard(self._handle).value

    @property
    def you_defeated_vlk_guard(self) -> str:
        DLL.ZkSvmInstance_getYouDefeatedVlkGuard.restype = ZkString
        return DLL.ZkSvmInstance_getYouDefeatedVlkGuard(self._handle).value

    @property
    def you_stole_from_me(self) -> str:
        DLL.ZkSvmInstance_getYouStoleFromMe.restype = ZkString
        return DLL.ZkSvmInstance_getYouStoleFromMe(self._handle).value

    @property
    def you_stole_from_us(self) -> str:
        DLL.ZkSvmInstance_getYouStoleFromUs.restype = ZkString
        return DLL.ZkSvmInstance_getYouStoleFromUs(self._handle).value

    @property
    def you_stole_from_ebr(self) -> str:
        DLL.ZkSvmInstance_getYouStoleFromEbr.restype = ZkString
        return DLL.ZkSvmInstance_getYouStoleFromEbr(self._handle).value

    @property
    def you_stole_from_gur(self) -> str:
        DLL.ZkSvmInstance_getYouStoleFromGur.restype = ZkString
        return DLL.ZkSvmInstance_getYouStoleFromGur(self._handle).value

    @property
    def stole_urom_mage(self) -> str:
        DLL.ZkSvmInstance_getStoleUromMage.restype = ZkString
        return DLL.ZkSvmInstance_getStoleUromMage(self._handle).value

    @property
    def you_killedmyfriend(self) -> str:
        DLL.ZkSvmInstance_getYouKilledmyfriend.restype = ZkString
        return DLL.ZkSvmInstance_getYouKilledmyfriend(self._handle).value

    @property
    def you_killed_ebr(self) -> str:
        DLL.ZkSvmInstance_getYouKilledEbr.restype = ZkString
        return DLL.ZkSvmInstance_getYouKilledEbr(self._handle).value

    @property
    def you_killed_gur(self) -> str:
        DLL.ZkSvmInstance_getYouKilledGur.restype = ZkString
        return DLL.ZkSvmInstance_getYouKilledGur(self._handle).value

    @property
    def you_killed_mage(self) -> str:
        DLL.ZkSvmInstance_getYouKilledMage.restype = ZkString
        return DLL.ZkSvmInstance_getYouKilledMage(self._handle).value

    @property
    def you_killed_oc_folk(self) -> str:
        DLL.ZkSvmInstance_getYouKilledOcFolk.restype = ZkString
        return DLL.ZkSvmInstance_getYouKilledOcFolk(self._handle).value

    @property
    def you_killed_nc_folk(self) -> str:
        DLL.ZkSvmInstance_getYouKilledNcFolk.restype = ZkString
        return DLL.ZkSvmInstance_getYouKilledNcFolk(self._handle).value

    @property
    def you_killed_psi_folk(self) -> str:
        DLL.ZkSvmInstance_getYouKilledPsiFolk.restype = ZkString
        return DLL.ZkSvmInstance_getYouKilledPsiFolk(self._handle).value

    @property
    def get_things_right(self) -> str:
        DLL.ZkSvmInstance_getGetThingsRight.restype = ZkString
        return DLL.ZkSvmInstance_getGetThingsRight(self._handle).value

    @property
    def you_defeated_me_well(self) -> str:
        DLL.ZkSvmInstance_getYouDefeatedMeWell.restype = ZkString
        return DLL.ZkSvmInstance_getYouDefeatedMeWell(self._handle).value

    @property
    def om(self) -> str:
        DLL.ZkSvmInstance_getOm.restype = ZkString
        return DLL.ZkSvmInstance_getOm(self._handle).value
