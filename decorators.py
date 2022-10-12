#2 diff decorators func and class

'''@mydecorator
def dosomthing():
    pass'''
#deco take another function as argument and extends  the behavior of this function

'''def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('end')
    return wrapper

@start_end_decorator
def print_name():
    print('alex')

#print_name - start_end_decorator(print_name)

print_name()'''

'''def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10) 
print(result)'''

import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('end')
        #return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(help(add5))
print(add5.__name__)
