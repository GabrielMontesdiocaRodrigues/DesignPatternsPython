from abc import ABC
from collections.abc import Iterable

class Connectibles(Iterable, ABC): 

    def connect_to(self, other):
        if self == other:
            return

        for s in self: 
            for o in other:
                s.output.append(o)
                o.input.append(s)
    

class Neuron(Connectibles): 
    def __init__(self, name):
        self.name = name
        self.input = []
        self.output = []

    def __str__(self):
        return f'{self.name} -> {len(self.input)} inputs, {len(self.output)} outputs'
    
    def __iter__(self):
        yield self 

class NeuronLayer(list, Connectibles) : 
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'Neuron {x}'))

    def __str__(self):
        return f'{self.name}: with {len(self)} neurons'
    
if __name__ == '__main__':
    neuron1 = Neuron('Neuron 1')
    neuron2 = Neuron('Neuron 2')
    layer1 = NeuronLayer('Layer 1', 3)
    layer2 = NeuronLayer('Layer 2', 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)