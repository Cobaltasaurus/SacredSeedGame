"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia import Command as BaseCommand
# from evennia import default_cmds


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """
    pass

# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super(MuxCommand, self).has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None

# file sacredseed/commands/command.py
# this is our dice roller lol

from evennia import default_cmds
from evennia import Command
import random
from collections import Counter

class Cmd_Roll(default_cmds.MuxCommand):
        """
        Prototype of the games roller.

        Usage:
          roll <# of dice>,<# of difficulty>

        Please god let this work....
        """

        key = "roll"
        aliases =["check, dice"]
        locks = "cmd:all()"
        help_category = "General Commands"

        def func(self):
                caller = self.caller
                location = caller.location
                num = int(self.lhslist[0])
                diff = int(self.lhslist[1])
                successes, rolls = self.roll(num, diff)
                location.msg_contents("|y<Roll>|n %s gained |350%s successes|n at difficulty |y%s|n. |222%s|n" % (str(caller), str(successes), str(diff), str(rolls)))

        def roll(self, num, diff):
                rolls = [random.randint(1, 12) for x in range(num)]
                successes = 0
                c = Counter(rolls)
                for roll, times in c.items():
                        if roll >= diff:
                                successes += times
                                continue
                        successes += (roll*times)//diff
#               print("That's %s successes" % str(successes))
                return successes, rolls


class CmdSheet(Command):

    """
    Shows your sheet to you.

    Usage:
      sheet

    Aliases:
      stats


    Displays a list of your current ability values.
    """

    key = "sheet"
    aliases = ["stats"]
    lock = "cmd:all()"
    help_category = "General Commands"

    def func(self):
        "implements the actual functionality"

        soma, fight, panache = self.caller.get_active_attr()
        vim, defend, wisdom = self.caller.get_passive_attr()
        influence, research, create, athletics, larceny, sail = self.caller.get_active_skills()
        integrity, knowledge, resistance, awareness, insight, navigation = self.caller.get_passive_skills()
        brawl, shoot, throw, melee, mount = self.caller.get_combat_skills()
        mana, luck = self.caller.get_spec_traits()
        full_name, age, court, vocation, position, concept, height, eyes, hair = self.caller.get_bio()

        name = self.caller.name
	name_disp = "{ Sheet: %s }" % name
	hdr_length = 78-len(name_disp)
        header = '|y' + name_disp + '-'*hdr_length + '|n'
	bio_block = "|/Fullname:|_%s|_---Age:|_|_|_|_|_|_|444%s---Court:|_|_|_|444%s|/Vocation:|_%s---Position:|_|444%s---Concept:|_|444%s|/|444Height:-|_|_|444%s|444---Eyes:-|_|_|444%s|444---Hair:|_|_|_|_|444%s|/|/" % (full_name, age, court, vocation, position, concept, height, eyes, hair)
        attr_block ="|550--------{{|_ATTRS|_}|/|=z |_ |_ |_ |_ |_ |_ |_ |_--Active |_ |_ |_ |_ ---Passive|/|=zPhysical |_ |_ |_ |_ |_ |_ |_ |_Soma: |_ |_%s|_ |_ |_ |_ |_ |_ |_Vim: |_ |_|444%s|/|=zCombat |_ |_ |_ |_ |_--Fight: |_ |444%s |_ |_ |_ |_ |_ |_ Defend:|_|444%s|/|=zAbstract |_ |_ |_ |_ |_ |_ |_ |_Panache:|_|444%s|_ |_ |_ |_ |_ |_ |_Wisdom:|_|444%s |\|\" % (soma, vim, fight, defend, panache, wisdom)
        skill_block = "|550--------{{|_SKILLS|_}|/|=zActive |_ |_ |_ |_ |_--Passive |_ |_ |_ |_ --Combat|/Influence: |_|444%s |_ |_ |_ |_ |_Integrity: |_|444%s |_ |_ |_ |_ |_Brawl: |_ |_ |_|444%s|/Research: |_ |444%s |_ |_ |_ |_ |_Knowledge: |_|444%s|_ |_ |_ |_ |_ Shoot: |_ |_ |_|444%s|/Create: |_ |_ |444%s |_ |_ |_ |_ |_Resistance:|_|444%s |_ |_ |_ |_ |_Throw: |_ |_ |_|444%s|/Athletics: |_|444%s |_ |_ |_ |_ |_Awareness: |_|444%s |_ |_ |_ |_ |_Melee: |_ |_ |_|444%s|/Larceny: |_ |_|444%s |_ |_ |_ |_ |_Insight: |_ |_|444%s |_ |_ |_ |_ |_Mount: |_ |_ |_|444%s|/Sail: |_ |_ |_ |444%s |_ |_ |_ |_ |_Navigation:|_|444%s|/|/|/" % (influence, integrity, brawl, research, knowledge, shoot, create, resistance, throw, athletics, awareness, melee, larceny, insight, mount, sail, navigation)

        spec_block = "|355Mana|333:|_10 |_ |_ |_ |_ |_ |_ |_ |_|355Luck|333:|_5|/|550------------------------------------------------------------------------------" % (mana, luck)
        self.caller.msg(header)
	self.caller.msg(bio_block)
	self.caller.msg(attr_block)
	self.caller.msg(skill_block)
	self.caller.msg(spec_block)

#	skills = evtable.EvTable("|gActive", " ", table=[["Influence", "Research", "Create", "Athletics", "Larceny", "Sail"], [influence, research, create, athletics, larceny, sail]])


