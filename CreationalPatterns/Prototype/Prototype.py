import copy	

class Address : 
    def __init__(self, steet_address, city, country):
        self.steet_address = steet_address
        self.city = city
        self.country = country  
    
    def __str__(self):
        return f'{self.steet_address}, {self.city}, {self.country}'
        

class Person: 
    def __init__(self, name, address):
        self.name = name
        self.address = address  
    
    def __str__(self):
        return f'{self.name} lives at {self.address}'   
    

john = Person('John', Address('123 London Road', 'London', 'UK'))
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.steet_address = '124 London Road'

print(john)
print(jane)