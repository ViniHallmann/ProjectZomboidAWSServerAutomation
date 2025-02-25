import boto3
import Utils.aws     as AWS
import Utils.server  as SERVER
from configs import load_config

def stop_server():
    config = load_config()
    ec2 = boto3.client("ec2")
    ssh = None
    
    try:
        ip = AWS.get_instance_ip(ec2, config["INSTANCE_ID"])
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