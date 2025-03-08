import boto3
from botocore.client import BaseClient
import Utils.aws    as AWS
import Utils.server as SERVER
from configs import load_config

def initialize_instance() -> None:
    """
    Inicializa a instância EC2.

    Usando .service o server do zomboid já inicializado automaticamente com o inicio da instância.
    """
    config: dict = load_config()
    ec2: BaseClient = boto3.client("ec2")
    
    try:
        if AWS.is_instance_running(ec2, config["INSTANCE_ID"]):
            print("Instância já está iniciada.")
            return
        
        AWS.start_instance(ec2, config["INSTANCE_ID"])
        print("Instância iniciada.")

        ip: str = AWS.wait_for_instance_ip(ec2, config["INSTANCE_ID"])
        print(f"IP da instância: {ip}")

    except Exception as e:
        print(f"Erro ao inicializar instância: {e}")
        return None, None

def start_server() -> None:
    """
    Para o servidor do zomboid.
    """
    config: dict = load_config()
    ec2: BaseClient = boto3.client("ec2")
    ssh = None

    try:
        if not AWS.is_instance_running(ec2, config["INSTANCE_ID"]):
            print("Instância está parada.")
            return
        print("Instância está rodando.")
        
        ip: str = AWS.get_instance_ip(ec2, config["INSTANCE_ID"])
        if ip == "IP não encontrado": raise ValueError("Não foi possível obter o IP da instância.")
 

        ###CRIAR COMANDO PARA VERIFICAR JANELA DO SERVIDOR ANTES
        print("Conectando ao servidor...")
        ssh = SERVER.connect_ssh(ip, config["KEY_PATH"], config["USER"])

        print("Iniciando servidor...")
        response = SERVER.execute_command(ssh, config["START_COMMAND"])
        print(response)

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if ssh:
            ssh.close()
            print("Conexão encerrada.")