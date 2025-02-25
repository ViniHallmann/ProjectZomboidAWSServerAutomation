import paramiko

def conect_ssh( public_ip: str, KEY_PATH: str, USER: str = "ubuntu" ) -> paramiko.SSHClient:
    key = paramiko.RSAKey( filename=KEY_PATH )
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
    ssh.connect( public_ip, username=USER, pkey=key )
    return ssh

def execute_command( ssh: paramiko.SSHClient, COMMAND: str ) -> None:
    stdin, stdout, stderr = ssh.exec_command( COMMAND )
    print( stdout.read().decode() )
    print( stderr.read().decode() )