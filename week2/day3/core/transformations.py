

from typing import DefaultDict


def convert_to_int(data : list):
    def safe_int(x):
        if x is None:
            return None
        if isinstance(x, str) and x.strip().lower() in ("none", ""):
            return None
        try:
            return int(x)
        except:
            return None
    return list(map(safe_int, data))

def replace_empty_with_none(data : dict):
    ret_dict = DefaultDict()
    try:
        for key, value in data.items():
            ret_dict[key] = list(map(lambda x: x if x else None, value))
    except Exception:
        print(Exception)
    return ret_dict

def scale_salary(data: list, scalefactor = 1.2):
    try:
        scaled_list = list(map(lambda x: int(x * 1.2) if x is not None else None,data))
    except Exception:
        print(Exception)
    
    return scaled_list