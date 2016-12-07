import actions
import logging
import mages
import schools
import spells


logger = logging.getLogger(__name__)


class Or(frozenset):
    def __repr__(self):
        return '%s' % super(Or, self).__repr__()


class And(frozenset):
    def __repr__(self):
        return '%s' % super(And, self).__repr__()


class Slot(object):
    def __init__(self, type_):
        self.type = type_
        super(Slot, self).__init__()


class AmuletSlot(Slot):
    def __init__(self):
        super(AmuletSlot, self).__init__(AmuletSlot)


class BootsSlot(Slot):
    def __init__(self):
        super(BootsSlot, self).__init__(BootsSlot)


class ChestPieceSlot(Slot):
    def __init__(self):
        super(ChestPieceSlot, self).__init__(ChestPieceSlot)


class CloakSlot(Slot):
    def __init__(self):
        super(CloakSlot, self).__init__(CloakSlot)


class HelmetSlot(Slot):
    def __init__(self):
        super(HelmetSlot, self).__init__(HelmetSlot)


class RingSlot1(Slot):
    def __init__(self):
        super(RingSlot1, self).__init__(RingSlot1)


class RingSlot2(Slot):
    def __init__(self):
        super(RingSlot2, self).__init__(RingSlot2)


class ShieldSlot(Slot):
    def __init__(self):
        super(ShieldSlot, self).__init__(ShieldSlot)


class WeaponSlot(Slot):
    def __init__(self):
        super(WeaponSlot, self).__init__(WeaponSlot)


class Equipment(spells.Spell):
    def __init__(self, slot_sets, *args, **kwargs):
        self.valid_slot_sets = Or(And(s) for s in slot_sets)
        logger.info("My Valid Slot Sets: %s" % self.valid_slot_sets)
        super(Equipment, self).__init__(*args, **kwargs)
        
    def can_use_slots(self, slot_set):
        logger.info("My Valid Slot Sets: %s" % self.valid_slot_sets)
        logger.info("Slot Set being attempted: %s" % set(s.__class__ for s in slot_set))
        for valid_slot_set in self.valid_slot_sets:
            if valid_slot_set == slot_set:
                return True
        return False


class Helmet(Equipment):
    def __init__(self, *args, **kwargs):
        super(Helmet, self).__init__([[HelmetSlot]], *args, **kwargs)


@spells.spell_book_point_cost(Dark=3)
@spells.casting_cost(8)
class HelmOfFear(Helmet):
    def __init__(self):
        super(HelmOfFear, self).__init__(
            action_required=actions.QuickSpellAction,
            effect=None,
            name='Helm of Fear',
            min_range=0,
            max_range=0,
            subtypes=None,
            target=mages.Mage
        )


class IvariumLongbow(Equipment):
    def __init__(self):
        super(IvariumLongbow, self).__init__(
            slot_sets=[[ShieldSlot, WeaponSlot]],
            action_required=actions.QuickSpellAction,
            effect=None,
            name='Ivarium Longbow',
            school_level_dicts=Or([{
                schools.Nature: 4
            }]),
            min_range=0,
            max_range=0,
            subtypes=None,
            target=mages.Mage,
            casting_cost=8
        )


class MageWand(Equipment):
    def __init__(self):
        super(MageWand, self).__init__(
            slot_sets=[[ShieldSlot], [WeaponSlot]],
            action_required=actions.QuickSpellAction,
            effect=None,
            name='Ivarium Longbow',
            school_level_dicts=[{
                schools.Nature: 4
            }],
            min_range=0,
            max_range=0,
            subtypes=None,
            target=mages.Mage,
            casting_cost=8)