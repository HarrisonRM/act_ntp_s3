frase = "programacion es divertida"
vocales = "aeiouáéíóú"
contador_vocales = 0
for letra in frase.lower():
    if letra in vocales:
        contador_vocales += 1
print(f"Total de vocales: {contador_vocales}")  
