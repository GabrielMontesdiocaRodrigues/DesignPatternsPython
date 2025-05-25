class Event(list):
    def __call__(self, *args, **kwds):
        for event in self:
            event(*args, **kwds)


class Game:
    def __init__(self):
        self.on_change_rats: Event = Event()


class Rat:
    def __init__(self, game: Game):
        self.game = game
        self.attack = 1

        game.on_change_rats.append(self.on_rat_added)
        game.on_change_rats.append(self.on_rat_removed)
        game.on_change_rats('added_rat', self)

    def on_rat_added(self, name, rat):
        if name == 'added_rat':
            if rat != self:
                rat.attack += 1
                self.attack += 1

    def on_rat_removed(self, name, rat):
        if name == 'removed_rat':
            if rat != self:
                rat.attack -= 1
                self.attack -= 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.game.on_change_rats.remove(self.on_rat_added)
        self.game.on_change_rats.remove(self.on_rat_removed)
        self.game.on_change_rats('removed_rat', self)

    def __repr__(self):
        return f"<Rat attack={self.attack}>"


if __name__ == "__main__":
    game = Game()

    rat = Rat(game)
    rat2 = Rat(game)
    rat3 = Rat(game)

    with Rat(game) as rat4:
        print(rat4)
        print(rat)

    print(rat)
