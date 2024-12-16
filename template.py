
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Speech_2_Text"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/Model.py",
    f"src/{project_name}/components/Prompt_and_chain.py",
    f"src/{project_name}/components/data_processing.py",
    
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",


    "config/config.yaml",
    ".env",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "notebook/trials.ipynb",
    "templates/index.html",
    "static/css/home.css",
    "static/css/speech_2_text.css",
    "static/js/home.js",
    "static/js/speech_2_text.js",
    ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")