import copy

class Address : 
    def __init__(self, street_adress, suite, city):
        self.street_adress = street_adress
        self.suite = suite 
        self.city = city

    def __str__(self):
        return f'{self.street_adress}, Suite #{self.suite}, {self.city}'
    
class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address  

    def __str__(self):
        return f'{self.name} works at {self.address}'   
    
class EmployeeFactory:

    main_office_employee = Employee('', Address('123 East Dr', 0, 'London'))
    aux_office_employee = Employee('', Address('124 East Dr', 0, 'London'))

    @staticmethod
    def __new_employee(prototype, name, suite):
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite
        return result


    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name, suite)
    


john = EmployeeFactory.new_main_office_employee('John', 101)
jane = EmployeeFactory.new_aux_office_employee('John', 500)

print(john)
print(jane)



