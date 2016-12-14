class Attack(type):
    @classmethod
    def __prepare__(mcs, name, bases, type_=None, **kwargs):
        namespace = super().__prepare__(name, bases, **kwargs)
        namespace['type'] = type_
        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        super(Attack, cls).__init__(name, bases, namespace)

    def resolve(self):
        for sequence in self.sequences:
            yield sequence.resolve()


class Quick(Attack):
    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, bases, namespace)


class Full(Attack):
    pass


class Melee(Attack):
    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, bases, namespace)


class Ranged(Attack):
    pass


class QuickMelee(Melee, Quick):
    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, bases, namespace)


class FullMelee(Melee, Full):
    pass


class QuickRanged(Ranged, Quick):
    pass


class FullRanged(Ranged, Full):
    pass


class Sequence:
    def __init__(self, steps):
        self.steps = steps

    def resolve(self):
        for step in self.steps:
            yield step.resolve()


class Step:
    def __init__(self):
        pass

    def resolve(self):
        raise NotImplementedError


class Declare(Step):
    def __init__(self, *args, **kwargs):
        super(Declare, self).__init__(*args, **kwargs)

    def resolve(self):
        yield {}


class Avoid(Step):
    def __init__(self, *args, **kwargs):
        super(Avoid, self).__init__(*args, **kwargs)


class Roll(Step):
    def __init__(self, *args, **kwargs):
        super(Roll, self).__init__(*args, **kwargs)


class DamageAndEffects(Step):
    def __init__(self, *args, **kwargs):
        super(DamageAndEffects, self).__init__(*args, **kwargs)


class DamageBarrier(Step):
    def __init__(self, *args, **kwargs):
        super(DamageBarrier, self).__init__(*args, **kwargs)