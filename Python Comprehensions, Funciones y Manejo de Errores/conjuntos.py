#CONJUNTOS
#En un conjunto no se pueden tener elementos repetidos
set_countries = {'col','mex','bol'}
print(set_countries)
print(type(set_countries))

set_num = {1,2,3,4,5,23}
print(set_num)
#Se imprime solo los números no repetidos

set_from_string =set('hoola')
print(set_from_string)

set_from_tuples = set(('abc','def','as','abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_num = set(numbers)
print(set_num)
unique_num = list(set_num) #Pasar los números unicos a una lista
print(unique_num)