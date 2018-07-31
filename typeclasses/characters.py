"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    def at_object_creation(self):

        # default attributes set when the character is first created.
        
        # bio stats
        self.db.bio={'Full_name': ' ', 'Age': ' ', 'Court': ' ', 'Vocation': ' ', 'Position': ' ', 'Concept': ' ', 'Height': 0, 'Eyes': ' ', 'Hair': ' '}

        # all players start with 1 in their attributes
        # active attributes
        self.db.active_attr= {'Soma': 1, 'Fight': 1, 'Panache': 1}

        #passive attributes
        self.db.passive_attr = {'Vim': 1, 'Defend': 1, 'Wisdom': 1}

        #players start with 0 in their skills
        #active skills
        self.db.active_skill={'Influence': 0, 'Research': 0, 'Create': 0, 'Athletics': 0, 'Larceny': 0, 'Sail': 0}

        #passive skills
        self.db.passive_skill = {'Integrity': 0, 'Knowledge': 0, 'Resistance': 0, 'Awareness': 0, 'Insight': 0, 'Navigation': 0}

        #combat skills
        self.db.combat_skill = {'Brawl': 0, 'Shoot': 0, 'Throw': 0, 'Melee': 0, 'Mount': 0}


        #traits are things that can be spent
        #special things players start with 5 luck 10 mana
        self.db.special_trait= {'Luck': 5, 'Mana': 10}
        
    def get_bio(self):
        """a simple method to get the bio attrs as a tuple"""
        return self.db.bio['Full_name'], self.db.bio['Age'], self.db.bio['Court'], self.db.bio['Vocation'], self.db.bio['Position'], self.db.bio['Concept'], self.db.bio['Height'], self.db.bio['Eyes'], self.db.bio['Hair']

    def get_active_attr(self):
        """simple method to get active attris as a tuple (some, fight, panache)"""

        return self.db.active_attr['Soma'], self.db.active_attr['Fight'], self.db.active_attr['Panache']


    def get_passive_attr(self):
        """simple method to get passive attrs as a tuple (vim, defend, wisdom"""

        return self.db.passive_attr['Vim'], self.db.passive_attr['Defend'], self.db.passive_attr['Wisdom']


    def get_active_skills(self):
        """simple method to get active skills as a long ass
        tuple (influence, research, create, athletics, larceny, sail)"""

        return self.db.active_skill['Influence'], self.db.active_skill['Research'], self.db.active_skill['Create'], self.db.active_skill['Athletics'], self.db.active_skill['Larceny'], self.db.active_skill['Sail']

    def get_passive_skills(self):
        """simple method to get passive skills as a long ass
        tuple (integrity, knowledge, resistance, awareness, insight, navigation)"""

        return self.db.passive_skill['Integrity'], self.db.passive_skill['Knowledge'], self.db.passive_skill['Resistance'], self.db.passive_skill['Awareness'], self.db.passive_skill['Insight'], self.db.passive_skill['Navigation']

    def get_combat_skills(self):
        """simple method to get combat skills in a long ass tuple
        (brawll, shoot, throw, melee, mount"""

        return self.db.combat_skill['Brawl'], self.db.combat_skill['Shoot'], self.db.combat_skill['Throw'], self.db.combat_skill['Melee'], self.db.combat_skill['Mount']

    def get_spec_traits(self):
        """simple method to get special traits as a tuple (mana, luck)"""

        return self.db.special_trait['Mana'], self.db.special_trait['Luck']
    

