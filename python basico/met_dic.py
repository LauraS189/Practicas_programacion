
'''
#Métodos en diccionarios

datos = {
    'name':'Laura',
    'last_name':'Rodriguez',
    'languages_pr':['python','java'],
    'age': 20
}

print(datos)

datos['name'] = 'Sofia'
datos['age'] -=1
datos['languages_pr'].append('rust')
datos.append('o')
print(datos) 

del datos['last_name']#Delete
print(datos) 

datos.pop('age')
print(datos) 

print('items')
print(datos.items())#Obtener los items del diccionario, los pares clave-valor el forma de tupla
print('keys')
print(datos.keys())#Obtener las keys del diccionario
print('values')
print(datos.values())#Solo devuelve los valores del diccionario
'''
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe t solución 👇
person['twitter'] = '@nicobytes'
person['name'] = 'felipe'
del person['age']
print(list(person.keys()))
print(list(person.values()))