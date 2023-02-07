#LIST COMPREHENSION

num = []
for i in range(1,11):
    num.append(i)
print(num)

num_v2=[element for element in range(1,11)] #Forma más corta
print(num_v2)


num = []
for i in range(1,11):
    if i%2==0:
        num.append(i*2)
print(num)

num_v2=[i*2 for i in range(1,11) if i%2==0]#Forma más corta
print(num_v2)

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

even_numbers_v2 = [num for num in numbers if num % 2 == 0]
print('v2 =>', even_numbers_v2)




