#Trasformación de tipos de variables

name = "Laura"
print(type(name))

name = 12
print(type(name)) # Cambiar el tipo de forma dinamica

name = True
print(type(name))

#Print("Laura" + 12) NO SE PUEDE CONCATENAR 2 TIPOS DE DATOS

age = 20
print("My age is: " + str(age))
print(f"My age is: {age}")

age =input("Escribe tu edad:")
print(type(age))
print(f"Tu edad en 10 años será {int(age)+10}") 