
#sorted
'''points2d = [(1,2), (15,1), (5, -1)]

points2d_sorted = sorted(points2d, key=lambda x: x[1])
#points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
print(points2d)
print(points2d_sorted)

#key is used when we want specific argument or rather a specific
rule how to sort it'''

#map (func, seq)
'''a = [1 ,2 ,3 ,4 ,5]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)''' 

#filter (func, seq)
'''a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)

print(list(b))'''

#reduce (func, seq)
from functools import reduce
a = [1, 2, 3, 4]

product_a = reduce(lambda x,y: x*y, a)
print(product_a)

