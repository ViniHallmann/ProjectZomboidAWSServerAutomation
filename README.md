# **Servidor Project Zomboid - Configuração e Automação**

Este repositório contém scripts em Python para automatizar o gerenciamento do servidor do **Project Zomboid** na AWS.

---

## **Requisitos**

Antes de começar, garanta que você tenha os seguintes requisitos:

- **AWS CLI**: A ferramenta de linha de comando da AWS deve estar instalada e configurada. Certifique-se de que a conta **`pz-user-organizer`** esteja configurada corretamente.
- **Bibliotecas Python**: As dependências do projeto estão listadas no arquivo `requirements.txt`.

Para instalar as bibliotecas, execute:

```bash
pip install -r requirements.txt
```

## **Iniciar instância**
Para iniciar o servidor, basta rodar o script initialize-server.py:
```bash
python main.py start-instance
```
Esse comando irá iniciar a instância EC2 na AWS, configurar o servidor do Project Zomboid e inicia-lo.

## **Finalizar servidor do Project Zomboid**
Quando precisar parar o servidor, basta executar o script main.py passando o argumento "stop-server":
```bash
python main.py stop-server
```
Este comando irá desligar o servidor do Project Zomboid.

## **Inicializar o servidor do Project Zomboid**
Quando precisar iniciar o servidor, basta executar o script main.py passando o argumento "start-server":
```bash
python main.py start-server
```
Este comando irá ligar o servidor do Project Zomboid.

## **Finalizar instância**
Quando precisar encerrar somente a instância, basta executar o script main.py passando o argumento "stop-instance":
```bash
python main.py stop-instance
```
Este comando irá desligar a instância. Verifique sempre se o servidor não está ligado, pois isso pode acarretar em corrompimento do save do servidor.

## **Finalizar ambos (Servidor e Instância)**
Quando quiser desligar tudo, basta executar o script main.py passando o argumento "terminate":
```bash
python main.py terminate
```
Este comando irá desligar o servidor do Project Zomboid e depois acabar com a execução da instância.

## **Atualziar arquivo .ini do server**
Quando quiser atualizar o servertest.ini como novos mods/configuracoes de servidor, basta executar o script main.py passando o argumento "update". Esse comando pegara o servernewtest.ini da pasta Server.ini e colocara dentro dos arquivos do servidor. Para isso o servidor precisa estar desligado(Usar python main.py stop-server antes)

Por fim rodar:

```bash
python main.py update
```

## **Como Configurar**
Configurar AWS CLI: Após instalar a AWS CLI, execute aws configure e insira as credenciais da conta **pz-user-organizer**.

Configurar Variáveis no .env: Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:

```plaintext
INSTANCE_ID   = "<ID da sua instância EC2>"
KEY_PATH      = "<Caminho para sua chave .pem>"
USER          = "ubuntu"
STOP_COMMAND  = "sudo systemctl start stop-zomboid.service"
START_COMMAND = "sudo systemctl start start-zomboid.service"
ACESS_COMMAND = "screen -r zomboid"

```

## **TO-DO**
Por ordem do que julgo mais facil e importante:

1. Backup do save no S3;
2. Acesso envio de mais comandos para o terminal do server.
