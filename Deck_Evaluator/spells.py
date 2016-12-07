import attacks
import schools


def casting_cost(cast_cost):
    def decorator(cls):
        cls.casting_cost = cast_cost
        return cls
    return decorator


def spell_book_point_cost(**kwargs):
    def decorator(cls):
        if not hasattr(cls, 'spell_book_point_cost'):
            cls.spell_book_point_cost = []

        cost_dict = {}
        for key, value in kwargs.items():
            if not hasattr(schools, key):
                raise ValueError("Costs must be from the schools contained in schools.py")
            cost_dict[getattr(schools, key)] = value
        cls.spell_book_point_cost.append(cost_dict)
        return cls
    return decorator


class Spell(object):
    def __init__(self, name, subtypes, action_required, min_range, max_range, target, effect):
        self.name = name
        self.subtypes = subtypes
        self.casting_cost = self.__class__.casting_cost
        self.action_required = action_required
        self.min_range = min_range
        self.max_range = max_range
        self.target = target
        self.effect = effect
        self.spell_book_point_cost = self.__class__.spell_book_point_cost

    def get_modified_cost(self, trained_schools, opposed_schools):
        penalty = 2
        if self.school in trained_schools:
            penalty = 1
        elif self.school in opposed_schools:
            penalty = 3
        return self.casting_cost * penalty

    def get_raw_cost(self):
        return min(sum(d.values()) for d in self.school_level_dicts)


class Attack(Spell, attacks.Attack):
    def __init__(self, *args, **kwargs):
        super(Attack, self).__init__(*args, **kwargs)


class Conjuration(Spell):
    def __init__(self, *args, **kwargs):
        super(Conjuration, self).__init__(*args, **kwargs)


class Creature(Spell):
    def __init__(self, *args, **kwargs):
        super(Creature, self).__init__(*args, **kwargs)


class Enchantment(Spell):
    def __init__(self, *args, **kwargs):
        super(Enchantment, self).__init__(*args, **kwargs)


class Incantation(Spell):
    def __init__(self, *args, **kwargs):
        super(Incantation, self).__init__(*args, **kwargs)


class Wall(Spell):
    def __init__(self, *args, **kwargs):
        super(Wall, self).__init__(*args, **kwargs)

