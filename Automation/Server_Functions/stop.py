import boto3
from botocore.client import BaseClient
import Utils.aws     as AWS
import Utils.server  as SERVER
from configs import load_config

def stop_server_and_instance() -> None:
    """
    Para o servidor e depois a instância EC2.
    """
    config: dict = load_config()
    ec2: BaseClient = boto3.client("ec2")
    ssh = None
    
    try:
        stop_server(config, ec2, ssh)
        stop_instance(ec2, config["INSTANCE_ID"])

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if ssh:
            ssh.close()
            print("Conexão encerrada.")

def stop_server(config: dict, ec2: BaseClient, ssh: None) -> None:
    """
    Para o servidor do zomboid.
    """
    
    try:
        if not AWS.is_instance_running(ec2, config["INSTANCE_ID"]):
            print("Instância está parada.")
            return
        
        ip: str = AWS.get_instance_ip(ec2, config["INSTANCE_ID"])
        if ip == "IP não encontrado": raise ValueError("Não foi possível obter o IP da instância.")
 
        ssh = SERVER.connect_ssh(ip, config["KEY_PATH"], config["USER"])
        ### CRIAR COMANDO PARA VERIFICAR JANELA DO SERVIDOR ANTES
        SERVER.execute_command(ssh, config["STOP_COMMAND"])

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if ssh:
            ssh.close()
            print("Conexão encerrada.")

def stop_instance(ec2: BaseClient, instance_id: str) -> None:
    """
    Para a instância EC2.
    """
    try:
        if not AWS.is_instance_running(ec2, instance_id):
            print("Instância está parada.")
            return
        #PRECISA VERIFICAR SE O SERVIDOR ESTA RODANDO 
        AWS.stop_instance(ec2, instance_id)
        print("Instância parada.")

    except Exception as e:
        print(f"Erro: {e}")