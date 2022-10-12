# lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

#which could be written with def func as

def add10_func(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2,7))

'''lambda is a simple func that is used only once in your code 
or it is used as an arugument to higher order functions, 
meaning functions that take in other functions as arguments'''