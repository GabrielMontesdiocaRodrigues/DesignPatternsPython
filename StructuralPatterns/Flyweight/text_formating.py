class FormattedText: 
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(c.upper() if self.caps[i] else c)
        return ''.join(result)
    
class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange: 
        def __init__(self, start, end, captalize=False):
            self.start = start
            self.end = end
            self.captalize = captalize

        def covers(self, position): 
            return self.start <= position < self.end
        
    def get_range(self, start, end):
        text_range = self.TextRange(start, end)
        self.formatting.append(text_range)
        return text_range
    
    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for text_range in self.formatting:
                if text_range.covers(i):
                    c = c.upper() if text_range.captalize else c
            result.append(c)
        return ''.join(result)

if __name__ == '__main__':
    ft = FormattedText('This is a brave new world')
    ft.capitalize(10, 15)
    print(ft)

    bft = BetterFormattedText('This is a brave new world')
    bft.get_range(16, 19).captalize = True
    print(bft)