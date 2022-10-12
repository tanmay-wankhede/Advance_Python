import secrets

#a = secrets.randbelow(10)
#a = secrets.randbits(4)
mylist = list("abcdefg")
a= secrets.choice(mylist)
print(a)
