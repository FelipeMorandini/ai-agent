import os

def get_files_info(working_directory, directory=None):
    try:
        working_directory = os.path.abspath(working_directory)

        if directory is None:
            target_directory = working_directory
            dir_arg = working_directory
        else:
            if os.path.isabs(directory):
                target_directory = os.path.abspath(directory)
            else:
                target_directory = os.path.abspath(os.path.join(working_directory, directory))
            dir_arg = directory

        if not os.path.commonpath([working_directory, target_directory]) == working_directory:
            return f'Error: Cannot list "{dir_arg}" as it is outside the permitted working directory'

        if not os.path.isdir(target_directory):
            return f'Error: "{dir_arg}" is not a directory'

        entries = []
        for entry in os.listdir(target_directory):
            entry_path = os.path.join(target_directory, entry)
            try:
                is_dir = os.path.isdir(entry_path)
                file_size = os.path.getsize(entry_path)
                entries.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
            except Exception as e:
                entries.append(f'- {entry}: Error: {str(e)}')
        return "\n".join(entries)

    except Exception as e:
        return f"Error: {str(e)}"