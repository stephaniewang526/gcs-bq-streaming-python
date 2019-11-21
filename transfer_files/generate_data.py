import datetime
import json
import os
import random
import uuid
import lorem
import pandas as pd
import sys


def people_generator(length):
  for x in range(length):
    generated_name = generate_name() + ' ' + generate_name()
    generated_company = random_pick_from_list(COMPANIES)
    yield {
        'id': generate_id(),
        'name': generated_name,
        'index': random.randrange(0,100,1),
        'guid': generate_id(),
        'isActive': bool(random.getrandbits(1)),
        'balance': generate_balance(),
        'age': random.randrange(5, 90, 1),
        'eyeColor': random_pick_from_list(EYE_COLORS),
        'gender': random_pick_from_list(GENDERS),
        'company': generated_company,
        'email': generated_name.split(' ')[0]+'@'+generated_company.split(' ')[0]+'.com',
        'phone': generate_phone(),
        'address': generate_address(),
        'about': lorem.paragraph(),
        'registered': generate_date(),
        'latitude': random.SystemRandom().uniform(-100.05, 100.95),
        'longitude': random.SystemRandom().uniform(-100.05, 100.95),
        'friends': [
            {
                'friendId': 0,
                'friendName': generate_name() + ' ' + generate_name()
            },
            {
                'friendId': 1,
                'friendName': generate_name() + ' ' + generate_name()
            },
            {
                'friendId': 2,
                'friendName': generate_name() + ' ' + generate_name()
            }
        ],
        'greeting': "Hello, " + lorem.sentence(),
        'favoriteFruit': random_pick_from_list(FRUITS)
    }


def generate_id():
  return str(uuid.uuid4())


def generate_name():
  with open('baby_names.txt', 'r') as f:
    names = f.readlines()
  return names[random.randrange(0, len(names) - 1, 1)][:-2]


def generate_balance():
  return '$' + str(random.randrange(0, 1000000))


def random_pick_from_list(list):
  return random.choice(list)


def get_snp500_companies():
  data = pd.read_html(
      'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
  table = data[0]
  company_name_col = table.iloc[:, 1]
  return company_name_col.values.tolist()


def generate_phone():
  return str(random.randrange(100, 999, 1))+'-'+str(random.randrange(100, 999, 1))+'-'+str(random.randrange(100, 999, 1))


def generate_address():
  return str(random.randrange(1, 999, 1))+' '+str(random.randrange(4, 250, 1))+'th St '+'New York, NY '+str(random.randrange(10001,19000,1))


def generate_date():
  date = datetime.datetime(random.randrange(1990, 2019, 1), random.randrange(1, 12, 1), random.randrange(1, 28, 1))
  return str(date).split(' ')[0]


EYE_COLORS = ['Brown', 'Blue', 'Black', 'Hazel', 'Grey', 'Maroon', 'Red', 'Rainbow']
GENDERS = ['Female', 'Male', 'Non-binary/ third gender', 'Prefer not to say']
COMPANIES = get_snp500_companies()
FRUITS = ['Apple', 'Pear', 'Kiwi', 'Strawberry', 'Raspberry', 'Blackberry', 'Orange', 'Banana']
LENGTH = 1000

def main(filename):
  people_objs = people_generator(LENGTH)
  with open('%s.json' % filename, 'w') as output:
    output.write('[')
    for i, obj in enumerate(people_objs):
      json.dump(obj, output)
      if i < LENGTH-1:
        output.write(',')
    output.write(']')


if __name__ == '__main__':
  main(sys.argv)