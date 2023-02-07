#DIC COMPREHENSION
import random
# dic = {}
# for i in range(1,10):
#     dic[i] = i*2
# print(dic)

# dic_v2={i:i*2 for i in range(1,10)}

countries = ['col','mex','bol','per']
population ={}
for j in countries:
    population[j] = random.randint(1,100)
print(population)

popu_v2 = {j:random.randint(1,100) for j in countries}
print(popu_v2)

names = ['laura','sergio','nancy','fray']
ages = [20,12,47,56]

print(list(zip(names,ages)))

new_dic = {name:ages for (name,ages) in zip(names,ages)}
print(new_dic)

