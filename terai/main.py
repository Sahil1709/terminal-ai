from .GroqApi import get_completions, check_api_key
import argparse
import subprocess

def main():

    check_api_key()
    
    parser = argparse.ArgumentParser(description="Terminal AI CLI")
    parser.add_argument("query", nargs=argparse.REMAINDER, help="User query for terminal commands")

    args = parser.parse_args()
    user_query = " ".join(args.query)

    if not user_query.strip():
        print("No query provided. Exiting.")
        return

    commands = get_completions(user_query)

    for command in commands:
        print(f"\t\033[1;32m$ {command}\033[0m")
        user_input = input("\033[1;37mPress Enter to execute the command, or press 'q' to cancel: \033[0m")
        if user_input.lower() == 'q':
            print("\033[1;31mCommand execution cancelled.\033[0m")
            break
        else:
            print("\033[1;33mExecuting command...\033[0m")
            subprocess.run(command, shell=True)
            print("\033[1;33m" + ". " * 20 + "\033[0m")

if __name__ == "__main__":
    main()
