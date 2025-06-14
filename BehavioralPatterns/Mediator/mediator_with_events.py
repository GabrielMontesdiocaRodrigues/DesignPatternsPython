class Event(list):
    def __call__(self, *args, **kwargs):
        for event in self:
            event(*args, **kwargs)


class Game:
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)


class GoalScoredInfo:
    def __init__(self, who_scored, gold_scored):
        self.who_scored = who_scored
        self.gold_scored = gold_scored


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        self.game.fire(GoalScoredInfo(self.name, self.goals_scored))


class Coach:
    def __init__(self, game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.gold_scored < 3:
            print(f"Coach celebrates that {args.who_scored} scored!")


if __name__ == '__main__':
    game = Game()
    player = Player("Sam", game)
    coach = Coach(game)

    player.score()
    player.score()
    player.score()
