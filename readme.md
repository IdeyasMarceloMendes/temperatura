# Temperatura
Um exemplo de uso de consumo de uma api de previsão do tempo.  
A api usada é https://hgbrasil.com/status/weather/  
Foi escolhida pela sua facilidadede uso e permissão de até 400 requisições dia de forma gratuita.   
Não há necessidade de inserir cartão de cŕedito.
## configuração
criar um arquivo .env 
```
touch .env
```
Dentro desse arquivo usar sua key cadastrada no site.  
KEY="sua key"  
a geração de key pede  nome do app mas é só pra registro do site.  
O site usa um sistema de ids para buscar por cidade só fazer uma busca no site pelo id da chave.
## Preparando ambiente
```
virtualenv .venv
source .venv/bin/acitivate
pip3 install python-decouple
pip3 install request
```
## Rodando a aplicação
Atualmente só faz uma requisição pela cidade de vitória.
```
pyton3 main.py
```
