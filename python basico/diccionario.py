my_dic = {}
print(type(my_dic))

my_dic = {
    'avion':'volar',
    'name':'Laura',
    'last_name':'Rodriguez',
    'age':20
}

print(my_dic)
print(len(my_dic))

print(my_dic['last_name'])
print(my_dic['age'])
print(my_dic.get('hola'))#Obtener el resultado - no hay error si la llave no existe, muestra un none

print('avion' in my_dic)
print('hola' in my_dic)