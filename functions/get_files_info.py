import os

def get_files_info(working_directory, directory="."):
    full_path_pre = os.path.join(working_directory, directory)
    full_path = os.path.abspath(full_path_pre)
    #full_path.startswith(working_directory)
    abs_work = os.path.abspath(working_directory)
    if not (abs_work == full_path or full_path.startswith(abs_work + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    files = os.listdir(full_path)
    result_list = []
    result_string = ""
    for file in files:
        try:
            file_path = os.path.join(full_path, file)
            result_list.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
            #- {file}: file_size={size} bytes, is_dir={is_dir}
            result_string = "\n".join(result_list)
        except Exception as e:
            return f"Error: {e}"
        
    return result_string