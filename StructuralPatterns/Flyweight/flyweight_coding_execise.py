class FormattedText: 
    def __init__(self, position, text, capitalize=False):
        self.position : int = position
        self.text : str = text
        self.capitalize : bool = capitalize

class Sentence(list):
    def __init__(self, plain_text):
        super().__init__()
        for position, text in enumerate(plain_text.split(' ')):
            self.append(FormattedText(position, text))
    
    def __str__(self):
        return ' '.join(text.text.upper() if text.capitalize else text.text for text in self)
            
                
sentence = Sentence('hello world')
sentence[0].capitalize = True
print(sentence)
