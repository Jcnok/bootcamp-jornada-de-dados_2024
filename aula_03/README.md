```python
#verifica se o ambiente virtual foi setado corretamente no jupyter
import site
site.getsitepackages()
```




    ['/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages']




```python
#Confere a versão do python 
!python --version
```

    Python 3.11.3


## Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
* Este projeto utilizar a versão 3.11.3 do python.
2. Clone ou baixe este repositório em sua máquina conforme o exemplo abaixo:
`git clone https://github.com/Jcnok/bootcamp-jornada-de-dados_2024.git`

3. Navegue até o diretório 'aula_03/src/' onde os exercicíos estão salvos confome o exemplo abaixo:
`$ cd bootcamp-jornada-de-dados_2024/aula_03/src`

* Exemplo de como executar o 'exercicio_01.py':
`$ python exercicio_25.pyxercicio_01.py`

# Aula 03: DEBUG, IF, FOR, While, Listas e Dicionários em Python

## Resolução dos Exercícios e Desafios

<a id="voltar"></a>

1.  **[Exercício 1: Verificação de Qualidade de Dados](#ancora01)**
2.  **[Exercício 2: Classificação de Dados de Sensor](#ancora02)**
3.  **[Exercício 3: Filtragem de Logs por Severidade](#ancora04)**
4.  **[Exercício 4: Validação de Dados de Entrada](#ancora05)**
5.  **[Exercício 5: Detecção de Anomalias em Dados de Transações](#ancora05)**
6.  **[Exercício 6: Contagem de Palavras em Textos](#ancora06)**
7.  **[Exercício 7: Normalização de Dados](#ancora07)**
8.  **[Exercício 8: Filtragem de Dados Faltantes](#ancora08)**
9.  **[Exercício 9: Extração de Subconjuntos de Dados](#ancora09)**
10. **[Exercício 10: Agregação de Dados por Categoria](#ancora10)**
11. **[Exercício 11:  Leitura de Dados até Flag](#ancora11)**
12. **[Exercício 12: Validação de Entrada](#ancora12)**
13. **[Exercício 13: Consumo de API Simulado](#ancora13)**
14. **[Exercício 14: Tentativas de Conexão](#ancora14)**
15. **[Exercício 15: Processamento de Dados com Condição de Parada](#ancora15)**
16. **[Desafio : Estruturas de Controle de Fluxo](#desafio)**



<a id="ancora01"></a>
### Exercício 1: Verificação de Qualidade de Dados

Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para `quantidade` e `preço`. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.



```python
# Exercício 1: Verificação de Qualidade de Dados
try:
    # Entrada dos valores de quantidade e preço
    quantidade = float(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))

    # Verificação se ambos os valores são positivos
    if quantidade > 0 and preco > 0:
        print("Dados válidos")
    else:
        print("Dados inválidos")
except ValueError:
    print("Entrada inválida. Por favor, digite um número válido para quantidade e preço.")

```

    The history saving thread hit an unexpected error (OperationalError('attempt to write a readonly database')).History will not be written to the database.


    Digite a quantidade:  -100
    Digite o preço:  200


    Dados inválidos


<a id="ancora02"></a>
### Exercício 2: Classificação de Dados de Sensor

Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como `Baixa`, `Normal` ou `Alta`. Considerando que:
* Temperatura < 18°C é 'Baixa'
* Temperatura >= 18°C e <= 26°C é 'Normal'
* Temperatura > 26°C é 'Alta'


```python
#Exercício 2: Classificação de Dados de Sensor
try:
    # Entrada da temperatura
    temperatura = float(input("Digite a temperatura em °C: "))

    # Classificação da temperatura
    if temperatura < 18:
        print("Baixa")
    elif 18 <= temperatura <= 26:
        print("Normal")
    else:
        print("Alta")
except ValueError:
    print("Entrada inválida. Por favor, digite um número válido para a temperatura.")

```

    Digite a temperatura em °C:  33


    Alta


<a id="ancora03"></a>
### Exercício 3: Filtragem de Logs por Severidade

Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.



```python
#Exercício 3: Filtragem de Logs por Severidade
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# Verifica se a severidade é 'ERROR' e imprime a mensagem
if log.get('level') == 'ERROR':
    print(log.get('message'))

```

    Falha na conexão


<a id="ancora04"></a>
### Exercício 4: Validação de Dados de Entrada

Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.



```python
#Exercício 4: Validação de Dados de Entrada
import re

# Entrada dos dados do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

# Validação da idade
if idade < 18:
    print("Idade menor que 18 anos.")
elif idade > 65:
    print("Idade maior que 65 anos.")
else:
    # Validação do email
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("Email inválido.")
    else:
        print("Dados de usuário válidos.")

```

    Digite seu nome:  Julio 
    Digite sua idade:  15
    Digite seu email:  jc@gmail.com


    Idade menor que 18 anos.


<a id="ancora05"></a>
### Exercício 5: Detecção de Anomalias em Dados de Transações

Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.



```python
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

```

    Transação suspeita: valor superior a R$ 10.000


[voltar](#voltar)

<a id="ancora06"></a>
### Exercício 6: Contagem de Palavras em Textos

**Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.



```python
# Exercício 6: Contagem de Palavras em Textos
# Texto de exemplo
texto = "Python é uma linguagem de programação de alto nível e de uso geral, que pode ser utilizada para uma ampla variedade de tarefas. Python é conhecida por sua sintaxe simples e legibilidade de código."

# Transforma o texto em minúsculas e separa as palavras
palavras = texto.lower().split()

# Cria um dicionário para armazenar a contagem de cada palavra única
contagem_palavras = {}

# Conta quantas vezes cada palavra única aparece no texto
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

# Imprime a contagem de cada palavra única
for palavra, contagem in contagem_palavras.items():
    print(f"A palavra '{palavra}' aparece {contagem} vez(es) no texto.")


```

    A palavra 'python' aparece 2 vez(es) no texto.
    A palavra 'é' aparece 2 vez(es) no texto.
    A palavra 'uma' aparece 2 vez(es) no texto.
    A palavra 'linguagem' aparece 1 vez(es) no texto.
    A palavra 'de' aparece 5 vez(es) no texto.
    A palavra 'programação' aparece 1 vez(es) no texto.
    A palavra 'alto' aparece 1 vez(es) no texto.
    A palavra 'nível' aparece 1 vez(es) no texto.
    A palavra 'e' aparece 2 vez(es) no texto.
    A palavra 'uso' aparece 1 vez(es) no texto.
    A palavra 'geral,' aparece 1 vez(es) no texto.
    A palavra 'que' aparece 1 vez(es) no texto.
    A palavra 'pode' aparece 1 vez(es) no texto.
    A palavra 'ser' aparece 1 vez(es) no texto.
    A palavra 'utilizada' aparece 1 vez(es) no texto.
    A palavra 'para' aparece 1 vez(es) no texto.
    A palavra 'ampla' aparece 1 vez(es) no texto.
    A palavra 'variedade' aparece 1 vez(es) no texto.
    A palavra 'tarefas.' aparece 1 vez(es) no texto.
    A palavra 'conhecida' aparece 1 vez(es) no texto.
    A palavra 'por' aparece 1 vez(es) no texto.
    A palavra 'sua' aparece 1 vez(es) no texto.
    A palavra 'sintaxe' aparece 1 vez(es) no texto.
    A palavra 'simples' aparece 1 vez(es) no texto.
    A palavra 'legibilidade' aparece 1 vez(es) no texto.
    A palavra 'código.' aparece 1 vez(es) no texto.


<a id="ancora07"></a>
### Exercício 7: Normalização de Dados

**Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.


```python
# Exercício 7: Normalização de Dados
# Lista de números de exemplo
numeros = [10, 20, 30, 40, 50]

# Calcula o valor mínimo e máximo da lista
minimo = min(numeros)
maximo = max(numeros)

# Normaliza os números para a escala de 0 a 1
numeros_normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# Imprime os números normalizados
print("Números normalizados:", numeros_normalizados)

```

    Números normalizados: [0.0, 0.25, 0.5, 0.75, 1.0]


<a id="ancora08"></a>
### Exercício 8: Filtragem de Dados Faltantes

**Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.


```python
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

```

    Usuários com o campo específico faltando:
    {'nome': 'Maria', 'idade': 30}


<a id="ancora9"></a>
### Exercício 9: Extração de Subconjuntos de Dados

**Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.


```python
# Exercício 9: Extração de Subconjuntos de Dados
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extrair apenas os números pares usando uma compreensão de lista
pares = [numero for numero in numeros if numero % 2 == 0]

# Alternativamente, você também pode usar a função filter()
# pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimir os números pares
print("Números pares:", pares)

```

    Números pares: [2, 4, 6, 8, 10]


<a id="ancora10"></a>
### Exercício 10: Agregação de Dados por Categoria

**Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.


```python
# Exercício 10: Agregação de Dados por Categoria
# Conjunto de registros de vendas (exemplo)
registros_vendas = [
    {'categoria': 'Eletrônicos', 'valor': 1000},
    {'categoria': 'Roupas', 'valor': 500},
    {'categoria': 'Eletrônicos', 'valor': 1500},
    {'categoria': 'Alimentos', 'valor': 800},
    {'categoria': 'Roupas', 'valor': 700},
    {'categoria': 'Alimentos', 'valor': 1200}
]

# Dicionário para armazenar o total de vendas por categoria
total_vendas_por_categoria = {}

# Calcular o total de vendas por categoria
for venda in registros_vendas:
    categoria = venda['categoria']
    valor_venda = venda['valor']
    total_vendas_por_categoria[categoria] = total_vendas_por_categoria.get(categoria, 0) + valor_venda

# Imprimir o total de vendas por categoria
print("Total de vendas por categoria:")
for categoria, total_vendas in total_vendas_por_categoria.items():
    print(f"{categoria}: R${total_vendas:.2f}")

```

    Total de vendas por categoria:
    Eletrônicos: R$2500.00
    Roupas: R$1200.00
    Alimentos: R$2000.00


[voltar](#voltar)

<a id="ancora11"></a>
### Exercício 11:  Leitura de Dados até Flag

**Objetivo:** Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.



```python
# Exercício 11:  Leitura de Dados até Flag
# Palavra-chave específica
palavra_chave = "sair"

# Lista para armazenar os dados de entrada
dados = []

# Loop para ler os dados de entrada
while True:
    entrada = input("Digite um dado (ou 'sair' para encerrar): ")
    if entrada.lower() == palavra_chave:
        break
    dados.append(entrada)

# Imprimir os dados lidos
print("Dados lidos:")
for dado in dados:
    print(dado)

```

    Digite um dado (ou 'sair' para encerrar):  phone
    Digite um dado (ou 'sair' para encerrar):  keyborad
    Digite um dado (ou 'sair' para encerrar):  mouse
    Digite um dado (ou 'sair' para encerrar):  sair


    Dados lidos:
    phone
    keyborad
    mouse


<a id="ancora12"></a>
### Exercício 12: Validação de Entrada

**Objetivo:** Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.


```python
# Exercício 12: Validação de Entrada
# Definir o intervalo específico
inicio_intervalo = 1
fim_intervalo = 10

# Loop para solicitar o número até que a entrada seja válida
while True:
    try:
        numero = int(input(f"Digite um número entre {inicio_intervalo} e {fim_intervalo}: "))
        if inicio_intervalo <= numero <= fim_intervalo:
            print("Número válido:", numero)
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

```

    Digite um número entre 1 e 10:  11


    Número fora do intervalo. Tente novamente.


    Digite um número entre 1 e 10:  3


    Número válido: 3


<a id="ancora13"></a>
### Exercício 13: Consumo de API Simulado

**Objetivo:** Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.


```python
# Exercício 13: Consumo de API Simulado
# Número total de páginas (simulação)
paginas_totais = 3  

# Se não houver páginas, exibe uma mensagem e sai do loop
if paginas_totais <= 0:
    print("Não há páginas para processar.")
else:
    # Inicializa a página atual
    pagina_atual = 1
    
    # Loop para processar cada página de dados
    while pagina_atual <= paginas_totais:
        print(f"Processando página {pagina_atual} de {paginas_totais}")

        # Simulação de processamento de dados
        print(f"Dados da página {pagina_atual}:")
        for i in range(1, 6):
            print(f"Dado {i}")

        # Atualiza a página atual
        pagina_atual += 1

print("Todas as páginas foram processadas.")


```

    Processando página 1 de 3
    Dados da página 1:
    Dado 1
    Dado 2
    Dado 3
    Dado 4
    Dado 5
    Processando página 2 de 3
    Dados da página 2:
    Dado 1
    Dado 2
    Dado 3
    Dado 4
    Dado 5
    Processando página 3 de 3
    Dados da página 3:
    Dado 1
    Dado 2
    Dado 3
    Dado 4
    Dado 5
    Todas as páginas foram processadas.


<a id="ancora14"></a>
### Exercício 14: Tentativas de Conexão

**Objetivo:** Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.


```python
# Exercício 14: Tentativas de Conexão
# Simulação de tentativas de reconexão
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    tentativas += 1
    print(f"Tentativa de reconexão {tentativas}")

    # Simulação de conexão ao serviço
    conexao_sucesso = False  # Simulação de falha na conexão

    if conexao_sucesso:
        print("Conexão bem-sucedida.")
        break
    else:
        print("Falha na conexão. Tentando novamente.")

# Verifica se atingiu o limite de tentativas
if tentativas == limite_tentativas:
    print("Limite de tentativas atingido. Não foi possível reconectar ao serviço.")

```

    Tentativa de reconexão 1
    Falha na conexão. Tentando novamente.
    Tentativa de reconexão 2
    Falha na conexão. Tentando novamente.
    Tentativa de reconexão 3
    Falha na conexão. Tentando novamente.
    Limite de tentativas atingido. Não foi possível reconectar ao serviço.


<a id="ancora15"></a>
### Exercício 15: Processamento de Dados com Condição de Parada

**Objetivo:** Processar itens de uma lista até encontrar um valor específico que indica a parada.


```python
# Exercício 15: Processamento de Dados com Condição de Parada
# Lista de itens
lista = [10, 20, 30, 40, 50, 60, 70, "parar", 80, 90, 100]

# Inicializa o índice
indice = 0

# Loop para processar os itens da lista
while indice < len(lista):
    item = lista[indice]

    # Verifica se o item é o valor específico que indica a parada
    if item == "parar":
        print("Encontrou o valor 'parar'. Parando o processamento.")
        break

    # Processa o item
    print("Processando item:", item)

    # Atualiza o índice para avançar para o próximo item
    indice += 1

```

    Processando item: 10
    Processando item: 20
    Processando item: 30
    Processando item: 40
    Processando item: 50
    Processando item: 60
    Processando item: 70
    Encontrou o valor 'parar'. Parando o processamento.


[voltar](#voltar)

<a id="desafio"></a>
### Desafio : Estruturas de Controle de Fluxo

**Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas**


```python
# Desafio : Estruturas de Controle de Fluxo
while True:
    try:
        # Solicita ao usuário que insira seu nome
        nome = input("Digite seu nome: ").strip()
        
        # Verifica se o nome está vazio ou contém números
        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")

        # Solicita ao usuário que insira o valor do salário e valida
        salario = float(input("Digite o valor do seu salário: "))
        if salario <= 0:
            print("Por favor, digite um valor positivo para o salário.")
            raise ValueError

        # Solicita ao usuário que insira o valor do bônus em porcentagem
        bonus_recebido = float(input("Digite o percentual do bônus recebido: "))
        if bonus_recebido < 0:
            print("Por favor, digite um valor positivo para o bônus.")
            raise ValueError

        # Calcula o total
        kpi = 1000 + salario * bonus_recebido  

        # Imprime as informações para o usuário
        print(f"{nome}, considerando seu salário de R${salario:.2f} o total com bônus é de R${kpi:.2f}.")
        
        # Sai do loop após inserir as informações corretas
        break
        
    except ValueError as e:
        print("Erro:", e)
    except Exception as e:
        print("Ocorreu um erro:", e)

```

    Digite seu nome:  Julio12


    Erro: O nome não deve conter números.


    Digite seu nome:  Julio
    Digite o valor do seu salário:  10000
    Digite o percentual do bônus recebido:  1.5


    Julio, considerando seu salário de R$10000.00 o total com bônus é de R$16000.00.


[voltar](#voltar)


```python

```
