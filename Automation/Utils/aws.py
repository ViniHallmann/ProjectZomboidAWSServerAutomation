from time import sleep
from botocore.client import BaseClient

def describe_instance( ec2: BaseClient, INSTANCE_ID: str ) -> dict:
    """
    Descreve a instância com o ID fornecido.
    """
    return ec2.describe_instances( InstanceIds=[INSTANCE_ID] )

def verify_instance_state( ec2: BaseClient, INSTANCE_ID: str ) -> str:
    """
    Verifica o estado atual da instância EC2.
    """
    return describe_instance( ec2, INSTANCE_ID )["Reservations"][0]["Instances"][0].get( "State" )["Name"]
    
def get_instance_ip( ec2: BaseClient, INSTANCE_ID: str ) -> str:
    """
    Obtém o IP público da instância EC2.
    """
    return describe_instance( ec2, INSTANCE_ID )["Reservations"][0]["Instances"][0].get( "PublicIpAddress", "IP não encontrado" )
    
def is_instance_running( ec2: BaseClient, INSTANCE_ID: str ) -> bool:
    """
    Verifica se a instância com o ID fornecido está em execução.
    """
    return verify_instance_state(ec2, INSTANCE_ID ) == "running"

def start_instance( ec2: BaseClient, INSTANCE_ID: str ) -> None:
    """
    Inicia a instância EC2, se não estiver em execução.
    """
    if is_instance_running( ec2, INSTANCE_ID ): return
    ec2.start_instances( InstanceIds=[INSTANCE_ID] )

def stop_instance( ec2: BaseClient, INSTANCE_ID: str ) -> None:
    """
    Para a instância EC2, se estiver em execução.
    """
    if not is_instance_running( ec2, INSTANCE_ID ): return
    ec2.stop_instances( InstanceIds=[INSTANCE_ID] )

def wait_for_instance_ip(ec2: BaseClient, instance_id: str, max_retries: int = 10, delay: int = 10) -> str:
    """
    Aguarda até que a instância esteja em execução e retorna o IP público.
    """
    for _ in range(max_retries):
        if is_instance_running(ec2, instance_id):
            ip = get_instance_ip(ec2, instance_id)
            if ip != "IP não encontrado":
                return ip
        sleep(delay)
    raise TimeoutError("Timeout ao aguardar o IP da instância.")