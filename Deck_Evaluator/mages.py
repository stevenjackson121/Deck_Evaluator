from collections import Counter, defaultdict
from copy import copy
import equipment
import logging
import json
import jsonpickle
import pprint
import schools

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class CardPile(object):
    def __init__(self, spells=None):
        if spells is None:
            spells = []
        self.spell_counts = Counter(spells)

    def contains_spells(self, spells):
        spell_counts_copy = copy(self.spell_counts)
        copy_copy = copy(spell_counts_copy)
        spell_counts_copy.subtract(spells)
        logger.debug("\n" + pprint.pformat({
            "self": self,
            "original": self.spell_counts,
            "copy": copy_copy,
            "after subtract": spell_counts_copy.most_common()[-1]}))
        return spell_counts_copy.most_common()[-1][1] >= 0

    def add_spell(self, spell):
        original = copy(self.spell_counts)
        self.spell_counts[spell] += 1

        logger.debug("\n" + pprint.pformat({
            "self": self,
            "adding spell": spell,
            "original": original.most_common(),
            "after add": self.spell_counts.most_common()}))

    def remove_spell(self, spell):
        if self.spell_counts[spell] == 0:
            raise ValueError("Cannot remove spell %s. Spell is not included in SpellBook." % str(spell))
        self.spell_counts[spell] -= 1


class SpellBook(CardPile):
    default_card_limits_by_level = defaultdict(lambda key: 4, {1: 6})

    def __init__(self, spells=None, card_limits_by_level=None):
        super(SpellBook, self).__init__(spells)
        if card_limits_by_level is None:
            self.card_limits_by_level = copy(SpellBook.default_card_limits_by_level)
        self.raw_cost = 0

    def __iter__(self):
        return iter(self.spell_counts.items())

    def __str__(self):
        return pprint.pformat({'ID': id(self), 'Spells': self.spell_counts, 'Total Raw Cost': self.raw_cost})


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


##################################
# Our standard mage template
##################################
class Mage(object):
    def __init__(self, channelling=9, life=32, prepared_spell_limit=2,
                 opposed_schools=None, spellbook=None, trained_schools=None):
        self.channelling = channelling
        self.equipment = Equipment()
        self.amulet_slot = equipment.AmuletSlot()
        self.boots_slot = equipment.BootsSlot
        self.helmet_slot = equipment.HelmetSlot()
        self.ring1_slot = equipment.RingSlot1()
        self.ring2_slot = equipment.RingSlot2()
        self.shield_slot = equipment.ShieldSlot()
        self.weapon_slot = equipment.WeaponSlot()

        self.prepared_spell_limit = prepared_spell_limit
        self.prepared_spells = None

        self.equipment = {
            self.amulet_slot: None,
            self.boots_slot: None,
            self.helmet_slot: None,
            self.ring1_slot: None,
            self.ring2_slot: None,
            self.shield_slot: None,
            self.weapon_slot: None,
            }

        self.life = life

        if opposed_schools is None:
            opposed_schools = []
        self.opposed_schools = opposed_schools

        if spellbook is None:
            spellbook = SpellBook()
        self.spellbook = spellbook
        self.spellbook_cost = self.get_spellbook_cost()

        if trained_schools is None:
            trained_schools = []
        self.trained_schools = trained_schools

    def prepare_spells(self, *spells):
        if len(spells) > self.prepared_spell_limit:
            raise ValueError("Can only prepare %d spells." % self.prepared_spell_limit)

        if not self.spellbook.contains_spells(spells):
            raise ValueError("Could not prepare. Can only prepare spells contained in spellbook.")

        self.prepared_spells = spells

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

    def equip_item_to_slots(self, item, slots):
        slot_set = equipment.And(s.type for s in slots)
        if not item.can_use_slots(slot_set):
            raise ValueError("Item %s cannot be equipped to slots %s" % (item, slot_set))

        for slot in slots:
            self.unequip_item_in_slot(slot)

        for slot in slots:
            self.equipment[slot] = item

    def unequip_item_in_slot(self, slot):
        if self.equipment[slot] is not None:
            logger.debug("Unequipping item in slot %s" % slot)
            item_to_remove = self.equipment[slot]
            for slot in self.equipment.keys():
                if self.equipment[slot] == item_to_remove:
                    self.equipment[slot] = None


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


def new_mage(type_, spellbook):
    if type_ == 'Wizard':
        return Wizard('Flame', spellbook=spellbook)
    elif type_ == 'BeastMaster':
        return BeastMaster(spellbook=spellbook)
    else:
        raise NotImplementedError
def mage_test():
    wizard = new_mage('Wizard', SpellBook(spells=[
        equipment.HelmOfFear,
        equipment.IvariumLongbow]))
    logger.info("%s" % wizard.amulet_slot)

    try:
        wizard.equip_item_to_slots(item=equipment.HelmOfFear(),
                                   slots=[wizard.amulet_slot])
        working_as_intended = False
    except ValueError as e:
        working_as_intended = True
    if not working_as_intended:
        raise RuntimeError("Exception was not thrown when helmet was equipped to Amulet slot")

    beast_master = new_mage('BeastMaster',
                            SpellBook(spells=[
                                equipment.HelmOfFear,
                                equipment.IvariumLongbow]))

    logger.debug('Mage:\n%s\n' % wizard)
    logger.debug('Spellbook:\n%s\n' % wizard.spellbook)
    logger.debug('Mage:\n%s\n' % beast_master)
    logger.debug('Spellbook:\n%s\n' % beast_master.spellbook)

    beast_master.prepare_spells(equipment.HelmOfFear,
                                equipment.IvariumLongbow)
    beast_master.equip_item_to_slots(item=equipment.HelmOfFear(),
                                     slots=[beast_master.helmet_slot])
    beast_master.equip_item_to_slots(item=equipment.IvariumLongbow(),
                                     slots=[
                                         beast_master.weapon_slot,
                                         beast_master.shield_slot])
    beast_master.equip_item_to_slots(item=equipment.MageWand(),
                                     slots=[beast_master.shield_slot])

    try:
        beast_master.equip_item_to_slots(item=equipment.IvariumLongbow(),
                                         slots=[beast_master.weapon_slot])
        working_as_intended = False
    except ValueError as e:
        working_as_intended = True
    if not working_as_intended:
        raise RuntimeError("Exception was not thrown when helmet was equipped to Ammy slot")


if __name__ == '__main__':
    obj = equipment.HelmOfFear()
    jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=2)
    serialized = jsonpickle.encode(obj, unpicklable=False)
    print serialized
