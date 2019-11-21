import json
import uuid
import random


def people_generator(length):
  for x in range(length):
    generated_name = generate_name() + ' ' + generate_name()
    yield {
        'id': generate_id(),
        'name': generated_name,
        'index': x,
        'guid': generate_id(),
        'isActive': bool(random.getrandbits(1)),
        'balance': '',
        'age': '',
        'eyeColor': '',
        'gender': '',
        'company': '',
        'email': '',
        'phone': '',
        'address': '',
        'about': '',
        'registered': '',
        'latitude': 0,
        'longitude': 0,
        'friends':[
            {
                'friendId': 0,
                'friendName': ''
            }
        ],
        'greeting': '',
        'favoriteFruit': ''
    }

    # yield OrderedDict([
    #     ('last_name', 'lastname_%i' % x),
    #     ('first_name', 'firstname_%i' % x),
    #     ('street_address', 'adress_%i' % x),
    #     ('email', 'email_%i' % x)])


def generate_id():
  return str(uuid.uuid4())


def generate_name():
  with open('baby_names.txt', 'r') as f:
    names = f.readlines()
  return names[random.randrange(0, len(names)-1, 1)][:-2]


filename = 'py-generated'
LENGTH = 3
people_objs = people_generator(LENGTH)
with open('%s.json' % filename, 'w') as output:
  output.write('[')
  for obj in people_objs:
    json.dump(obj, output)
    output.write(',')
  output.write(']')
print("Done.")
