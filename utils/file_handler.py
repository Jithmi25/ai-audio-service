import shutil
import os

def save_temp_file(upload_file):
    file_path = f"uploads/temp_{upload_file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path

def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
