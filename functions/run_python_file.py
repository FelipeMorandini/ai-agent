import os
import subprocess


def run_python_file(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        if not os.path.isabs(file_path):
            file_path_abs = os.path.abspath(os.path.join(working_directory_abs, file_path))
        else:
            file_path_abs = os.path.abspath(file_path)

        if not os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path_abs):
            return f'Error: File "{file_path}" not found.'

        if not file_path_abs.endswith('.py'):
            f'Error: "{file_path}" is not a Python file.'

        completed = subprocess.run(
            ['python3', file_path_abs],
            cwd=working_directory_abs,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = []
        stdout = completed.stdout.strip()
        stderr = completed.stderr.strip()

        if stdout:
            output.append(f"STDOUT:\n{stdout}")
        if stderr:
            output.append(f"STDERR:\n{stderr}")
        if completed.returncode != 0:
            output.append(f"Process exited with code {completed.returncode}")

        if not output:
            return "No output produced."
        return "\n\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"