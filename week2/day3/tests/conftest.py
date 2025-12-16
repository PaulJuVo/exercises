import pytest

@pytest.fixture
def sample_list_str():
    return list(map(lambda x: str(x), range(10, 100, 10)))

@pytest.fixture
def sample_list_w_none():
    return [range(10, 50, 10), None, 60, 70, None, 80]

@pytest.fixture
def sample_dict():
    return {"name":["Paul", "Jade", "Yashar", "Giosue"], 
            "age":[25, 20, 32, 23], 
            "city":["Cologne", "Grenoble", "Valencia", "Valencia"]}

@pytest.fixture
def sample_dict_w_none():
    return {"name":["Paul", "Jade", None, "Giosue"], 
            "age":[25, 20, None, 23], 
            "city":["Cologne", None, None, "Valencia"]}

@pytest.fixture
def sample_dict_w_missing_values():
    return {"name":["Paul", "", None, "Giosue"], 
            "age":[25, 20, None, 23], 
            "city":["Cologne", None, None, "Valencia"]}
    