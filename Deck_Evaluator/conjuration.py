import Deck_Evaluator.actions
import Deck_Evaluator.spell
import Deck_Evaluator.subtype
import Deck_Evaluator.target


class Conjuration(Deck_Evaluator.spell.Spell):
    default_class_properties = {
        "action_required":    Deck_Evaluator.actions.QuickSpellAction,
        "max_range":          1,
        "min_range":          0,
        "valid_target_rule": Deck_Evaluator.target.is_(Deck_Evaluator.subtype.Zone)}

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        namespace = super(Conjuration, mcs).__prepare__(name, bases, **kwargs)
        namespace["subtypes"] |= {"Equipment"}
        return namespace

    def __init__(cls, name, bases, namespace, **kwargs):
        for key, value in Conjuration.default_class_properties.items():
            namespace.setdefault(key, value)
        super(Conjuration, cls).__init__(name, bases, namespace, **kwargs)
