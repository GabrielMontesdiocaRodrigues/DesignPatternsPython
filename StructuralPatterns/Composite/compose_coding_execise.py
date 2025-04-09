from abc import ABC
import unittest

class SumComposite(ABC): 
    @property
    def sum(self) -> int:
        total = 0 
        for value in self:
            if isinstance(value, SingleValue):
                total += value.value
            elif isinstance(value, ManyValues): 
                total += sum(value)
        return total

class SingleValue(SumComposite):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class ManyValues(list, SumComposite):
    pass

class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)

if __name__ == '__main__' : 
    unittest.main()