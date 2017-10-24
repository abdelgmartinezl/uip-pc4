import threading
from queue import Queue

def crear_datos(data, c):
    print("Creando datos y colocandolos en la cola")
    for d in data:
        evt = threading.Event()
        c.put((d, evt))

def consumir_datos(c):
    while True:
        data, evt = c.get()
        print('se encontro data a procesar: {}'.format(data))
        procesada = data ** 2
        print('la data procesada es {}'.format(str(procesada)))
        evt.set()
        c.task_done()

if __name__ == '__main__':
    c = Queue()
    data = [7, 13, 17, 6]
    hilo_uno = threading.Thread(target=crear_datos, args=(data, c))
    hilo_dos = threading.Thread(target=consumir_datos, args=(c,))
    hilo_uno.start()
    hilo_dos.start()
    c.join()
    print("hasta luego")