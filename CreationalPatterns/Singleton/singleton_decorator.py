def singleton(class_): 
    instances = {} 
    def getinstance(*args, **kwargs): 
        if class_ not in instances: 
            instances[class_] = class_(*args, **kwargs) 
        return instances[class_] 
    return getinstance

@singleton
class Database:
    def __init__(self):
        print('Database created')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2) 