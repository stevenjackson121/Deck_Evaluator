import Deck_Evaluator.actions
import Deck_Evaluator.spell
import Deck_Evaluator.target
import Deck_Evaluator.subtype


class Creature(Deck_Evaluator.spell.Spell):
    default_class_properties = {
        "action_required":    Deck_Evaluator.actions.FullAction,
        "max_range":          0,
        "min_range":          0,
        "valid_target_rule": Deck_Evaluator.target.is_a(Deck_Evaluator.subtype.Zone)}

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Creature, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Creature"}
        return namespace

    def __init__(cls, name, bases, namespace, **kwargs):
        for key, value in Creature.default_class_properties.items():
            namespace.setdefault(key, value)
        super(Creature, cls).__init__(name, bases, namespace, **kwargs)
