def extrair_celulas_codigo(caminho_arquivo, caminho_destino, nome_arquivo):
  """
  Função para extrair e salvar o código de células de um Jupyter Notebook em arquivos Python.

  Argumentos:
    caminho_arquivo: Caminho para o arquivo Jupyter Notebook.
    caminho_destino: Caminho para a pasta onde os arquivos Python serão salvos.
    nome_arquivo: Nome base para os arquivos Python.

  Retorno:
    None.
  """

  # Importa as bibliotecas necessárias
  import nbformat as nbf
  import os

  # Lê o notebook
  with open(caminho_arquivo, 'r') as f:
    nb = nbf.read(f, as_version=4)

  # Contador para numerar as células
  numero_celula = 1

  # Lista para armazenar o código das células
  codigos_celulas = []

  # Itera pelas células do notebook
  for cell in nb['cells']:
    # Verifica se a célula é do tipo 'codigo'
    if cell['cell_type'] == 'code':
      # Armazena o código da célula
      codigos_celulas.append(cell['source'])

  # Imprime as 5 primeiras células de código
  print("**5 primeiras células de código:**")
  for i in range(5):
    print(f"Célula {numero_celula}:")
    numero_celula += 1
    print(codigos_celulas[i])

  # Imprime as 5 últimas células de código
  numero_celula = len(codigos_celulas) - 5
  print("**5 últimas células de código:**")
  for i in range(numero_celula, len(codigos_celulas)):
    print(f"Célula {numero_celula}:")
    numero_celula += 1
    print(codigos_celulas[i])

  # Solicita o número da célula inicial e final ao usuário
  numero_inicial = int(input("Digite o número da célula inicial: "))
  numero_final = int(input("Digite o número da célula final: "))

  # Cria a pasta de destino se não existir
  if not os.path.exists(caminho_destino):
    os.makedirs(caminho_destino)

  # Contador para o nome do arquivo
  contador_arquivo = 1

  # Salva o código de cada célula em um arquivo Python
  for i in range(numero_inicial - 1, numero_final):
    # Formata o nome do arquivo
    nome_arquivo_completo = f"{nome_arquivo}_{contador_arquivo:02}.py"

    # Salva o código em um arquivo
    with open(os.path.join(caminho_destino, nome_arquivo_completo), 'w') as f:
      f.write(codigos_celulas[i])

    # Incrementa o contador do nome do arquivo
    contador_arquivo += 1

# Solicita o caminho do arquivo, pasta de destino e nome base para os arquivos
caminho_arquivo = input("Digite o caminho do arquivo Jupyter Notebook: ")
caminho_destino = input("Digite o caminho da pasta de destino: ")
nome_arquivo = input("Digite o nome base para os arquivos Python: ")

# Extrai e salva o código das células
extrair_celulas_codigo(caminho_arquivo, caminho_destino, nome_arquivo)

print("Arquivos Python salvos com sucesso!")