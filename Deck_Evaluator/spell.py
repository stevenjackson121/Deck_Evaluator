import Deck_Evaluator.attacks as attacks
import logging
import re
logger = logging.getLogger(__name__)


class Spell(type):
    lower_list = {'Of', 'And', 'The'}
    required_attributes = frozenset(["action_required",
                                     "casting_cost",
                                     "min_range",
                                     "max_range",
                                     "school_levels",
                                     "subtypes",
                                     "valid_target_rule"])

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        # noinspection PyArgumentList
        namespace = super().__prepare__(name, bases, **kwargs)
        for key, value in kwargs.items():
            namespace[key] = value
        namespace.setdefault("subtypes", set())
        namespace['level'] = classmethod(lambda cls: min(sum(sl.values()) for sl in cls.school_levels))

        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, bases, namespace)

    # noinspection PyUnusedLocal
    def __init__(cls, name, bases, namespace, **kwargs):
        missing_attributes = Spell.required_attributes.difference(frozenset(namespace.keys()))
        if len(missing_attributes) > 0:
            raise TypeError("Cannot create new spell type \"%s\"; Missing required attributes %s" %
                            (name, sorted(missing_attributes)))
        namespace.setdefault('card_name', ' '.join(w if w not in Spell.lower_list else w.lower()
                                              for w in re.findall('[A-Z][^A-Z]*', name)))

        super(Spell, cls).__init__(name, bases, namespace)


class Epic(Spell):
    pass


class Attack(Spell, attacks.Attack):
    pass


class Conjuration(Spell):
    pass


class Incantation(Spell):
    pass


class Wall(Spell):
    pass
