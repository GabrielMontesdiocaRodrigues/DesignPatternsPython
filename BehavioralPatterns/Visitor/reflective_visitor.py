from abc import abstractmethod, ABC


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:
    @staticmethod
    def print(expression, buffer):
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(')')

    Expression.print = lambda self, buffer: ExpressionPrinter.print(
        self, buffer)


if __name__ == '__main__':
    # 1 + (2+3)

    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2), DoubleExpression(3)
        )
    )
    buffer = []
    # ExpressionPrinter.print(e, buffer)
    e.print(buffer)
    print(''.join(buffer))  # 1+(2+3)
