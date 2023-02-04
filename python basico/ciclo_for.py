#FOR
'''
for element in range(1,20):
    print(element)
'''

my_list = [23,45,67,89,43]
for element in my_list:
    print(element)

my_tuple = ('laura','sergio','nancy','fray')
for element in my_tuple:
    print(element)

my_dic = {
    'name':'camisa',
    'price':123,
    'stock':89
}
for element in my_dic:
    print(element,'=>', my_dic[element])

for key, value in my_dic.items():
    print(key, '=>',value)

people = [
    {
        'name':'John',
        'age':23,
    },
    {
        'name':'Laura',
        'age':20,
    },
    {
        'name':'Sergio',
        'age':12,
    },
]

for person in people:
    print('name =>',person['name'])


#Ejercicio - new list solo números positivos
my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for element in my_list:
  if element>0:
    new_list.append(element)
    
print(new_list)