# **Servidor Project Zomboid - Configuração e Automação**

Este repositório contém scripts em Python para automatizar o gerenciamento do servidor do **Project Zomboid** na AWS. Você poderá iniciar, parar e acessar o servidor.

---

## **Requisitos**

Antes de começar, garanta que você tenha os seguintes requisitos:

- **AWS CLI**: A ferramenta de linha de comando da AWS deve estar instalada e configurada. Certifique-se de que a conta **`pz-user-organizer`** esteja configurada corretamente.
- **Bibliotecas Python**: As dependências do projeto estão listadas no arquivo `requirements.txt`.

Para instalar as bibliotecas, execute:

```bash
pip install -r requirements.txt
```

## **Iniciar o Servidor**
Para iniciar o servidor, basta rodar o script initialize-server.py:
```bash
python main.py start
```
Esse comando irá automaticamente iniciar a instância EC2 na AWS e configurar o servidor do Project Zomboid.

## **Acessar o Servidor**
Para visualizar a janela do servidor (via screen), use o seguinte comando:
```bash
python python main.py acess
```
**Nota**: Este comando ainda não foi implementado.

## **Finalizar o Servidor**
Quando precisar parar o servidor, basta executar o script stop-server.py:

```bash
python main.py stop
```
Este comando irá desligar o servidor do Project Zomboid e finalizar a instância EC2.

## **Como Configurar**
Configurar AWS CLI: Após instalar a AWS CLI, execute aws configure e insira as credenciais da conta **pz-user-organizer**.

Configurar Variáveis no .env: Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:

```plaintext
INSTANCE_ID   = "<ID da sua instância EC2>"
KEY_PATH      = "<Caminho para sua chave .pem>"
USER          = "ubuntu"
STOP_COMMAND  = "sudo systemctl start stop-zomboid.service"
ACESS_COMMAND = "screen -r zomboid"
```