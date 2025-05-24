from enum import auto, Enum
from typing import List


class TokenType:
    INTEGER = auto()
    PLUS = auto()
    MINUS = auto()
    VARIABLE = auto()


class Token:
    def __init__(self, token_type: TokenType, text: str):
        self.token_type: TokenType = token_type
        self.text: str = text

    def __repr__(self):
        return f'`{self.text}, {self.token_type}`'


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def lex(self, expression: str):
        result = []
        i = 0
        while i < len(expression):
            if expression[i] == '+':
                result.append(Token(TokenType.PLUS, expression[i]))
            elif expression[i] == '-':
                result.append(Token(TokenType.MINUS, expression[i]))
            elif expression[i].isalpha():
                result.append(Token(TokenType.VARIABLE, expression[i]))
            else:
                digits = [expression[i]]
                for j in range(i + 1, len(expression)):
                    if expression[j].isdigit():
                        digits.append(expression[j])
                        i += 1
                    else:
                        break
                result.append(Token(TokenType.INTEGER, ''.join(digits)))
            i += 1
        return result

    def parse(self, tokens: List[Token]):
        def get_value(token):
            if token.token_type == TokenType.INTEGER:
                return int(token.text)
            elif token.token_type == TokenType.VARIABLE:
                return self.variables.get(token.text, 0)

        try:
            result = get_value(tokens[0])
            i = 1
            while i < len(tokens):
                op = tokens[i]
                rhs = get_value(tokens[i + 1])
                if op.token_type == TokenType.PLUS:
                    result += rhs
                elif op.token_type == TokenType.MINUS:
                    result -= rhs
                i += 2
        except Exception:
            result = 0
        return result

    def calculate(self, expression):
        tokens = self.lex(expression)
        result = self.parse(tokens)
        print(f'{expression} = {result}')
        return result


if __name__ == "__main__":
    ep = ExpressionProcessor()
    ep.variables['x'] = 3
    ep.calculate('1+2+3')
    ep.calculate('10-2-x')
    ep.calculate("1+2+xy")
