# Terminal AI

Terminal AI is a command-line interface (CLI) application that generates terminal commands based on user queries using API.

## Installation

```
pipx install terminal-ai
```

## Usage

1. Ensure you have set the `GROQ_API_KEY` environment variable:

    ```sh
    export GROQ_API_KEY=<your_api_key>
    ```

2. Run the application with a query:

    ```sh
    tai build a docker container
    ```

    Alternatively, you can run the script directly:

    ```sh
    python -m tai build a docker container
    ```

## Example

```sh
$ poetry run tai list files in the current directory
Command: ls
Press Enter to execute the command, or press 'q' to cancel: 