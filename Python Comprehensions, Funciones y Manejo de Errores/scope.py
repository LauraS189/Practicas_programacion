#Alcance - Scope

price=100 #Tiene un alcance global porque puede ser usado dentro de todo el archivo (def,if, etc)

def increment():
    price = 200
    price = price + 10 #Esta es una variable local pero el contexto será diferente
    #Esto se llama Scope 
    return price

print(price)
price_2 = increment()
print(price_2)
