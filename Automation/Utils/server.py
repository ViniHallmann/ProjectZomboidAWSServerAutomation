import paramiko

def connect_ssh( public_ip: str, KEY_PATH: str, USER: str = "ubuntu" ) -> paramiko.SSHClient:
    """
    Conecta ao servidor via SSH.
    """
    try:
        key = paramiko.RSAKey( filename=KEY_PATH )
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        ssh.connect( public_ip, username=USER, pkey=key )
        return ssh
    except Exception as e:
        print( f"Erro ao conectar via SSH: {e}" )
        return None
        
def execute_command( ssh: paramiko.SSHClient, COMMAND: str ) -> None:
    """
    Executa um comando no servidor via SSH.
    """
    try:
        stdin, stdout, stderr = ssh.exec_command( COMMAND )
    except Exception as e:
        print( f"Erro ao executar comando via SSH: {e}" )
        return None