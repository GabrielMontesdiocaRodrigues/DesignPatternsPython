from enum import Enum, auto


class Token:
    class TokenType(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type: TokenType, text: str):
        self.type = type
        self.text = text

    def __repr__(self):
        return f'`{self.text}`'
    
class Interger: 
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'`{self.value}`'
    
class BinaryExpression:
    class Type(Enum):
        ADD = auto()
        SUBTRACT = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None
    
    @property
    def value(self):
        if self.type == BinaryExpression.Type.ADD:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value

def parse(tokens):
    result = BinaryExpression()
    have_lhs = False
    i=0
    while i < len(tokens):
        token = tokens[i]
        if token.type == Token.TokenType.INTEGER:
            integer = Interger(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.TokenType.PLUS:
            result.type = BinaryExpression.Type.ADD
        elif token.type == Token.TokenType.MINUS:
            result.type = BinaryExpression.Type.SUBTRACT
        elif token.type == Token.TokenType.LPAREN: 
            j=i 
            while j < len(tokens):
                if tokens[j].type == Token.TokenType.RPAREN:
                    break
                j += 1
                
            subexepression = tokens[i+1:j]
            element = parse(subexepression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else: 
                result.right = element
            i = j
        i += 1
    return result


def lex(input: str):
    result = []
    i = 0
    while i < len(input):
        if input[i] == '+':
            result.append(Token(Token.TokenType.PLUS, input[i]))
        elif input[i] == '-':
            result.append(Token(Token.TokenType.MINUS, input[i]))
        elif input[i] == '(':
            result.append(Token(Token.TokenType.LPAREN, input[i]))
        elif input[i] == ')':
            result.append(Token(Token.TokenType.RPAREN, input[i]))
        else:
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(Token.TokenType.INTEGER, ''.join(digits)))
                    break
        i += 1
    return result


def calc(input): 
    token = lex(input)
    parsed = parse(token)
    print(f'{input} = {parsed.value}')

if __name__ == "__main__":
    calc('(13+4)-(12+1)')