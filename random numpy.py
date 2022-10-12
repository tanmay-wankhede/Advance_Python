import numpy as np

#a = np.random.rand(3, 4)
#a = np.random.randint(0, 4, (3,4))
#print(a)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)

#have diff number generator also have diff seed than standard python
#