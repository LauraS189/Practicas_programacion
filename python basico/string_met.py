#Métodos de string
texto = 'Ella sabe programar en python'
'''
print('JavaScript' in texto)
print('Python' in texto)

if 'JS' in texto:
    print('Correct')
else:
    print('Invalid')
'''

size = len(texto)
print(size)

print(texto.upper())#Mayuscula
print(texto.lower())#Minuscula
print(texto.count('a'))#Cuantas veces hay un caracter en el texto

print(texto.swapcase())#Cambiar los caracteres de mayuscula a minuscula y viceversa
print(texto.startswith('ELLa'))#Verifica si el texto empieza con esa palabra 
print(texto.endswith('Rust'))#Verifica si termian con esa palabra
print(texto.replace('Python', 'Go'))#Replaza la palabra

texto_2= 'este es un titulo'
print(texto_2.capitalize())#Pone la primera letra en mayuscula
print(texto_2.title())#Pone la primera letra en mayuscula de cada palabra
print(texto_2.isdigit())#Verifica si es un digito
print("234".isdigit())


