import os
from functions.config import *

def get_file_content(working_directory, file_path):
    abs_work = os.path.abspath(working_directory)
    pre_path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(pre_path)
    #print(abs_work)
    #print(full_path)
    if not (abs_work == file_path or full_path.startswith(abs_work + os.sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    #MAX_CHARS = 10000

    with open(full_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
        return file_content_string