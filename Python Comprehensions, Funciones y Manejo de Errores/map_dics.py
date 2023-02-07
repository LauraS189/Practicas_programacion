#Map y diccionario
items = [
    {
        'product':'camisa',
        'price':100, 
    },
    {
        'product':'pantalones',
        'price':300,
    },
    {
        'product':'saco',
        'price':200,
    }
]

#Transforma para obtener una lista de solo los precios

prices = list(map(lambda item:item['price'],items))
print(items)
print(prices) # --> [100,300,200]

#Agregar un nuevo atributo al diccionario

def add_taxes(item):
    item['taxes'] = item['price']*.19
    return(item)

new_items = list(map(add_taxes, items))
print(new_items)

#Cuando se trabaja con diccionarios toca tener cuidado con el map ya que se
#Puede modificar el array original y esto puede generar problemas de memoria
#El map no genera un nuevo diccionario 