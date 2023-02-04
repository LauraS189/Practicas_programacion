#CRUD - Create, Read, Update and Delete

num = [1,2,3,4,5]
print(num[2])
num[-1] = 10
print(num)

num.append(700) # Agregar un nuevo elemento
print(num)

num.insert(0,160) #Agregar un elemento en la posición indicada
print(num)
 
task =["todo 1", "todo 2", "todo 3",]
new_list = num + task
print(new_list)

index = new_list.index('todo 2') #En que posición esta un elemento de la lista 
new_list[index] = 'Todo changed'
print(new_list)

new_list.remove('todo 3')
print(new_list)

new_list.pop() #Elimina el último elemento de la lista
print(new_list)

new_list.pop(0) # Elimina el elemento de la lista según la posición
print(new_list)

new_list.reverse()
print(new_list)

numbers = [1,5,4,6,2,3]
numbers.sort()
print(numbers)


strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

