import argparse
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from rich import print
from rich.console import Console

# Function to read model configuration from a txt file
def load_model_configuration(config_file: str = "model_config.txt"):
    with open(config_file, "r") as file:
        config_lines = file.readlines()
    
    # Parse model settings from the file
    model_params = {}
    for line in config_lines:
        line = line.strip()
        if line and not line.startswith("#"):  # Skip empty lines or comments
            key, value = line.split("=", 1)
            model_params[key.strip()] = value.strip()
    
    return model_params

# Function to generate Zsh command based on the task input
def generate_zsh_command(task: str, model_params: dict):
    prompt = f"""You are a command generator. You must provide the user with only the macOS Zsh/bash command that will accomplish the following task. Do not include any explanations, descriptions, or additional information or formatting like ```zsh ```shell or ```bash.

    Task: {task}
    Command:
    """

    # Initialize the LLM model with dynamic parameters
    model = OllamaLLM(
        model=model_params.get("model", "phi3:latest"),  # Default to 'phi3:latest' if not specified
        max_tokens=int(model_params.get("max_tokens", 150)),
        temperature=float(model_params.get("temperature", 0.7)),
        num_predict=int(model_params.get("num_predict", 50))
    )
    
    # Generate the response from the model
    response = model.invoke(prompt)
    
    return response.strip()

# Main function for command-line execution
if __name__ == "__main__":
    # Parse command line argument for the task description (allow multi-word input)
    parser = argparse.ArgumentParser(description="Generate Zsh commands using OllamaLLM")
    parser.add_argument("task", type=str, nargs="+", help="The task description to generate the Zsh command for")

    # Get the arguments from the command line
    args = parser.parse_args()

    # Join all parts of the task into a single string (handles multi-word task input)
    task = " ".join(args.task)

    # Automatically load model configuration from the default file (model_config.txt)
    model_params = load_model_configuration()

    # Generate the Zsh command for the input task
    zsh_command = generate_zsh_command(task, model_params)

    # Print the generated Zsh command with colored output
    console = Console()
    console.print(f"[bold green]{zsh_command}[/bold green]", style="bold")
