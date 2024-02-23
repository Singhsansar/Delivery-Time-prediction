import os 
import sys 
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s',
    # filename='logfile.log' no need to save these logs 
) 
while True:
    project_name = input("Enter the project name: ")
    if project_name!="":
        break
    
# src/__init__.py
list_of_files = [
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/exception/__init__.py",
        f"src/{project_name}/logger/__init__.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"config/config.yaml","schema.yaml",
        "app.py",
        "main.py",
        "logs.py",
        "exceptions.py",
        "setup.py",
        "requirements.txt",
        "Dockerfile"
    ]

for filepath in list_of_files: 
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    print(f"Directory: {filedir}, Filename: {filename}")

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  
        logging.info(f"creating directory: {filedir} for the file {filename}")

    if (not filepath.exists()) or (filepath.stat().st_size == 0): 
        with open(filepath, 'w'):
            pass
        logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} already exists")