import Deck_Evaluator.actions
import Deck_Evaluator.spell
import Deck_Evaluator.subtype


class Incantation(Deck_Evaluator.spell.Spell):
    default_class_properties = {
        "action_required":    Deck_Evaluator.actions.QuickSpellAction,
        "min_range":          0}

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Incantation, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {Deck_Evaluator.subtype.Enchantment}
        return namespace

    def __init__(cls, name, bases, namespace, **kwargs):
        for key, value in Incantation.default_class_properties.items():
            namespace.setdefault(key, value)
        super(Incantation, cls).__init__(name, bases, namespace, **kwargs)
