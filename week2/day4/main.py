



class CSVFormatError(Exception):
    def __init__(self, message : str, errorcode : int) -> None:
        self.message = message
        self.errorcode = errorcode
    
    def __str__(self):
        return f'{self.message}: due to ERRORCODE {self.errorcode}'
    
'''
2. Löst sie aus, wenn:
   - eine Spalte fehlt
   - ein Datentyp nicht stimmt
'''


if __name__ == "__main__":
    pass