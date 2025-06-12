from google.genai import types

from functions.schemas.get_file_content_schema import schema_get_file_content
from functions.schemas.get_files_info_schema import schema_get_files_info
from functions.schemas.run_python_file_schema import schema_run_python_file
from functions.schemas.write_file_schema import schema_write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)