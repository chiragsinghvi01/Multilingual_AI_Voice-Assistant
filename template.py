import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "pyproject.toml",
    "app.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath)

    if not filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath} with size {os.path.getsize(filepath)} bytes")