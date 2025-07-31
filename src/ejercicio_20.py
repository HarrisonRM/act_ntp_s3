edad_mayor = -1
while True:
    edad = int(input("Introduce una edad (-1 para terminar): "))
    if edad == -1:
        break
    if edad > edad_mayor:
        edad_mayor = edad
if edad_mayor == -1:
    print("No se ingresaron edades.")
else:
    print(f"La edad mayor ingresada es: {edad_mayor}")