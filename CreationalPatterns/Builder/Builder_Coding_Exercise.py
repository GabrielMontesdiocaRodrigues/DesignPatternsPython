class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []
        
    def add_field(self, type, name):
        self.fields.append((type, name))
        return self

    def __str__(self):
        if not self.fields:
            return f'class {self.root_name}:\n' + \
                   f'  pass\n'
        return f'class {self.root_name}:\n' + \
               f'  def __init__(self):\n' + \
               ''.join([f'    self.{name} = {value}\n' for name, value in self.fields]) + '\n'
    

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')

print(cb)