class Event(list):
    def __call__(self, *args, **kwds):
        for event in self:
            event(*args, **kwds)


class Person:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.adress)


def call_doctor(name, address):
    print(f"{name} need a doctor at {address}")


if __name__ == "__main__":
    p = Person("Sherlock", "221B Baker St, London")
    p.falls_ill.append(lambda name, address: print(f"{name} is ill"))
    p.falls_ill.append(call_doctor)
    p.catch_a_cold()
    p.falls_ill.remove(call_doctor)
    p.catch_a_cold()
