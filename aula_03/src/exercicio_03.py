#Exercício 3: Filtragem de Logs por Severidade
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# Verifica se a severidade é 'ERROR' e imprime a mensagem
if log.get('level') == 'ERROR':
    print(log.get('message'))
