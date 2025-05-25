class Token:
    def __init__(self, value=0):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Memento:
    def __init__(self, tokens):
        self.tokens = tokens


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return Memento([Token(t.value) for t in self.tokens])

    def revert(self, memento):
        self.tokens = memento.tokens


if __name__ == "__main__":
    tm = TokenMachine()
    m1 = tm.add_token_value(1)
    m2 = tm.add_token_value(2)
    print(tm.tokens)

    tm.revert(m1)
    print(tm.tokens)
    tm.revert(m2)
    print(tm.tokens)
