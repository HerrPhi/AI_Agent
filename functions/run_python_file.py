import os
import subprocess
from google import genai # type: ignore
from google.genai import types # type: ignore

def run_python_file(working_directory, file_path, args=[]):
    abs_work = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not (abs_work == full_path or full_path.startswith(abs_work + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    args_list = ["python", full_path]
    for arg in args:
        args_list.append(arg)
    try:
        result = subprocess.run(args_list, cwd=working_directory, capture_output=True, text=True, timeout=30)
        
        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()

        if not stdout and not stderr:
            return "No output produced."

        exit_string =  f"STDOUT: {stdout} STDERR: {stderr}"
        if result.returncode != 0:
            exit_string += f" Process exited with code {result.returncode}"
       
        return exit_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python program that is at the specified file_path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the function that is beeing run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="The arguments that are passed into the file that is being run. If none are provided passes [\"python\", full_path] into subprocess.run() but no additional (possibly required) args are passed into the function.",
            ),
        },
    ),
)