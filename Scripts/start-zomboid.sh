#!/bin/bash

# Vai para o diretório do servidor
cd /home/ubuntu/.steam/steam/steamapps/common/Project\ Zomboid\ Dedicated\ Server/  

# Cria uma janela chamada zomboid e executa o script start-server.sh
screen -dmS zomboid ./start-server.sh