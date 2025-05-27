from abc import ABC, abstractmethod
import cmath
import math


class DiscriminantStrategy(ABC):
    @abstractmethod
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b**2 - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        discriminant = b**2 - 4*a*c
        return discriminant if discriminant >= 0 else float('nan')


class QuadraticEquationSolver:
    def __init__(self, strategy: DiscriminantStrategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        d = self.strategy.calculate_discriminant(a, b, c)

        if d == float('nan'):
            nan = float('nan')
            return nan, nan

        sqrt_disc = cmath.sqrt(d)
        two_a = 2 * a
        root1 = (-b + sqrt_disc) / two_a
        root2 = (-b - sqrt_disc) / two_a
        return root1, root2
