

import json
from locale import dcgettext

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

#serization or encoding
'''personJSON = json.dumps(person, indent=4, sort_keys=True)
#print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

#deserization

with open('person.json', 'r') as file:
    person = json.loads(personJSON)
    print(person) '''

#with custom class

'''import json

class user:

    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__:True}
    else:
        raise TypeError('object  of type User is not JSON serializable')

userJSON = json.dumps(user, defualt=encode_user)
print(userJSON)'''

#2nd Method with custom class
from json import JSONEncoder
class UserEnconder(JSONEncoder):

    def default(self, o: ):
        if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__:True}
    return JSONEncoder.default(self, o)

userJSON = UserEnconder().encode(user)
print(userJSON)

def decode_user(dct):
    if User. __name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)