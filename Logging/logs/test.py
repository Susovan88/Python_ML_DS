from logger import logging

def add(a,b):
    logging.debug("the add operation take plase")
    return a+b

def mul(a,b):
    logging.debug
    return a*b

logging.debug("add function call")
print(add(8,9))
logging.debug("mul function call")
print(mul(8,9))