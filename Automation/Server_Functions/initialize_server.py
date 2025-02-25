import boto3
import Utils.aws as AWS
from configs import load_config

def initialize_server():
    config = load_config()
    ec2 = boto3.client("ec2")
    
    try:
        AWS.start_instance(ec2, config["INSTANCE_ID"])
        ip = AWS.get_instance_ip(ec2, config["INSTANCE_ID"])
        print("Instância iniciada.")
        """NAO FUNCIONA O RETORNO DO IP
            - Tem que esperar o estado "executando" para resgatar IP
        
        print(f"IP da instância: {ip}")
        
        """
        return ec2, ip
    except Exception as e:
        print(f"Erro ao inicializar instância: {e}")
        return None, None
