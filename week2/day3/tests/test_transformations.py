import core.transformations as func



def test_convert_to_int(sample_list_str):
    expected= list(range(10, 100, 10))
    assert func.convert_to_int(sample_list_str) == expected

def test_replace_empty_with_none(sample_dict_w_missing_values):
    expected= {"name":["Paul", None, None, "Giosue"], 
            "age":[25, 20, None, 23], 
            "city":["Cologne", None, None, "Valencia"]}
    assert func.replace_empty_with_none(sample_dict_w_missing_values) == expected

def test_scale_salary():
    test_data = list(range(10,41,10))
    expected = [12, 24, 36, 48]
    assert func.scale_salary(test_data) == expected