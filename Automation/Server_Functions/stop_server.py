import boto3
from botocore.client import BaseClient
import Utils.aws     as AWS
import Utils.server  as SERVER
from configs import load_config

def stop_server_and_instnace() -> None:
    """
    Para o servidor e depois a instância EC2.
    """
    config: dict = load_config()
    ec2: BaseClient = boto3.client("ec2")
    ssh = None
    
    try:
        if not AWS.is_instance_running(ec2, config["INSTANCE_ID"]):
            print("Instância já está parada.")
            return
        
        ip: str = AWS.get_instance_ip(ec2, config["INSTANCE_ID"])
        if ip == "IP não encontrado": raise ValueError("Não foi possível obter o IP da instância.")
 
        ssh = SERVER.connect_ssh(ip, config["KEY_PATH"], config["USER"])

        SERVER.execute_command(ssh, config["STOP_COMMAND"])

        AWS.stop_instance(ec2, config["INSTANCE_ID"])
        print("Instância parada.")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if ssh:
            ssh.close()
            print("Conexão encerrada.")