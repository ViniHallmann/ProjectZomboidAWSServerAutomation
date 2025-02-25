import sys
import Utils.aws     as AWS
import Utils.server  as SERVER
from Server_Functions.initialize_server  import initialize_server
from Server_Functions.stop_server        import stop_server

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Uso: python main.py <start>||<stop>")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "start":
        initialize_server()
    elif command == "stop":
        stop_server()
    else:
        print(f"Comando desconhecido: {command}")
        print("Uso: python main.py <start>||<stop>")