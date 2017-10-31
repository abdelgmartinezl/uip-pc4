def hola_mundo():
    yield "Hola"
    yield "Mundo"

def generar_secuencia():
    numero = 0
    while True:
        yield numero
        numero = numero + 1

if __name__ == "__main__":
    generador = hola_mundo()
    print(next(generador))
    print(next(generador))

    numeros = generar_secuencia()
    for n in numeros:
        print(n)
        if n > 14:
            break