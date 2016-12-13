import Deck_Evaluator.subtype


def is_(subtype: Deck_Evaluator.subtype.Subtype):
    return lambda potential_target: isinstance(potential_target, subtype)
