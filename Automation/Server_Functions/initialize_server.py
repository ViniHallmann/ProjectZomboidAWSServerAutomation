import boto3
from botocore.client import BaseClient
import Utils.aws as AWS
from configs import load_config

def initialize_server() -> None:
    """
    Inicializa a instância EC2.
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
