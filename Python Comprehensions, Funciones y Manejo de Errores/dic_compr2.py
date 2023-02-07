#DIC COMPREHENSION

import random

countries = ['col','mex','bol','per']


popu_v2 = {country:random.randint(1,100) for country in countries}
print(popu_v2)


result = { country: population for (country, population) in popu_v2.items() if population > 50 }
print(result)


text = 'Hola soy Laura'
unique = {c:c.upper() for c in text if c in 'aeiou'}
print(unique)

