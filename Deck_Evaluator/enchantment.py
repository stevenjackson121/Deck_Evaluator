import Deck_Evaluator.actions
import Deck_Evaluator.spell
import Deck_Evaluator.subtype
import Deck_Evaluator.target


class Enchantment(Deck_Evaluator.spell.Spell):
    default_class_properties = {
        "action_required":    Deck_Evaluator.actions.QuickSpellAction,
        "max_range":          2,
        "min_range":          0,
        "valid_target_rule": Deck_Evaluator.target.is_(Deck_Evaluator.subtype.Creature)}

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Enchantment, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {Deck_Evaluator.subtype.Enchantment}
        return namespace

    def __init__(cls, name, bases, namespace, **kwargs):
        if "reveal_cost" not in namespace:
            raise TypeError("Cannot create new spell type \"%s\"; Missing required attribute \"reveal_cost\"" % name)
        for key, value in Enchantment.default_class_properties.items():
            namespace.setdefault(key, value)
        super(Enchantment, cls).__init__(name, bases, namespace, **kwargs)
