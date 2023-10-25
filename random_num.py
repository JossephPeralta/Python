import random

def adivina_num(x):

    print("=========================")
    print("Hola, Bienvenido al juego")
    print("=========================")
    print("Es hora de adivinar números")

    num_aleatorio = random.randint(1, x) #Número aleatorio entre 1 y x
    predit = 0

    while predit != num_aleatorio:
        predit = int(input(f"Adivina un numero entre el 1 y {x}: ")) #El usuario ingresa un número
        if predit < num_aleatorio:
            print("Intenta otra vez, este número es menor")
        elif predit > num_aleatorio:
            print("Intenta otra vez, el número es más grande")
    print(f"Felicitaciones, adivinaste el número {num_aleatorio} correctamente!!!")

adivina_num(15)