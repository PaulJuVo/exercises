from typing import DefaultDict


def average(data: dict):
    ret_dict = DefaultDict()
    ret_dict['info'] = "Average"
    for key, value in data.items():
        try:
            if isinstance(value, list):
                summable_values = [ v for v in value if isinstance(v, (int, float))]
                ret_dict[key] = sum(summable_values) / len(summable_values)
        except Exception as e:
            # print(e)
            ret_dict[key] = None
    
   
    return ret_dict

def count_missing(data : dict):
    ret_dict = DefaultDict()
    ret_dict['info'] = "Amount of Missing Values"
    for key, value in data.items():
        ret_dict[key] = len([v for v in value if v is None])
    
    return ret_dict

def min_max(data : dict):
    ret_dict = DefaultDict()
    ret_dict['info'] = "Min and Max"
    for key, value in data.items():
        try:
            if isinstance(value, list):
                    existing_values = [ v for v in value if isinstance(v, (int, float))]
                    ret_dict[key] = [min(existing_values), max(existing_values)]
        except Exception as e:
            # print(e)
            ret_dict[key] = None
    
    return ret_dict

