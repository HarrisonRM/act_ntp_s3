
def main():
    count = 0
    while True:
        word = input("Escribe una palabra (o 'fin' para terminar): ")
        if word.lower() == "fin":
            break
        count += 1
    print(f"Se leyeron {count} palabras.")