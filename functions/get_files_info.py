import os

def get_files_info(working_directory, directory="."):
    full_path_pre = os.path.join(working_directory, directory)
    full_path = os.path.abspath(full_path_pre)
    #full_path.startswith(working_directory)
    if working_directory not in full_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    files = os.listdir(full_path)
    result_string = ""
    for file in files:
        try:
            result_string += f"- {file} {os.path.getsize(file)}, {os.path.isdir(file)}" + "\n"
        except Exception as e:
            return f"Error: {e}"
        
    return result_string