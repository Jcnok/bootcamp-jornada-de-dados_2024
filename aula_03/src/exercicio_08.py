# Exercício 8: Filtragem de Dados Faltantes
# Lista de dicionários representando dados de usuários
dados_usuarios = [
    {'nome': 'João', 'idade': 25, 'email': 'joao@email.com'},
    {'nome': 'Maria', 'idade': 30},
    {'nome': 'Pedro', 'email': 'pedro@email.com'},
    {'nome': 'Ana', 'idade': 35, 'email': 'ana@email.com'}
]

# Campo específico que estamos verificando
campo_especifico = 'email'

# Filtrar os dicionários que têm o campo específico faltando
usuarios_faltando_campo = [usuario for usuario in dados_usuarios if campo_especifico not in usuario]

# Imprimir os usuários que têm o campo específico faltando
print("Usuários com o campo específico faltando:")
for usuario in usuarios_faltando_campo:
    print(usuario)
