import csv
from typing import DefaultDict

def load_csv(filename):
    read_data = DefaultDict(list)
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:          # row ist ein dict
            for key, value in row.items():
                read_data[key].append(value)
    return read_data

def check_columns_data_types(columns_dict : dict, data : dict):
    pass

def check_if_columns_exists(columns_set : set, data : dict):
    return 0==0

