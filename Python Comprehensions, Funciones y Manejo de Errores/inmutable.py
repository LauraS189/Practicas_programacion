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

def add_taxes(item):
    new_item = item.copy()#Hacer una copia pero no es la misma referencia
    new_item['taxes'] = item['price']*.19
    return new_item

new_items = list(map(add_taxes, items))
print('New_items')
print(new_items) #-->Esto pasa por la referencia de memoria,
#Cuando se hacen transformaciones a un diccionario se hace una referencia de memoria
#Es por esto que se modifican las 2 listas (new - old) y quedan con los valores del
#último espacio de memoria
print('Old_items')
print(items)
