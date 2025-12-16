import core.statistics as func



def test_average(sample_dict):
    expected_dict= {"age": 25.0}
    assert func.average(sample_dict) == expected_dict

def test_min_max(sample_dict):
    expected_dict= {"age": [20, 32]}
    assert func.min_max(sample_dict) == expected_dict

def test_count_missing(sample_dict_w_none):
    expected_dict= {"name": 1, "age": 1, "city": 2}
    assert func.count_missing(sample_dict_w_none) == expected_dict
