import random


def adivina_el_numero(x):
    print('____________________________')
    print('Bienvenido al juego')
    print('____________________________')
    print('Adivina el numero')


    numero_Aleatorio = random.randint(1,x)


    prediccion = 0


    while prediccion != numero_Aleatorio:
        prediccion = int(input(f"Adivina un numero entre 1 y {x}:"))


        if prediccion < numero_Aleatorio:
            print('intenta otra vez, el numero es muy pequeno')
        elif prediccion > numero_Aleatorio:
            print('intenta otra vez, el numero es muy grande')

    print(f'Felicitaciones ADIVINASTE EL NUMERO {numero_Aleatorio}')


adivina_el_numero(10)