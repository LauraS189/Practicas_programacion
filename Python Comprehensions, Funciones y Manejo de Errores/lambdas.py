#Funciones lambdas
def increment(x):
    return x+1

result = increment(9)
print(result)

#Transforma la funcion el lambda
increment2 = lambda x: x + 1 #Se usa la función lambda, la vaeriable y lo que se quiere hacer con la función
result2 = increment2(5)
print(result2)

full_name = lambda name, lastname: f'Full name is {name.title()} {lastname.title()}'
text = full_name('laura', 'Rodríguez')
print(text)