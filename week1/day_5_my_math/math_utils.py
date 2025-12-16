'''
Importiere dein eigenes Modul:

Lege eine Datei math_utils.py an mit Funktionen add(), subtract(), multiply(), divide().

Importiere und benutze sie in einem anderen Script.

Bonus:
Füge Logging hinzu (import logging) und schreibe Fehler in eine Datei.
'''
import logging

from day_5_logs.logger_decorator import log_calls

logger = logging.getLogger(__name__)

__all__ = ['add', 'substract', 'multiply', 'divide', 'safe_divide', 'safe_divide2', 'test']

@log_calls()
def test(): print("Import hat geklappt")


@log_calls()
def add(*args : int):
    result_sum = 0
    for k in args:
        result_sum += k
    return  result_sum

@log_calls()
def substract(*args : int): 
    result_sum = 0
    first_circle = True
    for k in args:
        if first_circle is True:
            first_circle = False
            result_sum = k
            continue
        
        result_sum -= k
    return  result_sum

def multiply(*args : int):
    logger.info('Started divison function') 
    result_sum = 1
    for k in args:
        result_sum *= k
    return  result_sum

@log_calls()
def divide(*args : int): 
    
    result_sum = 0
    first_circle = True
    for k in args:
        if k == 0: 
            raise Exception("Division by 0 is forbidden")

        if first_circle:
            first_circle = False
            result_sum = k
            continue

        result_sum = result_sum / k
    return  float(result_sum)

def safe_divide(a : int, b : int):
    # oder: if b is 0 ? 
    if b == 0:
        return None
    else:
        return a/b
    
def safe_divide2(a : int, b : int) : return a/b if b != 0 else None