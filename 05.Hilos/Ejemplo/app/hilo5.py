import threading

total = 0
lock = threading.RLock()

def hacer_algo():
    with lock:
        print('Bloqueo desde la funcion hacer_algo')
    print('Bloqueo liberado desde la funcion hacer_algo')
    return 'Termine de hacer algo'

def hacer_algo_mas():
    lock.acquire()
    try:
        print('Bloqueo desde la funcion hacer_algo_mas')
    finally:
        lock.release()
        print('Bloqueo liberado desde la funcion hacer_algo_mas')
    return 'Termine de hacer algo mas'

if __name__ == '__main__':
    with lock:
        r1 = hacer_algo()
        r2 = hacer_algo_mas()

    print(r1)
    print(r2)