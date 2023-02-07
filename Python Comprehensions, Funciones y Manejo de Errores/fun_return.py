#Return en funciones

def sum_with_range(a,b):
    print(a,b)
    sum = 0
    for i in range(a,b):
        sum += i
    return sum

result = sum_with_range(1,16)
print(result)
result_2 = sum_with_range(result,result+4)
print(result_2)