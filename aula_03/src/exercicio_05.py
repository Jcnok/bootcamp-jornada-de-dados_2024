# Exercício 5: Detecção de Anomalias em Dados de Transações
transacao = {'valor': 12000, 'hora': 20}

# Verifica se o valor da transação é superior a R$ 10.000
if transacao['valor'] > 10000:
    print("Transação suspeita: valor superior a R$ 10.000")
# Verifica se a hora da transação está fora do horário comercial
elif transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita: ocorreu fora do horário comercial")
else:
    print("Transação não suspeita")
