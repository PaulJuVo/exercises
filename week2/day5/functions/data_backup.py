from pathlib import Path
import shutil

def csv_backup(arg):

    input_directory  = Path(arg.input).resolve()
    output_directory = Path(arg.output).resolve()

    if not output_directory.exists():
        backup_dir = Path("backup").resolve()
        backup_dir.mkdir(exist_ok=True)

    if Path.exists(input_directory):
        for file_path in input_directory.glob("*.csv"):
            name = file_path.name
            print(f"Output from: {name}")
            
            shutil.copy(file_path, output_directory)
            

