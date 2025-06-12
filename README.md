# AI Agent

A functional, secure AI-powered software agent framework, written in Python. The agent uses the Google Gemini API to perform coding-related tasks on your filesystem, response-chain style, supporting tool-calling and conversational iterations.

---

## Features

- **Conversational Coding Agent**: Powered by Gemini, responds to instructions or coding questions.
- **Tool Usage/Function Calling**: 
  - **File Listing**: List files and directories within a configurable working directory.
  - **File Reading**: Safely read the content of files.
  - **File Writing**: Write or overwrite file content (with safety restrictions).
  - **Python Execution**: Run Python files and capture their output.
- **Chain of Thought**: The agent plans actions, calls tools, and updates the conversation.
- **Secure File Access**: All file operations are restricted to the working directory for security.
- **Conversational Iteration**: Continues running reasoning/planning/conversation up to a max step count.
- **Verbose Logging**: Optional extra output to debug or inspect actions.

---

## Usage

### 1. **Clone & Install**

```sh
  git clone https://github.com/FelipeMorandini/ai-agent.git
  cd ai-agent
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

### 2. **Configure**

Create a `.env` file at the root and define required environment variables:

```ini
GEMINI_API_KEY=<your-google-genai-api-key>
WORKING_DIRECTORY=./calculator
MAX_ITERS=20
```

- `GEMINI_API_KEY`: Get from Google Vertex AI or the Google MakerSuite/Gemini dashboard.
- `WORKING_DIRECTORY`: The directory that all file operations are limited to (This is an example folder created for testing purposes. Include a python project here for your usage).
- `MAX_ITERS`: Max steps the agent will take in one prompt (default: 20).

### 3. **Run**

```sh
  python3 main.py "Inspect all Python files and summarize their purpose."
```

Optional: Use `--verbose` for more detailed logs of actions and responses.

---

## Supported Capabilities

When prompted, the agent can:

- **List files**: Show files/directories (with their sizes) within the working directory or subdirectories.
- **Read files**: Retrieve the content of any readable file within the working directory.
- **Write files**: Create or overwrite files, with customizable content.
- **Execute Python scripts**: Run a `.py` file and return its output and errors.

It automatically chains these tools as needed based on your question (for example, "What does `main.py` do?").

---

## Example Prompts

```sh
  python3 main.py "List all Python files and show their first 10 lines."
  python3 main.py "Create a new file called example.txt with 'Hello, World!' inside."
  python3 main.py "How does the calculator app render the calculation result?"
```

---

## Project Structure

| File/Folder                   | Purpose                                                         |
|-------------------------------|-----------------------------------------------------------------|
| `main.py`                     | Entry point, main conversation loop.                            |
| `config/`                     | System prompt and other configuration.                          |
| `functions/`                  | Tool schemas and logic for tool calling.                        |
| `get_files_info.py`           | Lists files in a directory.                                     |
| `get_file_content.py`         | Reads and returns contents of a file.                           |
| `write_file.py`               | Writes/overwrites a file.                                       |
| `run_python_file.py`          | Executes Python script and captures output.                     |
| `requirements.txt`            | Python dependencies.                                            |
| `.env`                        | Local environment configuration (key, working directory, etc.). |

---

## Security Notice

- **File operations are always sandboxed** to the working directory. The agent will refuse to read/write/execute anything outside this folder.
- **No arbitrary code execution**: Only Python scripts (using `python3`) can be run, and only within the sandbox.

---

## Extending / Customizing

You can add new tool schemas to the `functions/` directory and declare them in the tool registration section. For more info on supported Gemini function calling, review the Gemini API [docs](https://ai.google.dev/).

---

## Requirements

- Python 3.10+
- Packages listed in `requirements.txt`
- A Google Gemini API key (see [Google MakerSuite](https://makersuite.google.com/) or [Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/get-started))

---

## Troubleshooting

- **API errors**: Ensure your API key is correct and you have quota.
- **File errors**: The agent cannot access files outside your working directory.
- **Dependency errors**: Make sure the virtual environment is activated and dependencies installed.

---

## License

MIT License (add your legal/license text here)

---

## Credits

Built using:
- [google-genai](https://pypi.org/project/google-genai/)
- [pydantic](https://docs.pydantic.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
