class Mediator:
    def __init__(self):
        self.participants = []

    def join(self, participant):
        self.participants.append(participant)

    def broadcast(self, sender, value):
        for participant in self.participants:
            if participant is not sender:
                participant.value = value


class Participant:
    def __init__(self, mediator: Mediator):
        self.value = 0
        self.mediator = mediator
        mediator.join(self)

    def say(self, value):
        self.mediator.broadcast(self, value)


if __name__ == '__main__':
    mediator = Mediator()
    p1 = Participant(mediator)
    p2 = Participant(mediator)
    p1.say(10)
    p2.say(20)
    print(p1.value)
    print(p2.value)
