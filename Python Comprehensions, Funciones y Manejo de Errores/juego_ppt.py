import random

def choose_option():
    options = ('piedra', 'papel', 'tijera')
    u_opcion = input("Escribe tu opción: Piedra, Papel o Tijera: ")
    opcion_f= u_opcion.lower()

    if not opcion_f in options:
        print("Esa opción no es valida")  
        return None, None

    pc_gamer = random.choice(options)

    print("Has elegido: ", opcion_f)
    print("La computadora ha elegido: ", pc_gamer)
    return opcion_f, pc_gamer

def check_rules(opcion_f, pc_gamer, gana_user, gana_pc):
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
    return gana_user, gana_pc

def run_game():
    gana_user = 0
    gana_pc = 0
    ronda = 1

    while True:
        print('-'*10)
        print('RONDA ',ronda)
        print('-'*10)
        print('Gano pc', gana_pc)
        print('Ganaste', gana_user)
        ronda +=1

        opcion_f, pc_gamer = choose_option()
        gana_user, gana_pc = check_rules(opcion_f,pc_gamer,gana_user, gana_pc)

        if gana_user == 2:
            print('Has ganado el juego!')
            break
        if gana_pc == 2:
            print('Has perdido el juego :()')
            break 

run_game()

    
