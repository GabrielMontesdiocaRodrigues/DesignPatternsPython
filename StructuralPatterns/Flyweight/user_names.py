import string
import random

class User: 
    def __init__(self, name):
        self.name = name

class User2: 
    strings = []

    def __init__(self, fullname):
        def get_or_create(string):
            if string in self.strings:
                return self.strings.index(string)
            else:
                self.strings.append(string)
                return len(self.strings) - 1

        self.names = [get_or_create(x) for x in fullname.split(' ')] 

    def __str__(self):
        return ' '.join(self.strings[x] for x in self.names)

def random_string():
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for _ in range(10)]
    )

if __name__ == '__main__':
    users = []

    fisrt_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    for first_name in fisrt_names:
        for last_name in last_names:
            user = User2(f'{first_name} {last_name}')
            users.append(user)
    
    print(users[0])