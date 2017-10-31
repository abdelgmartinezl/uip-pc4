import asyncio
import datetime
import random

def hola_mundo():
    yield "Hola"
    yield "Mundo"

def generar_secuencia():
    numero = 0
    while True:
        yield numero
        numero = numero + 1

def corutina_cadena():
    hola = yield "Hola"
    yield hola

@asyncio.coroutine
def mostrar_fecha(numero, loop):
    tiempo_final = loop.time() + 50.0
    while True:
        print("Ciclo: {} Tiempo: {}".format(numero, datetime.datetime.now()))
        if (loop.time() + 1.0) >= tiempo_final:
            break
        yield from asyncio.sleep(random.randint(0, 5))

if __name__ == "__main__":
    generador = hola_mundo()
    print(next(generador))
    print(next(generador))

    numeros = generar_secuencia()
    for n in numeros:
        print(n)
        if n > 14:
            break

    saludo = corutina_cadena()
    print(next(saludo))
    print(saludo.send("Mundo"))

    loop = asyncio.get_event_loop()
    asyncio.ensure_future(mostrar_fecha(1, loop))
    asyncio.ensure_future(mostrar_fecha(2, loop))
    loop.run_forever()
