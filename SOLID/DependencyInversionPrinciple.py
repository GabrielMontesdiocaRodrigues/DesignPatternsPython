from enum import Enum
from abc import abstractmethod

class Relacionship(Enum) : 
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipsBrowser:
    @abstractmethod
    def find_all_children_of(self, name): 
        pass

class Relationships(RelationshipsBrowser):
    def __init__(self):
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relacionship.PARENT, child)
        )
        self.relations.append(
            (child, Relacionship.CHILD, parent)
        )
    
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relacionship.PARENT:
                yield r[2].name

class Research:
    # This class is violating the Dependency Inversion Principle
    # def __init__(self, relationships : Relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relacionship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relacionship = Relationships()
relacionship.add_parent_and_child(parent, child1)
relacionship.add_parent_and_child(parent, child2)

Research(relacionship)