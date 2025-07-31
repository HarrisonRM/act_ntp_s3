n = int(input("Introduce un número entero positivo: "))
suma_digitos = 0
while n > 0:
    digito = n % 10
    suma_digitos += digito
    n //= 10
print(f"La suma de los dígitos es: {suma_digitos}")