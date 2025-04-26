class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

    def __str__(self):
        return str(self.creature)


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling attack {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class IncreseDefenseModifier(CreatureModifier):
    def handle(self):
        print(f"Increasing defense {self.creature.name}'s defense")
        self.creature.defense += 1
        super().handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print(f"No bonuses for {self.creature.name}")


if __name__ == "__main__":
    creature = Creature("Goblin", 10, 5)
    print(creature)
    creature_modifier = CreatureModifier(creature)

    creature_modifier.add_modifier(NoBonusesModifier(creature))

    creature_modifier.add_modifier(DoubleAttackModifier(creature))
    creature_modifier.add_modifier(DoubleAttackModifier(creature))

    creature_modifier.add_modifier(IncreseDefenseModifier(creature))
    creature_modifier.add_modifier(IncreseDefenseModifier(creature))
    creature_modifier.handle()
    print(creature)
