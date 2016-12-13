from abc import ABCMeta, abstractmethod
import logging
logger = logging.getLogger(__name__)


class EquipmentSlot(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    def equip(self, item):
        pass

    @abstractmethod
    def unequip(self):
        pass


class AmuletSlot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def amulet(self):
        return self._amulet

    @amulet.setter
    def amulet(self, item):
        self.equip_item_to_slots(item, frozenset([AmuletSlot]))

    def equip(self, item):
        self._amulet = item

    def unequip(self):
        self._amulet = None

    def __init__(self, amulet=None, **kwargs):
        super().__init__(**kwargs)
        self._amulet = amulet


class BeltSlot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def belt(self):
        return self._belt

    @belt.setter
    def belt(self, item):
        self.equip_item_to_slots(item, frozenset([BeltSlot]))

    def equip(self, item):
        self._belt = item

    def unequip(self):
        self._belt = None

    def __init__(self, belt=None, **kwargs):
        super().__init__(**kwargs)
        self._belt = belt


class BootsSlot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def boots(self):
        return self._boots

    @boots.setter
    def boots(self, item):
        self.equip_item_to_slots(item, frozenset([BootsSlot]))

    def equip(self, item):
        self._boots = item

    def unequip(self):
        self._boots = None

    def __init__(self, boots=None, **kwargs):
        super().__init__(**kwargs)
        self._boots = boots


class ChestPieceSlot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def chest_piece(self):
        return self._chest_piece

    @chest_piece.setter
    def chest_piece(self, item):
        self.equip_item_to_slots(item, frozenset([ChestPieceSlot]))

    def equip(self, item):
        self._chest_piece = item

    def unequip(self):
        self._chest_piece = None

    def __init__(self, chest_piece=None, **kwargs):
        super().__init__(**kwargs)
        self._chest_piece = chest_piece


class HelmetSlot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def helmet(self):
        return self._helmet

    @helmet.setter
    def helmet(self, item):
        self.equip_item_to_slots(item, frozenset([HelmetSlot]))

    def equip(self, item):
        self._helmet = item

    def unequip(self):
        self._helmet = None

    def __init__(self, helmet=None, **kwargs):
        super().__init__(**kwargs)
        self._helmet = helmet


class Ring1Slot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def ring1(self):
        return self._ring1

    @ring1.setter
    def ring1(self, item):
        self.equip_item_to_slots(item, frozenset([Ring1Slot]))

    def equip(self, item):
        self._ring1 = item

    def unequip(self):
        self._ring1 = None

    def __init__(self, ring1=None, **kwargs):
        super().__init__(**kwargs)
        self._ring1 = ring1


class Ring2Slot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def ring2(self):
        return self._ring2

    @ring2.setter
    def ring2(self, item):
        self.equip_item_to_slots(item, frozenset([Ring2Slot]))

    def equip(self, item):
        self._ring2 = item

    def unequip(self):
        self._ring2 = None

    def __init__(self, ring2=None, **kwargs):
        super().__init__(**kwargs)
        self._ring2 = ring2


class ShieldSlot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def shield(self):
        return self._shield

    @shield.setter
    def shield(self, item):
        self.equip_item_to_slots(item, frozenset([ShieldSlot]))

    def equip(self, item):
        self._shield = item

    def unequip(self):
        self._shield = None

    def __init__(self, shield=None, **kwargs):
        super().__init__(**kwargs)
        self._shield = shield


class WeaponSlot(EquipmentSlot, metaclass=ABCMeta):
    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, item):
        self.equip_item_to_slots(item, frozenset([WeaponSlot]))

    def equip(self, item):
        self._weapon = item

    def unequip(self):
        self._weapon = None

    def __init__(self, weapon=None, **kwargs):
        super().__init__(**kwargs)
        self._weapon = weapon


class MageGear(AmuletSlot, BeltSlot, BootsSlot, ChestPieceSlot, HelmetSlot,
               Ring1Slot, Ring2Slot, ShieldSlot, WeaponSlot, metaclass=ABCMeta):
    @property
    def equipment(self):
        return {AmuletSlot: self.amulet,
                BootsSlot: self.boots,
                BeltSlot: self.belt,
                ChestPieceSlot: self.chest_piece,
                HelmetSlot: self.helmet,
                Ring1Slot: self.ring1,
                Ring2Slot: self.ring2,
                ShieldSlot: self.shield,
                WeaponSlot: self.weapon}

    def equip_item_to_slots(self, item, slots):
        slots = frozenset(slots)
        if slots not in item.valid_slot_sets:
            raise ValueError("Item %s cannot be equipped to slots %s" % (item, slots))

        for slot in slots:
            self.unequip_item_in_slot(slot)

        for slot in slots:
            self.equip_item_to_slot(item, slot)

    def unequip_item_in_slot(self, slot):
        if self.equipment[slot] is not None:
            logger.debug("Unequipping item in slot %s" % slot)
            item_to_remove = self.equipment[slot]
            for slot in self.equipment.keys():
                if self.equipment[slot] == item_to_remove:
                    self.unequip_slot(slot)

    def equip_item_to_slot(self, item, slot):
        slot.equip(self, item)

    def unequip_slot(self, slot: EquipmentSlot):
        slot.unequip(self)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)