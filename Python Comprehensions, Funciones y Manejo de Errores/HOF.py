def increment(x):
    return x + 1

increment2 = lambda x: x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, increment) #Solo se envia la definición de la función
#porque HOF recibe la declaración de la funcion
#x + (x+1) = 2 + (2+1)
print(result)

result2 = high_ord_func(5,increment2)
print(result2)

result3 = high_ord_func(5,lambda x: x *2)
print(result3)
