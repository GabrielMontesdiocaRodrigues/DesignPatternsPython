from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()

    def turn_on(self):
        self.state.turn_on(self)

    def turn_off(self):
        self.state.turn_off(self)


class State(ABC):
    def __init__(self, switch):
        self.switch = switch

    def turn_on(self, switch):
        print("Light is alredy on")

    def turn_off(self, switch):
        print("Light is already off")


class OnState(State):
    def __init__(self):
        print("Light turned on")

    def turn_off(self, switch):
        print("Turning the light off")
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print("Light turned off")

    def turn_on(self, switch):
        print("Turning the light on")
        switch.state = OnState()


if __name__ == "__main__":
    switch = Switch()
    switch.turn_on()
    switch.turn_off()
    switch.turn_off()
