import os

def get_file_content(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        if not os.path.isabs(file_path):
            file_path_abs = os.path.abspath(os.path.join(working_directory_abs, file_path))
        else:
            file_path_abs = os.path.abspath(file_path)

        if not os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs:
            return f'Error: Cannot read "{file_path_abs}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path_abs}"'

        with open(file_path_abs, 'r', encoding='utf-8') as f:
            content = f.read()
            if len(content) > 10000:
                truncated_content = content[:10000]
                truncated_message = f'\n[...File "{file_path_abs}" truncated at 10000 characters]'
                return truncated_content + truncated_message
            else:
                return content
    except Exception as e:
        return f"Error: {str(e)}"