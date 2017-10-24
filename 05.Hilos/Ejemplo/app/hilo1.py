import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='hilo.log',
                    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
                    filemode='w')

def operacion(x):
    logging.debug('ejecucion de la operacion')
    r = x * 2
    logging.debug('la operacion da como resultado: {}'.format(str(r)))
    #print(threading.current_thread().getName() + " - " + str(x*2))

if __name__ == '__main__':
    lista_hilos = ['Juan', 'Petra', 'Josefa', 'Xenobia']
    for i in range(4):
        mi_hilo = threading.Thread(
            target=operacion, name=lista_hilos[i], args=(i,))
        mi_hilo.start()