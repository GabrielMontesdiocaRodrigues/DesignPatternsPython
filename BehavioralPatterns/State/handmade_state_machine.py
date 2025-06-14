from enum import Enum, auto


class State(Enum):
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()


class Trigger(Enum):
    CALL_DIALED = auto()
    HANG_UP = auto()
    CALL_CONNECTED = auto()
    PLACE_ON_HOLD = auto()
    TAKE_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


if __name__ == '__main__':
    rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            (Trigger.HANG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HANG_UP, State.ON_HOOK),
            (Trigger.PLACE_ON_HOLD, State.ON_HOLD)
        ],
        State.ON_HOLD: [
            (Trigger.TAKE_OFF_HOLD, State.CONNECTED),
            (Trigger.HANG_UP, State.ON_HOOK)
        ]
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f'The phone is currently {state}')

        for i in range(len(rules[state])):
            t = rules[state][i][0]
            print(f'{i}: {t}')

        idx = int(input('Enter the index of the trigger: '))
        state = rules[state][idx][1]

    print(f'The phone is currently {state}')
