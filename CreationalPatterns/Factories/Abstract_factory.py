from abc import ABC, abstractmethod
from enum import Enum, auto

class HotDrink:
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is nice with some honey and lemon.')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious!')

class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount} ml, add lemon, enjoy!')  
        return Tea()
    
class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount} ml, add cream and sugar, enjoy!')
        return Coffee()
    
class HotDrinkMachine:
    class AvaliableDrinks(Enum):
        COFFEE = auto()
        TEA = auto()

    factories : list[HotDrinkFactory]= []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for drink in self.AvaliableDrinks:
                name = drink.name[0] + drink.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f'{f[0]}')

        s = input(f'Please pick drink (0-{len(self.factories)-1}):')    
        inx = int(s)
        s = input('Specify amount:')
        amount = int(s)
        return self.factories[inx][1].prepare(amount)

if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink().consume()