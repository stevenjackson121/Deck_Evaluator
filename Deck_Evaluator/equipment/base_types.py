import Deck_Evaluator.actions as actions
import Deck_Evaluator.spell
from Deck_Evaluator.equipment.slots import AmuletSlot, BeltSlot, BootsSlot, ChestPieceSlot, HelmetSlot, Ring1Slot, \
    Ring2Slot, ShieldSlot, WeaponSlot
from Deck_Evaluator.mages import Mage
import logging
logger = logging.getLogger(__name__)


class Equipment(Deck_Evaluator.spell.Spell):
    default_class_properties = {"action_required": actions.QuickSpellAction,
                                "max_range": 2,
                                "min_range": 0,
                                "valid_target_rule": frozenset([Mage])}
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Equipment, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Equipment"}
        return namespace

    def __init__(cls, name, bases, namespace, **kwargs):
        for key, value in Equipment.default_class_properties.items():
            namespace.setdefault(key, value)
        super(Equipment, cls).__init__(name, bases, namespace, **kwargs)


class Amulet(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Amulet, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Amulet"}
        return namespace


class Belt(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Belt, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Belt"}
        return namespace


class Boots(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Boots, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Boots"}
        return namespace


class ChestPiece(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(ChestPiece, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Chest Piece"}
        return namespace


class Gloves(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Gloves, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Gloves"}
        return namespace


class Helmet(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Helmet, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Helmet"}
        return namespace


class Ring(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Ring, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Ring"}
        return namespace


class Shield(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Shield, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Shield"}
        return namespace


class Weapon(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Weapon, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Weapon"}
        return namespace


class LargeWeapon(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(LargeWeapon, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Weapon"}
        return namespace


class SmallWeapon(Equipment):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(SmallWeapon, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Weapon"}
        return namespace
