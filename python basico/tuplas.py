#Estructura de datos no modificables que contiene una secuencia ordenada de elementos

num = (1,2,3,4,5)
strings = ('Ana', 'Carlos', 'Sergio', 'Ana')

print(type(num))
print(num[0])
print(num[-1])

print(strings)

#CRUD - Create, read, write and delete (en la dubpla no se puede borrar)
#Las tuplas no tienen acceso a los métodos ya que es inmutable

print(strings.index('Sergio')) #La posición
print(strings.count('Ana'))#Frecuancia del elemento

my_list = list(strings)
print(my_list)#Si se convierte en lista si se pueden hacer modificaciones

my_list[1] = 'Andrea'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)