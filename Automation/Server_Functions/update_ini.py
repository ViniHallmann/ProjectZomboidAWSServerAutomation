"""
Adicionar o novo servertest.ini na instancia:
	1. > sftp -i "CAMINHO PARA CHAVE .PEM" ubuntu@ipdamaquina
		Exemplo: sftp -i "C:\Users\vinic\Desktop\pz-server-files-private\pz-server-key-pair.pem" ubuntu@18.231.109.208
	2. > put CAMINHO DO servertest.ini PAGINA DESTINO
		Exemplo: put C:/Users/vinic/Desktop/pz-server-files/servertest2.ini /home/ubuntu
	3. sudo mv servertest2.ini mv servertest.ini
	4. sudo mv servertest.ini ~/Zomboid/Server/

    local_file_path = "C:/Users/vinic/Desktop/pz-server-files/servertest2.ini"
    remote_temp_path = "/home/ubuntu/servertest2.ini"
    remote_final_path = "/home/ubuntu/Zomboid/Server/servertest.ini"
"""
import boto3
from botocore.client import BaseClient
import Utils.aws     as AWS
import Utils.server  as SERVER
from configs import load_config

def update_ini():
    config: dict = load_config()
    ec2: BaseClient = boto3.client("ec2")
    ssh = None
    
    try:
        if not AWS.is_instance_running(ec2, config["INSTANCE_ID"]):
            print("Instância está parada.")
            return
        
        ip: str = AWS.get_instance_ip(ec2, config["INSTANCE_ID"])
        if ip == "IP não encontrado": raise ValueError("Não foi possível obter o IP da instância.")
 
        ssh = SERVER.connect_ssh(ip, config["KEY_PATH"], config["USER"])
        sftp = ssh.open_sftp()
        
        sftp.put(config["INI_LOCAL_PATH"], config["INI_REMOTE_PATH"])
        ssh.exec_command(f'sudo mv {config["INI_REMOTE_PATH"] + "/servertestnew.ini"} {config["INI_REMOTE_PATH"] + "/servertest.ini"}')
        ssh.exec_command(f'sudo mv {config["INI_REMOTE_PATH"] + "/servertest.ini"} {config["INI_FINAL_PATH"]}')
    except Exception as e:
        print(f"Erro: {e}")

    sftp.close()
    ssh.close()
