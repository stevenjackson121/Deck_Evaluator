import Deck_Evaluator.subtype


def all_(*funcs):
    def all_true(potential_target):
        return all(f(potential_target) for f in funcs)
    return all_true


def any_(*funcs):
    def any_true(potential_target):
        return any(f(potential_target) for f in funcs)
    return any_true


def has_trait(trait):
    def has_trait_(potential_target):
        return potential_target.has_trait(trait)
    return has_trait_


def is_a(subtype: Deck_Evaluator.subtype.Subtype):
    def is_subtype(potential_target):
        return isinstance(potential_target, subtype)
    return is_subtype


def not_(function):
    def negated_function(potential_target):
        return not function(potential_target)
    return negated_function
