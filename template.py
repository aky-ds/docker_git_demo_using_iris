import os
from pathlib import Path
list_of_files=[
    'app/train.py',
    'app/predict.py',
    'app/__init__.py',
    'requirements.txt',
    'test/unit_test.py',
    'test/__init__.py',
    'setup.py'

]
for file in list_of_files:
    file_path = Path(file)
    if not file_path.exists():
        # Create the directory if it doesn't exist
        os.makedirs(file_path.parent, exist_ok=True)
        # Create an empty file
        with open(file_path, 'w') as f:
            pass  # Just create an empty file
    else:
        print(f"File {file} already exists.")

