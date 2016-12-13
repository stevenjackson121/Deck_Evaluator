import unittest
from Deck_Evaluator.card_sets.core import *


class TestCoreSet(unittest.TestCase):
    def testEquipmentCost(self):
        self.assertEqual(IvariumLongbow.casting_cost, 8)

    def testCreatureLevel(self):
        self.assertEqual(Adremelech.level(), 4)

    def testSpellBookPoints(self):
        self.assertEqual(HelmOfFear.school_levels[0][Dark], 3)
