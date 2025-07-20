import logging

## configration 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m_%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),  # Logs will be written to a file named app.log.
        logging.StreamHandler() ## Logs will also be displayed in the console/terminal.
    ]
)

logger=logging.getLogger("Calculation") ## You are creating (or getting) a logger instance called "Calculation"
logger.setLevel(logging.DEBUG)   # This ensures that the "Calculation" logger itself captures DEBUG level and above.

def add(a,b):
    logger.debug(f" add -> {a} + {b} = {a+b}")
    return a+b

def mul(a,b):
    logger.debug(F" mul -> {a} * {b} = {a*b}")
    return a*b

def div(a,b):
    try:
        res=a/b
        logger.debug(f" div -> {a} / {b} = {res}")
        return res
    except ZeroDivisionError as ex:
        logger.error(ex)

add(8,9)
mul(7,8)
div(9,98)
div(9,0)
