#!/bin/bash

# Função para enviar comandos diretamente para a screen zomboid
send_command() {
    screen -S zomboid -X stuff "$1\r"
}

# Verificar se a screen existe
if ! screen -list | grep -q "zomboid"; then
    echo "Erro: Sessão screen 'zomboid' não encontrada"
    exit 1
fi

# Aguardar 10 segundos
echo "Aguardando 10 segundos..."
sleep 10

# Salvar o jogo
echo "Salvando o jogo..."
send_command "save"

# Aguardar 5 segundos para o save completar
echo "Aguardando o save completar..."
sleep 5

# Fechar o servidor
echo "Fechando o servidor..."
send_command "quit"

# Aguardar o servidor fechar
echo "Aguardando o servidor fechar..."
sleep 15

# Verificar se a screen ainda existe
if ! screen -list | grep -q "zomboid"; then
    echo "Servidor fechado com sucesso"
    exit 0
else
    echo "Erro: O servidor não fechou corretamente após 15 segundos"
    exit 1
fi
