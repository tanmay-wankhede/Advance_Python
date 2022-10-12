from itertools import groupby

'''def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
#group_obj = groupby(a, key=lamba x: x<3)
for key, value in group_obj:
     print(key, list(value))'''

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'lisa', 'age': 27}]


group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
     print(key, list(value))
