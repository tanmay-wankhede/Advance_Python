#raising an expection

'''x = -5
if x < 0:
    raise Exception('x should be positive')'''


#assert

'''x = -5
assert(x>=0), 'x is not positive'
'''

#try
try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
#else clause is run if exception occurred.
finally:
    print('cleaning up..')
#finally clause is run whether or not exceptions as occured


