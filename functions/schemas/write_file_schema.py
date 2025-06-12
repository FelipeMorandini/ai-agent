from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to the specified file path, creating directories as needed. Constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file from the working directory to write to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to be written to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)