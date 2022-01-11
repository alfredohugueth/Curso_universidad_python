import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    # Agrega el nombre del archivo al mensaje del log
    datefmt='%I:%M:%S %p',
    handlers=[
        log.FileHandler('capa_datos.log'),
        log.StreamHandler()
    ]
)


if __name__ == '__main__':
    log.debug("Mensaje a nivel debug")
    log.info("Mensaje a nivel de info")
    log.warning("Mensaje a nivel de warning")
    log.error("Mensaje a nivel de Error")
    log.critical("Mensaje a nivel Critico")