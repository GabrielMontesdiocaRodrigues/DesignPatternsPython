from enum import Enum
from abc import ABC


class Event(list):
    def __call__(self, *args, **kwargs):
        for event in self:
            event(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature, what_to_query: WhatToQuery, default_value):
        self.value = default_value
        self.creature = creature
        self.what_to_query: WhatToQuery = what_to_query


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.game: Game = game
        self.creature: Creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender == self.creature and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


class Creature:
    def __init__(self, game: Game, name, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game: Game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


if __name__ == '__main__':
    game = Game()
    creature = Creature(game, 'Strong Goblin', 2, 2)
    print(creature)

    with DoubleAttackModifier(game, creature):
        print(creature)

    print(creature)
