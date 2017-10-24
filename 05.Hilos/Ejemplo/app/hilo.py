import threading
import logging

def ge_logger():
    logger = logging.getLogger("ejemplo_de_hilos")
    logger.setLevel(logging.DEBUG)
    log = logging.FileHandler("hilos.log")
    log_msg = '%(asctime)s - %(threadName)s - %(levelname)s - %'
    formatter = logging.Formatter(log_msg)
    log.setFormatter(formatter)
    logger.addHandler(log)
    return logger

def operacion(x, logger):
    logger.debug('ejecucion de la operacion')
    resultado = x * 2
    logger.debug('funcion operacion termina con: {}'. format(resultado))
    print(threading.current_thread().getName() + "-" + str(x*2))

if __name__ == '__main__':
    for i in range(3):
        mi_hilo = threading.Thread(target=operacion, args=(i,))
        mi_hilo.start()