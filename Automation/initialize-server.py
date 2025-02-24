import boto3
import os
from dotenv import load_dotenv

load_dotenv()

INSTANCE_ID = os.getenv("INSTANCE_ID")
KEY_PATH    = os.getenv("KEY_PATH")
USER        = os.getenv("USER")
COMMAND     = os.getenv("STOP_COMMAND")

ec2 = boto3.client("ec2")

def start_instance():
    if verify_instance_state() == "running": return
    response = ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print(response)

def verify_instance_state() -> str:
    response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
    return response["Reservations"][0]["Instances"][0].get("State")["Name"]

try:
    start_instance()

except Exception as e:
    print(f"Erro: {e}")

