import os
#import get_files_info
from google import genai # type: ignore
from google.genai import types # type: ignore

def write_file(working_directory, file_path, content):
    abs_work = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not (abs_work == full_path or full_path.startswith(abs_work + os.sep)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    

    try:
        #os.makedirs(os.path.dirname(full_path), exist_ok=True)  # python
        parent_dir = os.path.dirname(full_path)
        os.makedirs(parent_dir, exist_ok=True)
        with open(full_path, "w") as f:  # python
            f.write(content)
    except Exception as e:
        return f"Error: {e}"

    return f'Successfully wrote to "{full_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file, relative to the working directory. Must be provided.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that will be writen in the file.",
            ),
        },
    ),
)