import random

options = ('piedra', 'papel', 'tijera')
gana_user = 0
gana_pc = 0
ronda = 1


while True:

    print('-'*10)
    print('RONDA ',ronda)
    print('-'*10)

    u_opcion = input("Escribe tu opción: Piedra, Papel o Tijera: ")
    opcion_f= u_opcion.lower()
    ronda +=1

    if not opcion_f in options:
        print("Esa opción no es valida")   
    
    pc_gamer = random.choice(options)

    print("Has elegido: ", u_opcion)
    print("La computadora ha elegido: ", pc_gamer)

    if pc_gamer == opcion_f:
        print("Ha sido un empate")
    elif pc_gamer == "Tijera":
        if opcion_f == "piedra":
            print("Has ganado!")
            gana_user += 1
        else:
            print("Has perdido :(")
            gana_pc += 1
    elif pc_gamer == "piedra":
        if opcion_f == "papel":
            print("Has ganado!")
            gana_user += 1
        else:
            print("Has perdido :(")
            gana_pc += 1
    elif pc_gamer == "papel":
        if opcion_f == "tijera":
            print("Has ganado!")
            gana_user += 1
        else:
            print("Has perdido :(")
            gana_pc += 1

    if gana_user == 3:
        print('Has ganado el juego!')
        break
    if gana_pc == 3:
        print('Has perdido el juego :()')
        break 

    
