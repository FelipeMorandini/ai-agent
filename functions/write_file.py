import os


def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        if not os.path.isabs(file_path):
            file_path_abs = os.path.abspath(os.path.join(working_directory_abs, file_path))
        else:
            file_path_abs = os.path.abspath(file_path)

        if not os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs:
            return f'Error: Cannot write to "{file_path_abs}" as it is outside the permitted working directory'

        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)

        with open(file_path_abs, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path_abs}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"