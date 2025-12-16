from core.csv_loader import read_data_from_csv
from pathlib import Path

def test_csv_loader():
    expected_data = {"name":["Paul", "Jade", "Yashar", "Giosue"], 
                     "age":["25", "20", "32", "23"], 
                     "city":["Cologne", "Grenoble", "Valencia", "Valencia"]}
    test_file = Path(__file__).parent / "data" / "test_data.csv"
    assert read_data_from_csv(test_file) == expected_data

