def hola_mundo():
    yield "Hola"
    yield "Mundo"

generador = hola_mundo()
print(next(generador))
print(next(generador))