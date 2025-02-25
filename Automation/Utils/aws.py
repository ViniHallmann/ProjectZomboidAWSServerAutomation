from botocore.client import BaseClient

def describe_instances( ec2: BaseClient, INSTANCE_ID: str ) -> dict:
    return ec2.describe_instances( InstanceIds=[INSTANCE_ID] )

def verify_instance_state( ec2: BaseClient, INSTANCE_ID: str ) -> str:
    return describe_instances( ec2, INSTANCE_ID )["Reservations"][0]["Instances"][0].get( "State" )["Name"]
    
def get_instance_ip( ec2: BaseClient, INSTANCE_ID: str ) -> str:
    return describe_instances( ec2, INSTANCE_ID )["Reservations"][0]["Instances"][0].get( "PublicIpAddress", "IP não encontrado" )
    
def is_instance_running( ec2: BaseClient, INSTANCE_ID: str ) -> bool:
    return verify_instance_state(ec2, INSTANCE_ID ) == "running"

def start_instance( ec2: BaseClient, INSTANCE_ID: str ) -> None:
    if is_instance_running( ec2, INSTANCE_ID ): return
    ec2.start_instances( InstanceIds=[INSTANCE_ID] )

def stop_instance( ec2: BaseClient, INSTANCE_ID: str ) -> None:
    if not is_instance_running( ec2, INSTANCE_ID ): return
    ec2.stop_instances( InstanceIds=[INSTANCE_ID] )
