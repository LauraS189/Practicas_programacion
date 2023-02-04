x=3.3
y=1.1+2.2
print(x)
print(y)
print(x==y)

y_f = format(y,".2g")
print(y_f)
print(str(x)==y_f)
print('*'*20)

print(x, y)

tolerance = 0.00001
print(abs(x-y)<tolerance)
