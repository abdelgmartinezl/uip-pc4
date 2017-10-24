import threading

total = 0
lock = threading.Lock()

def actualizar_total(cantidad):
    global total
    with lock:
        total += cantidad
    print(total)

if __name__ == '__main__':
    for x in range(10):
        mi_hilo = threading.Thread(target=actualizar_total, args=(10,))
        mi_hilo.start()
