from core.csv_loader import read_data_from_csv
import core.transformations as mytransform
import core.statistics as mystatistics
from pathlib import Path



def print_dict(data : dict):
    for key, value in data.items():
        if key == 'info':
            print(f'---- {value} ----')
            continue
        if value:
            print(f"{key}: {value}" )


if __name__ == "__main__":
    print("started")
    filename = Path(__file__).parent / "data" / "data.csv"
    data = read_data_from_csv(filename=filename)
    data = mytransform.replace_empty_with_none(data=data)

    data['age'] = mytransform.convert_to_int(data['age'])
    data['salary'] = mytransform.convert_to_int(data['salary'])
    data['salary'] = mytransform.scale_salary(data['salary'])

    for key, value in data.items():
        print(f"{key}: {value}")

    statistic_functions = [mystatistics.average, 
                           mystatistics.min_max, 
                           mystatistics.count_missing ]
    
    for function in statistic_functions:
        print_dict(function(data))

    

    


     