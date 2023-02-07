#Función MAP

num = [1, 2, 3, 4]
num2 = []

for i in num:
    num2.append(i*2)
print(num)
print(num2)

#Aquí se transformo la lista pero se puede usar map para que sea solo una línea

num3 = map(lambda i: i * 2, num)
print(num3)#Toca pasarlo a lista 
print(list(num3))

list1 = [1,2,3,4]
list2 = [5,6,7]
print(list1)
print(list2)
result = list(map(lambda x,y: x+y, list1,list2))
print(result) # Genera un elemento con la suma de cada uno de los valores,
#dado el tamaño de la lista solo obtiene el resultado de la lista más pequeña
