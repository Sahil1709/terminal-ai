from groq import Groq
import os
import sys
import argparse
import json
import platform

client = None

def check_api_key():
    global client
    if not os.environ.get("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY not found in environment variables.")
        print("Go to https://console.groq.com/keys to get your API key and do `export GROQ_API_KEY=<your_api_key>`")
        sys.exit(1)

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

def get_completions(user_query: str):
    global client

    user_os = "macOS" if platform.system() == "Darwin" else platform.system()
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You're an expert systems engineer with 10 years of experience writing " + user_os + " terminal commands. Your task is to give a list of commands that are needed to fulfill user's query. Your JSON schema should follow:\n{\n    \"commands\": List[str]\n}"
            },
            {
                "role": "user",
                "content": user_query
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

    try: 
        response = completion.choices[0].message.content
        response = json.loads(response)
        return response["commands"]
    except Exception as e:
        print(response)
        print(e)
        return ["Some error occurred. Please try again."]
    
