import random

'''a = random.randint(1, 10)
#a = random.randrange(1, 10)
#a = random.normalvariate(1, 10)
print(a)'''

'''mylist = list("ABCDEFGH")
#a = random.choice(mylist)
#a = random.sample(mylist, 4)
#a = random.choices(mylist, k=4)
random.shuffle(mylist)
#print(a)
print(mylist)'''

#seed are pseudo random numbers bcoz they're reproducible
random.seed(1)

print(random.random())
print(random.randint(1, 5))

random.seed(3)

print(random.random())
print(random.randint(1, 5))
