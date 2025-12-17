import csv
from collections import defaultdict
from csvformaterror import CSVFormatError
import logging
from logger_utils import log_calls
logger = logging.getLogger(__name__)

def load_csv(filename):
    read_data = defaultdict(list)
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:          # row ist ein dict
            for key, value in row.items():
                read_data[key].append(value)
    return read_data

def check_columns_data_types(columns_dict : dict, data : dict):
    for key, value in columns_dict.items():
        if not isinstance(data[key], value):
            error_msg = f"Datatype of '{data[key]}' was expected to be {value}"
            # logging without logging decorator 
            logger.info(error_msg)
            logger.error(error_msg)
            raise CSVFormatError(error_msg, 333)

@log_calls(logger)
def check_if_columns_exists(expected_columns_set : set, data : dict):
    data_columns = set(data.keys())
    count_data_columns = len(data_columns)
    count_expected_columns = len(expected_columns_set)
    is_same = False

    if count_data_columns > count_expected_columns:
        raise CSVFormatError("Data has more Columns than expected", 123)
    elif count_expected_columns > count_data_columns:
        raise CSVFormatError("Data has less Columns than expected", 124)
    else:
        is_same = data_columns == expected_columns_set
        if not is_same:
            raise CSVFormatError("Column Names are not the same", 223)
        
    return is_same

