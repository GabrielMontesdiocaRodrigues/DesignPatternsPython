import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self.person: Person = person

    def drink(self):
        logging.info(f"Attempt to drink. Age: {self.person.age}")
        if self.person.age < 18:
            return 'too young'
        return self.person.drink()

    def drive(self):
        logging.info(f"Attempt to drive. Age: {self.person.age}")
        if self.person.age < 16:
            return 'too young'
        return self.person.drive()

    def drink_and_drive(self):
        logging.warning(f"Attempt to drink and drive. Age: {self.person.age}. Outcome: dead.")
        return 'dead'


if __name__ == '__main__':
    person = ResponsiblePerson(Person(22))
    logging.info(person.drink())
    logging.info(person.drive())
    logging.info(person.drink_and_drive())
