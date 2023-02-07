#MODIFICAR CONJUNTOS
set_countries = {'col','mex','bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)

#add 
set_countries.add('arg')
print(set_countries)

#Update
set_countries.update({'per','ecu','ven','col'})
print(set_countries)

#Remove
set_countries.remove('arg')
print(set_countries)

#discard
set_countries.discard('per')
print(set_countries)

set_countries.clear()
print(set_countries)