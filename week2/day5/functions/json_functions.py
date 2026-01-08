from dataclasses import dataclass, asdict
import json




@dataclass
class Person():
    name : str
    age : int
    city : str

def person_to_json(person : Person, path):
    json_path = path / "file.json"
    with open(path / "file.json", "w") as file:
        json.dump(asdict(person), file) 
    return json_path

def json_to_person(json_data_path):
    with open(json_data_path, "r") as file :
        json_data = json.load(file)
        person = Person(**json_data)
    return person