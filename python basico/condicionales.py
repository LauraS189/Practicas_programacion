'''
if True:
    print('Run')
if False:
    print("Don't run")

pet = input("¿Cuál es tu mascota favorita?")
if pet=="dog":
    print("Nice")
elif pet=="cat":
    print("Good")
elif pet=="horse":
    print("Wow")
else:
    print("Bad")


stock = int(input("Digita el stock= "))
if stock>=100 and stock<1000:
    print("Good")
else:
    print("Bad")
'''
#Número par o impar
num = int(input("Digite un número: "))
if num%2==0:
    print("Su número es par")
else:
    print("Su número es impar")