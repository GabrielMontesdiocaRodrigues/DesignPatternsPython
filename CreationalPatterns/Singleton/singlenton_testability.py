import unittest
from pathlib import Path

ROOT = Path(__file__).parent
POPULATION = ROOT / 'population.txt'

class Singleton(type): 
    _instances = {}
    def __call__(cls, *args, **kwargs): 
        if cls not in cls._instances: 
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs) 
        return cls._instances[cls]
    
class Database(metaclass=Singleton) : 
    def __init__(self):
        self.population = {}
        with open(POPULATION, 'r') as f:
            lines = f.readlines()
            for i in range(0,len(lines),2):
                self.population[lines[i].strip()] = int(lines[i+1].strip())

class DummyDatabase(metaclass=Singleton) :
    population = {
        'alpha' : 1,
        'beta' : 2,
        'gamma' : 3
    }

    def get_population(self, name) : 
        return self.population[name]

class ConfigurableRecordFinder : 
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for city in cities:
            result += self.db.population[city]
        return result

class SinglentonRecordFinder: 
    def total_population(self, cities):
        result = 0
        for city in cities:
            result += Database().population[city]
        return result
    

class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)  
    
    def test_singleton_total_population(self) : 
        rf = SinglentonRecordFinder()
        names = ['Sao Paulo', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(17700000 + 17400000, tp)
    
    ddb = DummyDatabase()

    def test_dependent_total_population(self) : 
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(3, crf.total_population(['alpha', 'beta']))


if __name__ == '__main__':
    unittest.main()