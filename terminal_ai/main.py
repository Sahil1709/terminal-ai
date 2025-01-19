from GroqApi import get_completions, check_api_key
import argparse

if __name__ == "__main__":
    check_api_key()
    
    parser = argparse.ArgumentParser(description="Terminal AI CLI")
    parser.add_argument("-q", "--query", required=True, help="User query for terminal commands")
    
    args = parser.parse_args()
    
    commands = get_completions(args.query)
    for command in commands:
        print(command)
