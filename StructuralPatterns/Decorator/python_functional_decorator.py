import time

def time_it(func): 
    def wapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int(end - start)*1000} ms')
    return wapper

@time_it
def some_op() :
    print('We are doing something')
    time.sleep(1)
    print('We are done')
    return 123 

if __name__ == '__main__' :
    # time_it(some_op)()
    some_op()