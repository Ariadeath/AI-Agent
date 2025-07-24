import os
from .config import MAX_CHARS

def get_files_info(working_directory, directory=None):
    try:
        joined_path = os.path.join(working_directory, directory)
        absolute_joined = os.path.abspath(joined_path)
        absolute_working = os.path.abspath(working_directory)
        if not absolute_joined.startswith(absolute_working):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(absolute_joined):
            return f'Error: "{directory}" is not a directory'
    
        directory_contents = os.listdir(absolute_joined)

        results = []
    
        for item in directory_contents:
            name = item
            file_path = os.path.join(absolute_joined, item)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            string = f"- {name}: file_size={file_size}, is_dir={is_dir}"
            results.append(string)

        formated_results = "\n".join(results)
        return formated_results
    
    except Exception as e:
        return f"Error: {e}"
    
def get_file_content(working_directory, file_path):
    try:
        joined_path = os.path.join(working_directory, file_path)
        absolute_joined = os.path.abspath(joined_path)
        absolute_working = os.path.abspath(working_directory)

        if not absolute_joined.startswith(absolute_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
        if not os.path.isfile(absolute_joined):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        original_size = os.path.getsize(absolute_joined)
        with open(absolute_joined, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if original_size > MAX_CHARS:
                return file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
    
def write_file(working_directory, file_path, content):
    try:
        joined_path = os.path.join(working_directory, file_path)
        absolute_joined = os.path.abspath(joined_path)
        absolute_working = os.path.abspath(working_directory)

        if not absolute_joined.startswith(absolute_working):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        directory_name = os.path.dirname(absolute_joined)
        os.makedirs(directory_name, exist_ok=True)

        with open(absolute_joined, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    
    except Exception as e:
        return f"Error: {e}"