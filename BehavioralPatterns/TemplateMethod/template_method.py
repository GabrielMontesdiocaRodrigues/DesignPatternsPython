from abc import ABC, abstractmethod


class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        self.hit(c1, c2)
        self.hit(c2, c1)

        c1_alive = c1.health > 0
        c2_alive = c2.health > 0

        if c1_alive and not c2_alive:
            return c1_index
        elif c2_alive and not c1_alive:
            return c2_index
        else:
            return -1

    @abstractmethod
    def hit(self, attacker, defender):
        pass


class TemporaryDamageCardGame(CardGame):
    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        original_health_c1 = c1.health
        original_health_c2 = c2.health

        result = super().combat(c1_index, c2_index)

        if c1.health > 0:
            c1.health = original_health_c1
        if c2.health > 0:
            c2.health = original_health_c2

        return result

    def hit(self, attacker, defender):
        defender.health -= attacker.attack


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
