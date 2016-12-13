from abc import ABCMeta
from collections import Counter, defaultdict
from copy import copy
from Deck_Evaluator.equipment.slots import MageGear
import Deck_Evaluator.schools as schools
import Deck_Evaluator.spell
import logging
import pprint

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class CardPile(object):
    def __init__(self, spells=None):
        if spells is None:
            spells = []
        self.spell_counts = Counter(spells)

    def contains_spells(self, spells):
        spell_counts_copy = copy(self.spell_counts)
        spell_counts_copy.subtract(spells)
        return spell_counts_copy.most_common()[-1][1] >= 0

    def add_spell(self, spell):
        self.spell_counts[spell] += 1

    def remove_spell(self, spell):
        if self.spell_counts[spell] == 0:
            raise ValueError("Cannot remove spell %s. Spell is not included in SpellBook." % str(spell))
        self.spell_counts[spell] -= 1


class SpellBook(CardPile):
    default_card_limits_by_level = defaultdict(lambda: 4, {1: 6})

    def __init__(self, spells=None, card_limits_by_level=None):
        super(SpellBook, self).__init__(spells)
        if card_limits_by_level is None:
            self.card_limits_by_level = copy(SpellBook.default_card_limits_by_level)
        self.raw_cost = 0
        for spell, count in self.spell_counts.items():
            if count > self.card_limits_by_level[spell().level]:
                raise ValueError("Cannot add %d copies of %s to SpellBook. Only %d copies are allowed." %
                                 (count, spell, self.card_limits_by_level[spell().level]))
            elif count > 1 and issubclass(spell, Deck_Evaluator.spells.Epic):
                raise ValueError("Cannot add more than 1 copy of Epic spell %s to SpellBook.")

    def __iter__(self):
        return iter(self.spell_counts.items())

    def __str__(self):
        return pprint.pformat(self.__dict__)


class DiscardPile(CardPile):
    def __init__(self, spells=None):
        super(DiscardPile, self).__init__(spells)


###################################
# Equipment
###################################
class Equipment(object):
    def __init__(self, amulet=None, belt=None, boots=None, helmet=None,
                 ring1=None, ring2=None, shield=None, weapon=None):
        self.amulet = amulet
        self.belt = belt
        self.boots = boots
        self.helmet = helmet
        self.ring1 = ring1
        self.ring2 = ring2
        self.shield = shield
        self.weapon = weapon


class Channelling(metaclass=ABCMeta):
    @property
    def channelling(self):
        return self._channelling

    def __init__(self, channelling=9, **kwargs):
        self._channelling = channelling
        super().__init__(**kwargs)


class Creature(metaclass=ABCMeta):
    pass


def max_life(max_life_: int):
    class MaxLife(metaclass=ABCMeta):
        @property
        def max_life(self):
            return self._max_life

        @max_life.setter
        def max_life(self, new_max_life):
            self._max_life = new_max_life

        @property
        def damage(self):
            return self._damage

        @damage.setter
        def damage(self, damage):
            self._damage = damage

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self._max_life = max_life_
            self._damage = 0
    return MaxLife


class Living(metaclass=ABCMeta):
    @property
    def living(self):
        return True


class NonLiving(metaclass=ABCMeta):
    @property
    def living(self):
        return False


class Caster(metaclass=ABCMeta):
    @property
    def channelling(self):
        return self._channelling

    @property
    def prepared_spell_limit(self):
        return self._prepared_spell_limit

    @property
    def prepared_spells(self):
        return self._prepared_spells

    @prepared_spells.setter
    def prepared_spells(self, spells):
        if len(spells) > self.prepared_spell_limit:
            raise ValueError("Can only prepare %d spells." % self.prepared_spell_limit)

        if not self.spellbook.contains_spells(spells):
            raise ValueError("Could not prepare. Can only prepare spells contained in spellbook.")

        self._prepared_spells = spells

    def __init__(self, prepared_spell_limit=1, prepared_spells_=tuple(), **kwargs):
        super().__init__(**kwargs)
        self._prepared_spell_limit = prepared_spell_limit
        self._prepared_spells = prepared_spells_


##################################
# Our standard mage template
##################################
class Mage(Caster, Channelling, Creature, Living, max_life(32), MageGear):
    @property
    def trained_schools(self):
        return self._trained_schools

    @property
    def opposed_schools(self):
        return self._opposed_schools

    @property
    def spellbook(self):
        return self._spellbook

    @property
    def spellbook_cost(self):
        return self.get_spellbook_cost()

    def __init__(self, prepared_spell_limit=2, opposed_schools=None, spellbook=None,
                 trained_schools=None, **kwargs):
        super().__init__(prepared_spell_limit=prepared_spell_limit, **kwargs)

        if opposed_schools is None:
            opposed_schools = []
        self._opposed_schools = tuple(opposed_schools)

        if spellbook is None:
            spellbook = SpellBook()
        self._spellbook = spellbook

        if trained_schools is None:
            trained_schools = []
        self._trained_schools = tuple(trained_schools)

    def return_spells_to_spellbook(self):
        for spell in self.prepared_spells:
            self.spellbook.add(spell)
        self.prepared_spells = []

    def get_spellbook_cost(self):
        for card, count in self.spellbook:
            logger.info("%s * %d = %d" % (card, count, card().get_raw_cost() * count))
        return 0

    def __str__(self):
        return pprint.pformat(self.__dict__)


###################################
# Our Mage classes
###################################
class BeastMaster(Mage):
    def __init__(self, **kwargs):
        super(BeastMaster, self).__init__(
            opposed_schools=[schools.Fire],
            trained_schools=[schools.Nature],
            **kwargs)


class Wizard(Mage):
    def __init__(self, element=None, **kwargs):
        trained_schools = ['Arcane']
        if element in ['Flame', 'Hydro', 'Wind']:
            trained_schools.append(element)

        super(Wizard, self).__init__(
            channelling=10,
            trained_schools=trained_schools,
            **kwargs)
