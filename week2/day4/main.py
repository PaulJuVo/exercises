import etl_functions 

from logger_config import setup_logging


#expected_columns = set(('age', 'name', 'city'))
expected_columns = set(('age', 'name'))

expected_data_types = {'age': int, 'name': str, 'city': str}

data = {'age': 22, 'name': 'Loredana', 'city': 'VLC'}

if __name__ == "__main__":
    setup_logging()
    etl_functions.check_columns_data_types(expected_data_types, data)
    etl_functions.check_if_columns_exists(expected_columns, data)
