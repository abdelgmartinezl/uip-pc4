import threading
import logging

logging. basicConfig(level=logging.DEBUG,
                     filename = 'hilo.log',
                     format = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
                    filemode = 'w')

class MiHilo(threading.Thread):
    def __init__(self, numero):
        threading.Thread.__init__(self)
        self.numero = numero

    def run(self):
        logging.debug('Llamando a la operacion')
        operacion(self.numero)


def operacion(x):
    logging.debug('ejecucion de la operacion')
    r = x * 2
    logging.debug('la operacion da como resultado: {}'.format(str(r)))


if __name__ == '__main__':
    lista_hilos = ['Juan', 'Petra', 'Josefa', 'Xenobia']
    for i in range(4):
        mi_hilo = MiHilo(i)
        mi_hilo.setName(lista_hilos[i])
        mi_hilo.start()
