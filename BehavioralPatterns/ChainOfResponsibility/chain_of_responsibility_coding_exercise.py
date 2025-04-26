from enum import Enum, auto
from abc import abstractmethod


class Stat(Enum):
    ATTACK = auto()
    DEFENSE = auto()


class Query:
    def __init__(self, creature_name, stat, initial_value):
        self.creature_name = creature_name
        self.stat = stat
        self.value = initial_value


class Game:
    def __init__(self):
        self.creatures = []

    def perform_query(self, source, query):
        for creature in self.creatures:
            creature.process_query(source, query)


class Creature:
    def __init__(self, game, name, base_attack, base_defense):
        self.game = game
        self.name = name
        self.base_attack = base_attack
        self.base_defense = base_defense

    @abstractmethod
    def process_query(self, source, query):
        pass

    @property
    def attack(self):
        q = Query(self.name, Stat.ATTACK, self.base_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, Stat.DEFENSE, self.base_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class Goblin(Creature):
    def __init__(self, game):
        super().__init__(game, "Goblin", 1, 1)

    def process_query(self, source, query):
        if self == source:
            return
        if query.stat == Stat.DEFENSE:
            query.value += 1


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game)
        self.name = "Goblin King"
        self.base_attack = 3
        self.base_defense = 3

    def process_query(self, source, query):
        if self == source:
            return
        if query.stat == Stat.ATTACK:
            query.value += 1
        elif query.stat == Stat.DEFENSE:
            query.value += 1


if __name__ == "__main__":
    game = Game()
    game.creatures.append(Goblin(game))
    game.creatures.append(Goblin(game))
    game.creatures.append(Goblin(game))
    game.creatures.append(GoblinKing(game))

    for creature in game.creatures:
        print(creature)
