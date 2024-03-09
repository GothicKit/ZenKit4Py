import sys

from zenkit import DaedalusInstance
from zenkit import DaedalusInstanceType
from zenkit import DaedalusVm
from zenkit import LogLevel
from zenkit import set_logger_default

if len(sys.argv) != 2:
    print("Please provide a path to GOTHIC.DAT.", file=sys.stderr)
    sys.exit(-1)

set_logger_default(LogLevel.DEBUG)

# Load the script file into a VM
vm = DaedalusVm.load(sys.argv[1])

# Register a catch-all callback for all calls to un-registered external functions. ZenKit will handle all required
# internal VM state as required so as to not corrupt the stack.
vm.register_external_default(lambda sym: print("VM: No external for", sym.name))

# Register implementations for external functions. Parameters and return values are checked to match their
# definitions in the script at runtime and any mismatches between definition and implementation will cause runtime
# exceptions to be thrown. Notice that you have to specify the argument types after providing the callback function.
vm.register_external("INTTOSTRING", lambda i: str(i), int)
vm.register_external("CONCATSTRINGS", lambda a, b: a + b, str, str)


def _ai_printscreen(msg: str, _i0: int, _i1: int, font: str, _i2: int) -> bool:
    print('AI: print "' + msg + '" with font "' + font + '"')
    return True


vm.register_external("AI_PRINTSCREEN", _ai_printscreen, str, int, int, str, int)

# Initialize some instances. Essentially, each Daedalus instance needs to be initialized in Python which causes the
# Daedalus code defining that instance to be executed. This needs to be done for every Daedalus instance BEFORE
# it can be used in a script. The fields of the Daedalus instances are synced, so any change in Python will be
# reflected in Daedalus and vice-versa.
xardas = vm.init_instance("NONE_100_XARDAS", DaedalusInstanceType.NPC)
hero = vm.init_instance("PC_HERO", DaedalusInstanceType.NPC)

# You can also move the actual instance initialization call to a later point. This might be useful when you need
# you want to manually initialize the instance in Python. To do it, first allocate an instance, then initialize it,
# when needed, like this:
gold = vm.alloc_instance("ITMI_GOLD", DaedalusInstanceType.ITEM)
vm.init_instance_direct(gold)

vm.register_external("NPC_ISPLAYER", lambda npc: npc.index == hero.index, DaedalusInstance)

# Some calls to VM function require a certain global context variable to be set. This applies mainly to NPC
# routine functions, state update functions (like item equip callbacks) and mission state query functions. The
# available global context variables are:
#
#  * `global_self` -> var C_NPC self
#  * `global_other` -> var C_NPC other
#  * `global_victim` -> var C_NPC victim
#  * `global_hero` -> var C_NPC hero
#  * `global_item` -> var C_ITEM item
vm.global_item = gold

# Call a function defined the script. The first parameter can either be the function's name or the DaedalusSymbol
# for the function. The following parameters are passed to the Daedalus function as arguments.
#
# In this case, the Daedalus function definition is:
#
#   func int B_GIVEINVITEMS(var C_NPC giver, var C_NPC taker, var int itemInstance, var int amount)
#
# Notice that you have to specify the return type manually.
ret = vm.call("B_GIVEINVITEMS", xardas, hero, gold.index, 2, rtype=int)

print("Calling B_GIVEINVITEMS(NONE_100_XARDAS, PC_HERO, " + str(gold.index) + ", 1) resulted in return of " + str(ret))
