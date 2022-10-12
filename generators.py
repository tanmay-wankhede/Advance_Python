'''def mygenerator():
    yield 1
    yield 2 
    yield 3
 g = mygenerator()
  
value = next(g)
print(value)

print(sum(g))

sorted(g)'''

'''def countdown(num):
    print('starting')
    while num > 0:
        yield num 
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))'''

#saves a lot of memory when you work with large database

'''import sys 
 def firstn(n):
    nums = []
    num = 0
    while num< n:
        num.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(100)))
print(sys.getsizeof(firstn_generator))'''

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
fib = fibonacci(20)
for i  in fib:
    print(i)
    