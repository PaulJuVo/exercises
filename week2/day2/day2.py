from dataclasses import dataclass
import csv
from itertools import groupby, chain, islice, combinations
import copy

@dataclass
class DataPerson:
    age: int
    name: str
    city: str

    @property
    def is_adult(self):
        return self.age > 17

class Person:
    
    def __init__(self, name : str, age : int, city : str) -> None:
        self.age = age
        self.name = name
        self.city = city

    @classmethod
    def from_csv_row(cls, row):
        return cls(*row)

    def __repr__(self) -> str:
        return f'Person(name={self.name}, age={self.age}, city={self.city})'
    
    @property
    def is_adult(self):
        return self.age > 17
    

class CsvLoader:

    def __init__(self, filename : str) -> None:
        self.filename : str = filename
        self.persons : list = list()
    
    def data_to_person(self, line : dict):
        
        name, age, city = line.values()
        age = int(age)
        
        self.persons.append(Person(name, age, city))
        

    def read_data(self):
        with open(self.filename, mode="r") as file:
            for each in csv.DictReader(file):
                self.data_to_person(each)
        

    def filter_by_city(self, city : str):
        persons = sorted(copy.deepcopy(self.persons), key=(lambda x : x.city))
        for key, group in groupby(persons, lambda x: x.city):
            if key == city:
                print(*group, sep="\n")


    def average_age(self):
        persons = self.persons
        count = sum(map(lambda x: x.age, persons))
        print(count/ len(persons))


if __name__ == "__main__":

    print( "---- Test Strtet __")
    test = CsvLoader("data.csv")
    test.read_data()
    test.filter_by_city("Valencia")
    test.average_age()