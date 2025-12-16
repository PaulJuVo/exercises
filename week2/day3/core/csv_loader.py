import csv
from typing import DefaultDict

def read_data_from_csv(filename):
    read_data = DefaultDict(list)
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:          # row ist ein dict
            for key, value in row.items():
                read_data[key].append(value)
    return read_data            