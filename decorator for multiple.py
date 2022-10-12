import functools
from unittest import result



def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v=!r}" for k, v in kwargs.items() ]
        signature = ",".join(args_repr = kwargs)
        print(f"calling {func.__name__} ({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
#@start_end_decorator
def say_hello(name):
    greeting = f'hello {name}'
    print(greeting)
    return greeting
say_hello('alex')