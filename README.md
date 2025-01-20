# OllamaShellCommand 🦙
**OllamaShellCommand** is a command-line utility powered by the Ollama LLM model that generates macOS Zsh/Bash commands based on natural language descriptions. You can use this tool to quickly generate and execute complex shell commands without needing to manually craft them. Just describe your task, and OllamaShellCommand will give you the right command to run.
![Alt text]([path/to/your/gif.gif](https://ibb.co/7Jbvw9t))
## Features

- **Natural Language Processing**: Generate Zsh/Bash commands by simply describing the task in natural language.
- **Ollama LLM Powered**: Uses Ollama's state-of-the-art model to generate commands based on your input.
- **Automatic Configuration**: Model configuration (like model name, max tokens, temperature) is read from a `.txt` file for flexibility.
- **Colorful Output**: Uses the `rich` library to enhance terminal output with color and styling for better readability.
- **Multi-word Task Input**: No need to quote your multi-word task descriptions—just pass them as they are.

## Installation

### Requirements

- Python 3.10 or higher
- `rich` library for styled console output
- `Ollama` Local model setup
- `Langchain` For interacting with Ollama


### Step 1: Clone the Repository

```bash
git clone https://github.com/salmonbrush/ollamashellcommand.git
cd ollamashellcommand
```

### Step 2: Install Dependencies
Create a virtual environment (optional but recommended) and install the required dependencies:
```bash
python3.10 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```
### Step 4: Set Up the Configuration File
Change the settings in model_config.txt so that it matches your Ollama model and your preferences. For example:
```bash
model = phi3:latest
max_tokens = 150
temperature = 0.7
num_predict = 50
```
##
I would love to see this project grow and become better so any contributions is as always much appreciated.
/Salmonbrush
