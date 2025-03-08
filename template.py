import os 
from pathlib import Path
import logging

# logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep", # to only upload the folders that have some files in them instead of uploading an empty folder to git
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath) # converts the string into a path object
    filedir,filename = os.path.split(filepath) # splits the path into file directory and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # creates a file directory and ensures no error is thrown if that directory already exists 
        logging.info(f'Creating directory; {filedir} for the file {filename}') #logs the creation of the file directory

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):# checks if there exists a file or if there is a file that is empty
        with open(filepath, 'w') as f: # creates a file or opens the already existing file in write mode and does nothing with. This is where the __init__.py files are getting created
            pass
        logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'{filename} already exists')