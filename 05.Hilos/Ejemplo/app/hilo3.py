import threading

total = 0
lock = threading.Lock()

def actualizar_total(cantidad):
    global total
    lock.acquire()
    try:
        total += cantidad
    finally:
        lock.release()
    print(total)

if __name__ == '__main__':
    for x in range(10):
        mi_hilo = threading.Thread(target=actualizar_total, args=(10,0))
        mi_hilo.start()
