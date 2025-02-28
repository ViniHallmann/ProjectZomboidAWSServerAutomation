import os
import boto3
from botocore.client import BaseClient
import Utils.aws     as AWS
import Utils.server  as SERVER
from configs import load_config

def update_ini():
    config: dict = load_config()
    ec2: BaseClient = boto3.client("ec2")
    ssh = None
    sftp = None

    try:
        if not AWS.is_instance_running(ec2, config["INSTANCE_ID"]):
            print("Instância está parada.")
            return
        
        ip: str = AWS.get_instance_ip(ec2, config["INSTANCE_ID"])
        if ip == "IP não encontrado": raise ValueError("Não foi possível obter o IP da instância.")

        ssh = SERVER.connect_ssh(ip, config["KEY_PATH"], config["USER"])
        print("Conectado ao servidor.")
        
        sftp = ssh.open_sftp()
        print("SFTP aberto.")
        
        sftp.put("C:/Users/vinic/Desktop/pz-server-files-public/Server.ini/servertestnew.ini", "/home/ubuntu/servertestnew.ini")
        ssh.exec_command('sudo mv /home/ubuntu/servertestnew.ini /home/ubuntu/servertest.ini')
        ssh.exec_command('sudo mv /home/ubuntu/servertest.ini /home/ubuntu/Zomboid/Server/')
        print("Arquivo Server.ini atualizado.")

    except Exception as e:
        print(f"Erro: {e}")

    sftp.close()
    ssh.close()
