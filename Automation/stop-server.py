import boto3
import paramiko
import os
from dotenv import load_dotenv

load_dotenv()

INSTANCE_ID = os.getenv("INSTANCE_ID")
KEY_PATH    = os.getenv("KEY_PATH")
USER        = os.getenv("USER")
COMMAND     = os.getenv("STOP_COMMAND")

ec2 = boto3.client("ec2")

def get_instance_ip() -> str:
    response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
    return response["Reservations"][0]["Instances"][0].get("PublicIpAddress")

def conect_ssh(public_ip: str) -> paramiko.SSHClient:
    key = paramiko.RSAKey(filename=KEY_PATH)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(public_ip, username=USER, pkey=key)
    return ssh

def execute_command(ssh: paramiko.SSHClient) -> None:
    stdin, stdout, stderr = ssh.exec_command(COMMAND)
    print(stdout.read().decode())
    print(stderr.read().decode())

def stop_instance() -> None:
    if verify_instance_state() == "stopped": return
    response = ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print(response)

def verify_instance_state() -> str:
    response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
    return response["Reservations"][0]["Instances"][0].get("State")["Name"]

try:
    ip = get_instance_ip()
    ssh = conect_ssh(ip)
    execute_command(ssh)
    stop_instance()

except Exception as e:
    print(f"Erro: {e}")

finally:
    ssh.close()
    print("Conexão encerrada.")
