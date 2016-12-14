from Deck_Evaluator.actions import FullAction
from Deck_Evaluator.attack_spell import AttackSpell
from Deck_Evaluator.attacks import QuickMelee
from Deck_Evaluator.conjuration import Conjuration
from Deck_Evaluator.creature import Creature
from Deck_Evaluator.enchantment import Enchantment
from Deck_Evaluator.equipment.base_types import Amulet, Belt, Boots, ChestPiece, Gloves, Helmet, LargeWeapon, Ring, \
    SmallWeapon, Weapon
from Deck_Evaluator.incantation import Incantation
from Deck_Evaluator.mages import Mage
from Deck_Evaluator.schools import Arcane, Dark, Fire, Nature
from Deck_Evaluator.target import is_a, not_, any_, all_, has_trait
from Deck_Evaluator.traits import Corporeal


class Adremelech(metaclass=Creature, card_name="Adremelech, Lord of Fire", casting_cost=24,
                 school_levels=[{Dark: 4, Fire: 2}], subtypes={'Demon'},
                 traits=["Flying", "Flame Immunity", "Legendary"]):
    class HellfireScythe(metaclass=QuickMelee, type_=Fire, dice=6, traits=["Defrost"]):
        pass

    class HellfireSweep(metaclass=QuickMelee, type_=Fire, dice=4, traits=["Defrost", "Sweeping"]):
        pass


class Agony(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{Dark: 1}], subtypes={'Curse'}):
    """Whenever this creature makes a non-spell ranged or melee attack, it rolls 2 fewer attach dice"""
    pass


class AnimalKinship(metaclass=Conjuration, casting_cost=8, school_levels=[{Nature: 2}], subtypes={'Totem'}):
    pass


class ArcaneRing(metaclass=Ring, casting_cost=2, school_levels=[{Arcane: 1}], subtypes={'Mana'}):
    pass


class AsyranCleric(metaclass=Creature, casting_cost=5, school_levels=[{'Holy': 1}], subtypes={'Cleric'}):
    pass


class Banish(metaclass=Incantation, casting_cost=14, max_range=2, school_levels=[{'Arcane': 3}], subtypes={'Teleport'},
             valid_target_rule=all_(is_a(Creature), not_(is_a(Mage)))):
    pass


class BattleForge(metaclass=Conjuration, casting_cost=8, school_levels=[{'Fire': '1', 'War': '1'}],
                  subtypes={'Structure'}):
    pass


class BattleFury(metaclass=Incantation, casting_cost=5, max_range=2, school_levels=[{'War': 1}], subtypes={'Command'},
                 valid_target_rule=all_(is_a(Creature), has_trait(Corporeal))):
    pass


class BearStrength(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Nature': 1}], subtypes={''}):
    pass


class Bearskin(metaclass=ChestPiece, casting_cost=6, school_levels=[{'Nature': 1}]):
    pass


class BeastMaster(metaclass=Mage):
    pass


class BitterwoodFox(metaclass=Creature, casting_cost=5, school_levels=[{'Nature': 1}], subtypes={'Animal', 'Canine'}):
    pass


class BlindingFlash(metaclass=AttackSpell, action_required=FullAction, casting_cost=7, max_range=0, min_range=0,
                    school_levels=[{'Holy': 2}], subtypes={'Light'}, valid_target_rule=lambda: True):
    pass


class Block(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Mind': 1}],
            subtypes={'Defense', 'Force'}):
    pass


class BlueGremlin(metaclass=Creature, casting_cost=7, school_levels=[{'Arcane': 2}], subtypes={'Gremlin'}):
    pass


class BroganBloodstone(metaclass=Creature, casting_cost=15, school_levels=[{'Holy': 4}],
                       subtypes={'Knight', 'Soldier'}):
    pass


class BullEndurance(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Nature': 1}]):
    pass


class CallOfTheWild(metaclass=Incantation, casting_cost=4, school_levels=[{'Nature': 1}]):
    pass


class CervereTheForestShadow(metaclass=Creature, casting_cost=15, school_levels=[{'Nature': 4}],
                             subtypes={'Animal', 'Cat'}):
    pass


class ChainLightning(metaclass=AttackSpell, casting_cost=12, school_levels=[{'Air': 3}], subtypes={'Lightning'}):
    pass


class ChainsOfAgony(metaclass=Enchantment, casting_cost=2, reveal_cost=1, school_levels=[{'Dark': 1}],
                    subtypes={'Curse'}):
    pass


class Charge(metaclass=Incantation, casting_cost=4, school_levels=[{'War': 1}], subtypes={'Command'}):
    pass


class CheetahSpeed(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Nature': 1}]):
    pass


class CobraReflexes(metaclass=Enchantment, casting_cost=2, reveal_cost=5, school_levels=[{'Nature': 2}],
                    subtypes={'Defense'}):
    pass


class CrownOfProtection(metaclass=Helmet, casting_cost=1, school_levels=[{'Holy': 1}], subtypes={'Protection'}):
    pass


class DarkPactSlayer(metaclass=Creature, casting_cost=13, school_levels=[{'Dark': 3}], subtypes={'Demon'}):
    pass


class DarkfenneBat(metaclass=Creature, casting_cost=5, school_levels=[{'Dark': 1}], subtypes={'Animal', 'Bat'}):
    pass


class DarkfenneHydra(metaclass=Creature, casting_cost=16, school_levels=[{'Arcane': 4}], subtypes={'Serpent'}):
    pass


class DawnbreakerRing(metaclass=Ring, casting_cost=3, school_levels=[{'Holy': 1}]):
    pass


class DeathLink(metaclass=Enchantment, casting_cost=2, reveal_cost=6, school_levels=[{'Dark': 2}], subtypes={'Curse'}):
    pass


class Deathlock(metaclass=Conjuration, casting_cost=9, school_levels=[{'Dark': 2}], subtypes={'Artifact'}):
    pass


class Decoy(metaclass=Enchantment, casting_cost=2, reveal_cost=0, school_levels=[{'Mind': 1}], subtypes={'Illusion'}):
    pass


class DeflectionBracers(metaclass=Gloves, casting_cost=6, school_levels=[{'War': 1}], subtypes={'Defense'}):
    pass


class DemonhideArmor(metaclass=ChestPiece, casting_cost=8, school_levels=[{'Dark': 2}]):
    pass


class Dispel(metaclass=Incantation, casting_cost='X', school_levels=[{'Arcane': 1}], subtypes={'Metamagic'}):
    pass


class Dissolve(metaclass=Incantation, casting_cost='X', school_levels=[{'Water': 1}], subtypes={'Acid'}):
    pass


class DivineIntervention(metaclass=Enchantment, casting_cost=2, reveal_cost=10, school_levels=[{'Holy': 3}],
                         subtypes={'Protection'}):
    pass


class DivineProtection(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Holy': 1}],
                       subtypes={'Aegis', 'Protection'}):
    pass


class DragonscaleHauberk(metaclass=ChestPiece, casting_cost=6, school_levels=[{'Fire': 1}]):
    pass


class DrainLife(metaclass=Incantation, casting_cost=12, school_levels=[{'Dark': 3}], subtypes={'Vampiric'}):
    pass


class DrainPower(metaclass=Incantation, casting_cost=16, school_levels=[{'Arcane': 3}], subtypes={'Mana'}):
    pass


class EagleWings(metaclass=Enchantment, casting_cost=2, reveal_cost=4, school_levels=[{'Nature': 2}]):
    pass


class Electrify(metaclass=AttackSpell, casting_cost=9, school_levels=[{'Air': 2}], subtypes={'Lightning'}):
    pass


class ElementalCloak(metaclass=ChestPiece, casting_cost=6, school_levels=[{'Arcane': 1}]):
    pass


class ElementalWand(metaclass=SmallWeapon, casting_cost=5,
                    school_levels=[{'Earth': '2'}, {'Fire': '2'}, {'Air': '2'}, {'Water': '2'}]):
    pass


class EmeraldTegu(metaclass=Creature, casting_cost=9, school_levels=[{'Nature': 2}], subtypes={'Animal', 'Reptile'}):
    pass


class EnchantersRing(metaclass=Ring, casting_cost=2, school_levels=[{'Arcane': '1'}, {'Nature': '1'}]):
    pass


class Enfeeble(metaclass=Enchantment, casting_cost=2, reveal_cost=4, school_levels=[{'Dark': 2}], subtypes={'Curse'}):
    pass


class EssenceDrain(metaclass=Enchantment, casting_cost=2, reveal_cost=4, school_levels=[{'Arcane': 2}],
                   subtypes={'Mana'}):
    pass


class Evade(metaclass=Incantation, casting_cost=3, school_levels=[{'War': 1}], subtypes={'Command'}):
    pass


class Explode(metaclass=Incantation, casting_cost='X', school_levels=[{'Fire': 2}], subtypes={'Flame'}):
    pass


class FellellaPixieFamiliar(metaclass=Creature, casting_cost=12, school_levels=[{'Nature': 3}], subtypes={'Faerie'}):
    pass


class FeralBobcat(metaclass=Creature, casting_cost=5, school_levels=[{'Nature': 1}], subtypes={'Animal', 'Cat'}):
    pass


class Fireball(metaclass=AttackSpell, casting_cost=8, school_levels=[{'Fire': 2}], subtypes={'Flame'}):
    pass


class FirebrandImp(metaclass=Creature, casting_cost=5, school_levels=[{'Dark': 1}], subtypes={'Demon'}):
    pass


class FireshaperRing(metaclass=Ring, casting_cost=3, school_levels=[{'Fire': 1}]):
    pass


class Firestorm(metaclass=AttackSpell, casting_cost=11, school_levels=[{'Fire': 3}], subtypes={'Flame'}):
    pass


class Flameblast(metaclass=AttackSpell, casting_cost=5, school_levels=[{'Fire': 1}], subtypes={'Flame'}):
    pass


class FlamingHellion(metaclass=Creature, casting_cost=13, school_levels=[{'Dark': 3}], subtypes={'Demon'}):
    pass


class FogBank(metaclass=Conjuration, casting_cost=4, school_levels=[{'Air': 1}], subtypes={'Cloud'}):
    pass


class ForceHold(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Mind': 2}], subtypes={'Force'}):
    pass


class ForceOrb(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Mind': 1}],
               subtypes={'Defense', 'Force'}):
    pass


class ForcePush(metaclass=Incantation, casting_cost=3, school_levels=[{'Mind': 1}], subtypes={'Force'}):
    pass


class ForceSword(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Mind': 1}],
                 subtypes={'Defense', 'Force'}):
    pass


class GateToHell(metaclass=Conjuration, casting_cost=12, school_levels=[{'Dark': 6}], subtypes={'Portal'}):
    pass


class GateToVoltari(metaclass=Conjuration, casting_cost=14, school_levels=[{'Arcane': 4}], subtypes={'Portal'}):
    pass


class GauntletsOfStrength(metaclass=Gloves, casting_cost=3, school_levels=[{'War': 1}]):
    pass


class Geyser(metaclass=AttackSpell, casting_cost=4, school_levels=[{'Water': 1}], subtypes={'Hydro'}):
    pass


class GhoulRot(metaclass=Enchantment, casting_cost=2, reveal_cost=4, school_levels=[{'Dark': 2}],
               subtypes={'Curse', 'Poison'}):
    pass


class GoranWerewolfPet(metaclass=Creature, casting_cost=15, school_levels=[{'Dark': 4}],
                       subtypes={'Canine', 'Lycanthrope'}):
    pass


class GorgonArcher(metaclass=Creature, casting_cost=16, school_levels=[{'Arcane': 4}], subtypes={'Serpent'}):
    pass


class GrayAngel(metaclass=Creature, casting_cost=12, school_levels=[{'Holy': 3}], subtypes={'Angel'}):
    pass


class GroupHeal(metaclass=Incantation, casting_cost=9, school_levels=[{'Holy': 2}], subtypes={'Healing'}):
    pass


class HandOfBimShalla(metaclass=Conjuration, casting_cost=5, school_levels=[{'Holy': 1}], subtypes={'Temple'}):
    pass


class Harmonize(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Arcane': 1}], subtypes={'Mana'}):
    pass


class Hawkeye(metaclass=Enchantment, casting_cost=2, reveal_cost=1, school_levels=[{'Nature': 1}]):
    pass


class Heal(metaclass=Incantation, casting_cost=9, school_levels=[{'Holy': 2}], subtypes={'Healing'}):
    pass


class HellfireTrap(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Dark': 1}],
                   subtypes={'Flame', 'Trap'}):
    pass


class HelmOfFear(metaclass=Helmet, casting_cost=8, school_levels=[{'Dark': 2}]):
    pass


class HighlandUnicorn(metaclass=Creature, casting_cost=13, school_levels=[{'Holy': 3}], subtypes={'Animal', 'Horse'}):
    pass


class HuginnRavenFamiliar(metaclass=Creature, casting_cost=11, school_levels=[{'Arcane': 3}],
                          subtypes={'Animal', 'Bird'}):
    pass


class IdolOfPestilence(metaclass=Conjuration, casting_cost=9, school_levels=[{'Dark': 2}], subtypes={'Artifact'}):
    pass


class IvariumLongbow(metaclass=LargeWeapon, casting_cost=8, school_levels=[{'War': 2}]):
    pass


class JetStream(metaclass=AttackSpell, casting_cost=4, school_levels=[{'Air': 1}], subtypes={'Wind'}):
    pass


class Jinx(metaclass=Enchantment, casting_cost=2, reveal_cost=1, school_levels=[{'Arcane': 1}], subtypes={'Metamagic'}):
    pass


class KnightOfWestlock(metaclass=Creature, casting_cost=13, school_levels=[{'Holy': 3}],
                       subtypes={'Knight', 'Soldier'}):
    pass


class Knockdown(metaclass=Incantation, casting_cost=3, school_levels=[{'Mind': 1}], subtypes={'Force'}):
    pass


class Lair(metaclass=Conjuration, casting_cost=15, school_levels=[{'Nature': 4}], subtypes={'Portal'}):
    pass


class LashOfHellfire(metaclass=Weapon, casting_cost=8, school_levels=[{'Dark': '1', 'Fire': '1'}]):
    pass


class LayHands(metaclass=Incantation, casting_cost=9, school_levels=[{'Holy': 3}], subtypes={'Healing'}):
    pass


class LeatherBoots(metaclass=Boots, casting_cost=2, school_levels=[{'War': 1}]):
    pass


class LeatherGloves(metaclass=Gloves, casting_cost=2, school_levels=[{'War': 1}]):
    pass


class LightningBolt(metaclass=AttackSpell, casting_cost=8, school_levels=[{'Air': 2}], subtypes={'Lightning'}):
    pass


class LightningRing(metaclass=Ring, casting_cost=3, school_levels=[{'Air': 1}]):
    pass


class MageStaff(metaclass=LargeWeapon, casting_cost=5, school_levels=[{'Arcane': 1}]):
    pass


class MageWand(metaclass=SmallWeapon, casting_cost=5, school_levels=[{'Arcane': 2}]):
    pass


class Magebane(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Dark': 1}], subtypes={'Curse'}):
    pass


class MaimWings(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Dark': 1}], subtypes={'Curse'}):
    pass


class Malacoda(metaclass=Creature, casting_cost=16, school_levels=[{'Dark': 4}], subtypes={'Demon'}):
    pass


class ManaCrystal(metaclass=Conjuration, casting_cost=5, school_levels=[{'Arcane': 1}], subtypes={'Mana'}):
    pass


class ManaFlower(metaclass=Conjuration, casting_cost=5, school_levels=[{'Nature': 1}], subtypes={'Mana', 'Plant'}):
    pass


class ManaLeech(metaclass=Creature, casting_cost=8, school_levels=[{'Arcane': 2}], subtypes={'Worm'}):
    pass


class ManaSiphon(metaclass=Conjuration, casting_cost=12, school_levels=[{'Arcane': 3}], subtypes={'Mana', 'Portal'}):
    pass


class MarkedForDeath(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Dark': 1}],
                     subtypes={'Curse'}):
    pass


class MinorHeal(metaclass=Incantation, casting_cost=5, school_levels=[{'Holy': 1}], subtypes={'Healing'}):
    pass


class MohktariGreatTreeOfLife(metaclass=Conjuration, casting_cost=8, school_levels=[{'Nature': 2}],
                              subtypes={'Plant', 'Tree'}):
    pass


class MolochsTorment(metaclass=Amulet, casting_cost=3, school_levels=[{'Dark': 1}]):
    pass


class MongooseAgility(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Nature': 1}],
                      subtypes={}):
    pass


class MoonglowAmulet(metaclass=Amulet, casting_cost=6, school_levels=[{'Arcane': 1}], subtypes={'Mana'}):
    pass


class MoonglowFaerie(metaclass=Creature, casting_cost=8, school_levels=[{'Arcane': 2}], subtypes={'Faerie'}):
    pass


class MordoksObelisk(metaclass=Conjuration, casting_cost=8, school_levels=[{'Arcane': 2}],
                     subtypes={'Artifact', 'Obelisk'}):
    pass


class MountainGorilla(metaclass=Creature, casting_cost=16, school_levels=[{'Nature': 4}], subtypes={'Animal', 'Ape'}):
    pass


class NecropianVampiress(metaclass=Creature, casting_cost=16, school_levels=[{'Dark': 4}], subtypes={'Vampire'}):
    pass


class Nullify(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Arcane': 1}],
              subtypes={'Metamagic'}):
    pass


class Pacify(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Holy': 1}], subtypes={'Psychic'}):
    pass


class Pentagram(metaclass=Conjuration, casting_cost=14, school_levels=[{'Dark': 4}], subtypes={'Portal', 'Rune'}):
    pass


class PerfectStrike(metaclass=Incantation, casting_cost=2, school_levels=[{'War': 1}], subtypes={'Command'}):
    pass


class PiercingStrike(metaclass=Incantation, casting_cost=2, school_levels=[{'War': 1}], subtypes={'Command'}):
    pass


class PillarOfLight(metaclass=AttackSpell, casting_cost=5, school_levels=[{'Holy': 1}], subtypes={'Light'}):
    pass


class PoisonGasCloud(metaclass=Conjuration, casting_cost=8, school_levels=[{'Air': 2}], subtypes={'Cloud', 'Poison'}):
    pass


class PoisonedBlood(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Dark': 1}],
                    subtypes={'Curse', 'Poison'}):
    pass


class Priestess(metaclass=Mage):
    pass


class PurgeMagic(metaclass=Incantation, casting_cost=12, school_levels=[{'Arcane': 3}], subtypes={'Metamagic'}):
    pass


class Purify(metaclass=Incantation, casting_cost='X', school_levels=[{'Holy': 1}], subtypes={'Healing'}):
    pass


class RajansFury(metaclass=Conjuration, casting_cost=7, school_levels=[{'Nature': 2}], subtypes={'Totem'}):
    pass


class RedclawAlphaMale(metaclass=Creature, casting_cost=16, school_levels=[{'Nature': 4}],
                       subtypes={'Animal', 'Canine'}):
    pass


class Regrowth(metaclass=Enchantment, casting_cost=2, reveal_cost=3, school_levels=[{'Nature': 1}]):
    pass


class RegrowthBelt(metaclass=Belt, casting_cost=6, school_levels=[{'Nature': 1}]):
    pass


class Resurrection(metaclass=Incantation, casting_cost='X', school_levels=[{'Holy': 4}], subtypes={'Healing'}):
    pass


class Retaliate(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'War': 1}]):
    pass


class ReverseAttack(metaclass=Enchantment, casting_cost=2, reveal_cost=5, school_levels=[{'Mind': 2}],
                    subtypes={'Defense', 'Force'}):
    pass


class ReverseMagic(metaclass=Enchantment, casting_cost=2, reveal_cost=5, school_levels=[{'Arcane': 2}],
                   subtypes={'Metamagic'}):
    pass


class RhinoHide(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Nature': 1}]):
    pass


class RingOfAsyra(metaclass=Ring, casting_cost=2, school_levels=[{'Holy': 1}], subtypes={'Mana'}):
    pass


class RingOfBeasts(metaclass=Ring, casting_cost=2, school_levels=[{'Nature': 1}], subtypes={'Mana'}):
    pass


class RingOfCurses(metaclass=Ring, casting_cost=2, school_levels=[{'Dark': 1}], subtypes={'Mana'}):
    pass


class RingOfFire(metaclass=AttackSpell, casting_cost=9, school_levels=[{'Fire': 2}], subtypes={'Flame'}):
    pass


class RouseTheBeast(metaclass=Incantation, casting_cost='X', school_levels=[{'Nature': 1}]):
    pass


class RoyalArcher(metaclass=Creature, casting_cost=12, school_levels=[{'Holy': 3}], subtypes={'HighElf', 'Soldier'}):
    pass


class SacredGround(metaclass=Enchantment, casting_cost=2, reveal_cost=4, school_levels=[{'Holy': 2}],
                   subtypes={'Aegis', 'Protection'}):
    pass


class SacrificialAltar(metaclass=Conjuration, casting_cost=4, school_levels=[{'Dark': 1}]):
    pass


class SamandrielAngelOfLight(metaclass=Creature, casting_cost=21, school_levels=[{'Holy': 5}], subtypes={'Angel'}):
    pass


class SeekingDispel(metaclass=Incantation, casting_cost=2, school_levels=[{'Arcane': 1}], subtypes={'Metamagic'}):
    pass


class ShiftEnchantment(metaclass=Incantation, casting_cost='X', school_levels=[{'Arcane': 1}], subtypes={'Metamagic'}):
    pass


class SkeletalSentry(metaclass=Creature, casting_cost=8, school_levels=[{'Dark': 2}], subtypes={'Skeleton', 'Undead'}):
    pass


class Sleep(metaclass=Incantation, casting_cost='X', school_levels=[{'Mind': 2}], subtypes={'Psychic'}):
    pass


class SosrukoFerretCompanion(metaclass=Creature, casting_cost=7, school_levels=[{'Nature': 2}], subtypes={'Animal'}):
    pass


class StaffOfAsyra(metaclass=LargeWeapon, casting_cost=9, school_levels=[{'Holy': 2}]):
    pass


class StaffOfBeasts(metaclass=LargeWeapon, casting_cost=7, school_levels=[{'Nature': 2}]):
    pass


class StaffOfTheArcanum(metaclass=LargeWeapon, casting_cost=8, school_levels=[{'Arcane': 2}]):
    pass


class StealEnchantment(metaclass=Incantation, casting_cost='X', school_levels=[{'Arcane': 3}], subtypes={'Metamagic'}):
    pass


class SteelclawGrizzly(metaclass=Creature, casting_cost=17, school_levels=[{'Nature': 4}], subtypes={'Animal', 'Bear'}):
    pass


class StonegazeBasilisk(metaclass=Creature, casting_cost=12, school_levels=[{'Arcane': 3}],
                        subtypes={'Lizard', 'Reptile'}):
    pass


class SuppressionCloak(metaclass=ChestPiece, casting_cost=8, school_levels=[{'Arcane': 2}], subtypes={'Mana'}):
    pass


class SuppressionOrb(metaclass=Conjuration, casting_cost=8, school_levels=[{'Mind': 2}],
                     subtypes={'Artifact', 'Force', 'Mana'}):
    pass


class Tanglevine(metaclass=Conjuration, casting_cost=5, school_levels=[{'Nature': 1}], subtypes={'Plant', 'Vine'}):
    pass


class TarokTheSkyhunter(metaclass=Creature, casting_cost=13, school_levels=[{'Nature': 3}],
                        subtypes={'Animal', 'Bird'}):
    pass


class Teleport(metaclass=Incantation, casting_cost='X', school_levels=[{'Arcane': 2}], subtypes={'Teleport'}):
    pass


class TeleportTrap(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{'Arcane': 1}],
                   subtypes={'Teleport', 'Trap'}):
    pass


class TempleOfAsyra(metaclass=Conjuration, casting_cost=10, school_levels=[{'Holy': 3}], subtypes={'Portal', 'Temple'}):
    pass


class TempleOfLight(metaclass=Conjuration, casting_cost=9, school_levels=[{'Holy': 2}], subtypes={'Temple'}):
    pass


class TempleOfTheDawnbreaker(metaclass=Conjuration, casting_cost=8, school_levels=[{'Holy': 2}], subtypes={'Temple'}):
    pass


class Thunderbolt(metaclass=AttackSpell, casting_cost=10, school_levels=[{'Air': 3}], subtypes={'Lightning'}):
    pass


class ThunderiftFalcon(metaclass=Creature, casting_cost=6, school_levels=[{'Nature': 1}], subtypes={'Animal', 'Bird'}):
    pass


class TimberWolf(metaclass=Creature, casting_cost=9, school_levels=[{'Nature': 2}], subtypes={'Animal', 'Canine'}):
    pass


class ToothNail(metaclass=Conjuration, casting_cost=7, school_levels=[{'Nature': 2}], subtypes={'Totem'}):
    pass


class TurnToStone(metaclass=Enchantment, casting_cost=2, reveal_cost=4, school_levels=[{'Earth': '1', 'Arcane': '2'}],
                  subtypes={'Transform'}):
    pass


class ValshallaLightningAngel(metaclass=Creature, casting_cost=21, school_levels=[{'Holy': 5}], subtypes={'Angel'}):
    pass


class VampiricStrike(metaclass=Incantation, casting_cost=3, school_levels=[{'Dark': 1}], subtypes={'Vampiric'}):
    pass


class Vampirism(metaclass=Enchantment, casting_cost=2, reveal_cost=4, school_levels=[{'Dark': 2}],
                subtypes={'Vampiric'}):
    pass


class WallOfFire(metaclass=Conjuration, casting_cost=7, school_levels=[{'Fire': 2}], subtypes={'Flame'}):
    pass


class WallOfStone(metaclass=Conjuration, casting_cost=7, school_levels=[{'Earth': 2}], subtypes={'Stone'}):
    pass


class WallOfThorns(metaclass=Conjuration, casting_cost=5, school_levels=[{'Nature': 1}], subtypes={'Plant'}):
    pass


class Warlock(metaclass=Mage):
    pass


class WhirlingSpirit(metaclass=Creature, casting_cost=12, school_levels=[{'Air': 4}], subtypes={'Wind'}):
    pass


class WindWyvernHide(metaclass=ChestPiece, casting_cost=6, school_levels=[{'Air': 1}]):
    pass


class Wizard(metaclass=Mage):
    pass
