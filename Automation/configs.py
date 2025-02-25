import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        "INSTANCE_ID": os.getenv("INSTANCE_ID"),
        "KEY_PATH": os.getenv("KEY_PATH"),
        "USER": os.getenv("USER"),
        "STOP_COMMAND": os.getenv("STOP_COMMAND")
    }