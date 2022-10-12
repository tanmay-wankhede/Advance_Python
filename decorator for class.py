import re


class countcalss:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'this is executed {self.num_calls} time')
        return self.func(*args, **kwargs)

@countcalss
def say_hello():
    print('hello')

# timer debug