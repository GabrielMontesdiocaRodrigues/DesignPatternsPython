
import unittest
from abc import ABC


def _qualname(obj):
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    name = _qualname(obj)
    return name[:name.rfind('.')]


_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    key = (_qualname(type(self)), type(arg))
    if not key in _methods:
        raise Exception('Key % not found' % key)
    method = _methods[key]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        return _visitor_impl

    return decorator


class Value:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class MultiplicationExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(Value)
    def visit(self, v):
        self.buffer.append(str(v.value))

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.buffer.append('(')
        self.visit(ae.left)
        self.buffer.append('+')
        self.visit(ae.right)
        self.buffer.append(')')

    @visitor(MultiplicationExpression)
    def visit(self, me):
        self.visit(me.left)
        self.buffer.append('*')
        self.visit(me.right)

    def __str__(self):
        return "".join(self.buffer)


if __name__ == '__main__':
    simple = AdditionExpression(Value(2), Value(3))
    ep = ExpressionPrinter()
    ep.visit(simple)
    print(ep)  # (2+3)
