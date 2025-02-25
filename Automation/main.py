import sys
import os

from typing import Dict, Callable

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Automation.Server_Functions.initialize_server import initialize_server
from Automation.Server_Functions.stop_server import stop_server_and_instnace

USAGE_MESSAGE = "Uso: python main.py <start>||<stop>"
UNKNOWN_COMMAND_MESSAGE = "Comando desconhecido: {}"
COMMANDS: Dict[str, Callable] = {
    "start": initialize_server,
    "stop": stop_server_and_instnace,
}

def main() -> None:
    
    if len(sys.argv) < 2:
        print(USAGE_MESSAGE)
        
    command = sys.argv[1].lower()
    
    if command not in COMMANDS:
        print(UNKNOWN_COMMAND_MESSAGE.format(command))
        print(USAGE_MESSAGE)
        sys.exit(1)

    try:
        COMMANDS[command]()
    except Exception as e:
        print(f"Erro ao executar o comando '{command}': {e}")
        sys.exit(1) 

if __name__ == "__main__":
    main()