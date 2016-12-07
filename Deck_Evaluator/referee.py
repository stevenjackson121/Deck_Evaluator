import random


class Engine:
    def __init__(self, name, current_score, mage='Wizard'):
        self.name = name
        self.current_score = current_score
        self.mage = mage

    def get_mage(self):
        return self.mage

    def get_spellbook(self):
        return SpellBook()


class Record:
    def __init__(self, wins=0, modified_wins=0, draws=0, losses=0):
        self.wins = wins
        self.modified_wins = modified_wins
        self.draws = draws
        self.losses = losses


class Game:
    def __init__(self, engines):
        self.engines = engines
        self.mage_book_dict = [new_mage(e.get_mage_type(), e.get_spellbook()) for e in engines]
        self.has_ended = False

    def play_round(self):
        pass


class Referee:
    def __init__(self, engine_arg_dict):
        self.engine_arg_dict = engine_arg_dict
        self.current_score = {
            'player1': Record(),
            'player2': Record()
        }

    def play_single_game(self):
        turn_order = self.engine_arg_dict.keys()
        random.shuffle(turn_order)
        engines = []
        for engine_name in turn_order:
            args, kwargs = self.engine_arg_dict[engine_name]
            engine_name.append(Engine(engine_name, current_score=self.current_score, *args, **kwargs))
        game = Game(engines)
        while not game.has_ended:
            game.play_round()
