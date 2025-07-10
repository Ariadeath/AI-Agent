import os

def get_files_info(working_directory, directory=None):
    try:
        joining_path = os.path.join(working_directory, directory)
        absolute_joined = os.path.abspath(joining_path)
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