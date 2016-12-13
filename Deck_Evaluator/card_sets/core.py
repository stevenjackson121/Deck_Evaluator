from Deck_Evaluator.attack_spell import Attack
from Deck_Evaluator.conjuration import Conjuration
from Deck_Evaluator.creature import Creature
from Deck_Evaluator.enchantment import Enchantment
from Deck_Evaluator.equipment.base_types import Amulet, Belt, Boots, ChestPiece, Gloves, Helmet, LargeWeapon, Ring, \
    SmallWeapon, Weapon
from Deck_Evaluator.incantation import Incantation
from Deck_Evaluator.mages import Mage
from Deck_Evaluator.schools import Dark, Fire


class Adremelech(metaclass=Creature, card_name="Adremelech, Lord of Fire", casting_cost=24,
                 school_levels=[{Dark: 2, Fire: 2}]):
    pass


class Agony(metaclass=Enchantment, casting_cost=2, reveal_cost=2, school_levels=[{Dark: 2}]):
    pass


class AnimalKinship(metaclass=Conjuration):
    pass


class ArcaneRing(metaclass=Ring):
    pass


class AsyranCleric(metaclass=Creature):
    pass


class Banish(metaclass=Incantation):
    pass


class BattleForge(metaclass=Conjuration):
    pass


class BattleFury(metaclass=Incantation):
    pass


class BearStrength(metaclass=Enchantment):
    pass


class Bearskin(metaclass=Enchantment):
    pass


class BeastMaster(metaclass=Mage):
    pass


class BitterwoodFox(metaclass=Creature):
    pass


class BlindingFlash(metaclass=Attack):
    pass


class Block(metaclass=Enchantment):
    pass


class BlueGremlin(metaclass=Creature):
    pass


class BroganBloodstone(metaclass=Creature):
    pass


class BullEndurance(metaclass=Enchantment):
    pass


class CallOfTheWild(metaclass=Incantation):
    pass


class CervereTheForestShadow(metaclass=Creature):
    pass


class ChainLightning(metaclass=Attack):
    pass


class ChainsOfAgony(metaclass=Enchantment):
    pass


class Charge(metaclass=Incantation):
    pass


class CheetahSpeed(metaclass=Enchantment):
    pass


class CobraReflexes(metaclass=Enchantment):
    pass


class CrownOfProtection(metaclass=Helmet):
    pass


class DarkPactSlayer(metaclass=Creature):
    pass


class DarkfenneBat(metaclass=Creature):
    pass


class DarkfenneHydra(metaclass=Creature):
    pass


class DawnbreakerRing(metaclass=Ring):
    pass


class DeathLink(metaclass=Enchantment):
    pass


class Deathlock(metaclass=Conjuration):
    pass


class Decoy(metaclass=Enchantment):
    pass


class DeflectionBracers(metaclass=Gloves):
    pass


class DemonhideArmor(metaclass=ChestPiece):
    pass


class Dispel(metaclass=Incantation):
    pass


class Dissolve(metaclass=Incantation):
    pass


class DivineIntervention(metaclass=Enchantment):
    pass


class DivineProtection(metaclass=Enchantment):
    pass


class DragonscaleHauberk(metaclass=ChestPiece):
    pass


class DrainLife(metaclass=Incantation):
    pass


class DrainPower(metaclass=Incantation):
    pass


class EagleWings(metaclass=Enchantment):
    pass


class Electrify(metaclass=Attack):
    pass


class ElementalCloak(metaclass=ChestPiece):
    pass


class ElementalWand(metaclass=SmallWeapon):
    pass


class EmeraldTegu(metaclass=Creature):
    pass


class EnchantersRing(metaclass=Ring):
    pass


class Enfeeble(metaclass=Enchantment):
    pass


class EssenceDrain(metaclass=Enchantment):
    pass


class Evade(metaclass=Incantation):
    pass


class Explode(metaclass=Incantation):
    pass


class FellelaPixieFamiliar(metaclass=Creature):
    pass


class FeralBobcat(metaclass=Creature):
    pass


class Fireball(metaclass=Attack):
    pass


class FirebrandImp(metaclass=Creature):
    pass


class FireshaperRing(metaclass=Ring):
    pass


class Firestorm(metaclass=Attack):
    pass


class Flameblast(metaclass=Attack):
    pass


class FlamingHellion(metaclass=Creature):
    pass


class FogBank(metaclass=Conjuration):
    pass


class ForceHold(metaclass=Enchantment):
    pass


class ForceOrb(metaclass=Enchantment):
    pass


class ForcePush(metaclass=Incantation):
    pass


class ForceSword(metaclass=Enchantment):
    pass


class GateToHell(metaclass=Conjuration):
    pass


class GateToVoltari(metaclass=Conjuration):
    pass


class GauntletsOfStrength(metaclass=Gloves):
    pass


class Geyser(metaclass=Attack):
    pass


class GhoulRot(metaclass=Enchantment):
    pass


class GoranWerewolfPet(metaclass=Creature):
    pass


class GorgonArcher(metaclass=Creature):
    pass


class GrayAngel(metaclass=Creature):
    pass


class GroupHeal(metaclass=Incantation):
    pass


class HandOfBimShalla(metaclass=Conjuration):
    pass


class Harmonize(metaclass=Enchantment):
    pass


class Hawkeye(metaclass=Enchantment):
    pass


class Heal(metaclass=Incantation):
    pass


class HellfireTrap(metaclass=Enchantment):
    pass


class HelmOfFear(metaclass=Helmet):
    pass


class HighlandUnicorn(metaclass=Creature):
    pass


class HuginnRavenFamiliar(metaclass=Creature):
    pass


class IdolOfPestilence(metaclass=Conjuration):
    pass


class IvariumLongbow(metaclass=LargeWeapon):
    pass


class JetStream(metaclass=Attack):
    pass


class Jinx(metaclass=Enchantment):
    pass


class KnightOfWestlock(metaclass=Creature):
    pass


class Knockdown(metaclass=Incantation):
    pass


class Lair(metaclass=Conjuration):
    pass


class LashOfHellfire(metaclass=Weapon):
    pass


class LayHands(metaclass=Incantation):
    pass


class LeatherBoots(metaclass=Boots):
    pass


class LeatherGloves(metaclass=Gloves):
    pass


class LightningBolt(metaclass=Attack):
    pass


class LightningRing(metaclass=Ring):
    pass


class MageStaff(metaclass=LargeWeapon):
    pass


class MageWand(metaclass=SmallWeapon):
    pass


class Magebane(metaclass=Enchantment):
    pass


class MaimWings(metaclass=Enchantment):
    pass


class Malacoda(metaclass=Creature):
    pass


class ManaCrystal(metaclass=Conjuration):
    pass


class ManaFlower(metaclass=Conjuration):
    pass


class ManaLeech(metaclass=Creature):
    pass


class ManaSiphon(metaclass=Conjuration):
    pass


class MarkedForDeath(metaclass=Enchantment):
    pass


class MinorHeal(metaclass=Incantation):
    pass


class MohktariGreatTreeOfLife(metaclass=Conjuration):
    pass


class MolochsTorment(metaclass=Amulet):
    pass


class MongooseAgility(metaclass=Enchantment):
    pass


class MoonglowAmulet(metaclass=Amulet):
    pass


class MoonglowFaerie(metaclass=Creature):
    pass


class MordoksObelisk(metaclass=Conjuration):
    pass


class MountainGorilla(metaclass=Creature):
    pass


class NecropianVampiress(metaclass=Creature):
    pass


class Nullify(metaclass=Enchantment):
    pass


class Pacify(metaclass=Enchantment):
    pass


class Pentagram(metaclass=Conjuration):
    pass


class PerfectStrike(metaclass=Incantation):
    pass


class PiercingStrike(metaclass=Incantation):
    pass


class PillarOfLight(metaclass=Attack):
    pass


class PoisonGasCloud(metaclass=Conjuration):
    pass


class PoisonedBlood(metaclass=Enchantment):
    pass


class Priestess(metaclass=Mage):
    pass


class PurgeMagic(metaclass=Incantation):
    pass


class Purify(metaclass=Incantation):
    pass


class RajansFury(metaclass=Conjuration):
    pass


class RedclawAlphaMale(metaclass=Creature):
    pass


class Regrowth(metaclass=Enchantment):
    pass


class RegrowthBelt(metaclass=Belt):
    pass


class Resurrection(metaclass=Incantation):
    pass


class Retaliate(metaclass=Enchantment):
    pass


class ReverseAttack(metaclass=Enchantment):
    pass


class ReverseMagic(metaclass=Enchantment):
    pass


class RhinoHide(metaclass=Enchantment):
    pass


class RingOfAsyra(metaclass=Ring):
    pass


class RingOfBeasts(metaclass=Ring):
    pass


class RingOfCurses(metaclass=Ring):
    pass


class RingOfFire(metaclass=Attack):
    pass


class RouseTheBeast(metaclass=Incantation):
    pass


class RoyalArcher(metaclass=Creature):
    pass


class SacredGround(metaclass=Enchantment):
    pass


class SacrificialAltar(metaclass=Conjuration):
    pass


class SamandrielAngelOfLight(metaclass=Creature):
    pass


class SeekingDispel(metaclass=Incantation):
    pass


class ShiftEnchantment(metaclass=Incantation):
    pass


class SkeletalSentry(metaclass=Creature):
    pass


class Sleep(metaclass=Incantation):
    pass


class SosrukoFerretCompanion(metaclass=Creature):
    pass


class StaffOfAsyra(metaclass=LargeWeapon):
    pass


class StaffOfBeasts(metaclass=LargeWeapon):
    pass


class StaffOfTheArcanum(metaclass=LargeWeapon):
    pass


class StealEnchantment(metaclass=Incantation):
    pass


class SteelclawGrizzly(metaclass=Creature):
    pass


class StonegazeBasilisk(metaclass=Creature):
    pass


class SuppressionCloak(metaclass=ChestPiece):
    pass


class SuppressionOrb(metaclass=Conjuration):
    pass


class Tanglevine(metaclass=Conjuration):
    pass


class TarokTheSkyHunter(metaclass=Creature):
    pass


class Teleport(metaclass=Incantation):
    pass


class TeleportTrap(metaclass=Enchantment):
    pass


class TempleOfAsyra(metaclass=Conjuration):
    pass


class TempleOfLight(metaclass=Conjuration):
    pass


class TempleOfTheDawnbreaker(metaclass=Conjuration):
    pass


class Thunderbolt(metaclass=Attack):
    pass


class ThunderiftFalcon(metaclass=Creature):
    pass


class TimberWolf(metaclass=Creature):
    pass


class ToothNail(metaclass=Conjuration):
    pass


class TurnToStone(metaclass=Enchantment):
    pass


class ValshallaLightningAngel(metaclass=Creature):
    pass


class VampiricStrike(metaclass=Incantation):
    pass


class Vampirism(metaclass=Enchantment):
    pass


class WallOfStone(metaclass=Conjuration):
    pass


class WallOfThorns(metaclass=Conjuration):
    pass


class Warlock(metaclass=Mage):
    pass


class WhirlingSpirit(metaclass=Creature):
    pass


class WindWyvernHide(metaclass=ChestPiece):
    pass


class Wizard(metaclass=Mage):
    pass


class WallOfFire(metaclass=Conjuration):
    pass
