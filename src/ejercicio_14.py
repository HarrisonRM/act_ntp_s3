import random
def main():
    numero_aleatorio = random.randint(1, 10)
    adivinado = False
    intentos = 0

    while not adivinado:
        intento = int(input("Adivina el número (del 1 al 10): "))
        intentos += 1
        if intento == numero_aleatorio:
            adivinado = True
            print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
        else:
            print("Inténtalo de nuevo.")
if __name__ == "__main__":
    main()