class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'Id : {self.id}, Name : {self.name}'

class PersonFactory:
    id = 0

    def create_person(self, name):
        return Person(self.get_id(), name)
    
    def get_id(self):
        r_id = self.id
        self.id += 1
        return r_id
        

if __name__ == '__main__':
    pf = PersonFactory()
    p1 = pf.create_person('John Doe')
    p2 = pf.create_person('Jane Doe')
    print(p1)
    print(p2)