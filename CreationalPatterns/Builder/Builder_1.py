class HtmlElements : 
    indent_size = 2 

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')
        if self.text:
            lines.append(' ' * (indent + 1) * self.indent_size + self.text)
        for e in self.elements:
            lines.append(e.__str(indent + 1))
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):  
        return self.__str(0)
    
    @staticmethod
    def create(name):
        return HtmlBuilder(name)
    
class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.___root = HtmlElements(root_name)

    def add_child(self, child_name, child_text):
        self.___root.elements.append(
            HtmlElements(child_name, child_text)
        )
    
    def add_child_fluent(self, child_name, child_text):
        self.___root.elements.append(
            HtmlElements(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.___root)


html = HtmlElements.create('ul').add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
# builder = HtmlBuilder('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')
# builder.add_child_fluent('li', 'hello').\
#         add_child_fluent('li', 'world')
print('Ordinary Builder is:')
print(html)