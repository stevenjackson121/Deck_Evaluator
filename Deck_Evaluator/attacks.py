class Attack:
    def __init__(self, type_, sequences):
        self.type = type_
        self.sequences = sequences

    def resolve(self):
        for sequence in self.sequences:
            yield sequence.resolve()


class Melee(Attack):
    def __init__(self, *args, **kwargs):
        super(Melee, self).__init__(Melee, *args, **kwargs)


class Ranged(Attack):
    def __init__(self, *args, **kwargs):
        super(Ranged, self).__init__(Ranged, *args, **kwargs)


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