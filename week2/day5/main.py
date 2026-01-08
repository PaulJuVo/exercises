from pathlib import Path
from functions.data_backup import csv_backup
import functions.json_functions as json
from functions.context_manager import Timer
import argparse

parser = argparse.ArgumentParser(add_help=True, prog='backup script', description="Backup script for .csv data")

parser.add_argument("--input", help="the name of the directory to backup")
parser.add_argument("--output", help="the name of the backup directory", default="backup")

arg = parser.parse_args()

if __name__ == "__main__":
    # Context Manager
    with Timer():
        csv_backup(arg)
        print("\n--- -- ---\n")
        json_path = Path.cwd() / "json"

        saved_json_path = json.person_to_json(json.Person("Paul", 25, 'Valencia'), json_path)
        person_from_json = json.json_to_person(saved_json_path)
        print(f"Loaded json: {person_from_json}")
    

  

