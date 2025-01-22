class CEO : 
    __shared_state = {
        'name' : 'Steve Jobs',
        'age' : 55
    }

    def __init__(self) :
        self.__dict__ = self.__shared_state

    def __str__(self) :
        return f'{self.name} is {self.age} years old'
    
class Monostate: 
    __shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls)
        obj.__dict__ = cls.__shared_state
        return obj
    
class CFO(Monostate) : 
    def __init__(self) :
        self.name = ''
        self.money_managed = 0

    def __str__(self) :
        return f'{self.name} is {self.money_managed} years old'

if __name__ == '__main__' :
    cfo1 = CFO()
    cfo1.name = 'Tim Cook'
    cfo1.money_managed = 100
    print(cfo1)
    
    cfo2 = CFO()
    cfo2.name = 'Sundar Pichai'
    cfo2.money_managed = 200
    print(cfo1, ' - ', cfo2)