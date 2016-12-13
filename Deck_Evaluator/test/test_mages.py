from Deck_Evaluator.card_sets.core import IvariumLongbow, NoviceBoots, FastBoots
from Deck_Evaluator.equipment.slots import ShieldSlot, WeaponSlot
from Deck_Evaluator.mages import *
import unittest


class TestEquipSingleSlot(unittest.TestCase):
    def runTest(self):
        mage = BeastMaster()
        boots = NoviceBoots()
        mage.boots = boots
        self.assertEqual(boots, mage.boots)

    def test_equip_single_bad_slot(self):
        beast_master = BeastMaster()
        boots = NoviceBoots()
        with self.assertRaises(ValueError):
            beast_master.helmet = boots

    def test_equip_double_slot(self):
        wizard = Wizard()
        bow = IvariumLongbow()
        wizard.equip_item_to_slots(bow, (ShieldSlot, WeaponSlot))
        self.assertEqual(bow, wizard.weapon)
        self.assertEqual(bow, wizard.shield)

    def test_equip_double_bad_slots(self):
        wizard = Wizard()
        bow = IvariumLongbow()
        with self.assertRaises(ValueError):
            wizard.equip_item_to_slots(bow, (WeaponSlot, WeaponSlot))

    def test_replace_equip_single_slot(self):
        beast_master = BeastMaster()
        boots1 = NoviceBoots()
        boots2 = FastBoots()
        beast_master.boots = boots1
        beast_master.boots = boots2
        self.assertEqual(boots2, beast_master.boots)

if __name__ == '__main__':
    unittest.main()