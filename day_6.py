'''
### **Tag 6 – Comprehensions & Mini-Projekt**

**Ziel:** Kombinieren aller Grundlagen in einem kleinen Programm.

**Mini-Projekt:**

**CSV-Statistik-Tool**

1. Lies eine CSV-Datei mit Spalten (z. B. `name, age, salary`).
2. Berechne:
    - Durchschnittliches Alter
    - Durchschnittsgehalt
    - Anzahl Zeilen mit fehlenden Werten
3. Nutze:
    - Dict/List Comprehensions
    - Funktionen
    - Exception Handling
4. Bonus:
    - CLI-Eingabe: Der Benutzer gibt den Dateinamen als Argument ein (`argparse`).
    - Ausgabe in eine neue Datei `summary.txt`.
'''

import csv
from collections import defaultdict
import pprint as pp
import day_6_logger 
from typing import Any, Callable, TypeVar
import argparse

logger6 = day_6_logger.logger

def write_to_txt(*args):
    with open('day_6_data/summary.txt', mode="w") as file:
        file.writelines(f'{arg} \n' for arg in args)

def read_csv(filename : str):
    result = defaultdict(list)

    with open(filename, mode="r") as file:
        csv_file = csv.DictReader(file)
        logger6.info('Read %s' + filename)
        for line in csv_file:
            result.update( {key: list((*result[key], value)) for (key, value) in line.items()} )
    #for k,v in result.items():
    #    print(f"{k} : {v}\n")
    return result

def missing_data_to_none(data : dict):
    result = data.copy()
    for k,v in data.items():
        result.update( {k: [None if value == "" else value for value in v]} )
    return result


A = TypeVar("A")
B = TypeVar("B")

to_int_or_none = lambda x : int(x) if x is not None else None
to_int = lambda x : int(x) if x is not None else 0

columns_to_transform = {'name': None, 'age': to_int, 'salary': to_int }

def transform(data: dict, transformations : dict[str, Callable[[A], B] | None]):
    cleaned_data = data.copy()
    for k in cleaned_data.keys():
        func = transformations.get(k, None)
        if func is not None:
            cleaned_data.update({k: list(map(func, cleaned_data[k]))})    
    return cleaned_data
        

def calc_avg(data : list) : return round(sum(data)/ len(data), 2)

def calc_rows_w_missing_values(data : dict):
    zipped_data = zip(*data.values())
    return len(list(filter(lambda x: x.count(None) > 0, zipped_data)))
    

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="CSV Statistik Tool")
    parser.add_argument("filename", help="Pfad zur CSV-Datei")
    args = parser.parse_args()

    # user_input = input("insert the filename:")
    data_path = "day_6_data/"
    user_input = "salary.csv"

    csv_data = read_csv(data_path + user_input)
    cleaned_data = missing_data_to_none(data=csv_data)
    transformed_data = transform(cleaned_data, columns_to_transform)
    
    amount_rows_w_mis_values = f'Anzahl an Zeilen mit fehlenden Werten: {calc_rows_w_missing_values(cleaned_data)}'
    salary_wo_zeros = f'Durchschnittliches Gehalt: {calc_avg([ x for x in transformed_data["salary"] if x != 0])}'
    age_wo_nones = f'Durchschnittliches Alter: {calc_avg([ x for x in transformed_data["age"] if x is not None])}'

    write_to_txt(amount_rows_w_mis_values, salary_wo_zeros, age_wo_nones)


