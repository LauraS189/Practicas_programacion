#AND - EsTrue siempre y cuando los 2 sean True
print('------------------AND---------------')
print('True AND True =', True and True)
print('True AND False =', True and False)
print('False AND True =', False and True)
print('False AND False =', False and False)

print(10>5 and 5>2)
stock = int(input('Ingrese el número del stock ='))
print(stock>=100 and stock<=1000)

#OR - Si alguno es True la operación es True
print('-----------------OR---------------')
print('True OR True =', True or True)
print('True OR False =', True or False)
print('False OR True =', False or True)
print('False OR False =', False or False)

print(24>3 or 2>4)
rol = input("Digita el rol: ")
print(rol=='admin' or rol=='seller') 

#NOT - Negación
print('-----------------NOT---------------')
print(not True)
print(not False)

